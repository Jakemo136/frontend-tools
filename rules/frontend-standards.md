---
paths:
  - "**/*.tsx"
  - "**/*.jsx"
  - "**/*.css"
---

# Frontend standards

- CSS Modules and CSS variables only. No runtime CSS-in-JS.
- All tokens live in `src/styles/tokens.css` and are used exclusively.
- E2E tests are immutable. Fix components, never tests.

## Design tokens (enforced)

Applies to every CSS edit regardless of what is driving it, whether
`impeccable`, an orchestration plugin, or hand-edits. The bar lives at
the file layer rather than inside one build loop, so nothing escapes it.

- **Tokens only.** Spacing, sizing, font-size, font-weight, line-height,
  radius, color, shadow, and z-index resolve through `var(--…)`. A
  `gap: 13px` written directly is a defect, not a shortcut.
- **Missing token means add it, never inline it.** Add it to
  `tokens.css` with a comment naming its step on the scale. Never paste
  a literal in as a "just this once."
- **Naming.** `--color-[intent]`, `--spacing-[size]`, `--font-[property]`,
  `--radius-[size]`, `--shadow-[level]`, `--z-[layer]`. Intent-named,
  not value-named: `--spacing-md`, never `--spacing-16`.
- **Scale, do not sprinkle.** New values snap to the existing rhythm.
  Reaching between two rungs is the signal the design wants an existing
  rung.
- **Units are chosen, never defaulted.** Every surviving literal, inside
  a token definition, a `clamp()`, or a fluid `calc()`, must be the
  intentional unit per Responsive sizing below: `rem` for type and
  token-scale spacing, `em` for breakpoints, `%`/`vw`/`vh` for fluid,
  `px` only for true hairlines.
- **Self-check.** Scan the diff for bare lengths in spacing, sizing,
  typography, and color properties. Any survivor is a missing token or
  an unchosen unit.

### Theming

Set `color-scheme: light dark` on `:root` and define each color token
once with `light-dark()`:

```css
:root {
  color-scheme: light dark;
  --color-surface: light-dark(#fff, #101014);
  --color-text:    light-dark(#101014, #f4f4f5);
}
```

`light-dark()` is Baseline, newly available since May 2024, and does
nothing unless `color-scheme` names both schemes.

This is not about brevity. A duplicate `[data-theme="dark"]` block is a
second place a token can be defined, so it is a place one can be
*missed*, and that failure is silent until someone looks at a
screenshot. Pairing both values on one line makes the omission a syntax
error instead of a review miss.

Keep an explicit override only where a user-facing toggle must beat the
system preference. `light-dark()` does not serve that.

### Cascade layers

Declare `@layer reset, base, components, utilities;` once, at the top,
and give third-party CSS its own layer. Layers settle specificity by
declaration order instead of by counting selectors, which is what
`!important` grows out of. It matters more once tokens are enforced: a
token is supposed to win everywhere, and an unlayered vendor stylesheet
is what quietly breaks that.

## Responsive sizing: the layout algorithm comes first

Before writing a fluid value, name what is already negotiating that
space. `justify-content: space-between`, `1fr`, `flex-grow`, and `auto`
margins resolve at render time against real content at a real width,
which is information a hand-written formula does not have.

**A `gap` on a `space-between` row is a floor, not the spacing.** Where
the row fits, `space-between` hands out more than the gap and the value
is invisible. Where it does not, the gap is overhead that can force the
wrap. Enforced by `hooks/no-unjustified-fluid.py`, which blocks a new
`clamp()` on a layout property until it carries a `fluid-ok:` marker
naming the width where deleting it changes the render.

**The delete test, before the value goes in.** Remove it, render, diff
positions across widths. If nothing moves, it is not load-bearing.
Playwright and the Chrome tools are right there, and skipping this is
how dead `clamp()`s accumulate.

`clamp()` earns its place on values nothing else negotiates: `font-size`
above all, `line-height`, and a fixed element's own dimension. Use
`ch`/`em` when the value should track content, as in `max-width: 65ch`.

`@container` is widely available and is the default tool for a component
appearing at more than one width, not a last resort. A card that must
work in a sidebar and in a three-up grid should ask about its own box,
never the viewport.

## Responsive sizing: prefer CSS to JS

A `ResizeObserver` that reads `getBoundingClientRect()` and writes back
inline styles is almost always overpowered for what CSS does natively,
and it costs a measure, layout, and paint per resize plus a flash of the
wrong layout on first paint.

This section argues against reaching for **JS**. It is not licence to
reach for `clamp()` ahead of the layout algorithm.

- **Once the layout algorithm cannot express it**, use `clamp()`,
  `min()`, `max()`, and `calc()` across units for fluid sizes, and
  `@media` only for genuine layout changes such as reflow, reorder, and
  show or hide. A value tracking the viewport continuously belongs in
  one expression, not a stack of breakpoint steps.
- **Mix units to interpolate.** `calc(35% + 8.2vw - 98px)` rides between
  two anchors across widths. Wrap it to pin the endpoints. This collapses
  a desktop value plus a tablet override into one continuous law.
- **Breakpoints in `em`.** `em` in a media query resolves against the
  browser default, so the layout adapts to a raised default font size,
  not just page zoom. 768px is 48em, 1024px is 64em.
- **Reach for JS** only when CSS genuinely cannot express it: behavior no
  `@container` query covers, measuring intrinsic size to feed an
  animation, or syncing to geometry with no CSS equivalent. Justify it in
  the PR.

### Three things that used to need JS

- **Parent and sibling state: `:has()`.** A card restyling when it
  contains a checked input, a row reacting to `:invalid`, a nav shifting
  when a menu opens. Widely available. A boolean prop whose only job is
  adding a class an ancestor reads can usually be deleted.
- **Entry and exit: `@starting-style` and `transition-behavior:
  allow-discrete`.** The first gives a transition a state to start from,
  the second lets it run on discrete properties like `display`. Together
  an element animates in on first paint and out to `display: none` with
  no mount flag, no `requestAnimationFrame` double-buffer, and no
  hand-matched timeout. `transition-behavior` is Baseline, newly
  available since August 2024. This is the largest JS deletion available
  here and the one most often still hand-rolled.
- **Animating to `auto`: `interpolate-size` and `calc-size()`.**
  `interpolate-size: allow-keywords` makes `height: auto` animatable.
  **Chromium-only, shipped in Chrome and Edge 129, not Baseline.** Treat
  it as progressive enhancement. Keep the `grid-template-rows: 0fr` to
  `1fr` fallback, and never ship an unguarded `calc-size()`.

## Images: never a hairline border plus a wide shadow

Pick one:

- a hairline border and no shadow, for framed or gallery treatment
- a soft shadow and no border, for something floating or lifting on hover
- neither, separating the image from its ground with the surface ramp

`border: 1px solid …` plus `box-shadow: 0 20px 50px -25px …` is the stock
card treatment generated layouts reach for by reflex. It reads as a
component library default rather than a deliberate frame, and reviewers
spot it immediately.

Shadows on images are legitimate as a response to state, meaning hover,
drag, or focus. Not as default decoration.
