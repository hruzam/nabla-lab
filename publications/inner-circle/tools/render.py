from pathlib import Path
import csv, math, re, json, html, argparse, io
import markdown
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics import renderSVG, renderPDF
from reportlab.lib.colors import HexColor

# Preserved from the 2026-10-27 research edition; formulas/styles below are unchanged.
parser = argparse.ArgumentParser(description='Render selected inner-circle studies and analytic figures.')
parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1],
                    help='Publication directory; use a scratch copy for preview builds.')
selection = parser.add_mutually_exclusive_group(required=True)
selection.add_argument('--study', action='append', metavar='SLUG', help='Render only this study; repeat for several.')
selection.add_argument('--all', action='store_true', help='Explicitly rebuild all studies and publication indexes.')
args = parser.parse_args()
ROOT = args.root.resolve()
SELECTED = set(args.study or [])
known = {p.parent.name for p in ROOT.glob('*/study.md')}
if SELECTED - known:
    parser.error('Unknown study: ' + ', '.join(sorted(SELECTED - known)))

def write_changed(path, data):
    data = data.encode('utf-8') if isinstance(data, str) else data
    if not path.exists() or path.read_bytes() != data:
        path.write_bytes(data)
COLORS = ['#087f8c', '#c86b32', '#283c63', '#8c629d']

def save(d, stream, name, columns, rows):
    if SELECTED and stream not in SELECTED:
        return
    folder = ROOT / stream / 'figures'
    folder.mkdir(parents=True, exist_ok=True)
    svg = renderSVG.drawToString(d)
    svg = svg.encode('utf-8') if isinstance(svg, str) else svg
    table = io.StringIO(newline='')
    w = csv.writer(table); w.writerow(columns); w.writerows(rows)
    csv_bytes = table.getvalue().encode('utf-8')
    svg_path, csv_path, pdf_path = [folder / (name + ext) for ext in ('.svg', '.csv', '.pdf')]
    unchanged = (svg_path.is_file() and csv_path.is_file()
                 and svg_path.read_bytes() == svg and csv_path.read_bytes() == csv_bytes)
    # Preserve the existing PDF when its figure inputs/output agree; metadata alone
    # must not cause churn. The verifier checks expected constructions, not PDF layout.
    if not unchanged or not pdf_path.is_file():
        write_changed(pdf_path, renderPDF.drawToString(d))
    write_changed(svg_path, svg)
    write_changed(csv_path, csv_bytes)

def plot(stream, name, title, subtitle, series, labels, xlabel, ylabel, xmin, xmax, ymin, ymax):
    if SELECTED and stream not in SELECTED:
        return
    d = Drawing(720, 390)
    d.add(String(18, 365, title, fontName='Helvetica-Bold', fontSize=16, fillColor=HexColor('#172838')))
    d.add(String(18, 345, subtitle, fontName='Helvetica', fontSize=10, fillColor=HexColor('#526675')))
    p = LinePlot(); p.x=65; p.y=76; p.width=625; p.height=245
    p.data = series; p.joinedLines=1
    p.xValueAxis.valueMin=xmin; p.xValueAxis.valueMax=xmax
    p.yValueAxis.valueMin=ymin; p.yValueAxis.valueMax=ymax
    p.xValueAxis.labels.fontSize=9; p.yValueAxis.labels.fontSize=9
    p.xValueAxis.strokeColor=HexColor('#a5b2bc'); p.yValueAxis.strokeColor=HexColor('#a5b2bc')
    p.yValueAxis.visibleGrid=1; p.yValueAxis.gridStrokeColor=HexColor('#e4e9ed')
    for i in range(len(series)):
        p.lines[i].strokeColor=HexColor(COLORS[i % len(COLORS)]); p.lines[i].strokeWidth=2.2
    d.add(p)
    d.add(String(65, 330, ylabel, fontSize=9))
    d.add(String(350, 45, xlabel, fontSize=10, textAnchor='middle'))
    for i, label in enumerate(labels):
        d.add(String(65+i*205, 20, label, fontSize=9, fillColor=HexColor(COLORS[i % len(COLORS)])))
    xs=sorted(set(x for series_i in series for x,y in series_i))
    lookup=[dict(s) for s in series]
    save(d,stream,name,['x']+labels,[[x]+[v.get(x,'') for v in lookup] for x in xs])

ts=[i/50 for i in range(151)]
flow=[]
for deg in [120,170,180]:
    flow.append([(t, 180 if deg==180 else math.degrees(2*math.atan(math.tan(math.radians(deg)/2)*math.exp(-2*t)))) for t in ts])
plot('stance-geometry','flow','A specified law selects a path','Analytic two-agent attractive circle model; coupling = 1',flow,['initial 120 deg','initial 170 deg','exact antipode'],'time (model units)','separation (degrees)',0,3,0,185)
fisher=[(i/200,2*math.acos(min(1,math.sqrt(.5*i/200)+math.sqrt(.5*(1-i/200))))) for i in range(201)]
plot('stance-geometry','fisher','A categorical metric occupies one orthant','Analytic binary Fisher-Rao distance from p = (0.5, 0.5)',[fisher],['categorical distance'],'q in (q, 1-q)','Fisher-Rao distance',0,1,0,1.6)

alpha=.85; mean_walk=alpha/(1-alpha)
lam=[i/100 for i in range(201)]
plot('spectral-retrieval','filters','Same mean walk length, different filters','Analytic normalized-Laplacian responses; alpha = 0.85',
     [[(x,math.exp(-mean_walk*x)) for x in lam],[(x,(1-alpha)/(1-alpha+alpha*x)) for x in lam]],
     ['heat','personalized PageRank'],'normalized Laplacian eigenvalue','filter response',0,2,0,1.02)

d=Drawing(720,390)
d.add(String(18,365,'Equal voter indices conceal coalition differences',fontName='Helvetica-Bold',fontSize=16,fillColor=HexColor('#172838')))
d.add(String(18,345,'Exact four-voter capacity; every Shapley value is 0.25',fontSize=10,fillColor=HexColor('#526675')))
bc=VerticalBarChart();bc.x=55;bc.y=85;bc.width=640;bc.height=235
coalitions=sorted(range(16),key=lambda k:(k.bit_count(),tuple(i for i in range(4) if k&(1<<i))))
caps=[.5*int(k&3==3)+.5*int(k&12==12) for k in coalitions]
adds=[k.bit_count()/4 for k in coalitions]
bc.data=[caps,adds]; bc.categoryAxis.categoryNames=[''.join(str(i+1) for i in range(4) if k&(1<<i)) or 'none' for k in coalitions]
bc.categoryAxis.labels.fontSize=8;bc.valueAxis.valueMin=0;bc.valueAxis.valueMax=1;bc.valueAxis.valueStep=.25
bc.bars[0].fillColor=HexColor(COLORS[0]);bc.bars[1].fillColor=HexColor(COLORS[1]);bc.barSpacing=1;bc.groupSpacing=6
d.add(bc);d.add(String(55,45,'Approving coalition',fontSize=10))
d.add(String(55,20,'complete-pair capacity',fontSize=9,fillColor=HexColor(COLORS[0])))
d.add(String(300,20,'uniform additive baseline',fontSize=9,fillColor=HexColor(COLORS[1])))
save(d,'coalition-evidence','coalitions',['coalition','capacity','additive'],list(zip(bc.categoryAxis.categoryNames,caps,adds)))

gens=range(16)
twotype=[(t,.6**t+(0 if t==0 else .7*t*.6**(t-1))) for t in gens]
plot('cascade-diagnostics','transient','Subcritical dynamics can amplify transiently','Exact expectations; no immigration and one initial type-2 event',
     [twotype,[(t,.6**t) for t in gens]],['two-type model','one-type mean 0.6'],'generation','expected total activity',0,15,0,1.4)

times=[i/100 for i in range(101)]
plot('tensor-analytics','factors','Known factors for a recovery test','Analytic generating profiles, not estimated factors',
     [[(t,math.exp(-(t-.30)**2/.02)) for t in times],[(t,math.exp(-(t-.75)**2/.02)) for t in times]],
     ['early profile b1','late profile b2'],'normalized time','prescribed loading',0,1,0,1.05)

kh=[i/100 for i in range(401)]
plot('flow-control-stopping','sampling','The update rule changes stability','Analytic scalar system; exact sampling versus forward Euler',
     [[(x,math.exp(-x)) for x in kh],[(x,abs(1-x)) for x in kh],[(x,1) for x in kh]],
     ['exact sampling','Euler realization','stability boundary'],'k times sample interval','discrete pole magnitude',0,4,0,3.1)

ss=[i/100 for i in range(-200,201)]
plot('coherence-composition','cycle','A cycle exposes an affine inconsistency','Analytic unweighted three-cycle; residual minimum = circulation squared / 3',
     [[(s,s*s/3) for s in ss]],['minimum squared residual'],'required circulation s','squared comparison residual',-2,2,0,1.4)

plot('mental-map','coverage','A revisit does not establish coverage','Constructed graph: s -> a -> s, with another edge s -> b',
     [[(0,1/3),(1,2/3),(2,2/3),(3,2/3)],[(0,1/3),(1,2/3),(2,2/3),(3,1)]],
     ['stop on first revisit','exhaust the frontier'],'walk / processing step','fraction of reachable vertices visited',0,3,0,1.1)
budgets=[i/100 for i in range(401)]
plot('scratch-instruments','budget','Increasing cost need not yield an interior optimum','Analytic counterexamples: Q(b) = 1 - exp(-b) - a*b; b is dimensionless',
     [[(b,1-math.exp(-b)-a*b) for b in budgets] for a in [.2,1,1.2]],
     ['cost slope a = 0.2','cost slope a = 1','cost slope a = 1.2'],'dimensionless capacity b','illustrative quality Q(b)',0,4,-4,1)
times2=[i/100 for i in range(401)]
plot('interactive-interposition','completion','Completion needs the declared observations','Synthetic event at t = 2; correlated record at t = 3; not measured latency',
     [[(t,int(t>=2)+int(t>=3)) for t in times2],[(t,2*int(t>=3)) for t in times2]],
     ['observations available','accepted (shown at 2)'],'time (arbitrary units)','observations / acceptance signal',0,4,0,2.2)

ps=[i/200 for i in range(201)]
plot('jev-judgment','joint-bounds','Marginals do not determine joint correctness','Analytic bounds; hypothetical equal marginal probability p, not API confidence',
     [[(p,max(0,2*p-1)) for p in ps],[(p,p*p) for p in ps],[(p,p) for p in ps]],
     ['lower bound','independence case','upper bound'],'hypothetical marginal correctness p','joint correctness probability',0,1,0,1.05)

def render_all():
    css='''body{margin:0;background:#f4f1eb;color:#20303b;font:18px/1.65 Georgia,serif}main{max-width:880px;margin:48px auto;padding:56px 64px;background:#fffdf8;border-top:7px solid #087f8c;box-shadow:0 10px 45px #18344512}h1,h2,h3,th,.masthead{font-family:Arial,sans-serif}h1{font-size:42px;line-height:1.12;letter-spacing:-1px;color:#173c49}h2{font-size:24px;margin-top:2em;border-top:1px solid #d9e2e2;padding-top:22px}h3{font-size:19px}p{margin:1em 0}a{color:#087080;text-decoration-thickness:1px}table{border-collapse:collapse;width:100%;font-size:14px;line-height:1.45;margin:25px 0}th,td{border-bottom:1px solid #d5dfdf;padding:12px 10px;text-align:left;vertical-align:top}th{background:#e8efed}pre{background:#edf2f2;padding:18px;font:13px/1.65 monospace;overflow:auto;border-left:3px solid #087f8c}code{font-size:.84em}pre code{font-size:inherit}img,svg{max-width:100%;height:auto}figure{margin:32px 0}u{text-decoration-color:#087f8c;text-underline-offset:4px}li{margin:.65em 0}.masthead{font-size:12px;letter-spacing:2px;text-transform:uppercase;color:#607580}footer{font:12px/1.5 Arial,sans-serif;color:#657781;margin-top:45px;border-top:1px solid #d5dfdf;padding-top:18px}@media(max-width:720px){main{margin:0;padding:28px 22px}h1{font-size:32px}table{display:block;overflow:auto}}@media print{body{background:white;font-size:11pt}main{max-width:none;margin:0;padding:0;box-shadow:none;border:0}h1{font-size:26pt}h2{break-after:avoid}pre,figure,svg{break-inside:avoid}a{color:inherit}table{font-size:9pt}}'''
    for path in sorted(ROOT.rglob('*.md')):
        relative = path.relative_to(ROOT)
        if 'tools' in relative.parts or (SELECTED and relative.parts[0] not in SELECTED):
            continue
        body=markdown.markdown(path.read_text(),extensions=['tables','fenced_code'])
        def embed(m):
            p=path.parent/m.group(1)
            if p.suffix=='.svg' and p.is_file():
                s=p.read_text(); s=s[s.index('<svg'):]; s=re.sub(r'<svg\b','<svg role="img" aria-label="'+html.escape(m.group(2),quote=True)+'"',s,count=1)
                return '<figure>'+s+'</figure>'
            return m.group(0)
        body=re.sub(r'<img alt="([^"]*)" src="([^"]*)"\s*/?>',lambda m:embed(type('Match',(),{'group':lambda self,i:{1:m.group(2),2:m.group(1)}[i]})()),body)
        body=re.sub(r'<p>(<figure>.*?</figure>)</p>',r'\1',body,flags=re.S)
        title=re.search(r'^# (.+)',path.read_text(),re.M).group(1)
        out=path.with_suffix('.html') if path.name!='README.md' else path.with_name('index.html')
        page='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title><style>'+css+'</style><main><div class="masthead">Nabla-lab / Inner-circle publications / Research edition</div>'+body+'<footer>SHIFT_1 research · SHIFT_2 synthesis · 2026-10-27<br>Self-contained reading copy. Analytic and synthetic figures are identified in their captions. No external scripts or fonts are required.</footer></main></html>'
        write_changed(out, page)

if __name__=='__main__':
    render_all()
    print('Rendered', ', '.join(sorted(SELECTED)) if SELECTED else 'all publication studies/indexes', 'under', ROOT)
