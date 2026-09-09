# frontend-tools

Three Claude Code commands, the reference files they score against, and the
browser tooling behind them. The lens is the last 10 percent: accessibility,
interaction psychology, motion, and design tokens, measured against named
principles rather than taste assertions.

## What a finding looks like

`/ux-check` audited the work gallery on my portfolio in July 2026. Verbatim
output, unedited:

> **P2**
> - **Von Restorff + Recognition-over-Recall (mobile CTA prominence)** —
>   `.visit` ("See it live") is `--color-on-dark-muted` at rest and only gains
>   `--color-accent-bright` on `:hover`. On touch there's no hover, so on
>   mobile the *primary conversion action* (get to the client's live site) is
>   the least prominent thing in the tile, while the big, obvious screenshot
>   frame does something else (plays the hero). A mobile visitor's instinct is
>   "tap the site to go to it" → they get an animation, then have to spot a
>   muted text link to actually leave. The whole meta row is tappable (so
>   target *size* is fine), but the *signal* is weak. **Fix:** under
>   `@media (hover: none)`, render `.visit` in the accent color at rest
>   (persistent, not hover-gated) so the "See it live →" affordance is always
>   visible on touch.

That is the bar. A named principle, the mechanism that breaks, the human
consequence, and a fix you can apply. Not "improve mobile CTA visibility."

A companion finding from the same run, on timing rather than interaction:

> **P3**
> - **Doherty Threshold (first-play latency)** — hero clips are
>   `preload="none"`, so the first hover/tap fetches the webm (52–190 KB)
>   before it plays; on a slow connection the motion can start >400ms late.
>   It's not *broken* ... just laggy on the first interaction. **Fix:**
>   `preload="metadata"` on the feature tile only (warms the flagship without
>   eager-loading all three), or accept the payload tradeoff.

Both fixes shipped in the same session as commit `8eb1b2a` and are still in
the tree.

## Commands

**`/ux-check`** runs two lenses over a surface. Laws of UX for cognition and
interaction, and a motion pass asking whether each animation does a real
usability job or is decoration. It measures rendered reality at 1280px and
390px when a browser is available, and says so when it fell back to source.
It is the only pass here that audits motion.

**`/tokenize`** is a clean-up pass for hard-coded CSS. It runs
[Impeccable](https://github.com/pbakaus/impeccable)'s `extract` and `polish`
in order, then adds a third step those two do not cover: a unit-intentionality
sweep confirming every surviving literal uses a deliberate unit. `rem` for type
and token-scale spacing, `em` for breakpoints, `%`/`vw`/`vh` for fluid, `px`
only for true hairlines.

**`/design-audit`** runs accessibility and design at every breakpoint. It
dispatches three subagents in parallel and drives a real browser through
`mcp/a11y-scanner`, which launches chromium via Playwright and runs
`@axe-core/playwright` against the rendered page, so violations come from the
DOM the user gets. Auto-fix for Critical and Major is rollback-safe: it
checkpoints, verifies, and reverts on any new violation or test failure.

## Layout

| Path | What it holds |
|---|---|
| `rules/laws-of-ux.md` | 30 principles and the Trigger Map that scopes them |
| `rules/motion.md` | Motion decision model, mood table, §9 review checklist |
| `rules/frontend-standards.md` | Enforced design tokens, theming, responsive sizing |
| `rules/design-and-a11y.md` | WCAG 2.2 AA checklist and breakpoints |
| `subagents/` | The three workers `/design-audit` dispatches |
| `mcp/a11y-scanner` | axe-core over Playwright |
| `mcp/screenshot-review` | Breakpoint capture and baseline diffing |
| `hooks/no-unjustified-fluid.py` | Blocks fluid values that are not load-bearing |

The rules files carry `paths:` frontmatter, so they auto-load on `.tsx`,
`.jsx`, and `.css` and stay out of context otherwise.

The hook blocks a newly written `clamp()` on a layout property until it carries
a `fluid-ok:` marker naming the width at which deleting the value changes the
render. A fluid value on a property flex or grid was already negotiating does
nothing at the width it was designed for, breaks at a width nobody checked, and
is miserable to hand-tune later.

## Attribution

The reference files paraphrase takeaways from work that is not mine. Each file
names its sources in the header:

- **Motion**: IBM Carbon Motion, Nielsen Norman Group, Material 3 Motion Physics
- **Laws of UX**: [lawsofux.com](https://lawsofux.com/) by Jon Yablonski

Paraphrased and applied, never reproduced. Read the originals.

## Install

`commands/*.md` into `~/.claude/commands/`, `rules/*.md` into your project's
`.claude/rules/`, `subagents/*.md` where your harness looks for agents. For
`/design-audit`, `npm install` inside each `mcp/*` directory and register them
as MCP servers. Wire the hook through `settings.json` under `PostToolUse`.

MIT.
