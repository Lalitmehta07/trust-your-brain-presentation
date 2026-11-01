import sys
p = '/workspace/index.html'
s = open(p, encoding='utf-8').read()

def rep(old, new, cnt=1):
    global s
    assert s.count(old) == cnt, "anchor count %d != %d: %r" % (s.count(old), cnt, old[:80])
    s = s.replace(old, new)

# ---------- 1. CSS additions (before </style>) ----------
css_extra = """
/* ---- Revision 2: per-slide music toggle ---- */
.music-toggle{min-height:44px;padding:6px 14px;border:1px solid var(--line);border-radius:999px;background:var(--paper);font-size:clamp(10px,1vw,14px);font-weight:700;color:var(--muted);cursor:pointer;box-shadow:var(--neu-out);white-space:nowrap}
.music-toggle[aria-pressed="true"]{color:var(--cobalt);border-color:var(--cobalt);box-shadow:var(--neu-in)}
/* ---- Slide 4: dots + impact rings ---- */
.dot-b{fill:#0F172A}
.dot-w{fill:#FFFFFF;stroke:#CBD5E1;stroke-width:2}
.imp-ring{fill:none;stroke:#16A34A;stroke-width:6;opacity:0}
.s4-vote{display:flex;gap:clamp(10px,1.6vw,22px);flex-wrap:wrap;justify-content:center;margin-top:6px}
/* ---- Slide 5: speech status ---- */
.speech-note{margin-top:6px;font-size:clamp(10px,1.05vw,15px);font-weight:700;color:var(--muted);text-align:center;min-height:1.4em}
/* ---- Slide 6: verb chips + collision anim ---- */
.lp-collide{background:var(--paper);border:1px solid var(--line);border-radius:14px;box-shadow:var(--neu-in);padding:6px}
.cars-svg{width:100%;height:auto;display:block}
.verb-chips{display:flex;gap:clamp(6px,1vw,14px);flex-wrap:wrap;justify-content:center;margin-top:8px}
.chip-btn{min-height:44px;padding:8px 16px;border:1.5px solid var(--line);border-radius:999px;background:var(--paper);font-weight:800;font-size:clamp(11px,1.2vw,17px);cursor:pointer;color:var(--ink)}
.chip-btn:hover{border-color:var(--cobalt);color:var(--cobalt)}
.chip-btn.on{border-color:var(--cobalt);color:var(--cobalt);box-shadow:var(--neu-in)}
/* ---- Slide 7: gorilla video player ---- */
.gv-shell{background:#0B1220;border-radius:14px;overflow:hidden;box-shadow:var(--neu-in)}
.gv-video{display:block;width:100%;aspect-ratio:16/9;background:#000}
.gv-bar{display:flex;align-items:center;gap:10px;padding:8px 12px;background:#111827}
.gv-play,.gv-replay,.gv-mute{min-height:40px;padding:6px 14px;border:1px solid #374151;border-radius:10px;background:#1F2937;color:#E5E7EB;font-weight:700;font-size:clamp(11px,1.1vw,15px);cursor:pointer}
.gv-time{font-family:var(--mono);font-size:clamp(10px,1vw,14px);color:#9CA3AF;white-space:nowrap}
.gv-track{position:relative;flex:1;height:10px;background:#374151;border-radius:6px;cursor:pointer;min-width:80px}
.gv-prog{position:absolute;left:0;top:0;bottom:0;width:0%;background:var(--cobalt);border-radius:6px;pointer-events:none}
</style>"""
rep('</style>', css_extra)

# ---------- 2. Remove global BGM button from topbar ----------
rep('    <button class="icon-btn audio-toggle" id="bgmBtn" type="button" aria-pressed="false" title="Background music (off)">Music \u00b7 Off</button>\n', '')

# ---------- 3. Per-slide music toggle in nav-cluster ----------
rep('<span class="slide-ind" id="slideInd">1 / 10</span>',
    '<span class="slide-ind" id="slideInd">1 / 10</span>\n      <button class="music-toggle" id="musicToggle" type="button" aria-pressed="false" title="Play this slide\u2019s background music">Music \u00b7 Off</button>')

# ---------- 4. SLIDE 1: restore opening content, remove five-dot experiment ----------
s1_start = s.index('      <!-- ================= SLIDE 1')
s1_end = s.index('      <!-- ================= SLIDE 2 : Ebbinghaus ================= -->')
new_s1 = '''      <!-- ================= SLIDE 1 : Title / opening ================= -->
      <section class="slide" id="s1" aria-label="Slide 1: title and opening question">
        <div class="slide-bg" aria-hidden="true"><svg viewBox="0 0 960 540" preserveAspectRatio="xMidYMid slice"><g class="anim-a"><circle class="bg-orb" cx="820" cy="90" r="180" stroke="#2547D1"></circle><circle class="bg-orb" cx="820" cy="90" r="120" stroke="#2547D1"></circle></g><g class="anim-d"><rect x="60" y="430" width="140" height="140" rx="24" fill="#0F172A" opacity=".04"></rect></g></svg></div>
        <div style="display:flex;flex-direction:column;align-items:center;flex:1 1 auto;min-height:0;gap:clamp(6px,1.4vh,16px);justify-content:center;text-align:center">
          <p class="eyebrow">Perception \u00b7 01</p>
          <h1 class="title" id="s1-title">Can You Trust Your Own Brain?</h1>
          <p class="instruction" id="fd-instruction" style="max-width:min(90%,900px)">How perception, attention, memory and judgement shape our reality \u2014 demonstrated live, on this screen, with you as the participants.</p>
          <div class="stim-card" style="width:min(92%,860px);display:flex;align-items:center;justify-content:center;gap:clamp(18px,3vw,44px);padding:clamp(10px,1.6vh,20px) clamp(14px,2vw,28px)">
            <svg viewBox="0 0 96 96" width="72" height="72" role="img" aria-label="An eye whose pupil is a five-pointed star." style="flex:0 0 auto"><circle cx="48" cy="48" r="44" fill="none" stroke="#2547D1" stroke-width="4" opacity=".85"></circle><path d="M48 26 l6.5 13.5 15 2 -11 10.5 3 15 -13.5 -7.5 -13.5 7.5 3 -15 -11 -10.5 15 -2 z" fill="#2547D1" opacity=".9"></path></svg>
            <p style="font-weight:800;font-size:clamp(13px,1.5vw,22px);color:var(--ink-soft);line-height:1.35;margin:0">Ten slides. Six live experiments. One question: how much of what you experience is your brain\u2019s interpretation?</p>
          </div>
          <p class="credit credit-inline"><img class="avatar" src="__PROFILE_B64__" alt="Portrait of the presenter, Lalit Mehta" width="44" height="44"><span>Presented by <strong>Lalit Mehta</strong></span></p>
          <p class="evidence">Opening slide \u00b7 the demonstrations that follow draw on Simons &amp; Chabris (1999); Rensink, O\u2019Regan &amp; Clark (1997)</p>
        </div>
      </section>

'''
s = s[:s1_start] + new_s1 + s[s1_end:]

# ---------- 5. SLIDE 4 HTML ----------
rep('<section class="slide" id="s4" aria-label="Slide 4: selective attention counting task">',
    '<section class="slide" id="s4" aria-label="Slide 4: inattentional blindness \u2014 count the white dot\u2019s bounces">')
rep('<h1 class="title" id="s4-title">Count the White Ball\u2019s Bounces</h1>\n          <p class="instruction">For 12 seconds, silently count how many times the WHITE ball hits a wall. Ignore the dark disc.</p>',
    '<h1 class="title" id="s4-title">Count the White Dot\u2019s Bounces</h1>\n          <p class="instruction">For 12 seconds, silently count how many times the WHITE dot hits a wall. It bounces exactly ten times \u2014 make each one easy to see.</p>')
rep('<svg id="arena-svg" viewBox="-12 -12 984 524" role="img" aria-label="An arena with one white ball and one dark disc moving and bouncing off the walls. Count only the white ball\u2019s wall bounces.">\n                  <rect id="arena-bg" x="0" y="0" width="960" height="500" rx="14" fill="#64748B" stroke="#334155" stroke-width="4" style="transition:stroke .3s linear"></rect>\n                  <g id="arena-discs"></g>\n                  <polygon id="arena-star" points="" fill="#0F172A" opacity="0"></polygon>\n                  <g id="arena-highlights" opacity="0" style="transition:opacity .3s"></g>',
    '<svg id="arena-svg" viewBox="-12 -12 984 524" role="img" aria-label="An arena with five black dots and one white dot drifting around. The white dot bounces off the walls ten times in twelve seconds. Count only the white dot\u2019s wall bounces.">\n                  <rect id="arena-bg" x="0" y="0" width="960" height="500" rx="14" fill="#64748B" stroke="#334155" stroke-width="4" style="transition:stroke .3s linear"></rect>\n                  <g id="arena-discs"></g>\n                  <polygon id="arena-star" points="" fill="#EA580C" stroke="#0F172A" stroke-width="2" opacity="0"></polygon>\n                  <g id="arena-highlights" opacity="0" style="transition:opacity .3s"></g>')
rep('<div class="counter-chip" id="s4-counter" style="display:none">White bounces: <span id="s4-count">0</span></div>',
    '<div class="counter-chip" id="s4-counter" style="display:none">White bounces: <span id="s4-count">0</span></div>\n            <div class="counter-chip" id="s4-answer" style="display:none">The answer is <strong>10</strong>.</div>')
rep('<div class="row ask"><span class="k">Ask</span><span class="v">Eyes on the arena. Count the white ball\u2019s wall bounces only. Keep the number to yourself.</span></div>',
    '<div class="row ask"><span class="k">Ask</span><span class="v">Eyes on the arena. Count the white dot\u2019s wall bounces only \u2014 each bounce flashes green on the wall. Keep your number secret until the reveal.</span></div>')
rep('<div class="row reveal hidden-row" id="s4-reveal"><span class="k">Reveal</span><span class="v">The white ball hit the walls 6 times. Did you also notice the dark star drifting across the middle, and the border turning from slate to crimson?</span></div>',
    '<div class="row reveal hidden-row" id="s4-reveal"><span class="k">Reveal</span><span class="v">The white dot hit the walls exactly 10 times. Now the honest questions: did the circle-into-square change catch your eye? Did you notice the orange star travelling across the arena?</span></div>\n            <div class="row ask hidden-row" id="s4-askblind"><span class="k">Ask</span><span class="v">Hands up if you noticed the shape change. Hands up for the travelling star. Watch how many hands stay down while everyone was busy counting.</span></div>')
rep('<button class="act-btn" id="act-s4" type="button">Start the 12-second task</button>',
    '<button class="act-btn" id="act-s4" type="button">Start the 12-second task</button>\n              <button class="act-btn" id="s4-replay-btn" type="button" disabled>Replay with highlights</button>')

# ---------- 6. SLIDE 5 HTML ----------
rep('<p class="instruction">Words will appear one at a time. Read silently \u2014 don\u2019t write, don\u2019t speak.</p>',
    '<p class="instruction">Words appear one at a time in large type and are spoken aloud. Just listen and read \u2014 don\u2019t write, don\u2019t speak.</p>')
rep('<p class="idle-hint">Press start. Words appear for about a second each.</p>',
    '<p class="idle-hint">Press start. Each word appears large and is spoken aloud, then the next follows automatically.</p>')
rep('<button class="act-btn" id="act-s5" type="button">Start the word list</button>',
    '<button class="act-btn" id="s5-prev" type="button" disabled>Previous</button>\n              <button class="act-btn" id="act-s5" type="button">Start the word list</button>\n              <button class="act-btn" id="s5-pause" type="button" disabled>Pause</button>\n              <button class="act-btn" id="s5-next" type="button" disabled>Next</button>\n              <button class="act-btn" id="s5-auto" type="button" aria-pressed="true">Auto: On</button>\n              <p class="speech-note" id="s5-speech" role="status" aria-live="polite"></p>')

# ---------- 7. SLIDE 6 HTML ----------
rep('''<svg class="crash-svg" viewBox="0 0 340 150" role="img" aria-label="Simple illustration of two stylized cars meeting at an intersection.">''',
    '''<div class="lp-collide"><svg class="cars-svg" id="lp-cars" viewBox="0 0 340 150" role="img" aria-label="Animated scene: a blue car drives in from the left and a red car crosses the intersection; they collide with a brief flash. Nothing graphic."><g id="lp-cars-scene">''')
rep('''                <g transform="translate(96,78)">
                  <rect x="-46" y="-14" width="92" height="26" rx="8" fill="#2547D1"></rect>
                  <rect x="-26" y="-26" width="46" height="16" rx="6" fill="#2547D1"></rect>
                  <circle cx="-28" cy="14" r="8" fill="#0F172A"></circle><circle cx="26" cy="14" r="8" fill="#0F172A"></circle>
                </g>
                <g transform="translate(216,52) rotate(90)">
                  <rect x="-46" y="-14" width="92" height="26" rx="8" fill="#E11D48"></rect>
                  <rect x="-26" y="-26" width="46" height="16" rx="6" fill="#E11D48"></rect>
                  <circle cx="-28" cy="14" r="8" fill="#0F172A"></circle><circle cx="26" cy="14" r="8" fill="#0F172A"></circle>
                </g>
                <g stroke="#F59E0B" stroke-width="4" stroke-linecap="round">
                  <line x1="160" y1="66" x2="150" y2="52"></line><line x1="166" y1="60" x2="162" y2="44"></line><line x1="172" y1="66" x2="184" y2="54"></line>
                </g>
              </svg>''',
    '''                <g id="lp-car-a" transform="translate(-120,78)">
                  <rect x="-46" y="-14" width="92" height="26" rx="8" fill="#2547D1"></rect>
                  <rect x="-26" y="-26" width="46" height="16" rx="6" fill="#2547D1"></rect>
                  <circle cx="-28" cy="14" r="8" fill="#0F172A"></circle><circle cx="26" cy="14" r="8" fill="#0F172A"></circle>
                </g>
                <g id="lp-car-b" transform="translate(216,-120) rotate(90)">
                  <rect x="-46" y="-14" width="92" height="26" rx="8" fill="#E11D48"></rect>
                  <rect x="-26" y="-26" width="46" height="16" rx="6" fill="#E11D48"></rect>
                  <circle cx="-28" cy="14" r="8" fill="#0F172A"></circle><circle cx="26" cy="14" r="8" fill="#0F172A"></circle>
                </g>
                <g id="lp-flash" stroke="#F59E0B" stroke-width="4" stroke-linecap="round" opacity="0">
                  <line x1="160" y1="66" x2="150" y2="52"></line><line x1="166" y1="60" x2="162" y2="44"></line><line x1="172" y1="66" x2="184" y2="54"></line>
                </g>
                </g></svg></div>
              <div class="verb-chips" id="lp-chips" role="group" aria-label="Choose the verb used in the question">
                <button class="chip-btn" data-verb="contacted" type="button">CONTACTED</button>
                <button class="chip-btn" data-verb="hit" type="button">HIT</button>
                <button class="chip-btn" data-verb="bumped" type="button">BUMPED</button>
                <button class="chip-btn" data-verb="collided" type="button">COLLIDED</button>
                <button class="chip-btn" data-verb="smashed" type="button">SMASHED</button>
              </div>''')
rep('<p class="axis-note">Average estimated speed (mph) \u00b7 axis 0\u201345</p>',
    '<p class="axis-note">Average estimated speed (mph) \u00b7 axis 0\u201345 \u00b7 bars grow when revealed</p>')
rep('<button class="act-btn" id="act-s6" type="button">Show the first word</button>',
    '<button class="act-btn" id="act-s6" type="button">Play the collision film</button>\n              <button class="act-btn" id="s6-replay" type="button" disabled>Replay the film</button>')

# ---------- 8. SLIDE 7 HTML: full section replacement ----------
s7_start = s.index('      <!-- ================= SLIDE 7 : Confirmation bias ================= -->')
s7_end = s.index('      <!-- ================= SLIDE 8 : Confidence & accuracy ================= -->')
new_s7 = '''      <!-- ================= SLIDE 7 : Gorilla video + confirmation bias ================= -->
      <section class="slide" id="s7" aria-label="Slide 7: selective attention video and confirmation bias investigation">
        <div class="slide-bg" aria-hidden="true"><svg viewBox="0 0 960 540" preserveAspectRatio="xMidYMid slice"><g class="anim-c"><circle class="bg-orb" cx="80" cy="470" r="130" stroke="#E11D48"></circle></g><g class="anim-b"><path d="M700,80 q60,-40 120,0 t120,0" fill="none" stroke="#2547D1" stroke-width="3" opacity=".05"></path></g></svg></div>
        <div>
          <p class="eyebrow">Judgement \u00b7 07</p>
          <h1 class="title" id="s7-title">Count the Passes \u2014 Then Check Your Assumptions</h1>
          <p class="instruction">Two demos, one theme: what you attend to shapes what you believe. First, watch the clip and count every pass made by the <strong>WHITE team</strong>. Don\u2019t announce the count yet \u2014 and don\u2019t spoil it for anyone watching later.</p>
        </div>
        <div class="cols">
          <div class="stim-col">
            <div class="gv-shell">
              <video id="gorilla-video" class="gv-video" src="classroom-clip.mp4" preload="metadata" playsinline controls aria-label="Excerpt from The Monkey Business Illusion by Daniel Simons: people pass basketballs while an unexpected event unfolds."></video>
              <div class="gv-bar">
                <button class="gv-play" id="gv-play" type="button" aria-label="Play or pause the video">Play</button>
                <button class="gv-replay" id="gv-replay" type="button" aria-label="Replay the video from the start">Replay</button>
                <button class="gv-mute" id="gv-mute" type="button" aria-pressed="false" aria-label="Mute or unmute the video">Sound: On</button>
                <div class="gv-track" id="gv-track" role="slider" aria-label="Video position" tabindex="0"><div class="gv-prog" id="gv-prog"></div></div>
                <span class="gv-time" id="gv-time">0:00 / 0:36</span>
              </div>
            </div>
            <div class="cb-result" id="cb-result" role="status" aria-live="polite"></div>
          </div>
          <div class="side-col">
            <div class="row ask"><span class="k">Ask</span><span class="v">After the clip: how many passes did the white team make? And \u2014 did you notice the gorilla? Anyone spot the other mid-scene change?</span></div>
            <div class="row reveal hidden-row" id="s7-gorillareveal"><span class="k">Reveal</span><span class="v">A person in a gorilla suit walks through the scene. Many viewers miss it while counting passes \u2014 that is inattentional blindness, not bad eyesight.</span></div>
            <div class="row why hidden-row" id="s7-why"><span class="k">Why</span><span class="v">Attention is a limited resource. What you focus on determines what you fail to see \u2014 and what you miss becomes evidence you never weigh.</span></div>
            <div class="row"><span class="k">Investigate</span><span class="v">Now a short fictional case. Claim: <strong>\u201cThis study method improves test scores.\u201d</strong> Form a gut judgement first, then tap any evidence card to inspect it.</span></div>
            <div class="ev-grid" id="ev-grid" role="group" aria-label="Evidence cards \u2014 tap to inspect">
              <button class="ev-card sup" data-ev="a" type="button"><span class="ev-k">Class A report</span><span class="ev-t">\u201cStudents using the method say they feel more prepared.\u201d</span><span class="ev-back">Feeling prepared isn\u2019t measured learning.</span></button>
              <button class="ev-card sup" data-ev="b" type="button"><span class="ev-k">Post on social media</span><span class="ev-t">\u201cMy grades went up after I started this method!\u201d</span><span class="ev-back">One happy post \u2014 no comparison group.</span></button>
              <button class="ev-card dis" data-ev="c" type="button"><span class="ev-k">Controlled comparison</span><span class="ev-t">A similar class that kept old habits scored just as high.</span><span class="ev-back">With a baseline, the gain shrinks to noise.</span></button>
              <button class="ev-card dis" data-ev="d" type="button"><span class="ev-k">Follow-up year</span><span class="ev-t">Last year\u2019s users regressed to their previous average scores.</span><span class="ev-back">Regression to the mean explains the \u201ccure.\u201d</span></button>
            </div>
            <div class="action-zone">
              <button class="act-btn" id="act-s7" type="button">Reveal the overlooked evidence</button>
            </div>
          </div>
        </div>
        <div class="callout callout-q" id="s7-takeaway" hidden>What evidence would change my mind?</div>
        <p class="evidence">Evidence \u00b7 Simons &amp; Chabris (1999), \u201cThe Monkey Business Illusion\u201d (local classroom excerpt, 0:05\u20130:41); Nickerson (1998) \u00b7 the fictional evidence cards are a classroom illustration, not real data</p>
      </section>

'''
s = s[:s7_start] + new_s7 + s[s7_end:]

# ---------- 9. SLIDE 8: remove confidence sliders ----------
rep('<p class="instruction">Feeling sure and being right are different things \u2014 but they are not opposites. Predict each claim, set your confidence, then reveal.</p>',
    '<p class="instruction">Feeling sure and being right are different things \u2014 but they are not opposites. Commit to each answer, then reveal.</p>')
rep('<span class="conf-wrap">Confidence <input class="conf-range" type="range" min="50" max="100" value="70" step="5" aria-label="Confidence percent"><span class="conf-val">70%</span></span>', '', 2)

open(p,'w',encoding='utf-8').write(s)
print("HTML edits OK; size:", len(s))
