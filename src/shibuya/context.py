import re
from pathlib import Path

CSS_PATH = Path(__file__).parent / "css"


def css_to_dict(filename: str):
    filepath = (CSS_PATH / filename).resolve()
    rv = {}
    with open(filepath, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith('--'):
                key, value = line.split(':')
                rv[key.strip()] = value.strip().rstrip(';')
    return rv


def normalize_pageurl(pageurl: str, builder: str):
    if pageurl is None:
        return pageurl
    if pageurl.endswith('/index.html'):
        return re.sub(r'index\.html$', '', pageurl)
    if builder == 'dirhtml' and pageurl.endswith('.html'):
        return re.sub(r'\.html$', '/', pageurl)
    return pageurl


def normalize_toc(toc: str):
    toc = re.sub(r'^<ul>\n<li>.*?</a>', '', toc)
    toc = re.sub(r'</li>\n</ul>$', '', toc)
    return toc
