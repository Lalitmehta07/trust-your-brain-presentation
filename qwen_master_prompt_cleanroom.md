CLEAN-ROOM MASTER BUILD PROMPT
Project: “Can You Trust Your Own Brain?” — a new interactive science presentation

READ THIS FIRST
This is a completely new project. Treat this prompt as the complete specification and start from a clean implementation. Do not rely on previous conversations, hidden context, previous prompts, old files, or an existing deck. Do not read, copy, refactor, or modify any pre-existing presentation code in the workspace. Do not require an existing index.html to be attached. If a Research Brief PDF is attached, use it only as scientific background; this prompt is the implementation source of truth. That PDF contains historical discussion and older draft directions, some of which conflict with this prompt. Ignore those older implementation instructions wherever they conflict.

Do not merely describe what you would build. Build it, save it to disk, and verify it with the tools available in your coding environment. Do not ask questions first. Make reasonable choices where a detail is unspecified and record consequential assumptions in README.md.

======================================================================
1. ROLE AND PROJECT GOAL
======================================================================
Act as a senior front-end engineer, interaction designer, accessibility-minded creative technologist, and careful science communicator. Build a polished, working, self-contained, 10-slide interactive presentation called:

“Can You Trust Your Own Brain?”
Subtitle: “How Perception, Attention, Memory, and Judgement Shape Our Reality”

The talk is for a mixed-background college classroom; assume no psychology background. It should run for approximately 8–12 minutes, aiming for about 11 minutes before questions. It should make the audience participate in short first-person demonstrations, then explain what each demonstration does and does not show.

Core thesis: The brain is not broken and is not generally unreliable. It is fast and adaptive, using context, expectations, memory associations, and mental shortcuts to interpret a complicated world. Those efficient processes have predictable blind spots. Understanding them can help us make better decisions, but no technique guarantees perfect judgement.

Priority order:
1. Scientific accuracy and honest limitations.
2. Clarity for non-specialists.
3. Audience participation and pacing.
4. Visual quality and smooth operation.

Audience participation is by looking, silently counting, and raising hands. Do not require students to use phones or submit personal information.

======================================================================
2. CLEAN-ROOM IMPLEMENTATION AND DELIVERABLES
======================================================================
Create a new folder named `trust-your-brain-deck` in the current workspace, unless the current workspace is already an empty, dedicated project directory; in that case you may write the files at its root. Do not change or delete files outside this new project folder.

Create at minimum:
- `index.html` — the finished, directly runnable presentation.
- `README.md` — how to run it, controls, optional remote-sync requirements, verification actually performed, any limitations, and the references used.

Prefer one self-contained HTML file: CSS and JavaScript inline; experiment artwork drawn with inline SVG or Canvas; no separate images or build system. Do not depend on old image files, fonts, project-specific CSS classes, or prior implementation utilities. Use a system font stack so the deck is legible without a network connection. The presentation itself must work locally even when remote sync is unavailable. No build step should be necessary: opening `index.html` in a modern browser should work.

Do not paste a giant source file into the chat as multiple fragments and ask the user to concatenate it. Write the complete implementation to the project files using your filesystem/editor tools. Never leave placeholders such as `TODO`, `...rest unchanged`, `same as above`, omitted functions, or fake test results. Do not stop after making a plan. The work product is the actual functioning project.

If filesystem tools are genuinely unavailable, state that limitation and then provide a complete implementation in clearly numbered, contiguous code parts with exact boundaries. Otherwise, write the files directly.

======================================================================
3. DESIGN DIRECTION
======================================================================
Create a premium, restrained, modern scientific-exhibit/editorial visual identity from scratch. It should feel thoughtfully art-directed, not like a generic slide template or a dashboard. Use a light background, strong dark ink typography, a small consistent accent palette (for example cobalt/blue, coral, slate, and restrained amber), deliberate spacing, crisp borders, and subtle soft depth on interface panels only. Use strong, legible typography and obvious hierarchy. Use CSS variables and `clamp()`, `vw`, `vh`, grid/flex layouts, and SVG viewBoxes for responsive sizing.

Important visual rules:
- The stimulus or experiment is the main visual, not a decorative background.
- Do NOT add a paragraph describing abstract vector art behind every slide. Do NOT place decorative SVG patterns behind every slide. Ambient decoration should be minimal, subtle, and never compete with content.
- Stimulus artwork must be geometrically faithful and visually isolated. Do not put gradients, translucency, backdrop blur, blending, background sheen, or animated decoration over a stimulus. In particular, the identical gray patches on Slide 1 must not be tinted differently by any overlay.
- Use a solid white stimulus card for the precision visual tasks. No translucent background or `backdrop-filter` on or above the stimulus card.
- Use no emoji anywhere: not in slide text, buttons, code comments, labels, alt text, or remote cues. Icons may be simple inline SVG line icons or CSS shapes. Do not require an icon CDN.
- Avoid unnecessary text on the canvas. Public-facing slide copy must be concise, large, and readable from the back of a classroom. Put speaker guidance in a private presenter/remote cues panel, not in long visible paragraphs.
- Use a stable 16:9 stage. Support at least 1280×720, 1920×1080, and 3840×2160. Account for browser CSS viewport size differing from physical pixel resolution and devicePixelRatio; do not assume 4K means a 3840 CSS-pixel viewport.
- Fit all slide content without horizontal or vertical page scrolling. On smaller viewports, shrink the stimulus before clipping text. Use `min-height: 0`, responsive grid/flex, and sensible `clamp()` limits.
- At 1080p, primary action/touch buttons should be at least approximately 56 CSS pixels high where practical. All interactive controls must have visible labels and a useful focus style.
- Respect `prefers-reduced-motion` for decorative transitions. The 12-second attention arena is the experiment itself, so its task animation must still run; decorative animations elsewhere can be reduced or disabled.
- No external images, videos, tracking, analytics, or remote fonts. All experiment drawings must be generated locally in SVG/Canvas. If remote-sync libraries/services are used, they must be optional and fail gracefully, without breaking the presentation.

Make the opening and experiment slides visually striking through scale, contrast, precise stimuli, controlled animation, and progressive disclosure—not through decorative noise.

======================================================================
4. APP STRUCTURE AND GLOBAL CONTROLS
======================================================================
Build a single-page slide deck with exactly ten slides, in this order. Each slide should be a stage-sized section and only one slide should be active/visible at a time. Provide:
- A restrained top bar with presentation title/current section and a fullscreen control.
- Clear previous/next controls and a 10-step progress indicator.
- A visible current-slide indicator.
- A running presentation timer; Slide 10 may also show the elapsed time in the Q&A state.
- Keyboard navigation and presenter actions.
- A replay row on Slide 10 for the main interactive experiments.
- A small on-slide evidence/source line for each science slide.
- A concise, private presenter cue for each slide, accessible in a presenter panel and (if remote sync works) the phone remote.

Required keyboard behaviour:
- ArrowRight / PageDown / N: next slide.
- ArrowLeft / PageUp / P: previous slide.
- Number keys 1–9 go to those slides; 0 goes to Slide 10.
- F toggles fullscreen.
- A triggers the active slide’s next experiment action when the active slide has a demo.
- Keep Tab as normal focus navigation. Do not hijack Tab for experiment actions.
- Space/Enter may advance when focus is on the stage/background, but must keep native button/link activation intact when focus is on an interactive control. Do not intercept keyboard shortcuts when the event target is an input, textarea, select, or contenteditable element.
- If a demo action can be triggered by a keyboard shortcut, it must also be reachable by a visibly labelled button. Do not use accidental clicker keys to advance a demo: Space, Enter, PageDown, arrows, and digits navigate only.
- Touch swipe can navigate between slides, but do not treat a swipe on a button/control or active experiment stimulus as slide navigation.

Use clean architecture from scratch. Names such as `.slide`, `.is-active`, `.act-btn`, and `DEMO` are available if helpful, but no particular legacy class name or function is required. Keep slide state and demo state separate. Use a central `navigateToSlide()` function and a central `triggerActiveSlideAction()` function. Do not scatter unrelated keyboard, button, and remote logic across individual slides.

======================================================================
5. DEMO ACTION SYSTEM AND LIFECYCLE
======================================================================
Slides 1–7 have guided demo actions. Slides 8–10 do not. Build a central demo registry keyed by zero-based slide index (Slide 1 = index 0). Each demo object must provide:
- `label()` — the human-readable label for the next action, or `null` when finished.
- `act()` — perform exactly one next guided step.
- `reset()` — return to the slide’s pristine state, cancel all timers/animation frames, clear logs/counters, hide reveals, reset title and controls, and restore default visual values. It must be safe to call repeatedly at any time.

Each demo slide must have a clear, large action button whose label mirrors the current demo label. Also show a small “or press A” hint. A click, the A key, and (if enabled) the phone remote ACT command all call the same `triggerActiveSlideAction()` function. The button should be disabled or change to a clear finished state when the demo is complete.

Lifecycle requirements:
- Leaving a demo slide calls its `reset()` so no timers, animations, or hidden states leak into other slides.
- Entering a demo slide starts from a clean state. Replay buttons on Slide 10 must reliably replay the whole demo from its beginning.
- A reset cancels pending `setTimeout`/`requestAnimationFrame` work, pauses any running demo, and clears the current state. Resetting several times must not create duplicate handlers or loops.
- When `document.visibilityState` becomes hidden, stop/cancel active demo timers and RAF loops. The slide must remain resettable and resume only through an explicit action.
- Keep at most one active animation loop for decorative visuals or the current experiment at a time. Do not run timers on inactive slides.
- Experiment-reveal headlines must not spoil the answer before the audience has voted or completed the task. Use neutral questions at first, and reveal the explanation only when the relevant demo action is taken.
- On each active-slide change and after each action, update button labels, slide controls, progress, timer/status displays, and remote state consistently.
- Any slide-level status message must be updated through DOM text safely; do not inject user-provided values via `innerHTML`.

======================================================================
6. OPTIONAL PHONE REMOTE / ROOM SYNC
======================================================================
Implement a simple phone remote at `?mode=remote` if it can be done reliably in the available environment. This must be a newly implemented, optional feature—not copied from any old project. Core deck operation must not depend on it.

Remote requirements:
- Remote UI has large Prev, Next, ACT, jump-to-slide 1–10 controls, current slide/progress, connection status, a timer, and private presenter cues for the current slide.
- Use a new default room topic such as `trust-brain/lalit/2026`; do not use any prior project’s room topic. Permit changing the room topic in a clearly labelled room/settings dialog if feasible.
- If MQTT over WebSockets is implemented, use a public broker only as an optional transport and document that public brokers are not private. Use the message types below and prevent message loops:
  - Navigation message: `{type:'NAV', slideIndex, timestamp, src}`.
  - Remote action: `{type:'ACT', slideIndex, timestamp, src:'remote'}`.
  - Board state: `{type:'STATE', slideIndex, label, hasDemo, timestamp, src:'board'}`.
- Board accepts ACT only if the source is `remote`, the message index matches the current slide, and it is not an echo. Remote ignores its own ACT messages and board should ignore its own STATE messages. Keep remote navigation messages from causing feedback loops; preserve source/echo protection.
- The remote ACT label must mirror the current slide’s next demo action. If the current slide has no demo, disable ACT and explain that no demo action is available.
- If connection or CDN/network access fails, show a clear disconnected/unavailable status. The local deck and its controls must keep working without errors.
- Do not claim remote sync was tested against a live broker unless it actually was.
- Do not make a QR-code image or external script critical to deck startup. A QR code can be generated through an optional online service if connectivity exists; also show the remote URL/room details as readable text so the feature is not QR-only.

If implementing remote sync would materially destabilize the core app or the environment has no way to test it, build a clean local remote UI shell with gracefully disabled sync, document that limitation accurately, and finish the core deck. Do not fake a connected status.

======================================================================
7. SCIENTIFIC ACCURACY RULES — NON-NEGOTIABLE
======================================================================
Use plain language, calibrated claims, and visible author-year source lines. The presentation should never frame the brain as broken, as a liar, or as generally unreliable. It should never suggest that everyone fails an experiment. Use phrasing such as “many people,” “can,” “often,” and “results vary.”

Allowed framing:
- “Your visual system judges brightness and size by comparison with the surroundings.”
- “Perception combines the image with expectation; one drawing can support two readings.”
- “When attention is busy, unexpected things can go unnoticed.” Not noticing is different from forgetting.
- “Memory keeps the gist and rebuilds details; a rebuilt memory can feel real.”
- “A question can carry information, and that information can blend into what we remember.”
- “We tend to test examples that should get a ‘yes’.”
- “Confidence can be wrong. That is not the same as confidence always being wrong.”
- “Habits that change the process can reduce errors; awareness of bias alone is not enough. We may spot bias in other people more easily than in ourselves.”

Do not claim or imply:
- All memories are false, memory is a video recording that gets edited, or eyewitnesses are always wrong.
- Everyone misses the same surprise, a missed event proves carelessness, or a classroom exercise is an exact replication of a published experiment.
- Confidence is always misleading or confident people are usually incompetent.
- The “10% of the brain” myth, fixed attention-span myths, left-brain/right-brain personality claims, learning styles, or a Dunning–Kruger curve.
- Any invented sample size, percentage, effect size, study result, or “studies show” claim without a traceable source.
- Percentages purporting to quantify the strength of an optical illusion.

For classroom versions of the Wason and DRM tasks, state that this is a “classroom demonstration, not an exact replication.” Keep the audience’s dignity intact: no calling out individuals or treating a wrong answer as a personal failure.

Verified numerical facts that may be used in science copy (do not introduce other numerical research statistics without verifying a primary source):
1. Loftus & Palmer (1974), Experiment 1: 45 students watched 7 short car-crash film clips. Asked “About how fast were the cars going when they ___ each other?”, the mean estimates were: contacted 31.8 mph, hit 34.0 mph, bumped 38.1 mph, collided 39.3 mph, smashed 40.8 mph. The difference from contacted to smashed is 9.0 mph. IMPORTANT: use 40.8 for “smashed”; older draft material may incorrectly say 40.5.
2. Loftus & Palmer (1974), Experiment 2: 150 students; one week later, when asked whether they had seen broken glass, 32% of the “smashed” group said yes, compared with 14% of the “hit” group and 12% of a control group not asked about speed. There was no broken glass in the film.
3. Drew, Võ & Wolfe (2013): 24 radiologists searched lung CT scans for nodules; a gorilla image about 48 times the size of a typical nodule was inserted into one case. 20 of 24 did not report it, and eye-tracking showed 12 of those 20 had looked directly at its location.
4. Wason (1960): in the 2–4–6 task, 6 of 29 participants announced the correct rule on their first announcement (about 1 in 5).
5. Brugger & Brugger (1993): one study found “rabbit” was the most common first answer when the duck-rabbit figure was shown around Easter, while “bird/duck” was more common in October. Present it as “one study found”; do not generalise it as a universal effect.
6. DRM, Roediger & McDermott (1995): if using a numerical summary, use this carefully bounded wording only: “In the original studies, many people falsely recalled the missing word — about 40% in free recall — and in recognition tests they said ‘yes’ to it about as often as to words actually shown. Rates in one classroom will vary.” This exact summary should be flagged in README.md as worth checking directly against the paper before presenting. Do not claim that a given percentage of this specific classroom will falsely remember the missing word.

======================================================================
8. VISUAL AND RESPONSIVE PATTERN FOR EXPERIMENT SLIDES
======================================================================
For Slides 2–7, use a clear header with an eyebrow/section label, neutral question title, and one short instruction. Beneath it, use a responsive two-column layout when the viewport allows:
- Left, around 60%: solid white stimulus card, ideally at least about 40% of the stage width at 1080p, with the actual experiment as the hero.
- Right, around 40%: a compact sequence of four labelled rows: Ask, Reveal, Why, Careful. Ask is visible from the beginning; Reveal/Why/Careful are progressively disclosed at the appropriate action stage.
- Place the action button and “or press A” hint in a stable, reachable position.
- Add a discreet evidence line near the bottom of the slide, not hidden inside presenter notes.

The page must not scroll at 1280×720, 1920×1080, or 3840×2160. Use `min-height: 0`, responsive grids, `clamp()` and relative units so the stimulus shrinks before text becomes clipped. If a two-column layout is too cramped at 1280×720, allow the columns to rebalance or become a compact stacked layout within the slide stage while keeping the task fully visible.

The main stimulus card should not become a generic “vector art illustration.” Each experiment has exact construction instructions below. Follow those rather than improvising an aesthetically similar but scientifically different picture.

======================================================================
9. EXACT TEN-SLIDE CONTENT AND INTERACTIONS
======================================================================
Preserve the intent, exact key text, and numeric parameters below. Minor punctuation changes are acceptable only if needed for readable layout; do not change scientific facts or the order of an experiment.

SLIDE 1 — TITLE + QUICK BRIGHTNESS TEST
Purpose: open with a quick, first-person surprise. Keep this slide visually distinctive and not overdecorated.
Visible copy:
- Eyebrow: “Live Experiments · 2026”
- Main heading: “Can You Trust” / accent line “Your Own Brain?”
- Subtitle: “Your brain isn’t broken — it’s fast, and fast comes with predictable blind spots. Let’s find a few together.”
- Presenter credit: “Lalit Mehta” with a simple LM monogram/avatar; do not expect any profile image file to exist.
- Three topic pills: “Perception”, “Attention & Memory”, “Judgement”.
- On the right, a solid-white stimulus card labelled “Quick test · 10 seconds” with the question “Do these two gray squares look the same?”
Stimulus requirements:
- Inline SVG `viewBox="0 0 400 220"`, `shape-rendering="crispEdges"`.
- Left half background rectangle x=0..200, fill `#1F1F1F`; right half x=200..400, fill `#EBEBEB`.
- Square A: x=55, y=65, width=90, height=90, fill exactly `#7A7A7A`.
- Square B: x=255, y=65, width=90, height=90, fill exactly `#7A7A7A`.
- A bridge rectangle x=145, y=90, width=110, height=40, fill exactly `#7A7A7A`, initially invisible/opacity 0.
- Keep all overlays and background effects off the stimulus so its colour values remain exact.
Readout before action: “Hands up: left looks lighter · right looks lighter · they look the same.”
Demo action 1 label: “Bridge the two squares”. Fade the bridge in over 0.6 seconds and change the readout to: “Same gray. Identical pixel values. Your brain judged each square by what surrounds it.”
Reset restores the bridge to opacity 0 and the initial readout.
Evidence line: “Simultaneous contrast · Adelson (2000)”.

SLIDE 2 — SIZE BY CONTEXT: EBBINGHAUS ILLUSION
Neutral title before reveal: “Which Orange Circle Is Bigger?”
Revealed title: “Your Eyes Judge Size by Comparison”.
Instruction: “Decide first. Hands up: left is bigger, right is bigger, or the same?”
Stimulus: inline SVG `viewBox="0 0 870 460"`.
- Both orange target circles have radius exactly 40, fill `#EA580C`, cy=230; left cx=230, right cx=640.
- Left target has 6 larger slate inducers, radius 60, fill `#94A3B8`, on a ring radius 132 around (230,230), at angles 0°, 60°, 120°, 180°, 240°, and 300°.
- Right target has 8 smaller slate inducers, radius 16, same fill, on a ring radius 78 around (640,230), at angles k×45° for k=0..7.
- Geometry must not overlap neighbouring inducer circles. The targets are exactly identical even though they may look different in context.
- A verification/caliper group starts at opacity 0: dashed dark horizontal lines at y=190 and y=270 from x=190 to x=680, plus a bold “=” between targets. Avoid obscuring the targets.
Demo: one action labelled “Verify the size”. Fade inducers to 10% opacity over 0.8 seconds, fade in the guides, reveal the title and the Reveal/Why/Careful rows.
Rows:
Ask: “Compare the two orange circles. No ruler yet — go with what you see.”
Reveal: “They are identical. The rings fade and the lines show the same width.”
Why: “Your visual system judges size by comparison with neighbours — a smart strategy in a 3-D world.”
Careful: “This doesn’t mean vision is ‘broken’, and the effect varies from person to person.”
Evidence: “Evidence · Massaro & Anderson (1971); Roberts, Harris & Yates (2005)”.

SLIDE 3 — AMBIGUOUS FIGURE: DUCK OR RABBIT
Neutral title before reveal: “Duck or Rabbit?”
Revealed title: “One Drawing, Two Interpretations”.
Instruction: “Which animal did you see first? Keep it to yourself — then try to find the other one.”
Draw one fixed line illustration as inline SVG `viewBox="0 0 600 440"`. Use the following outline path exactly, stroke `#0F172A`, stroke-width 7, round joins/caps, fill none. It is deliberately left open at the bottom; use an SVG mask with a vertical linear gradient that fades the lower 25% of the neck lines to transparent so there is no bottom line:
`M 330 112 C 270 98, 160 98, 64 124 C 48 130, 50 150, 68 152 C 150 160, 235 168, 300 182 L 300 192 C 235 190, 160 186, 92 182 C 74 182, 70 200, 90 204 C 160 212, 250 226, 308 262 C 316 300, 330 340, 336 400 L 492 400 C 486 340, 492 300, 500 262 C 540 258, 552 214, 538 178 C 524 140, 480 108, 420 104 C 385 102, 355 106, 330 112`.
Add this mouth line, stroke only, width 6, round cap: `M 462 254 C 490 258, 520 250, 537 233`.
Eye: filled circle at (378,180), r=14, fill `#0F172A`, plus white highlight at (383,175), r=4.5.
Interpretations: duck facing left; the two left projections are the bill. Rabbit facing right; the same two projections are ears and the short curve on the right is the mouth. Do not alter the line drawing between states. Only add translucent colour overlays BEHIND the line art, clipped to x<250, and labels.
Under the stimulus card provide two accessible small controls: “Duck reading” and “Rabbit reading”. Duck reading: amber overlay behind the left projections, labels “BILL” and “Duck: looks LEFT”. Rabbit reading: rose overlay behind the same projections, labels “EARS”, “MOUTH”, and “Rabbit: looks RIGHT”.
Demo action 1 label: “Show the duck reading”; apply amber overlay, reveal title and Reveal row. Action 2 label: “Show the rabbit reading”; apply rose overlay and reveal Why/Careful rows. After action 2 the demo is complete. Manual interpretation buttons still work. Reset clears highlights and returns to the neutral picture/title.
Rows:
Ask: “Hands up on my count: duck first, or rabbit first? Now try to flip it.”
Reveal: “Same lines, two readings: a bill facing left, or ears and a mouth facing right.”
Why: “Perception blends the lines with what you expect. One study found ‘rabbit’ was the most common first answer around Easter, and ‘bird’ in October.”
Careful: “Not ‘anything goes’: the lines allow only these two readings, and you usually see one at a time.”
Evidence: “Evidence · Jastrow (1899); Brugger & Brugger (1993); Kornmeier & Bach (2012)”.

SLIDE 4 — SELECTIVE ATTENTION: COUNT WHITE BOUNCES
Neutral title before reveal: “Count the White Bounces”.
Revealed title: “You Can Miss What Is Right in Front of You”.
Instruction: “Silently count how many times a WHITE disc bounces off a wall for 12 seconds. Ignore the dark discs.”
Build an arena using inline SVG or Canvas. Prefer a stable SVG viewBox `-12 -12 984 524` and an arena rectangle x=0,y=0,width=960,height=500, fill `#64748B`, rx=14, stroke `#334155`, width 4. Use 8 discs of radius 26: four white (`#FFFFFF`) and four dark (`#0F172A`). All discs move smoothly and may pass through one another; discs do not collide with each other.
Physics must be deterministic and time-based, not frame-count based. Use `performance.now()` and analytical triangle-wave folding per axis, so dropped frames do not change the count. For an axis, with `lo=R`, `hi=W-R` or `H-R`, `L=hi-lo`, and elapsed seconds `t`, compute `u=(p0-lo)+v*t`, `m=((u % (2*L))+2*L)%(2*L)`, then `pos=lo+(m<=L ? m : 2*L-m)`. Apply to both x and y. A wall bounce is when a disc centre reaches R or W-R on x, or R or H-R on y (the disc edge touches the arena wall). No sound, flash, ring, or other cue on a bounce. Task length exactly 12.0 seconds.
White disc starting positions and velocities in arena coordinates (px/s):
- W1: x0=210.2033, y0=108.5417, vx=133.1217, vy=60.7708.
- W2: x0=135.4850, y0=341.4616, vx=-207.5515, vy=-100.7433.
- W3: x0=166.9922, y0=385.6760, vx=-148.8655, vy=-101.5090.
- W4: x0=140.9494, y0=175.4572, vx=197.9411, vy=-54.7522.
These parameters produce exactly 15 white-disc wall bounces in 12 seconds: W1=2, W2=5, W3=4, W4=4. Expected bounce times (seconds): 0.53, 0.95, 2.73, 3.13, 3.54, 4.01, 4.90, 5.44, 6.01, 7.05, 7.58, 7.96, 8.59, 9.28, 10.91. Minimum time gap is 0.378 seconds; none occur in the first or last 0.4 seconds. Independently compute and test the bounce count; do not merely hardcode “15” as the test result.
Dark discs (they bounce but are not counted):
- D1: x0=480, y0=250, vx=-160, vy=120.
- D2: x0=700, y0=120, vx=-140, vy=-95.
- D3: x0=300, y0=400, vx=185, vy=-70.
- D4: x0=820, y0=380, vx=-120, vy=-150.
First-run surprises (do not mention or visually hint at these before the reveal):
- A dark five-pointed star, outer radius 30, fill `#0F172A`, enters at x=-40 and crosses horizontally at y=250 at constant speed, entering at t=3.5 s and reaching x=1000 at t=8.5 s. Draw it above the discs.
- At t=6.0 s the arena border transitions from `#334155` to crimson `#E11D48` over 0.3 s, then stays crimson.
- At t=8.0 s dark disc D1 morphs from circle into a square of side 46 over 0.4 s, then remains square. Its wall-collision bounds stay the original radius-26 bounds.
Under the arena add a thin time bar that fills linearly over 12 seconds. At t=12.0 seconds freeze the task and show: “Time! How many white-disc bounces?”
Demo action 1 label: “Start the 12-second task”; run the task. Action 2 becomes available after it ends, label “Reveal and replay”; replay the same time-based scene with orange highlights around the star, changed border, and morphing disc, with labels “star”, “border”, and “square”. Show a side-panel counter that tracks the 15 white-disc wall bounces during the replay; reveal the title and explanation rows. Do not introduce any additional cues during the count task.
Rows:
Ask: “Eyes on the arena. Count white-disc wall bounces only. Keep the number to yourself.”
Reveal: “White discs hit the walls 15 times. Did you also see a dark star crossing the middle, the border turn from slate to crimson, and a dark disc turn into a square?”
Why: “When attention is busy, unexpected things can go unnoticed. In one study, 20 of 24 radiologists searching lung scans missed a gorilla image — and 12 of those 20 looked right at it.”
Careful: “Not everyone misses these, and it isn’t carelessness. Not noticing is different from forgetting.”
Evidence: “Evidence · Simons & Chabris (1999); Drew, Võ & Wolfe (2013); Mack & Rock (1998)”.

SLIDE 5 — MEMORY: THE MISSING WORD
Neutral title before reveal: “Memorize the Words”.
Revealed title: “Memory Rebuilds. It Doesn’t Replay.”
Instruction: “Words will appear one at a time. Read silently — don’t write, don’t speak.”
Crucial spoiler rule: before the word-list activity finishes, do not show or say the missing lure word, do not mention its theme, and do not show icons or artwork that hint at the theme. Do not put the lure word in visible hidden DOM text or audience-accessible descriptions before reveal. The internal JS may know the data, but the audience must not see or hear it early.
Create a large central stimulus panel with four states, only one visible at a time, transitions by opacity: idle hint → one large word → poll view → results grid. Idle hint: “Press start. Words appear for about a second each.”
Word list, in this exact order: bed, rest, awake, tired, dream, wake, snooze, blanket, doze, slumber, snore, nap. Show each word uppercase for 1.0 second, then a blank view for 0.3 seconds. Show 12 small progress dots beneath the word panel. The sequence therefore takes 15.6 seconds. Use cancellable timers or a timing loop that reset/slide-leave can stop immediately.
After word 12, automatically switch to poll view with the question “Which of these were on the screen?” and four word chips: TIRED, BLANKET, SLEEP, WINDOW, plus “Hands up for each word you remember seeing.” Do not collect a tally; the presenter polls the room verbally.
Demo action 1 label: “Start the word list”; play the word sequence, then show the poll. Action 2 label: “Reveal which were shown”; mark TIRED and BLANKET “was shown”, WINDOW “not shown”, and mark SLEEP “NEVER shown” with a restrained coral pulse; reveal the title and the Reveal row. Action 3 label: “Show the full list”; show a grid of the 12 actually presented words plus a dashed coral tile “SLEEP — never on the screen”; reveal Why and Careful rows. Then finish.
Rows:
Ask: “After the list: show of hands for each word. Did you see it?”
Reveal: “‘Sleep’ was never shown. Every word you did see points toward it.”
Why: “Memory keeps the gist, and the gist can feel like a real memory. In the original studies, many people falsely recalled the missing word — about 40% in free recall — and in recognition tests they said ‘yes’ to it about as often as to words actually shown. Rates in one room will vary.”
Careful: “A hand up for ‘sleep’ isn’t a bad memory — it’s normal, gist-based memory.”
Evidence: “Evidence · Roediger & McDermott (1995); Deese (1959); Gallo (2010) · classroom demonstration, not an exact replication”.
Keep the missing-word result hidden until the relevant action. Reset must immediately cancel the word sequence and hide all results.

SLIDE 6 — SUGGESTION: LOFTUS & PALMER
Title: “Can One Word Change a Memory?”
Instruction: “Same film of a car crash. Same question. Only one word changes.”
Build a clear left-side evidence visualization with a simple, non-graphic stylized car-crash/intersection illustration (locally drawn, no external image). Show this sentence: “About how fast were the cars going when they ____ each other?” The selected verb should be bold and prominent. Reveal verb chips and horizontal bars progressively. Bar chart axis 0–45 mph, label “Average estimated speed (mph)”. Bars must show exact values:
- contacted: 31.8
- hit: 34.0
- bumped: 38.1
- collided: 39.3
- smashed: 40.8
Animate bars using transform: scaleX with transform-origin left; include readable numeric labels.
Demo actions:
1. Label “Show the first word”; show contacted and its 31.8 bar.
2. Label “Now change one word”; show smashed and its 40.8 bar, reveal the row: “About 9 mph apart, from a single word. (45 students watched crash films.)”
3. Label “Show the other three words”; reveal hit, bumped, collided and their data in order, using the exact values above.
4. Label “One week later”; show a panel: “One week later · ‘Did you see any broken glass?’” with three tiles: “32% asked ‘smashed’”, “14% asked ‘hit’”, “12% never asked about speed”, and the note “There was no broken glass in the film.” Reveal Why and Careful rows. Then finish.
Rows:
Ask: “Predict: how far apart will the average guesses be for ‘contacted’ and ‘smashed’?”
Why: “A question can carry information, and that information can blend into what we think we remember.”
Careful: “Not ‘witnesses are always wrong’. Researchers still debate exactly how the effect works.”
Evidence: “Evidence · Loftus & Palmer (1974); Loftus (2005)”.
IMPORTANT: use 40.8 mph for “smashed”, not 40.5. Do not change or exaggerate the published percentages.

SLIDE 7 — JUDGEMENT: THE SECRET RULE (WASON 2–4–6)
Neutral title before reveal: “Guess the Secret Rule”.
Revealed title: “Why We Lock Onto a Wrong Guess”.
Instruction: “The triple 2 – 4 – 6 fits a secret rule. Suggest triples to test — I’ll say yes or no.”
Show the seed row “Fits the rule: 2 – 4 – 6 [YES]”. Provide four large test buttons:
- “8 – 10 – 12” → YES
- “20 – 22 – 24” → YES
- “3 – 17 – 104” → YES (this should surprise people who guessed a +2/even-number rule)
- “10 – 8 – 6” → NO
The hidden rule is: “Any three numbers in ascending order (a < b < c).” Implement exactly `a < b && b < c` for the rule logic. The preset buttons and a “Your own triple” input control may append to a visible “Tested so far” log with YES/NO. If adding custom numbers, use three accessible numeric inputs or button-based steppers with validated bounds; custom controls must not interfere with global keyboard shortcuts.
Demo guided actions, in five steps:
1. “Test 8 – 10 – 12” → YES.
2. “Test 20 – 22 – 24” → YES.
3. “Test 3 – 17 – 104” → YES.
4. “Test 10 – 8 – 6” → NO.
5. “Reveal the rule” → show the ascending-number rule, change title, and reveal the explanation rows.
Manual test buttons remain usable at any time and write to the log. `reset()` clears the log and hides the rule banner.
Rows:
Ask: “Say your guess for the rule — then pick the test you think is most useful.”
Reveal: “Any ascending numbers fit. ‘+2’ and ‘even numbers’ were just guesses that happened to work.”
Why: “We tend to test examples that should get a ‘yes’. That builds confidence in a guess that may be too narrow.”
Careful: “Not stubbornness or dishonesty — it’s a natural default. In Wason’s 1960 study, only about 1 in 5 got it right on the first announcement.”
Evidence: “Evidence · Wason (1960); Klayman & Ha (1987); Nickerson (1998) · classroom demonstration, not an exact replication”.

SLIDE 8 — CONFIDENCE AND ACCURACY (NO DEMO)
Eyebrow: “Calibration · 08”
Title: “Confidence Does Not Guarantee Accuracy”
Subtitle: “Feeling sure and being right are different things — but they are not opposites.”
Present three concise, highly readable numbered rows/cards:
01, gauge icon — “Confidence is a feeling, not a measurement” / “It reflects how smoothly the story fits together in your head — not how much evidence you checked.” Tag: “Koriat 2012”.
02, check icon — “A clean first impression can be informative” / “Under fair conditions, confidence can carry useful information about accuracy. Reliability depends on how the judgement was made and what happened afterwards.” Tag: “Wixted & Wells 2017”.
03, caution icon — “Illusions and nudges can inflate certainty” / “Misleading context, divided attention, leading questions and untested assumptions can make a wrong answer feel as sure as a right one — like confident hands for the missing word.” Tag: “Slides 2 · 4 · 5 · 6 · 7”.
Callout: “Confidence can be wrong. That is not the same as confidence always being wrong.”
Evidence: “Evidence · Koriat (2012); Wixted & Wells (2017); Kahneman & Klein (2009)”.
No demo action on this slide. Avoid saying that confidence is generally useless or that confident witnesses are always wrong.

SLIDE 9 — PRACTICAL HABITS (NO DEMO)
Eyebrow: “Habits · 09”
Title: “How to Check Yourself”
Subtitle: “Knowing about biases isn’t enough. Changing the process helps.”
Use a readable four-row table or set of aligned cards with columns “Where”, “The brain’s shortcut”, “→”, “A habit that helps”:
- Seeing | Judges by surroundings | Measure it, don’t eyeball it: a ruler, a number, a second look.
- Attention | Filters out the unexpected | Don’t multitask when it matters; pause and scan on purpose.
- Memory | Fills gaps with what fits | Write it down early, and ask neutral questions, not leading ones.
- Judgement | Tests only for “yes” | Ask what would prove you wrong — then test that.
Footer: “These habits reduce errors in studies; they don’t remove bias. We spot bias in others more easily than in ourselves.”
Evidence: “Evidence · Lord, Lepper & Preston (1984); Pronin, Lin & Ross (2002); Milkman, Chugh & Bazerman (2009)”.
No demo action on this slide. Keep copy concise enough to read; use row highlights or simple icons, not decorative diagrams.

SLIDE 10 — CLOSING AND REPLAY
Eyebrow: “Closing · 10”
Title: “What Else Might You Be Missing?” with a restrained accent on the final words.
Thesis: “You can trust your brain to get you through a complex world. Just check what it skips, fills in, and assumes.”
Three pillar rows:
- “Perception & Attention — it compares, and it filters.”
- “Memory — it reconstructs.”
- “Judgement — it looks for ‘yes’, and feels sure.”
Add a clearly labelled “Replay an experiment” row of buttons that navigate to and cleanly reset:
- Size → Slide 2
- Duck / rabbit → Slide 3
- Attention → Slide 4
- Memory → Slide 5
- Secret rule → Slide 7
The replay must start from each experiment’s initial state, with timers and reveals cleared. Add a “Replay from Slide 1” control and a “Questions?” closing state. If MQTT telemetry exists, show honest connection status and the current room topic; otherwise show a useful local presentation status, not a fake live telemetry panel.
Evidence/source line: “Synthesis of the evidence on slides 2–9”.

======================================================================
10. PRIVATE PRESENTER CUES AND PACING
======================================================================
Provide one private presenter cue per slide. Cues should contain the answer/spoiler, what to ask the room, and a time budget; do not place them as long paragraphs on the public slide. Total target is about 11 minutes (approximately 11:30 by these cues, plus Q&A):
1. “Title + bridge test” — 0:45. Ask which gray square looks lighter; bridge them; the pixels are identical, judged by surroundings.
2. “Size by comparison” — 1:15. Hands up before verification; the circles are identical; explain context.
3. “Duck or rabbit” — 1:15. Ask which appeared first; show duck then rabbit; mention the Easter/October result as one study only.
4. “Attention arena” — 1:45. Ask for WHITE bounces only during the 12-second run; answer is 15; replay with highlights and ask about the star, border, and square.
5. “Memory words” — 1:45. Do not say or hint at the missing-word theme before the word list and poll; the missing lure was never shown; keep the tone friendly.
6. “Loftus & Palmer” — 1:15. Ask for a prediction before revealing verbs; 31.8 vs 40.8 mph; there was no broken glass; explain the debated mechanism carefully.
7. “Secret rule” — 1:30. Ask yes/no before each guided test; 3–17–104 returns YES; the rule is any ascending triple.
8. “Confidence ≠ accuracy” — 0:45. Say both halves: confidence can be wrong, but is not always wrong.
9. “Check yourself” — 0:45. Walk through four habits; emphasise changing the process rather than relying on willpower.
10. “Closing + Q&A” — 0:30 plus questions. Repeat the thesis and offer replay of any experiment.

If the optional remote exists, show these private cue notes there. Never display spoilers from private cues on the main stage before the action that reveals them.

======================================================================
11. ACCESSIBILITY, ENGINEERING AND ROBUSTNESS
======================================================================
- Use semantic HTML and correct button elements. Every control must be keyboard reachable, visibly labelled, and have an accessible name. All stimulus SVGs/canvas views need a useful `role="img"` and descriptive `aria-label` that does not disclose a surprise answer early.
- Maintain strong text/background contrast, clear focus indicators, and adequate line-height. Do not communicate correct/incorrect using colour alone: pair colour with YES/NO or readable status text.
- No horizontal/vertical page scroll in presentation mode. No clipped text at 1280×720. Avoid giant fixed-pixel constraints and fixed stimulus sizes; use viewBox scaling and responsive layout.
- Use one delegated click listener where practical, but do not create duplicate listeners on each slide entry.
- All timer and animation cleanup must be explicit. Cancel pending sequences on reset, slide change, page visibility loss, and before a replay starts.
- The running arena is the actual experiment, so do not disable its movement under reduced-motion settings; do disable non-essential decoration and reduce slide-transition movement.
- No console errors, unhandled promise rejections, invalid DOM nesting, dead buttons, missing assets, or undefined handlers.
- Do not expose global variables unnecessarily. A named `window.__selfTest()` is acceptable for testing.
- Do not autoplay music. Do not play any sound during the perception, memory, or attention tasks. Prefer no audio at all unless there is a strong educational reason and it can never interfere with the experiment.
- Do not load remote images, fonts, analytics, or nonessential scripts. If an optional external remote-sync dependency fails, catch/report it and preserve local functionality.
- Do not claim the physical classroom smart board was tested unless it truly was. Verify at available emulated viewport sizes and clearly state what was and was not tested.

======================================================================
12. REQUIRED SELF-TESTS AND VERIFICATION
======================================================================
Implement `window.__selfTest()` and arrange for it to run once after the page has loaded (for example after 1–2 seconds) inside a `try/catch`. It must check and report each item, using `[deck self-test] PASS` if all checks pass or a list of concrete failures otherwise:
1. Exactly ten slide sections exist and their IDs are `s1` through `s10`.
2. The demo-action button exists on each demo slide 1–7.
3. Slide 1’s two square fill attributes are both exactly `#7A7A7A`.
4. Slide 2’s target circles both have radius exactly 40.
5. The arena bounce model independently computes exactly 15 white-disc wall bounces over 12 seconds, with the expected per-disc counts W1=2, W2=5, W3=4, W4=4.
6. The Wason rule function returns YES for 2–4–6, 8–10–12, 20–22–24, and 3–17–104; NO for 10–8–6.
7. The Slide 5 word sequence contains exactly the 12 specified words in the exact order.
8. Slide 6 contains all five exact verbs and numerical values: 31.8, 34.0, 38.1, 39.3, 40.8.
9. Navigating away from a running demo cancels its timers/RAF; reset is idempotent; replay returns it to the initial state.
10. If remote sync is implemented, self-originated messages are ignored, ACT only works on the matching active slide, and unavailable networking does not break local controls.

Testing requirements:
- Run any available syntax validation (for example, extract/validate inline JavaScript with Node if present).
- If a browser automation tool is available, open the deck and check navigation, the action button flow, the word sequence cancellation, the attention animation ending at 12 seconds, and replay. Check 1280×720, 1920×1080, and a 3840×2160 viewport where possible. If browser automation is unavailable, do not pretend you performed browser tests; run the static/self-tests and clearly state the limit.
- Check that the console is clean at startup and that no unexpected scrollbars or clipped slide content are obvious at the available sizes.
- Do not state that the deck passes tests that were not actually run.

======================================================================
13. SOURCE AND CLAIM CHECKLIST
======================================================================
Put source lines on the corresponding slides and a more complete reference list in README.md. Use author-year references consistently. Traceable core sources include:
- Adelson (1993), “Perceptual organization and the judgment of brightness,” Science, DOI: 10.1126/science.8266102; and Adelson (2000), “Lightness perception and lightness illusions.”
- Massaro & Anderson (1971), “Judgmental model of the Ebbinghaus illusion,” Journal of Experimental Psychology, DOI: 10.1037/h0031158.
- Roberts, Harris & Yates (2005), “The roles of inducer size and distance in the Ebbinghaus illusion,” Perception, DOI: 10.1068/p5273.
- Jastrow (1899), duck-rabbit figure; Brugger & Brugger (1993), DOI: 10.2466/pms.1993.76.2.577; Kornmeier & Bach (2012), DOI: 10.3389/fnhum.2012.00051.
- Simons & Chabris (1999), DOI: 10.1068/p281059; Drew, Võ & Wolfe (2013), DOI: 10.1177/0956797613479386; Mack & Rock (1998), *Inattentional Blindness*.
- Roediger & McDermott (1995), DOI: 10.1037/0278-7393.21.4.803; Deese (1959); Gallo (2010), DOI: 10.3758/MC.38.7.833.
- Loftus & Palmer (1974), DOI: 10.1016/S0022-5371(74)80011-3; Loftus (2005), DOI: 10.1101/lm.94705.
- Wason (1960), DOI: 10.1080/17470216008416717; Klayman & Ha (1987), DOI: 10.1037/0033-295X.94.2.211; Nickerson (1998), DOI: 10.1037/1089-2680.2.2.175.
- Koriat (2012), DOI: 10.1037/a0025648; Wixted & Wells (2017), DOI: 10.1177/1529100616686966; Kahneman & Klein (2009), DOI: 10.1037/a0016755.
- Lord, Lepper & Preston (1984); Pronin, Lin & Ross (2002); Milkman, Chugh & Bazerman (2009).

If any DOI or title cannot be verified from the provided research brief or available resources, do not invent details; mark it for review in README.md. The source list is a starting bibliography, not permission to overstate a paper’s findings.

======================================================================
14. FINAL ACCEPTANCE CHECKLIST
======================================================================
Before finishing, ensure:
- The clean-room project folder and `index.html`/`README.md` exist.
- The presentation has exactly 10 slides with working navigation and coherent visual hierarchy.
- Slides 1–7 have reliable, resettable demos; slides 8–10 do not accidentally show demo controls.
- All experiment timings and stimulus geometry match this specification.
- The hidden memory lure and attention surprises do not leak before the reveal.
- “Smashed” is 40.8 mph everywhere, never 40.5.
- Replay buttons restart demos cleanly.
- Core functionality works without internet. Optional remote sync is honest about its connection state.
- The self-test results and actual validation steps are recorded in README.md.
- Any unverified browser/physical-board behaviours are identified as not tested; do not fake certainty.

When done, respond with a brief completion report containing: the project folder/path, files created, what was actually tested, any limitations, and whether remote sync is live-tested or only implemented. Do not paste the whole HTML into your final response if the files were created successfully.

START BUILDING NOW. Do not ask for confirmation.
