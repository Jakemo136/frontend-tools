---
name: tokenize
description: Clean-up pass that replaces hard-coded CSS values with design tokens. Sweeps a frontend surface for raw color, spacing, sizing, and typography literals and routes each one through a token per the "Design tokens (enforced)" bar in rules/frontend-standards.md. Use when the user says "/tokenize", "tokenize this", "replace the hard-coded values", "pull these colors into tokens", or after a large generative UI burst that left one-off literals behind.
---

# Tokenize

Hold a surface to the token bar in `rules/frontend-standards.md`, section
"Design tokens (enforced)": every spacing, sizing, typography, and color value
resolves through a token, no raw literals, units chosen on purpose.

This is the clean-up pass for code that already exists. New work is covered by
the file-layer rule at write time.

Target: `$ARGUMENTS`. If empty, scope to the current frontend diff, meaning
changed `.css`, `.tsx`, and `.jsx` files.

Run these in order against the same target. Do not stop between them.

1. **`/impeccable extract $ARGUMENTS`.** Pull hard-coded colors, spacing,
   typography, shadows, and radii into `src/styles/tokens.css`. Name new
   tokens per the enforced rule (`--color-[intent]`, `--spacing-[size]`,
   `--font-[property]`, `--radius-[size]`, `--shadow-[level]`, `--z-[layer]`),
   intent-named and snapped to the existing scale rather than inventing rungs.

2. **`/impeccable polish $ARGUMENTS`.** Flags remaining hard-coded values,
   random gaps, and inconsistent token usage. Resolve what it surfaces.

3. **Unit-intentionality sweep.** Neither sub-command covers this. Scan the
   touched CSS for every surviving literal, including those inside token
   definitions, `clamp()`, and fluid `calc()`, and confirm each unit is
   deliberate per the "Responsive sizing" rules: `rem` for type and
   token-scale spacing, `em` for breakpoints, `%`/`vw`/`vh` for fluid, `px`
   only for true hairlines. Fix any unit that is there by default.

Report tokens added, literals collapsed, and unit changes as a bullet list,
file by file. Do not commit or open a PR unless asked.
