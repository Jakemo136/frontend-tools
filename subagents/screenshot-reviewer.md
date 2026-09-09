# Screenshot reviewer subagent

Receives: url, route name, optional baseline directory.

Captures the route through the `screenshot-review` MCP tool at the breakpoints
in `rules/design-and-a11y.md`: 375px, 768px, 1280px, 1440px.

Reviewing multiple routes means one capture per route in a single Agent tool
message. Never sequentially.

## Component level

- Overflow or clipping at any breakpoint
- Misaligned elements, vertical or horizontal
- Text too small to read on mobile
- Spacing inconsistencies visible to the eye
- Broken or incomplete components
- Layout correct at desktop but breaking at tablet or mobile

## Page level

Then review the whole page as a user would see it. Discovery, not a checklist.
Ask whether a first-time user would find anything confusing or broken.

- Duplicate elements: two headers, repeated nav, echoed titles
- Things that should align and do not, such as nav links off the logo baseline
- Unclear hierarchy, meaning it is not obvious what matters most
- Header and footer inconsistent across routes
- Empty regions suggesting incomplete rendering
- Placeholder or test data left in

If a baseline exists, note unexpected visual changes.

Returns: screenshot paths, component issues, composition issues, and a
baseline diff summary when applicable.
