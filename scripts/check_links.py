#!/usr/bin/env python3
"""Check every relative link and external URL in the gallery, pack, PDF, and deck."""

from __future__ import annotations

import re
import sys
import tempfile
import zipfile
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "downloads" / "link-check.txt"
NS = {"pr": "http://schemas.openxmlformats.org/package/2006/relationships"}
BANNED = [
    (r"linktree", "linktree"),
    (r"linktr\.ee", "linktr.ee"),
    (r"laxman", "laxman"),
    (r"kadiyala", "kadiyala"),
    (r"\blucky\b", "lucky"),
    (r"cypher", "cypher"),
    (r"cipher0x9", "cipher0x9"),
    (r"\bhermes\b", "hermes"),
    (r"h-1b", "h-1b"),
    (r"\bh1b\b", "h1b"),
    (r"grokbot", "grokbot"),
    (r"[\w.+\-]+@[\w\-]+\.[A-Za-z]{2,}", "email address"),
]
SKIP_DIRS = {".git", "__pycache__", "fonts"}


def fetch(url: str, cache: dict[str, str]) -> str:
    if url in cache:
        return cache[url]
    last = "no response"
    for agent in ("GemsLinkCheck/1.0", "Mozilla/5.0"):
        req = Request(url, headers={"User-Agent": agent}, method="GET")
        try:
            with urlopen(req, timeout=25) as res:
                code = getattr(res, "status", 200)
                cache[url] = "ok" if 200 <= code < 400 else f"HTTP {code}"
                return cache[url]
        except HTTPError as exc:
            last = f"HTTP {exc.code}"
            if exc.code in {301, 302, 303, 307, 308}:
                cache[url] = "ok"
                return "ok"
            if exc.code == 403:
                continue
        except URLError as exc:
            last = f"URL error {exc.reason}"
        except Exception as exc:  # noqa: BLE001
            last = str(exc)
    cache[url] = last
    return last


def md_html_targets(text: str) -> list[str]:
    found = re.findall(r"\]\(([^)\s]+)\)", text)
    found += re.findall(r"""(?:href|src)\s*=\s*["']([^"']+)["']""", text, flags=re.I)
    found += [item.strip("\"'") for item in re.findall(r"""url\(([^)]+)\)""", text)]
    return found


def has_anchor(text: str, anchor: str) -> bool:
    if not anchor:
        return True
    return f'id="{anchor}"' in text or f"id='{anchor}'" in text


def check_tree(root: Path, label: str, failures: list[str], cache: dict[str, str]) -> int:
    checked = 0
    files = [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in {".md", ".html", ".css"}]
    for path in files:
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for raw in md_html_targets(text):
            if raw.startswith(("data:", "mailto:", "javascript:")):
                failures.append(f"{label} {path.relative_to(root)}: disallowed target {raw}")
                continue
            checked += 1
            target, _, anchor = raw.partition("#")
            if target.startswith(("http://", "https://")):
                result = fetch(target, cache)
                if result != "ok":
                    failures.append(f"{label} {path.relative_to(root)}: {raw} -> {result}")
                continue
            if not target:
                if not has_anchor(text, anchor):
                    failures.append(f"{label} {path.relative_to(root)}: missing anchor #{anchor}")
                continue
            dest = (path.parent / target).resolve()
            try:
                dest.relative_to(root.resolve())
            except ValueError:
                failures.append(f"{label} {path.relative_to(root)}: link escapes the tree {raw}")
                continue
            if not dest.is_file():
                failures.append(f"{label} {path.relative_to(root)}: missing file {raw}")
                continue
            if anchor and not has_anchor(dest.read_text(encoding="utf-8", errors="replace"), anchor):
                failures.append(f"{label} {path.relative_to(root)}: missing anchor {raw}")
    return checked


def check_pdf(path: Path, label: str, failures: list[str], cache: dict[str, str]) -> int:
    from pypdf import PdfReader

    reader = PdfReader(str(path))
    page_refs = set()
    for page in reader.pages:
        ref = page.indirect_reference
        if ref is not None:
            page_refs.add((ref.idnum, ref.generation))
    checked = 0
    for index, page in enumerate(reader.pages, 1):
        annots = page.get("/Annots") or []
        for annot in annots:
            obj = annot.get_object()
            if obj.get("/Subtype") != "/Link":
                continue
            checked += 1
            action = obj.get("/A")
            dest = obj.get("/Dest")
            if action is not None and action.get("/S") == "/URI":
                url = str(action.get("/URI"))
                result = fetch(url, cache)
                if result != "ok":
                    failures.append(f"{label} PDF page {index}: {url} -> {result}")
                continue
            if dest is not None:
                if isinstance(dest, list) and dest:
                    ref = dest[0]
                    key = (getattr(ref, "idnum", None), getattr(ref, "generation", None))
                    if key not in page_refs:
                        failures.append(f"{label} PDF page {index}: destination is not a page")
                else:
                    failures.append(f"{label} PDF page {index}: unsupported destination {dest!r}")
                continue
            failures.append(f"{label} PDF page {index}: link has no URI or destination")
    if checked == 0:
        failures.append(f"{label} PDF has no links")
    return checked


def check_pptx(path: Path, base: Path, label: str, failures: list[str], cache: dict[str, str]) -> int:
    checked = 0
    with zipfile.ZipFile(path) as archive:
        for name in archive.namelist():
            if not name.startswith("ppt/slides/_rels/") or not name.endswith(".rels"):
                continue
            root = ElementTree.fromstring(archive.read(name))
            for rel in root.findall("pr:Relationship", NS):
                if not str(rel.get("Type", "")).endswith("/hyperlink"):
                    continue
                checked += 1
                target = rel.get("Target") or ""
                mode = rel.get("TargetMode")
                if mode != "External":
                    failures.append(f"{label} PPTX {name}: hyperlink is not external ({target})")
                    continue
                if target.startswith(("http://", "https://")):
                    result = fetch(target, cache)
                    if result != "ok":
                        failures.append(f"{label} PPTX: {target} -> {result}")
                    continue
                dest = (base / target).resolve()
                tree = base.parent.resolve()
                try:
                    dest.relative_to(tree)
                except ValueError:
                    failures.append(f"{label} PPTX: link escapes the pack {target}")
                    continue
                if not dest.is_file():
                    failures.append(f"{label} PPTX: missing {target} from {base}")
    if checked == 0:
        failures.append(f"{label} PPTX has no hyperlinks")
    return checked


def check_privacy(root: Path, failures: list[str]) -> int:
    scanned = 0
    files = []
    for path in root.rglob("*"):
        if not path.is_file() or any(part in {".git", "__pycache__"} for part in path.parts):
            continue
        if path.name in {"check_links.py", "link-check.txt"}:
            continue
        if path.suffix.lower() in {".md", ".html", ".css", ".js", ".py", ".txt", ".svg"}:
            files.append(path)
    blob = []
    for path in files:
        scanned += 1
        blob.append(path.read_text(encoding="utf-8", errors="replace"))
    pdf = root / "downloads" / "Gemini-Gems-Guide.pdf"
    pptx = root / "downloads" / "Gemini-Gems-Overview.pptx"
    if pdf.is_file():
        from pypdf import PdfReader

        blob.append("\n".join((page.extract_text() or "") for page in PdfReader(str(pdf)).pages))
        scanned += 1
    if pptx.is_file():
        with zipfile.ZipFile(pptx) as archive:
            for name in archive.namelist():
                if name.startswith("ppt/slides/slide") and name.endswith(".xml"):
                    blob.append(archive.read(name).decode("utf-8", "replace"))
        scanned += 1
    haystack = "\n".join(blob)
    for pattern, name in BANNED:
        match = re.search(pattern, haystack, flags=re.I)
        if match:
            failures.append(f"privacy: found {name} near '{match.group(0)[:80]}'")
    return scanned


def main() -> int:
    failures: list[str] = []
    cache: dict[str, str] = {}
    repo_links = check_tree(ROOT, "repo", failures, cache)
    pdf_links = check_pdf(ROOT / "downloads" / "Gemini-Gems-Guide.pdf", "repo", failures, cache)
    pptx_links = check_pptx(
        ROOT / "downloads" / "Gemini-Gems-Overview.pptx",
        ROOT / "downloads",
        "repo",
        failures,
        cache,
    )
    pack = ROOT / "downloads" / "gemini-gems-pack.zip"
    with tempfile.TemporaryDirectory() as tmp:
        dest = Path(tmp)
        with zipfile.ZipFile(pack) as archive:
            names = set(archive.namelist())
            archive.extractall(dest)
        required = [
            "README.md",
            "LICENSE",
            "site/index.html",
            "site/print.html",
            "site/assets/gallery.css",
            "site/assets/gallery.js",
            "examples/README.md",
            "examples/gem_app.py",
            "examples/gem_app.mjs",
            "downloads/Gemini-Gems-Guide.pdf",
            "downloads/Gemini-Gems-Overview.pptx",
            "scripts/build_gallery.py",
            "scripts/check_links.py",
        ]
        required += [f"gems/{path.name}" for path in sorted((ROOT / "gems").glob("*.md"))]
        required += [f"site/gems/{path.name}" for path in sorted((ROOT / "site" / "gems").glob("*.html"))]
        for rel in required:
            if rel not in names:
                failures.append(f"zip missing {rel}")
        if "downloads/gemini-gems-pack.zip" not in names:
            failures.append("zip is missing its unpacked download link")
        zip_links = check_tree(dest, "zip", failures, cache)
        zip_pdf = check_pdf(dest / "downloads" / "Gemini-Gems-Guide.pdf", "zip", failures, cache)
        zip_pptx = check_pptx(dest / "downloads" / "Gemini-Gems-Overview.pptx", dest / "downloads", "zip", failures, cache)
    privacy_files = check_privacy(ROOT, failures)
    lines = [
        "Gemini Gems Gallery link and privacy check",
        f"repo document links checked: {repo_links}",
        f"pdf links checked: {pdf_links}",
        f"pptx links checked: {pptx_links}",
        f"zip document links checked: {zip_links}",
        f"zip pdf links checked: {zip_pdf}",
        f"zip pptx links checked: {zip_pptx}",
        f"privacy files scanned: {privacy_files}",
        f"external urls checked: {len(cache)}",
    ]
    for url, result in sorted(cache.items()):
        lines.append(f"  {result}: {url}")
    if failures:
        lines.append(f"FAILURES: {len(failures)}")
        lines.extend(f"- {item}" for item in failures)
    else:
        lines.append("FAILURES: 0")
        lines.append("All checked links resolved. No personal-detail patterns matched.")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
