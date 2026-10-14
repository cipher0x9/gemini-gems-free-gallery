"""Original poster illustrations for the 33 Gems. One scene per desk."""

import html

def poster(num, accent, label, body):
    gid = f"glow{num:02d}"
    dots = f"dots{num:02d}"
    art = body.replace("@@", accent)
    safe = html.escape(label, quote=True)
    return f'''<svg class="poster-svg" viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{safe}">
  <defs>
    <linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{accent}" stop-opacity="0.5"/>
      <stop offset="68%" stop-color="{accent}" stop-opacity="0"/>
    </linearGradient>
    <pattern id="{dots}" width="18" height="18" patternUnits="userSpaceOnUse">
      <circle cx="1.2" cy="1.2" r="1.1" fill="#E8EEF9" opacity="0.16"/>
    </pattern>
  </defs>
  <rect width="400" height="300" rx="28" fill="#10192C"/>
  <rect width="400" height="300" rx="28" fill="url(#{gid})"/>
  <rect width="400" height="300" rx="28" fill="url(#{dots})"/>
  {art}
  <text x="28" y="272" fill="{accent}" font-family="Inter, sans-serif" font-size="13" font-weight="700">{num:02d}</text>
</svg>'''


def _scenes():
    return {
        "sales-call-prep-desk": '''
          <g class="drift">
            <rect x="46" y="78" width="150" height="128" rx="18" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <path d="M68 112h106M68 132h84M68 152h70" stroke="#C9D4EA" stroke-width="3" stroke-linecap="round"/>
            <circle cx="78" cy="98" r="6" fill="@@"/>
          </g>
          <path class="draw" d="M196 142 H250" stroke="#F59E0B" stroke-width="3" stroke-linecap="round" stroke-dasharray="6 7"/>
          <g class="driftb">
            <circle cx="300" cy="142" r="52" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <circle cx="300" cy="142" r="28" stroke="#F59E0B" stroke-width="3" fill="none"/>
            <circle cx="300" cy="142" r="6" fill="#22C55E"/>
            <path d="M300 98 v12 M300 174 v12 M256 142 h12 M332 142 h12" stroke="@@" stroke-width="2.5" stroke-linecap="round"/>
          </g>''',
        "meeting-recap-desk": '''
          <g class="drift">
            <circle cx="92" cy="118" r="26" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <circle cx="148" cy="108" r="26" fill="#17233A" stroke="#F59E0B" stroke-width="2.5"/>
            <circle cx="124" cy="162" r="26" fill="#17233A" stroke="#22C55E" stroke-width="2.5"/>
          </g>
          <path class="draw" d="M180 140 H230" stroke="@@" stroke-width="3" stroke-linecap="round" stroke-dasharray="6 7"/>
          <g class="driftb">
            <rect x="236" y="74" width="122" height="150" rx="16" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <path d="M258 108 h78 M258 132 h78 M258 156 h60 M258 180 h48" stroke="#C9D4EA" stroke-width="3" stroke-linecap="round"/>
            <path d="M258 104 l6 6 12-14" stroke="#22C55E" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
          </g>''',
        "resume-tailor-desk": '''
          <g class="drift">
            <rect x="58" y="58" width="150" height="184" rx="16" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <path d="M80 96h106M80 118h90M80 140h96M80 162h70" stroke="#C9D4EA" stroke-width="3" stroke-linecap="round"/>
          </g>
          <g class="driftb" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="286" cy="92" r="18" fill="#22C55E"/>
            <circle cx="330" cy="150" r="18" fill="#F59E0B"/>
            <circle cx="286" cy="208" r="18" fill="#6366F1"/>
            <path d="M220 150 H250" class="draw" stroke="@@" stroke-width="3" stroke-dasharray="5 6"/>
          </g>
          <path d="M248 78 l28 18 -28 18 z" fill="@@"/>''',
        "bedtime-story-desk": '''
          <g class="drift">
            <path d="M250 70 a46 46 0 1 0 0 92 a36 36 0 1 1 0-92z" fill="#F59E0B"/>
            <circle class="twinkle" cx="120" cy="78" r="3" fill="#E8EEF9"/>
            <circle class="twinkle" cx="168" cy="54" r="2.5" fill="#E8EEF9"/>
            <circle class="twinkle" cx="90" cy="120" r="2" fill="#E8EEF9"/>
          </g>
          <g class="driftb">
            <path d="M70 210 c40-48 90-48 130 0 v28 H70z" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <path d="M118 168 v42 M100 188 h36" stroke="#F59E0B" stroke-width="3" stroke-linecap="round"/>
          </g>
          <path class="draw" d="M40 230 H360" stroke="@@" stroke-width="2" stroke-dasharray="4 8"/>''',
        "weekly-planning-desk": '''
          <g class="drift">
            <rect x="48" y="64" width="304" height="168" rx="18" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <path d="M48 104 H352" stroke="#2A3A58" stroke-width="2"/>
            <rect x="70" y="122" width="70" height="86" rx="10" fill="#0F9B8E"/>
            <rect x="156" y="140" width="70" height="68" rx="10" fill="#F59E0B"/>
            <rect x="242" y="158" width="70" height="50" rx="10" fill="#6366F1"/>
          </g>
          <path class="draw" d="M78 92 H250" stroke="#E8EEF9" stroke-width="3" stroke-linecap="round" stroke-dasharray="2 8"/>''',
        "inbox-triage-desk": '''
          <g class="drift">
            <rect x="70" y="58" width="200" height="36" rx="10" fill="#17233A" stroke="#22C55E" stroke-width="2.5"/>
            <rect x="86" y="104" width="200" height="36" rx="10" fill="#17233A" stroke="#F59E0B" stroke-width="2.5"/>
            <rect x="102" y="150" width="200" height="36" rx="10" fill="#17233A" stroke="#6366F1" stroke-width="2.5"/>
            <rect x="118" y="196" width="200" height="36" rx="10" fill="#17233A" stroke="@@" stroke-width="2.5"/>
          </g>
          <path class="draw" d="M40 76 H70 M56 122 H86 M72 168 H102 M88 214 H118" stroke="#E8EEF9" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="4 6"/>''',
        "homework-coach-desk": '''
          <g class="drift">
            <rect x="150" y="48" width="36" height="150" rx="8" fill="#F59E0B"/>
            <path d="M132 196 h72 l-10 28 h-52z" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <circle cx="168" cy="86" r="22" fill="#10192C" stroke="#0B1220" stroke-width="4"/>
          </g>
          <g class="driftb">
            <circle cx="92" cy="150" r="16" fill="#22C55E"/>
            <circle cx="250" cy="168" r="16" fill="#6366F1"/>
            <circle cx="318" cy="130" r="16" fill="@@"/>
          </g>
          <path class="draw" d="M108 150 H250" stroke="#E8EEF9" stroke-width="3" stroke-linecap="round" stroke-dasharray="6 8"/>''',
        "budget-tracker-desk": '''
          <g class="drift">
            <path d="M64 214 H336" stroke="#C9D4EA" stroke-width="2.5" stroke-linecap="round"/>
            <rect x="84" y="140" width="36" height="74" rx="8" fill="#17233A" stroke="@@" stroke-width="2"/>
            <rect x="140" y="110" width="36" height="104" rx="8" fill="@@"/>
            <rect x="196" y="156" width="36" height="58" rx="8" fill="#F59E0B"/>
            <rect x="252" y="92" width="36" height="122" rx="8" fill="#6366F1"/>
          </g>
          <path class="draw" d="M70 128 C140 128, 180 90, 300 96" stroke="#22C55E" stroke-width="3" fill="none" stroke-dasharray="6 7"/>''',
        "interview-prep-desk": '''
          <g class="drift">
            <rect x="58" y="150" width="70" height="64" rx="12" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <rect x="168" y="150" width="70" height="64" rx="12" fill="#17233A" stroke="#F59E0B" stroke-width="2.5"/>
            <circle cx="93" cy="124" r="22" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <circle cx="203" cy="124" r="22" fill="#17233A" stroke="#F59E0B" stroke-width="2.5"/>
          </g>
          <g class="driftb">
            <rect x="268" y="78" width="84" height="110" rx="14" fill="#17233A" stroke="#22C55E" stroke-width="2.5"/>
            <path d="M290 116 h40 M290 138 h40 M290 160 h24" stroke="#C9D4EA" stroke-width="3" stroke-linecap="round"/>
          </g>''',
        "study-plan-desk": '''
          <g class="drift">
            <path d="M64 200 C120 200, 140 120, 200 120 S300 70, 348 78" stroke="@@" stroke-width="3" fill="none" stroke-linecap="round"/>
            <circle cx="64" cy="200" r="10" fill="#F59E0B"/>
            <circle cx="200" cy="120" r="10" fill="#6366F1"/>
            <circle cx="348" cy="78" r="12" fill="#22C55E"/>
          </g>
          <g class="driftb">
            <rect x="78" y="150" width="244" height="70" rx="14" fill="#17233A" stroke="@@" stroke-width="2"/>
            <path d="M100 185 h36 M156 185 h36 M212 185 h36 M268 185 h30" stroke="#C9D4EA" stroke-width="6" stroke-linecap="round"/>
          </g>''',
        "support-reply-desk": '''
          <g class="drift">
            <rect x="48" y="70" width="180" height="120" rx="22" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <path d="M78 170 l-10 28 36-20" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <path d="M128 118 c0-18 28-18 28 2 0 14-28 10-28 26" stroke="#F59E0B" stroke-width="3" fill="none" stroke-linecap="round"/>
            <circle cx="142" cy="162" r="3" fill="#F59E0B"/>
          </g>
          <g class="driftb">
            <rect x="230" y="86" width="120" height="140" rx="16" fill="#17233A" stroke="#22C55E" stroke-width="2.5"/>
            <path d="M252 122 h76 M252 146 h64 M252 170 h70" stroke="#C9D4EA" stroke-width="3" stroke-linecap="round"/>
          </g>''',
        "sop-writer-desk": '''
          <g class="drift">
            <circle cx="78" cy="86" r="22" fill="@@"/>
            <circle cx="78" cy="156" r="22" fill="#F59E0B"/>
            <circle cx="78" cy="226" r="22" fill="#6366F1"/>
          </g>
          <path class="draw" d="M100 86 H210 M100 156 H250 M100 226 H300" stroke="#C9D4EA" stroke-width="3" stroke-linecap="round" stroke-dasharray="7 8"/>
          <g class="driftb">
            <rect x="220" y="68" width="120" height="36" rx="10" fill="#17233A" stroke="@@" stroke-width="2"/>
            <rect x="250" y="138" width="110" height="36" rx="10" fill="#17233A" stroke="#F59E0B" stroke-width="2"/>
            <rect x="300" y="208" width="70" height="36" rx="10" fill="#17233A" stroke="#6366F1" stroke-width="2"/>
          </g>''',
        "onboarding-guide-desk": '''
          <g class="drift">
            <rect x="150" y="70" width="120" height="150" rx="14" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <path d="M186 70 v-24 h48 v24" fill="none" stroke="#F59E0B" stroke-width="3"/>
            <circle cx="210" cy="150" r="8" fill="#22C55E"/>
          </g>
          <g class="driftb">
            <rect x="40" y="150" width="70" height="48" rx="10" fill="#0F9B8E"/>
            <rect x="40" y="96" width="70" height="44" rx="10" fill="#6366F1"/>
            <rect x="300" y="120" width="64" height="36" rx="8" fill="#F59E0B"/>
            <rect x="300" y="164" width="64" height="36" rx="8" fill="#22C55E"/>
            <rect x="300" y="208" width="64" height="36" rx="8" fill="#6366F1"/>
          </g>''',
        "signal-brief-desk": '''
          <g class="drift">
            <path d="M200 170 l70-18 18 70 -70 18z" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <path d="M150 150 a70 70 0 0 1 100-40" stroke="#F59E0B" stroke-width="3" fill="none" stroke-linecap="round"/>
            <path d="M124 168 a110 110 0 0 1 150-70" stroke="@@" stroke-width="3" fill="none" stroke-linecap="round"/>
            <circle cx="214" cy="156" r="6" fill="#22C55E"/>
          </g>
          <g class="driftb">
            <rect x="286" y="70" width="28" height="90" rx="6" fill="#22C55E"/>
            <rect x="322" y="96" width="28" height="64" rx="6" fill="#F59E0B"/>
            <rect x="250" y="116" width="28" height="44" rx="6" fill="#6366F1"/>
          </g>''',
        "social-post-desk": '''
          <g class="drift">
            <rect x="48" y="78" width="90" height="140" rx="16" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <rect x="156" y="58" width="90" height="160" rx="16" fill="#17233A" stroke="#F59E0B" stroke-width="2.5"/>
            <rect x="264" y="90" width="90" height="128" rx="16" fill="#17233A" stroke="#6366F1" stroke-width="2.5"/>
          </g>
          <path class="draw" d="M68 112 h50 M176 96 h50 M284 124 h50" stroke="#E8EEF9" stroke-width="4" stroke-linecap="round" stroke-dasharray="2 10"/>''',
        "newsletter-desk": '''
          <g class="drift">
            <rect x="54" y="78" width="180" height="130" rx="16" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <path d="M54 78 l90 70 90-70" fill="none" stroke="#F59E0B" stroke-width="3"/>
          </g>
          <g class="driftb">
            <rect x="250" y="70" width="110" height="22" rx="8" fill="#22C55E"/>
            <rect x="250" y="104" width="110" height="22" rx="8" fill="#F59E0B"/>
            <rect x="250" y="138" width="110" height="22" rx="8" fill="#6366F1"/>
            <rect x="250" y="184" width="80" height="28" rx="14" fill="@@"/>
          </g>''',
        "pr-review-desk": '''
          <g class="drift">
            <rect x="48" y="64" width="200" height="160" rx="16" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <path d="M72 100 h140 M72 126 h110 M72 152 h130 M72 178 h80" stroke="#8EA0C4" stroke-width="3" stroke-linecap="round"/>
          </g>
          <g class="driftb">
            <circle cx="292" cy="128" r="46" fill="none" stroke="#F59E0B" stroke-width="6"/>
            <path d="M324 162 l36 36" stroke="#F59E0B" stroke-width="8" stroke-linecap="round"/>
            <circle cx="330" cy="70" r="8" fill="#EF4444"/>
            <circle cx="354" cy="96" r="8" fill="#F59E0B"/>
            <circle cx="360" cy="128" r="8" fill="#6366F1"/>
            <circle cx="348" cy="160" r="8" fill="#22C55E"/>
          </g>''',
        "bug-triage-desk": '''
          <g class="drift">
            <ellipse cx="150" cy="160" rx="70" ry="46" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <circle cx="128" cy="150" r="6" fill="#E8EEF9"/>
            <circle cx="156" cy="150" r="6" fill="#E8EEF9"/>
            <path d="M110 130 l-24-20 M190 130 l24-20 M104 170 l-28 16 M198 170 l28 16" stroke="#F59E0B" stroke-width="3" stroke-linecap="round"/>
          </g>
          <g class="driftb">
            <rect x="250" y="78" width="100" height="130" rx="16" fill="#17233A" stroke="#22C55E" stroke-width="2.5"/>
            <path d="M270 112 h60 M270 140 h48 M270 168 h54" stroke="#C9D4EA" stroke-width="3" stroke-linecap="round"/>
          </g>''',
        "incident-postmortem-desk": '''
          <path class="draw" d="M40 150 H360" stroke="@@" stroke-width="3" stroke-linecap="round" stroke-dasharray="8 8"/>
          <g class="drift">
            <circle cx="80" cy="150" r="14" fill="#22C55E"/>
            <circle cx="160" cy="150" r="14" fill="#F59E0B"/>
            <circle cx="250" cy="150" r="18" fill="#6366F1"/>
            <circle cx="330" cy="150" r="14" fill="@@"/>
          </g>
          <g class="driftb">
            <rect x="214" y="48" width="92" height="48" rx="12" fill="#17233A" stroke="#6366F1" stroke-width="2"/>
            <path d="M250 96 V132" stroke="#6366F1" stroke-width="2"/>
          </g>''',
        "runbook-desk": '''
          <g class="drift">
            <rect x="56" y="48" width="150" height="200" rx="16" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <path d="M80 88 h100 M80 116 h80 M80 144 h90" stroke="#C9D4EA" stroke-width="3" stroke-linecap="round"/>
            <rect x="80" y="168" width="100" height="40" rx="10" fill="#F59E0B"/>
          </g>
          <g class="driftb">
            <path d="M280 90 l28 48 H252z" fill="#17233A" stroke="#F59E0B" stroke-width="3" stroke-linejoin="round"/>
            <path d="M280 112 v16" stroke="#F59E0B" stroke-width="3" stroke-linecap="round"/>
            <circle cx="280" cy="140" r="2.5" fill="#F59E0B"/>
            <path class="draw" d="M230 188 H340" stroke="#22C55E" stroke-width="3" stroke-dasharray="5 6"/>
          </g>''',
        "api-docs-desk": '''
          <g class="drift">
            <rect x="40" y="100" width="120" height="70" rx="14" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <rect x="240" y="100" width="120" height="70" rx="14" fill="#17233A" stroke="#22C55E" stroke-width="2.5"/>
            <path d="M78 128 h44 M78 146 h28" stroke="#C9D4EA" stroke-width="3" stroke-linecap="round"/>
            <path d="M262 128 h60 M262 146 h40" stroke="#C9D4EA" stroke-width="3" stroke-linecap="round"/>
          </g>
          <path class="draw" d="M160 135 H240" stroke="#F59E0B" stroke-width="3" stroke-linecap="round" stroke-dasharray="6 7"/>
          <rect x="176" y="168" width="48" height="36" rx="10" fill="#17233A" stroke="#6366F1" stroke-width="2.5"/>''',
        "architecture-diagram-desk": '''
          <g class="drift">
            <rect x="40" y="48" width="110" height="64" rx="12" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <rect x="250" y="48" width="110" height="64" rx="12" fill="#17233A" stroke="#F59E0B" stroke-width="2.5"/>
            <rect x="146" y="180" width="110" height="64" rx="12" fill="#17233A" stroke="#22C55E" stroke-width="2.5"/>
          </g>
          <path d="M150 80 H250" stroke="@@" stroke-width="3" stroke-linecap="round"/>
          <path class="draw" d="M95 112 C95 180, 146 200, 146 212" stroke="#F59E0B" stroke-width="3" fill="none" stroke-dasharray="6 7"/>
          <path d="M305 112 C305 180, 256 200, 256 212" stroke="#22C55E" stroke-width="3" fill="none"/>''',
        "claim-check-desk": '''
          <g class="drift">
            <circle cx="110" cy="150" r="52" fill="none" stroke="#22C55E" stroke-width="8"/>
            <path d="M86 150 l16 16 32-36" fill="none" stroke="#22C55E" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
            <circle cx="210" cy="150" r="52" fill="none" stroke="#F59E0B" stroke-width="8"/>
            <path d="M210 126 v30" stroke="#F59E0B" stroke-width="6" stroke-linecap="round"/>
            <circle cx="310" cy="150" r="52" fill="none" stroke="#6366F1" stroke-width="8"/>
            <path d="M292 132 l36 36 M328 132 l-36 36" stroke="#6366F1" stroke-width="6" stroke-linecap="round"/>
          </g>''',
        "competitive-landscape-desk": '''
          <g class="drift">
            <rect x="48" y="70" width="300" height="150" rx="16" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <path d="M48 112 H348 M148 70 V220 M248 70 V220" stroke="#2C3E5E" stroke-width="2"/>
            <rect x="168" y="132" width="60" height="18" rx="6" fill="#22C55E"/>
            <rect x="268" y="154" width="60" height="18" rx="6" fill="#F59E0B"/>
            <rect x="68" y="144" width="60" height="18" rx="6" fill="#6366F1"/>
          </g>''',
        "certification-coach-desk": '''
          <g class="drift">
            <circle cx="150" cy="130" r="56" fill="#17233A" stroke="#F59E0B" stroke-width="8"/>
            <path d="M110 168 l40 22 40-22 v-20 H110z" fill="#F59E0B"/>
            <path d="M94 176 l-20 36 M206 176 l20 36" stroke="@@" stroke-width="4" stroke-linecap="round"/>
          </g>
          <g class="driftb">
            <rect x="250" y="78" width="110" height="130" rx="14" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <path d="M270 112 h70 M270 140 h50 M270 168 h60" stroke="#C9D4EA" stroke-width="3" stroke-linecap="round"/>
          </g>''',
        "money-desk": '''
          <g class="drift">
            <rect x="48" y="64" width="190" height="160" rx="16" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <path d="M72 104 h140 M72 132 h100 M72 160 h120 M72 188 h80" stroke="#C9D4EA" stroke-width="3" stroke-linecap="round"/>
          </g>
          <g class="driftb">
            <rect x="250" y="96" width="110" height="44" rx="12" fill="#F59E0B"/>
            <path d="M268 118 h74" stroke="#0B1220" stroke-width="4" stroke-linecap="round"/>
            <circle cx="300" cy="196" r="28" fill="none" stroke="#22C55E" stroke-width="4"/>
            <path d="M286 182 l28 28 M314 182 l-28 28" stroke="#22C55E" stroke-width="4" stroke-linecap="round"/>
          </g>''',
        "language-drill-desk": '''
          <g class="drift">
            <rect x="40" y="70" width="150" height="90" rx="20" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <path d="M70 160 l-8 26 30-18" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <path d="M64 108 h100 M64 130 h70" stroke="#C9D4EA" stroke-width="3" stroke-linecap="round"/>
          </g>
          <g class="driftb">
            <rect x="210" y="120" width="150" height="90" rx="20" fill="#17233A" stroke="#F59E0B" stroke-width="2.5"/>
            <path d="M234 158 h100 M234 180 h64" stroke="#C9D4EA" stroke-width="3" stroke-linecap="round"/>
          </g>
          <circle cx="120" cy="214" r="8" fill="#22C55E"/>
          <circle cx="160" cy="214" r="8" fill="#F59E0B"/>
          <circle cx="200" cy="214" r="8" fill="#6366F1"/>''',
        "lesson-plan-desk": '''
          <g class="drift">
            <circle cx="110" cy="120" r="46" fill="#22C55E"/>
            <path d="M110 74 v18 M110 148 v18 M64 120 h18 M138 120 h18" stroke="#14532D" stroke-width="4" stroke-linecap="round"/>
            <rect x="92" y="168" width="36" height="48" rx="8" fill="#F59E0B"/>
          </g>
          <g class="driftb">
            <rect x="200" y="64" width="150" height="170" rx="16" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <path d="M222 100 h106 M222 128 h90 M222 156 h100 M222 184 h70" stroke="#C9D4EA" stroke-width="3" stroke-linecap="round"/>
          </g>''',
        "curious-kids-science-desk": '''
          <g class="drift">
            <circle cx="168" cy="128" r="48" fill="none" stroke="#F59E0B" stroke-width="8"/>
            <path d="M202 162 l40 40" stroke="#F59E0B" stroke-width="10" stroke-linecap="round"/>
          </g>
          <g class="driftb">
            <rect x="270" y="120" width="70" height="80" rx="10" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <path d="M285 150 h40" stroke="#6366F1" stroke-width="8" stroke-linecap="round"/>
            <circle cx="96" cy="80" r="16" fill="#22C55E"/>
            <circle cx="70" cy="120" r="10" fill="#6366F1"/>
          </g>''',
        "family-chore-chart-desk": '''
          <g class="drift">
            <circle cx="140" cy="146" r="70" fill="none" stroke="@@" stroke-width="10"/>
            <path d="M140 146 L140 96 A50 50 0 0 1 183 166 Z" fill="#F59E0B"/>
            <path d="M140 146 L100 176 A50 50 0 0 1 140 96 Z" fill="#6366F1" opacity="0.9"/>
            <circle cx="140" cy="146" r="10" fill="#10192C"/>
          </g>
          <g class="driftb">
            <rect x="240" y="70" width="110" height="150" rx="14" fill="#17233A" stroke="#22C55E" stroke-width="2.5"/>
            <path d="M262 108 h16 M262 142 h16 M262 176 h16" stroke="#F59E0B" stroke-width="6" stroke-linecap="round"/>
            <path d="M290 108 h36 M290 142 h36 M290 176 h36" stroke="#C9D4EA" stroke-width="3" stroke-linecap="round"/>
          </g>''',
        "receipt-and-expense-desk": '''
          <g class="drift">
            <path d="M150 48 h100 l0 190 -16-12 -16 12 -16-12 -16 12 -16-12 -20 12z" fill="#F4F0E6" stroke="@@" stroke-width="2.5"/>
            <path d="M170 86 h60 M170 110 h60 M170 134 h40" stroke="#334155" stroke-width="3" stroke-linecap="round"/>
            <path d="M170 170 h60" stroke="#0B1220" stroke-width="4" stroke-linecap="round"/>
          </g>
          <g class="driftb">
            <rect x="40" y="120" width="90" height="56" rx="10" fill="#17233A" stroke="#F59E0B" stroke-width="2.5"/>
            <path d="M56 148 h58" stroke="#F59E0B" stroke-width="4" stroke-linecap="round"/>
          </g>''',
        "travel-itinerary-desk": '''
          <g class="drift">
            <path d="M50 200 C120 120, 180 210, 240 130 S340 80, 360 110" stroke="@@" stroke-width="3" fill="none" stroke-linecap="round"/>
            <circle cx="50" cy="200" r="8" fill="#22C55E"/>
            <circle cx="240" cy="130" r="8" fill="#F59E0B"/>
            <circle cx="360" cy="110" r="8" fill="#6366F1"/>
          </g>
          <g class="driftb">
            <path d="M168 70 l48 16 -18 8 22 22 -12 6 -16-18 -10 6z" fill="#F59E0B"/>
          </g>
          <path class="draw" d="M70 230 H330" stroke="#C9D4EA" stroke-width="2" stroke-dasharray="3 8"/>''',
        "event-planner-desk": '''
          <g class="drift">
            <rect x="48" y="64" width="140" height="150" rx="16" fill="#17233A" stroke="@@" stroke-width="2.5"/>
            <path d="M48 104 H188" stroke="#F59E0B" stroke-width="6"/>
            <circle cx="86" cy="150" r="8" fill="#22C55E"/>
            <circle cx="122" cy="150" r="8" fill="#6366F1"/>
            <circle cx="158" cy="186" r="8" fill="#F59E0B"/>
          </g>
          <g class="driftb">
            <rect x="214" y="80" width="140" height="120" rx="16" fill="#17233A" stroke="#22C55E" stroke-width="2.5"/>
            <path d="M236 116 h96 M236 142 h70 M236 168 h80" stroke="#C9D4EA" stroke-width="3" stroke-linecap="round"/>
          </g>''',
    }


SCENES = _scenes()


def illustration(num, slug, accent, label):
    body = SCENES[slug]
    return poster(num, accent, label, body)
