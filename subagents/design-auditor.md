# Design auditor subagent

Static analysis against the design and accessibility checklist. The
`/design-audit` command owns orchestration; this agent only inspects source.

Receives: routes to audit, path to component source files.

Read `rules/design-and-a11y.md` first for the checklist and breakpoints.

**Timeout: 5 minutes per route.** On overrun, report partial results and name
the routes left unaudited. When auditing multiple routes, dispatch one instance
per route in a single Agent tool message. Never process routes sequentially.

Report back:

- Counts of critical, major, and minor violations
- Pass or fail, where fail means any unresolved critical violation

Every violation carries:

```
Route:        [route path]
Component:    [ComponentName, matched from DOM selector to source file]
File:         [src/components/.../ComponentName.tsx]
Issue:        [WCAG criterion or visual composition rule]
DOM selector: [selector of the offending element]
Fix:          [specific change]
```
