# A11y scanner subagent

Receives: url, optional WCAG standard, defaulting to `WCAG22AA`.

Runs axe-core against the live route through the `a11y-scanner` MCP tool.

Returns violations grouped by impact, critical through minor, each carrying its
WCAG success criterion, impact level, affected DOM elements, and a suggested
fix.
