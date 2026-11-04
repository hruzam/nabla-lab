"""Check only the new research edition, evidence links and publication entrance."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re
import json
import xml.etree.ElementTree as ET

evidence = Path(__file__).resolve().parent
root = evidence.parent.parent
pub = root / 'publications/inner-circle'
edition = pub / 'jev-usage'
receipt = evidence / 'artifact-checks.json'
files = (list(edition.glob('*.md')) + list(edition.glob('*.html'))
         + list(evidence.glob('*.md')) + [pub/'README.md', pub/'index.html'])

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.urls.extend(attrs[key] for key in ('href', 'src') if key in attrs)

errors, local_links, embedded = [], 0, 0
for path in files:
    text = path.read_text()
    if path.suffix == '.html':
        parser = Links()
        parser.feed(text)
        urls = parser.urls
        if path.parent == edition:
            assert '<head>' in text and '<body>' in text
            assert '<script' not in text.lower()
        if path.name == 'study.html' and path.parent == edition:
            embedded = text.count('<svg')
    else:
        urls = re.findall(r'\[[^\]]*\]\(([^)]+)\)', text)
    for url in urls:
        parts = urlsplit(url)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        target = (path.parent / unquote(parts.path)).resolve()
        local_links += 1
        if target != receipt and not target.exists():
            errors.append({'file': str(path.relative_to(root)), 'target': url})
for path in (edition/'figures').glob('*.svg'):
    ET.parse(path)
assert embedded == 2
result = {
    'date': '2026-11-03', 'files_checked': len(files),
    'local_links_checked': local_links, 'broken_local_links': errors,
    'study_embedded_svg': embedded, 'svg_xml_valid': True,
    'scope': 'local file existence, HTML structure and figure XML; '
             'no external URL availability or browser interaction assertion',
}
receipt.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
assert not errors
