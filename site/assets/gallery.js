(function () {
  var root = document.documentElement;
  var toggle = document.querySelector("[data-theme-toggle]");

  function apply(theme) {
    root.dataset.theme = theme;
    try { localStorage.setItem("gems-theme", theme); } catch (err) { /* private mode */ }
    if (toggle) {
      var dark = theme !== "light";
      toggle.setAttribute("aria-pressed", dark ? "true" : "false");
      toggle.textContent = dark ? "Light theme" : "Dark theme";
    }
  }

  if (toggle) {
    toggle.addEventListener("click", function () {
      apply(root.dataset.theme === "light" ? "dark" : "light");
    });
  }
  apply(root.dataset.theme || "dark");

  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var el = document.getElementById(btn.getAttribute("data-copy"));
      var text = el ? el.textContent : "";
      var done = function () {
        var old = btn.textContent;
        btn.textContent = "Copied";
        setTimeout(function () { btn.textContent = old; }, 1400);
      };
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(text).then(done).catch(function () { fallback(text); done(); });
      } else {
        fallback(text);
        done();
      }
    });
  });

  function fallback(text) {
    var area = document.createElement("textarea");
    area.value = text;
    document.body.appendChild(area);
    area.select();
    document.execCommand("copy");
    area.remove();
  }

  document.querySelectorAll("[data-print]").forEach(function (btn) {
    btn.addEventListener("click", function () { window.print(); });
  });

  var q = document.getElementById("q");
  var grid = document.getElementById("grid");
  if (!q || !grid) return;
  var cards = Array.prototype.slice.call(grid.querySelectorAll(".card"));
  var empty = document.getElementById("empty");
  var result = document.getElementById("result-count");
  var buttons = Array.prototype.slice.call(document.querySelectorAll("[data-filter]"));
  var cat = "All";

  function render() {
    var term = q.value.trim().toLowerCase();
    var n = 0;
    cards.forEach(function (card) {
      var hay = card.getAttribute("data-hay") || "";
      var ok = (cat === "All" || card.getAttribute("data-cat") === cat) && (!term || hay.indexOf(term) !== -1);
      card.hidden = !ok;
      if (ok) n += 1;
    });
    if (empty) empty.hidden = n !== 0;
    if (result) result.textContent = n + (n === 1 ? " desk" : " desks");
  }

  buttons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      cat = btn.getAttribute("data-filter");
      buttons.forEach(function (other) {
        other.setAttribute("aria-pressed", other === btn ? "true" : "false");
      });
      render();
    });
  });
  q.addEventListener("input", render);
  document.addEventListener("keydown", function (event) {
    if (event.key === "/" && document.activeElement !== q && !event.metaKey && !event.ctrlKey) {
      event.preventDefault();
      q.focus();
    }
  });
  render();
})();
