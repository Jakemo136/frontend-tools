---
paths:
  - "**/*.tsx"
  - "**/*.jsx"
  - "**/*.css"
---

# Website motion

Deciding whether an animation belongs, what job it does, and how to keep
it useful rather than decorative.

Sources: IBM Carbon Motion, Nielsen Norman Group, Material 3 Motion
Physics. Attribution preserved, takeaways paraphrased.

**While building**, run every animation through §1 and §2, match the
brand in §5, and reach for a §7 default instead of inventing motion per
component. **While reviewing**, §9 is what `/ux-check` scores against.

---

## 1. Core rule

Motion must do one of three jobs: improve usability, clarify meaning, or
express brand at an intentional moment. If it does none, remove it.

---

## 2. First decision: productive, expressive, or unnecessary

Decide the category before choosing a style.

| | **Productive** | **Expressive** |
|---|---|---|
| Job | Supports the user's task | Supports brand, mood, story |
| Question | "Does this help the user use the interface?" | "Is this moment important enough to deserve attention?" |
| Traits | fast, subtle, functional, low drama, repeatable | choreographed, atmospheric, memorable, sparing |
| Timing | 150-300ms small feedback · 250-400ms menus/cards/drawers · 300-500ms larger transitions | 400-700ms one headline · 700-1200ms a choreographed hero · rarely >1200ms |
| Use for | buttons, menus, forms, accordions, filters, modals, section reveals, page transitions | hero entrances, launch intros, case-study reveals, key CTA emphasis |

Reserve expressive motion for important moments. Not every heading
performs, not every button bounces, not every scroll section animates.

---

## 3. Systemize

Build reusable patterns rather than a new animation per component: hero
reveal · section reveal · card reveal · hover feedback · modal entrance ·
menu transition · loading state.

Avoid random directions, delays, and mixed styles. A page should not read
like several animation tutorials glued together.

Use motion to answer: what should the user notice first, what appears
next, what is related, what changed, what is actionable.

---

## 4. What motion is good for

- **Feedback.** Confirm the interface responded. Button press, save
  success, invalid-field shake, item added, upload progress.
- **State change.** Clarify what changed when the before and after
  relationship matters. Accordion opens, filter results update, card to
  detail view.
- **Navigation metaphor.** Direction matching the mental model. Page
  slides forward, modal rises, drawer enters from its side, carousel
  moves horizontally.
- **Signifiers.** Show something is interactive. Hover lift, underline
  expansion, caret rotation. Invite interaction, do not beg for it.
- **Attention.** Motion spends attention, so spend it deliberately.
  Reveal a CTA, highlight a changed value, draw the eye to an error.
  Never animate decoration near body copy or loop while users read.

Every animation should answer one of: **attention** (where should the
user look next), **transition** (what just changed), **relation** (how
are these connected).

---

## 5. Mood to motion

Pick the row matching the project's brand maturity.

| Mood | Use | Avoid | Best for |
|---|---|---|---|
| **Serious / Trustworthy** | fade in · slight rise · phrase-level entrance · minimal stagger | bounce · elastic · glitch · letter waterfalls | consultants, professional services, legal, finance, B2B SaaS |
| **Refined / Premium** | masked reveal · soft rise · subtle blur-to-sharp · restrained word stagger | big slides · obvious springiness · cartoon bounce · long delays | portfolio sites, premium services, design studios, polished product pages |
| **Creative / Crafted** | word stagger · selective letter animation on *one* key word · choreographed line sequencing | animating every word the same · long typewriter · decorative motion with no concept | creative portfolios, studios, personal brands, editorial landing pages |
| **Playful / Friendly** | light spring · small scale pop · mild overshoot · staggered letters | heavy rubbery motion · constant bouncing · childish motion unless brand fits | consumer brands, family products, casual apps, playful campaigns |
| **Bold / Confident** | directional slide · fast wipe · sharp stagger · strong entrance | slow float · timid fades · delicate motion | launches, bold brands, campaign pages, strong CTAs |
| **Technical / Precise** | clipped reveal · typewriter · cursor effect · grid-like sequencing | organic bounce · dreamy drift · decorative flourishes | developer portfolios, AI tools, code editors, technical products |
| **Editorial / Storytelling** | staggered phrase reveal · line-by-line entrance · gentle scroll reveals · masked typography | interface-like microanimations · mechanical timing · repetition | narrative, magazine-style landing pages |
| **Mystical / Atmospheric** | slow fade · soft vertical drift · subtle blur · glow reveal | hard slides · fast snaps · bouncy motion · aggressive easing | quiet, ceremonial, spacious brands |
| **Disruptive / Futuristic** | glitch · jitter · split text · distortion · sharp opacity cuts | trust-based businesses · looping glitch · glitch on body copy | music, gaming, experimental tech, edgy visual brands |

### What each animation type signals

- **Fade in.** Calm, clean, professional. Generic if overused.
- **Fade plus slight rise.** Modern, refined, trustworthy. The safe
  default for professional, SaaS, and portfolio work. Predictable.
- **Slide from side.** Directional, assertive. Salesy if too strong.
- **Word-by-word stagger.** Intentional, editorial, crafted. Slows
  reading if overdone.
- **Letter-by-letter.** Theatrical. One key word only. Gimmicky
  otherwise.
- **Typewriter.** Technical, code-like. Cliché, often overused.
- **Masked reveal.** Premium, controlled, editorial. Cold if too slick.
- **Bounce or spring.** Friendly, playful. Weakens seriousness fast.
- **Glitch.** Unstable, digital, rebellious. Bad fit for trust, clarity,
  accessibility.

---

## 6. Easing and spring

- **Ease-out.** Default for anything entering. Natural, settled.
- **Ease-in.** For anything leaving.
- **Ease-in-out.** For transitions between states.
- **Spring.** Tactile UI, sparingly, on buttons and small objects.
- **Linear.** Mechanical. Only when that is the point.

Spring is about perceived behavior, not playfulness. Tune by stiffness
(higher is snappier) and damping (higher is less bounce). Visible
overshoot and long oscillation are what read as cartoonish. Avoid them
on trust-heavy, legal, financial, and medical sites.

---

## 7. Per-element defaults

- **Hero headline.** Expressive but restrained. First line a calm
  fade and rise, second slightly more crafted, one key word may get a
  selective letter or mask reveal. No looping, no full-paragraph
  animation.
- **Section headings.** Subtle fade and rise, short, minimal stagger.
- **Body copy.** Usually none. Maybe a section reveal. Never
  letter-by-letter, never long fades that slow reading.
- **Buttons and CTAs.** Quick hover, subtle transform, clear focus
  state. No pulsing, nothing that hides the label.
- **Cards.** Small hover lift, slight shadow or transform, quick grid
  entrance.
- **Modals and drawers.** Direction matching origin, opacity and
  transform, quick both ways.

The pattern for professional creative sites: the message enters calmly
and one meaningful word gets the crafted animation. Subtle line
entrance, word-level stagger, one expressive detail. No bounce, no heavy
overshoot, no looping headline.

---

## 8. Performance and accessibility

Non-negotiable.

- Respect `prefers-reduced-motion` with a real fallback. Content must be
  fully usable without animation.
- Animate `transform` and `opacity` only.
- Avoid animating many nodes, and avoid expensive scroll-linked effects.
- Text must be readable immediately. Motion must never block
  comprehension or screen-reader sense.

---

## 9. Review checklist

What `/ux-check` scores against. Record what is wrong, where, the
severity (`P1` blocks the task or fails accessibility · `P2` real
friction · `P3` polish), and a specific fix.

**Red flags.** Remove or simplify when motion:

- delays reading or comprehension
- competes with the CTA or a form
- loops near important content, or refires while scrolling
- makes the brand less trustworthy, or ordinary UI theatrical
- lacks a reduced-motion fallback
- uses layout-heavy animation unnecessarily
- exists only because it looks cool, or because it could be built

**Per piece:**

- **Purpose.** Which job, and is it productive or expressive?
- **Fit.** Does it match the brand and the page's seriousness?
- **Frequency.** Once, every visit, or repeatedly during a task? The
  more often seen, the quieter it must be.
- **Simplicity.** Can it be 20% simpler? Fewer things moving?
  Phrase-level instead of letter-level?
- **Timing.** Fast enough not to delay reading? Done before the user
  wants to act?
- **Accessibility.** Reduced-motion fallback? `transform` and `opacity`
  only? Node count sane? No expensive scroll-linked effects?

---

## 10. Per-element motion plan

The build-time counterpart to §9. Fill one block per animated element
before building it, and save it as `docs/MOTION_PLAN.md`. `/ux-check`
reconciles observed motion against these rows, so shipped-but-unplanned,
planned-but-missing, and drifted entries become findings and the plan
stays a true registry.

Decide the role first; everything else follows. Keep the reduced-motion
row last so it is never an afterthought.

```
Element / section:        e.g. Hero headline, line 2
Purpose:                  attention / transition / relation / brand
Desired mood:             e.g. Refined / Premium  (§5 row)
Animation role:           productive | expressive
Recommended motion:       e.g. masked reveal + soft rise on key word
Timing:                   e.g. 600ms
Easing:                   e.g. ease-out  (spring: stiffness/damping)
Stagger:                  e.g. none | 40ms phrase-level
What to avoid:            e.g. bounce, letter-by-letter, looping
Reduced-motion fallback:  e.g. instant opacity 0→1, no transform
```

Or project-wide:

| Element / section | Purpose | Mood | Role | Motion | Timing | Easing | Stagger | Avoid | Reduced-motion |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
