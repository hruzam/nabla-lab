from pathlib import Path
import csv, json, math, re, hashlib, itertools, argparse
from datetime import date
from html.parser import HTMLParser

# Re-run the original construction/link checks without rewriting the historical receipt.
parser = argparse.ArgumentParser(description='Check the eleven-edition publication snapshot; read-only unless --output is supplied.')
parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
parser.add_argument('--output', type=Path, help='Explicit destination for a new check receipt; otherwise print it.')
args = parser.parse_args()
ROOT = args.root.resolve()
LAB = ROOT.parents[1]
checks={}; missing=[]; checked_links=0
for p in ROOT.rglob('*.md'):
    for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',p.read_text()):
        if target.startswith(('https://','http://','#','mailto:')): continue
        checked_links+=1
        if not (p.parent/target.split('#')[0]).exists(): missing.append({'source':str(p.relative_to(ROOT)),'target':target})
checks['local_markdown_links']=not missing

class Parser(HTMLParser):
    def __init__(self): super().__init__(); self.svg=0; self.external=[]; self.images=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='svg': self.svg+=1
        if tag in ('script','img','link'):
            v=a.get('src',a.get('href',''))
            if v.startswith(('https://','http://')): self.external.append(v)
            if tag=='img': self.images.append(v)
html_results=[]
for p in ROOT.rglob('study.html'):
    parser=Parser();parser.feed(p.read_text())
    html_results.append({'path':str(p.relative_to(ROOT)),'inline_figures':parser.svg,'external_assets':parser.external,'remaining_image_tags':parser.images})
checks['standalone_html_figures']=len(html_results)==11 and all(x['inline_figures']>=1 and not x['external_assets'] and not x['remaining_image_tags'] for x in html_results)
def rows(rel):
    with (ROOT/rel).open() as f: return list(csv.DictReader(f))

flow=rows('stance-geometry/figures/flow.csv')
checks['flow_initial_and_antipode']=abs(float(flow[0]['initial 120 deg'])-120)<1e-10 and all(float(r['exact antipode'])==180 for r in flow)
checks['flow_decreases']=all(float(a['initial 120 deg'])>=float(b['initial 120 deg']) for a,b in zip(flow,flow[1:]))
fr=rows('stance-geometry/figures/fisher.csv')
checks['fisher_symmetry_and_limits']=all(abs(float(a['categorical distance'])-float(b['categorical distance']))<1e-7 for a,b in zip(fr,reversed(fr))) and abs(float(fr[0]['categorical distance'])-math.pi/2)<1e-10 and abs(float(fr[100]['categorical distance']))<1e-7
checks['fisher_worked_example']=abs(2*math.acos(.6)-1.8545904360032246)<1e-14
filters=rows('spectral-retrieval/figures/filters.csv')
checks['spectral_filter_order']=all(float(r['personalized PageRank'])+1e-14>=float(r['heat']) for r in filters) and float(filters[0]['heat'])==1
def capacity(a): return .5*({0,1}<=a)+.5*({2,3}<=a)
subs=[set(i for i in range(4) if k&(1<<i)) for k in range(16)]
phi=[]
for i in range(4):
    value=0
    for a in subs:
        if i not in a:
            s=len(a); value+=math.factorial(s)*math.factorial(3-s)/math.factorial(4)*(capacity(a|{i})-capacity(a))
    phi.append(value)
checks['capacity_monotone_equal_shapley_non_symmetric']=all(capacity(a)<=capacity(b) for a in subs for b in subs if a<=b) and all(abs(v-.25)<1e-14 for v in phi) and capacity({0,1})!=capacity({0,2})
cr=rows('cascade-diagnostics/figures/transient.csv'); z=[0.,1.]; errors=[]
for r in cr:
    errors.append(abs(sum(z)-float(r['two-type model'])));z=[.6*z[0]+.7*z[1],.6*z[1]]
checks['cascade_matrix_matches_formula']=max(errors)<1e-12
tf=rows('tensor-analytics/figures/factors.csv')
checks['tensor_declared_peaks']=abs(float(tf[30]['early profile b1'])-1)<1e-14 and abs(float(tf[75]['late profile b2'])-1)<1e-14
sp=rows('flow-control-stopping/figures/sampling.csv')
checks['sampling_boundaries']=float(sp[0]['Euler realization'])==1 and float(sp[200]['Euler realization'])==1 and float(sp[300]['Euler realization'])>1 and all(float(r['exact sampling'])<1 for r in sp[1:])
x=[0,2/3,4/3];b=[1,1,-1];bx=[x[1]-x[0],x[2]-x[1],x[0]-x[2]]
checks['cycle_residual']=abs(sum((a-c)**2 for a,c in zip(bx,b))-1/3)<1e-14
checks['all_figure_formats']=len(list(ROOT.rglob('*.svg')))==12 and len(list(ROOT.rglob('*.pdf')))==12 and len(list(ROOT.rglob('*.csv')))==12
joint=rows('jev-judgment/figures/joint-bounds.csv')
checks['jev_joint_bounds']=all(float(r['lower bound'])-1e-14<=float(r['independence case'])<=float(r['upper bound'])+1e-14 for r in joint) and abs(float(joint[160]['lower bound'])-.6)<1e-14 and abs(float(joint[160]['independence case'])-.64)<1e-14 and abs(float(joint[160]['upper bound'])-.8)<1e-14
checks['jev_choice_confidence_example']=abs((.8-.5)/(1-.5)-.6)<1e-14
coverage=rows('mental-map/figures/coverage.csv')
checks['coverage_counterexample']=float(coverage[-1]['stop on first revisit'])==2/3 and float(coverage[-1]['exhaust the frontier'])==1
budget=rows('scratch-instruments/figures/budget.csv')
best=max(budget,key=lambda r:float(r['cost slope a = 0.2']))
checks['budget_boundary_and_interior']=abs(float(best['x'])-math.log(5))<.011 and all(float(r['cost slope a = 1'])<=1e-12 and float(r['cost slope a = 1.2'])<=1e-12 for r in budget)
completion=rows('interactive-interposition/figures/completion.csv')
checks['completion_conjunction']=float(completion[200]['observations available'])==1 and float(completion[200]['accepted (shown at 2)'])==0 and float(completion[300]['accepted (shown at 2)'])==2
ledger=json.loads((ROOT/'research-coverage.json').read_text())
checks['original_research_unchanged']=all(hashlib.sha256((LAB/r['path']).read_bytes()).hexdigest()==r['sha256'] for r in ledger['files'])
g=LAB/'.germline/agents/oraculum/nabla-lab.md';s=g.read_text();stamp=re.search(r'(?m)^stamp: (.+)',s).group(1)
digest=hashlib.sha256(re.sub(r'(?m)^stamp: .*\n','',s).encode()).hexdigest()[:8]
checks['germline_stamp']=stamp==digest
checks['germline_discovery_link']=(g.parent/'../../../publications/inner-circle/README.md').resolve()==ROOT/'README.md' and 'publications/inner-circle/README.md' in s
result={'date':date.today().isoformat(),'scope':'eleven inner-circle research editions and bounded coverage/gap registers; no empirical agent validation','checks':checks,'all_pass':all(checks.values()),'local_links_checked':checked_links,'missing_links':missing,'html':html_results,'study_count':len(list(ROOT.glob('*/study.md'))),'figure_count':12,'shapley_counterexample_values':phi,'germline_stamp':stamp,'stamp_method':'first eight SHA256 hex digits of UTF-8 addendum with stamp line omitted','visual_review':['flow PDF raster preview','coalition PDF raster preview','scratch budget PDF raster preview','completion timeline PDF raster preview'],'html_browser_preview':'Earlier Firefox headless attempt crashed with exit 139; HTML structure/assets checked, live browser layout not claimed'}
# Do not claim the historical visual previews as newly performed checks.
result.pop('visual_review', None)
result.pop('html_browser_preview', None)
result['verification_limit'] = 'Construction, links and assets only; no new browser, visual, empirical or runtime-model witness.'
if args.output:
    args.output.write_text(json.dumps(result,indent=2)+'\n')
else:
    print(json.dumps(result,indent=2))
print(json.dumps({'all_pass':result['all_pass'],'checks':len(checks),'local_links':checked_links,'missing':missing,'studies':result['study_count'],'figures':12,'germline_stamp':stamp}))
if not result['all_pass']: raise SystemExit(1)
