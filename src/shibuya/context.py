import re
from typing import Dict, Any
from pathlib import Path
import xml.etree.ElementTree as ET


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
    if not toc:
        return toc

    root = ET.fromstring(toc)
    if len(root) != 1:
        return toc

    child = root[0]
    if len(child) == 2 and child[1].tag == "ul":
        return ET.tostring(child[1]).decode("utf-8")
    return toc


def create_edit_source_link(context: Dict[str, Any]):
    source_type = context.get("source_type")
    if not source_type:
        source_type = _normalize_readthedocs_context(context)

    source_user = context.get("source_user")
    source_repo = context.get("source_repo")
    source_docs_path = context.get("source_docs_path", "/docs/")
    source_edit_template = context.get("source_edit_template")

    def edit_source_link(filename: str) -> str:
        if source_edit_template:
            return source_edit_template.format(filename)

        if not source_user or not source_repo:
            return

        if source_type == "github":
            return f"https://github.com/{source_user}/{source_repo}/blob/master{source_docs_path}{filename}"
        elif source_type == "gitlab":
            return f"https://gitlab.com/{source_user}/{source_repo}/-/blob/master{source_docs_path}{filename}"
        elif source_type == "bitbucket":
            return  f"https://bitbucket.org/{source_user}/{source_repo}/src/master{source_docs_path}{filename}"

    return edit_source_link


def _normalize_readthedocs_context(context: Dict[str, Any]):
    if context.get("display_github"):
        source_type = "github"
    elif context.get("display_gitlab"):
        source_type = "gitlab"
    elif context.get("display_bitbucket"):
        source_type = "bitbucket"
    else:
        return

    context["source_type"] = source_type
    context["source_user"] = context.get(f"{source_type}_user")
    context["source_repo"] = context.get(f"{source_type}_repo")
    context["source_docs_path"] = context.get("conf_py_path")
    return source_type
