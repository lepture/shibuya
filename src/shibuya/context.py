import re
from typing import Dict, Any
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


def create_edit_source_link(context: Dict[str, Any]):
    source_type = context.get("source_type")
    source_repo = context.get("source_repo")
    source_docs_path = context.get("source_docs_path", "docs")

    def edit_source_link(filename: str):
        if not source_repo:
            return
        # TODO: add more source types
        if source_type == "github":
            return f"https://github.com/{source_repo}/edit/master/{source_docs_path}/{filename}"

    return edit_source_link
