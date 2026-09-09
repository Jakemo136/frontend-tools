# Design and accessibility standards

Conformance target: **WCAG 2.2 AA minimum** on all UI work. AAA where it costs
nothing significant.

Priority order when references disagree:

1. **WCAG 2.2 AA.** Non-negotiable, tested on every component.
2. **Nielsen's 10 heuristics.** Interaction patterns.
3. **Material Design.** Spacing, elevation, motion.
4. **Apple HIG.** Interaction feedback, gestures.
5. **Polaris and Atlassian.** SaaS-specific patterns.

## Breakpoints

`375px` mobile · `768px` tablet · `1280px` desktop · `1440px` large desktop.

Review and test every component at all four.

## Checklist

### Visual composition

Review as a first-time user, not as someone ticking boxes.

- No duplicate elements, such as a page rendering its own header inside a
  shared layout
- Visual hierarchy distinguishes primary, secondary, and tertiary content
- Related elements align on baselines, edges, or centers
- Navigation is consistent across routes
- Empty states are helpful, not blank

### Spacing and layout

- Token scale exclusively, no magic numbers
- No layout-shift sources, such as fixed heights on dynamic content
- No overflow or clipping at any breakpoint

### Interactive states

- `hover`, `focus`, `active`, `disabled` defined on every interactive element
- Focus indicators meet 3:1 contrast
- Keyboard order is logical
- No focus traps except intentional ones such as modals and drawers

### Motion

- Elements that appear or disappear have transitions
- Motion respects `prefers-reduced-motion`
- `transform` and `opacity` only, nothing that triggers layout

### Color and typography

- Text contrast 4.5:1 minimum, 3:1 for 18pt and above
- Non-text UI elements 3:1 minimum
- Color is never the sole carrier of information
- Typography uses the token scale, no hardcoded sizes

### Accessibility

- ARIA roles and labels on non-semantic elements
- Meaningful `alt` text, or `aria-hidden` when decorative
- Form inputs have associated labels
- Error messages programmatically associated with their inputs
- Live regions for dynamic updates
- Landmarks present: `main`, `nav`, `header`, `footer`

## Scope

Covers WCAG conformance, visual composition, interactive states, and
typography, spacing, and color tokens.

Does not cover UX quality: task-flow efficiency, discoverability, Gestalt
grouping, or frustration signals. Those belong to `/ux-check`.

Used by `/design-audit`.
