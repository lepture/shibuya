import re
import os
from typing import Dict, Any
import xml.etree.ElementTree as ET


def normalize_pageurl(pageurl: str, builder: str):
    if pageurl is None:
        return pageurl
    if pageurl.endswith('/index.html'):
        return re.sub(r'index\.html$', '', pageurl)
    if builder == 'dirhtml' and pageurl.endswith('.html'):
        return re.sub(r'\.html$', '/', pageurl)
    return pageurl


def normalize_localtoc(toc: str):
    if not toc:
        return toc

    pattern = re.compile(r'<span class="pre">\w+?\.')
    root = ET.fromstring(toc)
    if len(root) != 1:
        return pattern.sub('.', toc)

    child = root[0]
    if len(child) == 2 and child[1].tag == "ul":
        toc = ET.tostring(child[1]).decode("utf-8")
    return pattern.sub('', toc)


def normalize_globaltoc(toc: str, depth: int = 0):
    depth = int(depth)
    if not toc or not depth:
        # fix for accessibility
        return toc.replace('role="heading">', 'role="heading" aria-level="3">')

    root = ET.fromstring('<div>' + toc.strip() + '</div>')
    for i in range(1, depth + 1):
        elements = root.findall(f'.//li[@class="toctree-l{i}"]')
        for el in elements:
            _classname = el.get('class')
            el.set('class', _classname + ' _expand')

    result = ET.tostring(root).decode('utf-8')[5:-6]
    # fix for accessibility
    return result.replace('role="heading">', 'role="heading" aria-level="3">')


def create_edit_source_link(context: Dict[str, Any]):
    source_type = context.get("source_type")
    source_user = context.get("source_user")
    source_repo = context.get("source_repo")
    source_docs_path = context.get("source_docs_path", "/docs/")
    source_version = context.get("source_version", "main")
    source_edit_template = context.get("source_edit_template")

    def edit_source_link(filename: str) -> str:
        if source_edit_template:
            return source_edit_template.format(filename)

        if not source_user or not source_repo:
            return

        if source_type == "github":
            url = f"https://github.com/{source_user}/{source_repo}/blob"
        elif source_type == "gitlab":
            url = f"https://gitlab.com/{source_user}/{source_repo}/-/blob"
        elif source_type == "bitbucket":
            url = f"https://bitbucket.org/{source_user}/{source_repo}/src"
        else:
            return

        return f"{url}/{source_version}{source_docs_path}{filename}"

    return edit_source_link


def generate_readthedocs_context():
    context = {}
    project_slug = os.environ.get("READTHEDOCS_PROJECT")
    if project_slug:
        context["theme_readthedocs_url"] = f"https://readthedocs.org/projects/{project_slug}"
    return context
