#!/usr/bin/env python3
"""Block newly-written fluid values on layout properties unless they are proven
load-bearing.

The failure this exists to stop: a clamp() written on a spacing property because
"responsive" felt like it needed one, when the layout algorithm was already
distributing that space. Those values do nothing at the width they were designed
for, break at a width nobody checked, and are miserable to hand-tune later
because the number on screen is not the number in the file.

The bar is a delete-test. Remove the value, render, and see whether anything
moves. If something does, record the width where it moves:

    /* fluid-ok: under 640px the rail overlaps the figure without this */
    inset-inline-start: clamp(1rem, 4vw, 3rem);

If nothing moves at any width, it was not load-bearing and should be a plain
value. Reads the marker from the file on disk, so a justification written on an
earlier pass keeps counting.

Fails open: any unexpected error exits 0. A broken checker must never wedge an
edit.
"""
import json
import os
import re
import sys

EXTENSIONS = {'.css', '.scss', '.sass', '.less', '.styl',
              '.tsx', '.jsx', '.astro', '.vue', '.svelte'}

# Properties whose value the layout algorithm is usually already negotiating.
# font-size and line-height are deliberately absent: fluid type is the one place
# clamp() is straightforwardly the right tool.
PROPERTIES = (
    r'gap|row-gap|column-gap'
    r'|margin|margin-(?:top|right|bottom|left)'
    r'|margin-(?:inline|block)(?:-(?:start|end))?'
    r'|padding|padding-(?:top|right|bottom|left)'
    r'|padding-(?:inline|block)(?:-(?:start|end))?'
    r'|width|height|min-width|max-width|min-height|max-height'
    r'|inline-size|block-size|min-inline-size|max-inline-size'
    r'|inset|inset-(?:inline|block)(?:-(?:start|end))?'
    r'|top|right|bottom|left'
    r'|flex-basis|column-width'
    r'|grid-template-columns|grid-template-rows'
    r'|grid-auto-columns|grid-auto-rows'
    r'|translate|scale'
)

DECL = re.compile(r'(?:^|[;{,\s"\'`])(' + PROPERTIES + r')\s*:\s*([^;}]*)', re.I)
VIEWPORT_UNIT = re.compile(r'\d\s*(?:d|s|l)?v(?:w|h|min|max|i|b)\b', re.I)
MARKER = re.compile(r'fluid-ok\s*:', re.I)
LOOKBACK = 3


def offending(value):
    """clamp() always counts. min()/max() only when a viewport unit is inside:
    min(100%, 60ch) is a measure cap and hurts nobody; min(100%, 40vw) is the
    same fluid guesswork clamp() is."""
    if re.search(r'\bclamp\s*\(', value, re.I):
        return 'clamp()'
    if re.search(r'\b(?:min|max)\s*\(', value, re.I) and VIEWPORT_UNIT.search(value):
        return 'min()/max() with a viewport unit'
    return None


def main():
    raw = sys.stdin.read()
    if not raw.strip():
        return 0
    payload = json.loads(raw)

    if payload.get('tool_name') not in ('Write', 'Edit'):
        return 0

    tool_input = payload.get('tool_input') or {}
    path = tool_input.get('file_path') or ''
    if os.path.splitext(path)[1].lower() not in EXTENSIONS:
        return 0

    # Only what this call introduced. Edit gives the replacement text; Write
    # gives the whole file, which for a new stylesheet is the same thing.
    added = tool_input.get('new_string')
    if added is None:
        added = tool_input.get('content') or ''
    if not added.strip():
        return 0
    added_lines = {ln.strip() for ln in added.splitlines() if ln.strip()}

    try:
        with open(path, encoding='utf-8') as handle:
            lines = handle.read().splitlines()
    except OSError:
        return 0

    findings = []
    for index, line in enumerate(lines):
        if line.strip() not in added_lines:
            continue
        for prop, value in DECL.findall(line):
            kind = offending(value)
            if not kind:
                continue
            context = lines[max(0, index - LOOKBACK):index + 1]
            if any(MARKER.search(c) for c in context):
                continue
            findings.append((index + 1, prop.strip(), kind, line.strip()))

    if not findings:
        return 0

    out = [
        f'Unjustified fluid value in {os.path.basename(path)}.',
        '',
    ]
    for line_no, prop, kind, text in findings:
        out.append(f'  line {line_no}: {prop} uses {kind}')
        out.append(f'    {text}')
    out += [
        '',
        'Run the delete-test before keeping these: remove the value, render the',
        'page, and compare positions across widths. Flex and grid already',
        'distribute free space, so a fluid value on a property they negotiate',
        'usually changes nothing at all.',
        '',
        'If nothing moves at any width, replace it with a plain value.',
        'If something does move, say where, on the line above:',
        '',
        '    /* fluid-ok: below 640px the columns collide without this */',
        '',
        'Do not add the marker without running the test. The marker is a claim',
        'that you measured, not a way to silence this.',
    ]
    print('\n'.join(out), file=sys.stderr)
    return 2


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)
