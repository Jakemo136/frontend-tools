---
paths:
  - "**/*.tsx"
  - "**/*.jsx"
  - "**/*.css"
---

# Laws of UX

Adapted from [Laws of UX](https://lawsofux.com/) by Jon Yablonski.
Takeaways paraphrased, not reproduced.

**While building**, find the Trigger Map row matching what you are making and
check the design against those laws before calling the screen done.
**While reviewing**, this catalog is what `/ux-check` scores against. A finding
names the law it violates: "CTA fails Fitts's, 28px tap target on mobile."

These are heuristics and they trade off. Hick's wants fewer options, Tesler's
says the complexity has to live somewhere. Name the tension, pick deliberately.

## Trigger Map

| Building | Check |
|---|---|
| **Navigation, menus** | Hick's, Miller's, Serial Position, Jakob's, Similarity |
| **A primary CTA** | Fitts's, Von Restorff, Aesthetic-Usability |
| **Forms and input** | Tesler's, Postel's, Hick's, Parkinson's, Chunking, Doherty |
| **Multi-step flows, onboarding** | Goal-Gradient, Zeigarnik, Chunking, Paradox of the Active User, Flow |
| **Layout, grouping, hierarchy** | Proximity, Common Region, Uniform Connectedness, Similarity, Prägnanz |
| **Content, copy, scannability** | Chunking, Working Memory, Selective Attention, Miller's |
| **Loading, feedback, perceived speed** | Doherty, Goal-Gradient, Flow, Zeigarnik |
| **Choices, pricing, option sets** | Hick's, Choice Overload, Von Restorff, Pareto |
| **Polish, first impression** | Aesthetic-Usability, Peak-End, Prägnanz, Occam's Razor |
| **Reusing conventions** | Jakob's, Mental Model, Postel's |
| **Deciding what to build** | Pareto, Occam's Razor, Tesler's |

---

## Core laws

### Aesthetic-Usability Effect
Attractive interfaces are perceived as easier to use.
- Polish buys tolerance for minor friction.
- It also masks real usability problems. Beauty is not a substitute for testing.

### Cognitive Load
Every element spends mental bandwidth.
- Surface only what serves the current goal. Cut decoration and redundancy.
- When content must be complex, sequence it so users hold one piece at a time.

### Doherty Threshold
Response under 400ms keeps users in flow.
- Target under 400ms and instrument for regressions.
- Optimistic UI, skeletons, and progress indicators make waits feel tracked.

### Fitts's Law
A target is faster to hit the bigger and closer it is.
- Generous tap targets, spaced to prevent mis-taps.
- Primary actions where they are easiest to reach: thumb zone on mobile, near
  the cursor on desktop.

### Hick's Law
Decision time grows with the number and complexity of choices.
- Reduce options on critical paths and highlight a recommended default.
- Break complex tasks into steps, revealing advanced options progressively,
  without simplifying away needed context.

### Jakob's Law
Users expect your site to work like the others they know.
- Follow conventions for nav placement, icon meaning, and form patterns so
  existing mental models transfer.
- When changing familiar UI, let users opt in while the old version remains.

### Miller's Law
Working memory holds roughly seven items, plus or minus two.
- Chunking matters more than the number. Do not cargo-cult "seven items."
- Break long lists, forms, and flows into smaller groups.

### Parkinson's Law
A task expands to fill the time expected for it.
- Cut steps so completion beats expectation.
- Autofill, saved defaults, and prefill collapse task time.

### Tesler's Law
Irreducible complexity lives either in the product or on the user.
- Absorb it in the build, not at runtime.
- Put contextual help exactly where the complexity surfaces.

## Gestalt: perception and grouping

### Law of Common Region
Elements inside a shared boundary read as one group.
- A border or distinct background signals that enclosed elements belong together.
- Use it to make page structure scannable at a glance.

### Law of Proximity
Elements near each other read as related.
- Tighten spacing between related elements. Put controls beside what they affect.
- Spacing, not lines, is the primary grouping tool.

### Law of Prägnanz
The eye resolves ambiguity into the simplest available form.
- Reduce visual noise. Prefer simple shapes and layouts.
- Consolidate fragmented elements. Simple figures are easier to retain.

### Law of Similarity
Visually alike elements read as a set, even when separated.
- Consistent color, shape, size, and weight signal shared category or behavior.
- Links and interactive items must look distinct from body text.

### Law of Uniform Connectedness
A connector beats proximity. Joined elements read as more related.
- Group related actions under a shared container or background.
- Lines and arrows link dependent elements when proximity is not enough.

## Memory, motivation, bias

### Choice Overload
Too many options degrade decision quality and satisfaction.
- Limit simultaneous options. Surface the most relevant per decision point.
- Filters, search, a recommended default, or side-by-side comparison.

### Goal-Gradient Effect
Effort accelerates as a goal gets closer.
- Show progress and make remaining steps visually obvious.
- Granting early progress motivates starting.

### Peak-End Rule
People judge an experience by its most intense moment and its end.
- Pour polish into the highest-stakes interaction and the final screen.
- Hunt the sharpest pain points. Negative peaks dominate memory.

### Serial Position Effect
First and last items are recalled best. The middle fades.
- Most important nav actions at far left and far right.
- Low-priority items in the middle.

### Von Restorff Effect
Among similar items, the one that stands out is remembered.
- Give critical actions a distinct treatment. One or two only, or they cancel.
- Never color alone. Add shape, label, or icon, and a non-motion alternative
  if the distinction uses motion.

### Working Memory
Roughly four to seven items, held 20 to 30 seconds.
- Every extra item competes for scarce slots.
- Favor recognition over recall: visited-link styling, breadcrumbs, carried
  context.

### Zeigarnik Effect
Unfinished tasks stay top of mind longer than completed ones.
- Signal that more exists, via chevrons, "load more", or scroll cues.
- Show progress through multi-step flows, even a little upfront.

## Principles and heuristics

### Chunking
Small labeled groups let users scan and locate faster.
- Group related content into visually distinct blocks with clear hierarchy.
- Spacing, headings, and borders make chunk boundaries carry meaning.

### Cognitive Bias
Mental shortcuts shape decisions below awareness.
- Design for pattern-matching behavior, not idealized rational users.
- Audit your own assumptions. Your mental model is not the user's.

### Flow
Deep engagement comes from matching challenge to skill.
- Calibrate difficulty and give immediate feedback after every action.
- Strip friction and reveal features progressively.

### Mental Model
Users carry an internal picture of how things work and apply it to your UI.
- Match patterns they already know so skill transfers immediately.
- Close the gap between your assumptions and theirs through research.

### Occam's Razor
Among equal solutions, prefer the fewest moving parts.
- Remove anything not load-bearing.
- A design is done when removing more would break it.

### Paradox of the Active User
Users dive in without reading docs, even when reading would be faster.
- Assume people click before they read. Do not depend on onboarding.
- Embed contextual help at the point of need, on every entry path.

### Pareto Principle
Roughly 80% of effects come from 20% of causes.
- Find the few interactions most users actually perform and optimize those.
- Direct effort at the minority that serves the widest audience.

### Postel's Law
Be liberal in what you accept, conservative in what you emit.
- Tolerate varied input formats and normalize internally.
- Anticipate edge cases so the UI degrades gracefully, with specific feedback
  at the boundaries.

### Selective Attention
Users filter out anything unrelated to their current goal.
- Reduce noise and direct focus. Never style content to look like ads.
- Make changes obvious. Competing simultaneous changes get missed.
