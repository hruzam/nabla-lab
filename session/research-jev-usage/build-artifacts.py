"""Offline research figures, reading copies and finite checks; no Jev client.

Run from any directory: python3 /.../session/research-jev-usage/build-artifacts.py
Writes only this evidence home's receipts, the new Jev edition and the reading index.
The shared historical renderer/checker is deliberately not changed.
"""
from pathlib import Path
from itertools import product, combinations
from collections import Counter
import csv
import hashlib
import html
import json
import math
import re
import sys
import markdown
from reportlab.graphics.shapes import Drawing, String, Line, Circle, Rect, PolyLine
from reportlab.graphics import renderPDF, renderSVG
from reportlab.lib.colors import HexColor

EVIDENCE = Path(__file__).resolve().parent
LAB = EVIDENCE.parent.parent
PUB = LAB / 'publications/inner-circle'
EDITION = PUB / 'jev-usage'
FIGURES = EDITION / 'figures'
FIGURES.mkdir(exist_ok=True)

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write_changed(path, text):
    if not path.exists() or path.read_text() != text:
        path.write_text(text)

# The existing papers and operator drafts are inputs, not writable outputs.
source_paths = sorted((LAB / 'drafts/jev').glob('*.md'))
source_paths += sorted(p for p in PUB.glob('*/study.md') if p.parent != EDITION)
source_paths += [PUB / x for x in ('substrate-gap-register.md', 'research-tracks.md',
                                  'provenance.md', 'editorial-evidence.md')]
source_paths += [LAB / 'session/flag.md']
source_before = {str(p.relative_to(LAB)): digest(p) for p in source_paths}

f = lambda x: int((x[0] and x[1]) or (x[2] and x[3]))
counts, pivcounts = Counter(), Counter()
completion_count = 0
for partial in product((-1, 0, 1), repeat=5):
    unknown = [i for i, t in enumerate(partial) if t == -1]
    completions = []
    for bits in product((0, 1), repeat=len(unknown)):
        it = iter(bits)
        completions.append(tuple(next(it) if t == -1 else t for t in partial))
    outputs = {f(x) for x in completions}
    lo = f(tuple(0 if t == -1 else t for t in partial))
    hi = f(tuple(1 if t == -1 else t for t in partial))
    pivots = {i for i in unknown if any(
        f(x) != f(x[:i] + (1,) + x[i+1:]) for x in completions if x[i] == 0)}
    result = lo if lo == hi else -1
    assert result == (next(iter(outputs)) if len(outputs) == 1 else -1)
    assert (result == -1) == bool(pivots)
    counts[result] += 1
    pivcounts[len(pivots)] += 1
    completion_count += len(completions)
assert counts == {-1: 117, 0: 75, 1: 51}
assert completion_count == 1024

majority_checked = 0
for unknown in combinations(range(7), 4):
    fixed = [i for i in range(7) if i not in unknown]
    for bits in product((0, 1), repeat=3):
        partial = dict(zip(fixed, bits))
        # Build all 16 resolutions directly, with no inferred independence.
        completions = []
        for resolution in product((0, 1), repeat=4):
            state = partial | dict(zip(unknown, resolution))
            completions.append(tuple(state[i] for i in range(7)))
        vote = lambda x: int(sum(x) >= 4)
        pivots = {i for i in unknown if any(vote(x) != vote(x[:i]+(1,)+x[i+1:])
                                          for x in completions if x[i] == 0)}
        assert {vote(x) for x in completions} == {0, 1}
        assert len(pivots) == 4
        majority_checked += 1
assert majority_checked == 280

ink, teal, orange, grid = map(HexColor, ['#20303b', '#087f8c', '#b65e24', '#d5dfdf'])
def label(d, x, y, text, size=11, color=ink):
    d.add(String(x, y, text, fontName='Helvetica', fontSize=size, fillColor=color))

def save(drawing, name, header, rows):
    svg_path = FIGURES / (name + '.svg')
    svg = renderSVG.drawToString(drawing)
    changed = not svg_path.exists() or svg_path.read_text() != svg
    write_changed(svg_path, svg)
    pdf_path = FIGURES / (name + '.pdf')
    if changed or not pdf_path.exists():
        renderPDF.drawToFile(drawing, str(pdf_path))
    with (FIGURES / (name + '.csv')).open('w', newline='') as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)

d = Drawing(720, 330)
label(d, 24, 305, 'One binary observation cannot recover orientation', 17)
label(d, 24, 284, 'Analytic construction; no measured Jev data', 11)
cx, cy, radius = 155, 150, 94
d.add(Rect(cx - .2*radius, cy-radius, .4*radius, 2*radius,
           fillColor=HexColor('#e8efed'), strokeColor=None))
d.add(Circle(cx, cy, radius, strokeColor=ink, fillColor=None))
d.add(Line(cx-radius-15, cy, cx+radius+20, cy, strokeColor=grid))
d.add(Line(cx, cy-radius-10, cx, cy+radius+10, strokeColor=grid))
for sign in (-1, 1):
    d.add(Circle(cx, cy+sign*radius, 5, strokeColor=None, fillColor=teal if sign==1 else orange))
label(d, 175, 249, 'EDGE_POS: p = 0.5', 10, teal)
label(d, 175, 44, 'EDGE_NEG: p = 0.5', 10, orange)
label(d, 273, cy-4, 'a', 12)
label(d, 143, 259, 'b', 12)
label(d, 44, 16, 'Shaded band: |a.x| <= 0.2', 10)
x0, y0, w, h = 380, 68, 310, 170
d.add(Line(x0, y0, x0+w, y0, strokeColor=ink))
d.add(Line(x0, y0, x0, y0+h, strokeColor=ink))
for value in (0, .5, 1):
    yy = y0+h*value
    d.add(Line(x0, yy, x0+w, yy, strokeColor=grid))
    label(d, x0-27, yy-3, str(value), 10)
rows, points = [], []
for deg in range(-180, 181):
    angle = math.radians(deg)
    s, orientation_projection = math.cos(angle), math.sin(angle)
    probability = (1+s)/2
    state = 'EDGE' if abs(s) <= .2 else ('FACE' if s > 0 else 'TAIL')
    orientation = ('undefined' if abs(orientation_projection) < 1e-12
                   else ('positive' if orientation_projection > 0 else 'negative'))
    rows.append((deg, s, probability, orientation_projection, state, orientation))
    points.extend((x0+w*(deg+180)/360, y0+h*probability))
d.add(PolyLine(points, strokeColor=teal, strokeWidth=2))
for deg, sign in ((-90, -1), (90, 1)):
    d.add(Circle(x0+w*(deg+180)/360, y0+h*.5, 4,
                 fillColor=teal if sign==1 else orange, strokeColor=None))
for deg in (-180, -90, 0, 90, 180):
    label(d, x0+w*(deg+180)/360-12, y0-20, str(deg), 9)
label(d, 430, 24, 'State angle phi (degrees)', 11)
label(d, 390, 253, 'p = (1 + cos phi) / 2', 12)
save(d, 'rotation', ['phi_degrees', 'a_dot_x', 'p', 'b_dot_x', 'state', 'orientation'], rows)

d = Drawing(720, 300)
label(d, 24, 274, 'Endpoint certificates across all 243 partial assignments', 17)
label(d, 24, 251, 'Synthetic pair-coalition game with a fifth dummy element', 11)
bar_rows = [('TAIL', 75), ('FACE', 51), ('GROUP_EDGE', 117)]
for i, (name, count) in enumerate(bar_rows):
    x = 100 + 205*i
    d.add(Rect(x, 60, 95, 1.35*count, fillColor=orange if i==2 else teal, strokeColor=None))
    label(d, x+35, 68+1.35*count, str(count), 14)
    label(d, x-2, 38, name, 11)
label(d, 24, 14, 'Zero disagreements with full-completion evaluation; counts are not task prevalence.', 10)
save(d, 'completions', ['result', 'partial_assignments'], bar_rows)

# Use the established publication style; render only this edition and its entrance.
index_path = PUB / 'index.html'
css = re.search(r'<style>(.*?)</style>', index_path.read_text(), re.S).group(1)
targets = list(EDITION.glob('*.md')) + [PUB / 'README.md']
generated = []
for source in targets:
    text = source.read_text()
    body = markdown.markdown(text, extensions=['tables', 'fenced_code', 'toc'])
    def inline_figure(match):
        asset = source.parent / html.unescape(match.group(1))
        if asset.suffix == '.svg' and asset.exists():
            return '<figure>' + re.sub(r'<\?xml.*?\?>|<!DOCTYPE.*?>', '', asset.read_text(), flags=re.S) + '</figure>'
        return match.group(0)
    body = re.sub(r'<img[^>]*src="([^"]+)"[^>]*/?>', inline_figure, body)
    body = re.sub(r'<p>(<figure>.*?</figure>)</p>', r'\1', body, flags=re.S)
    def reading_link(match):
        href = html.unescape(match.group(1))
        base, separator, anchor = href.partition('#')
        candidate = source.parent / base
        if base.endswith('.md') and (candidate.with_suffix('.html').exists() or candidate in targets):
            base = base[:-3] + '.html'
        if candidate.resolve() == (PUB / 'README.md').resolve():
            base = str(Path(base).with_name('index.html'))
        return 'href="' + html.escape(base + (separator+anchor if separator else ''), quote=True) + '"'
    body = re.sub(r'href="([^"]+)"', reading_link, body)
    title = text.splitlines()[0].lstrip('# ')
    page = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>'+html.escape(title)+'</title><style>'+css+'</style></head><body><main>'
            '<div class="masthead">Nabla-lab / Inner-circle / 2026-11-03 research edition</div>'
            +body+'<footer>SHIFT_2 research and synthesis. Analytic figures are not model performance data.'
            ' No external fonts or scripts are required.</footer></main></body></html>')
    dest = index_path if source == PUB / 'README.md' else source.with_suffix('.html')
    write_changed(dest, page)
    generated.append(str(dest.relative_to(LAB)))

source_after = {str(p.relative_to(LAB)): digest(p) for p in source_paths}
assert source_before == source_after
receipt = {
    'date': '2026-11-03', 'scope': 'offline mathematical construction and document generation only',
    'python': sys.version.split()[0], 'markdown': markdown.__version__,
    'partial_assignments': 243, 'completions': completion_count,
    'verdict_counts': dict(counts), 'pivot_histogram': dict(pivcounts),
    'endpoint_or_pivot_discrepancies': 0, 'majority_configurations_checked': majority_checked,
    'zero_of_50_one_sided_95_upper_bound': 1-.05**(1/50),
    'original_inputs_unchanged_during_build': True, 'source_sha256': source_after,
    'generated_html': generated,
    'figure_sha256': {str(p.relative_to(LAB)): digest(p) for p in sorted(FIGURES.iterdir())},
    'live_inference': False,
}
write_changed(EVIDENCE / 'construction-checks.json', json.dumps(receipt, indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k not in ('source_sha256','figure_sha256')}, indent=2))
