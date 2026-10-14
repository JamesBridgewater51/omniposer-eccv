#!/usr/bin/env python3
"""Render the four quantitative-results tables for the project page.

Input:  tools/tables.md  (the table data, transcribed from the paper's
        experiments.tex; best/second-best flags and the specialist/unified
        block split are recorded per cell)
Output: tools/tables_fragment.html (paste the <!-- TABLE_n --> blocks into
        index.html at the matching markers when the numbers change)

Usage: python3 tools/build_tables.py
"""
import json
import re
import sys

from pathlib import Path
HERE = Path(__file__).resolve().parent
SRC = str(HERE / 'tables.md')
OUT = str(HERE / 'tables_fragment.html')

ARROW = {'lower': '↓', 'higher': '↑'}


def load_json():
    text = open(SRC).read()
    m = re.search(r'```json\n(.*?)\n```', text, re.S)
    if not m:
        sys.exit('json block not found')
    return json.loads(m.group(1))


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def cell_html(c):
    if c is None:
        return '<td>–</td>'
    v = esc(c['v']) if c['v'] != '-' else '–'
    if c.get('best'):
        return f'<td><b>{v}</b></td>'
    if c.get('second'):
        return f'<td><u>{v}</u></td>'
    return f'<td>{v}</td>'


def render_table(t):
    benchmarks = t['benchmarks']
    # Table 2: single benchmark — no benchmark header row
    multi = len(benchmarks) > 1

    h = ['<div class="table-wrap">']
    h.append('<table class="table is-narrow is-fullwidth results-table">')

    if multi:
        h.append('<thead><tr><th rowspan="2">Method</th>')
        for b in benchmarks:
            n = len(t['metrics'][b])
            h.append(f'<th colspan="{n}" class="has-text-centered">{esc(b)}</th>')
        h.append('</tr><tr>')
        for b in benchmarks:
            for m in t['metrics'][b]:
                lab = m['label'].rstrip('↓↑')
                arrow = ARROW[m['direction']]
                h.append(f'<th class="has-text-centered">{esc(lab)}{arrow}</th>')
        h.append('</tr></thead>')
    else:
        b = benchmarks[0]
        h.append('<thead><tr><th>Method</th>')
        for m in t['metrics'][b]:
            lab = m['label'].rstrip('↓↑')
            arrow = ARROW[m['direction']]
            h.append(f'<th class="has-text-centered">{esc(lab)}{arrow}</th>')
        h.append('</tr></thead>')

    # split into specialist/unified blocks when present (paper's midrule)
    rows = t['rows']
    blocks = []
    cur = []
    for r in rows:
        if cur and r.get('block') and cur[0].get('block') and r['block'] != cur[0]['block']:
            blocks.append(cur)
            cur = []
        cur.append(r)
    blocks.append(cur)

    h.append('<tbody>')
    for bi, blk in enumerate(blocks):
        split_cls = ' class="block-split"' if (bi > 0 and multi) else ''
        for ri, r in enumerate(blk):
            tr_extra = split_cls if ri == 0 else ''
            name = esc(r['method'])
            if r.get('method_bold'):
                name = f'<b>{name}</b>'
            h.append(f'<tr{tr_extra}><th>{name}</th>')
            for b in benchmarks:
                for m in t['metrics'][b]:
                    h.append(cell_html(r['cells'].get(b, {}).get(m['key'])))
            h.append('</tr>')
    h.append('</tbody></table></div>')
    return '\n'.join(h)


def main():
    data = load_json()
    parts = []
    for i, t in enumerate(data['tables'], 1):
        parts.append(f'<!-- TABLE_{i} -->\n' + render_table(t))
    open(OUT, 'w').write('\n\n'.join(parts) + '\n')
    print(f'wrote {OUT}: {len(data["tables"])} tables')


if __name__ == '__main__':
    main()
