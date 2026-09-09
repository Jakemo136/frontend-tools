---
name: ux-check
description: Audit a frontend surface through the Laws of UX and Motion lenses. Fitts's law, Hick's law, Doherty threshold, tap-target sizing, choice overload, and whether each animation does a real usability job or is decoration. Measures rendered reality at desktop and mobile widths when a browser is available. Use when the user says "/ux-check", "check the UX", "audit the interaction design", "is this animation doing anything", or asks about cognitive load, friction, or motion quality. This is the psychology, interaction, and animation lens, and the only one that audits motion.
---

# UX check

Two lenses:

- **Laws of UX.** The principles catalogued in `rules/laws-of-ux.md`.
- **Motion.** Whether each animation does a real job, per the §9 Review
  Checklist in `rules/motion.md`.

Cite the specific law or red flag. Propose concrete fixes. No generic advice.

## 1. Load the reference

Both auto-load on frontend files. If they are not in context, read them first.

## 2. Pick the target

`$ARGUMENTS` if it names a route, component, or file. Otherwise the current
frontend changes: `git diff` against the base branch, scoped to
`*.tsx`/`*.jsx`/`*.css`.

## 3. Observe the rendered thing

If a dev or preview server is running, or you can start one, open the target
and screenshot at **~1280px** and **~390px**. Measure tap targets, option
counts, and spacing rather than eyeballing them.

If no browser is available, read the markup and CSS, reason from that, and say
in the report that you worked from source.

## 4. Scope with the Trigger Map

Identify what the target is (nav, CTA, form, multi-step flow, layout, content
block, pricing, first-impression surface) and pull only the Trigger Map rows
that apply. **Evaluate the relevant laws; do not force all 30.** Record which
ones you checked.

If the target has motion, classify each piece as productive, expressive, or
unnecessary, then check it against the §9 red flags. If the target is static,
say so and skip the motion lens.

### 4a. Reconcile against the motion plan

If `docs/MOTION_PLAN.md` exists, compare observed motion against its rows
(§10 of `rules/motion.md`):

- **Shipped but unplanned.** Motion in the code or render with no matching
  row. `P3`, or `P2` if it trips a §9 red flag. Add a row or remove it.
- **Planned but missing.** A row with nothing shipped. Note it. Not a defect.
- **Drifted.** Shipped motion contradicts its row on role, timing, easing, or
  a promised reduced-motion fallback. Severity per §9.

No plan file means skip this step. Do not invent one.

## 5. Evaluate

For each applicable law and each piece of motion, decide pass or violation.
Record every violation as:

- **Law or motion job.** The named law, or the red flag it trips ("loops while
  user reads", "competes with CTA", "no reduced-motion fallback").
- **What's wrong.** The element, the measurement, the count. Not "could be
  clearer."
- **Severity.** `P1` blocks or badly slows the task. `P2` real friction.
  `P3` polish.
- **Fix.** A specific change to size, copy, order, grouping, default, or
  progress cue. Not a restatement of the law.

Laws trade off against each other, Hick's against Tesler's above all. When a
fix for one worsens another, name the tension and recommend a deliberate call.

## 6. Report

Grouped by severity, `P1` first:

```
### P1
- **<Law>.** <What's wrong and where>. Fix: <specific change>.
```

Then **Top fixes**, the two or three highest-leverage changes.

If you reconciled against a motion plan, add a **Motion plan** section with the
three verdicts above. One line if plan and reality match.

Close by listing the checks that **passed**, so a clean screen reads as audited
rather than skipped.

Report only. Do not edit files. Offer to apply the fixes.
