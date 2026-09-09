---
description: Run a full design and accessibility audit at all breakpoints, with auto-fix for critical and major issues
---

# /design-audit [route?]

Audit the given route, or every route if none is given.

Read `rules/design-and-a11y.md` first for the checklist and breakpoints.
Requires a running dev server. If none is running, tell the user to start one
and stop.

## Phase 1: automated checks

Dispatch all three subagents **in a single Agent tool message**. They are
independent, and running them sequentially bloats context.

- `design-auditor` for static analysis
- `a11y-scanner` for the axe-core scan, falling back to Playwright if the MCP
  tool fails
- `screenshot-reviewer` for capture at all breakpoints

Present results in two layers. A **summary** of violation counts by severity
and routes affected, then **every violation on its own line**:

```
Severity | WCAG criterion | Route | DOM selector | Description
```

Condense the narrative around the violations, never the violations themselves.

## Phase 2: visual composition review

Once screenshots exist, review each one. This is a design evaluation, not a
checklist pass. Look at every route at every breakpoint as if seeing the app
for the first time, and flag anything unintentional, duplicated, misaligned,
or confusing. **Err toward flagging.** False positives are cheap.

- **Layout.** Duplicate elements, such as a page rendering its own header
  inside a layout that already provides one. Unclear primary, secondary, and
  tertiary hierarchy. Wasted or cramped space. Elements that should align and
  do not.
- **Wayfinding.** Does the user know where they are, via active nav state,
  breadcrumbs, or page title? Redundant paths? A clear next action?
- **Content.** Does seed data look realistic at every breakpoint? Are empty
  states helpful? Do tables, cards, and lists degrade gracefully on mobile?
- **Consistency.** Similar pages sharing layout structure, interactive
  elements styled alike, header and footer correct everywhere.

File these alongside the automated findings, in the matching severity bucket.

## Report: `/docs/DESIGN_AUDIT.md`

Every violation carries route, component name, source file path, and DOM
selector.

**Critical**, fix before merge. WCAG AA violations, broken layouts at any
breakpoint, missing focus indicators, missing alt text, duplicate page
elements.

**Major**, fix this sprint. Incomplete interactive states, missing transitions
on dynamic elements, contrast approaching AA, keyboard navigation problems,
misalignment between related elements, confusing hierarchy or navigation.

**Minor**, fix when next touching the component. Spacing inconsistencies,
typography scale deviations, motion ignoring `prefers-reduced-motion`, AAA
opportunities.

Close with **Screenshots**, grouped by route then breakpoint, and **Passes**,
what is already correct.

### Acknowledged issues

Record anything the user has approved shipping:

```
- Issue: [description]
  Acknowledged: [date]
  Reason: "[user's stated reason]"
  Tracked: [issue URL]
```

Skip these on re-run unless the component source changed since acknowledgment,
or the criterion moved from Minor to Critical.

## Phase 3: auto-fix Critical and Major

Never auto-fix Minor. Flag those for human review.

1. **Checkpoint.** Record the files about to change. `git stash push -m
   "pre-autofix"`, or copy to a temp location outside a git repo.
2. **Apply.** Critical first, then Major.
3. **Verify.** Re-run `a11y-scanner` on fixed routes, re-capture screenshots,
   re-run the Phase 2 review on them, and run the full component test suite.
4. **Evaluate.** Zero new violations and passing tests means the fixes hold;
   update the report. Any new violation absent from the original report, or
   any test failure, means **roll back to the checkpoint** and mark that
   violation as needing a manual fix, naming which of the two happened.
5. **Escalate.** For anything unfixable, report the violation, the fix
   attempted, why it failed, and a suggested manual approach.
