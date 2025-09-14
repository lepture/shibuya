import re
import os
import xml.etree.ElementTree as ET
from typing import Dict, Any
from pathlib import Path
from sphinx.application import Sphinx
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.builders.dirhtml import DirectoryHTMLBuilder
from ._wrapper import WrapLineFormatter


def patch_app_builder(app: Sphinx):
    if isinstance(app.builder, StandaloneHTMLBuilder):
        app.builder.templates.environment.globals.update(_add_readthedocs_context())
        app.builder.templates.environment.globals["expandtoc"] = _expandtoc
        app.builder.templates.environment.globals["edit_source_link"] = (
            _create_edit_source_link(app.config.html_context)
        )
        app.builder.highlighter.formatter = WrapLineFormatter

    if isinstance(app.builder, DirectoryHTMLBuilder):
        _get_outfilename = app.builder.get_outfilename

        def get_outfilename(pagename: str) -> str:
            if pagename == "404":
                return (Path(app.builder.outdir) / "404.html").resolve()
            return _get_outfilename(pagename)

        app.builder.get_outfilename = get_outfilename


def patch_html_page_context(
    app: Sphinx, pagename: str, templatename: str, context: Dict[str, Any], doctree: Any
) -> None:
    if not isinstance(app.builder, StandaloneHTMLBuilder):
        return

    _fix_context_pageurl(app, context)
    _fix_context_toc(context)

    def create_i18n_link(pattern: str):
        url = pattern.replace("%s", pagename)
        if pagename == "index" or pagename.endswith("/index"):
            if url.endswith("/index/"):
                url = url.replace("/index/", "/")
            elif url.endswith("/index.html"):
                url = url.replace("/index.html", "/")
        return url

    context["i18n_link"] = create_i18n_link


def _fix_context_pageurl(app: Sphinx, context: Dict[str, Any]) -> None:
    if "pageurl" not in context:
        return

    pageurl: str = context["pageurl"]
    if pageurl.endswith("/index.html"):
        context["pageurl"] = re.sub(r"index\.html$", "", pageurl)
    if isinstance(app.builder, DirectoryHTMLBuilder) and pageurl.endswith(".html"):
        context["pageurl"] = re.sub(r"\.html$", "/", pageurl)


def _fix_context_toc(context: Dict[str, Any]):
    if "toc" not in context:
        return

    toc: str = context["toc"]
    pattern = re.compile(r'<span class="pre">\w+?\.')
    root = ET.fromstring(toc)
    if len(root) != 1:
        context["toc"] = pattern.sub(".", toc)
        return

    child = root[0]
    if len(child) == 2 and child[1].tag == "ul":
        toc = ET.tostring(child[1]).decode("utf-8")
    context["toc"] = pattern.sub("", toc)


def _expandtoc(toc: str, depth: int = 0):
    depth = int(depth)
    if not toc or not depth:
        # fix for accessibility
        return toc.replace('role="heading">', 'role="heading" aria-level="3">')

    root = ET.fromstring("<div>" + toc.strip() + "</div>")
    for i in range(1, depth + 1):
        elements = root.findall(f'.//li[@class="toctree-l{i}"]')
        for el in elements:
            _classname = el.get("class")
            el.set("class", _classname + " _expand")

    result = ET.tostring(root).decode("utf-8")[5:-6]
    # fix for accessibility
    return result.replace('role="heading">', 'role="heading" aria-level="3">')


def _create_edit_source_link(context: Dict[str, Any]):
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


def _add_readthedocs_context():
    context = {}
    project_slug = os.environ.get("READTHEDOCS_PROJECT")
    if project_slug:
        context["theme_readthedocs_url"] = (
            f"https://readthedocs.org/projects/{project_slug}"
        )
    return context
