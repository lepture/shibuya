import re
import os
import xml.etree.ElementTree as ET
from typing import Dict, Any, List, Optional
from pathlib import Path
from sphinx.config import Config
from sphinx.application import Sphinx
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.builders.dirhtml import DirectoryHTMLBuilder
from ._pygments import ShibuyaPygmentsBridge
from ._social_links import patch_social_context


def patch_builder_inited(app: Sphinx):
    if isinstance(app.builder, StandaloneHTMLBuilder):
        _fix_builder_highlighter(app.builder)
        _fix_builder_globals(
            app.builder,
            {
                "expandtoc": _expandtoc,
                "edit_source_link": _create_edit_source_link(app.config.html_context),
                "view_source_link": _create_view_source_link(app.config),
            },
        )

    if isinstance(app.builder, DirectoryHTMLBuilder):
        _get_outfilename = app.builder.get_outfilename

        def get_outfilename(pagename: str) -> str:
            if pagename == "404":
                return (Path(app.builder.outdir) / "404.html").resolve()
            return _get_outfilename(pagename)

        app.builder.get_outfilename = get_outfilename


def patch_html_page_context(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: Dict[str, Any],
    doctree: Any,
) -> None:
    if not isinstance(app.builder, StandaloneHTMLBuilder):
        return

    patch_social_context(context)
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
    context["_sphinx_extensions"] = app.config.extensions

    # Section-scoped navigation support
    theme_options = context.get("theme_navigation_scope", "")
    if theme_options == "section":
        _patch_section_navigation(app, context)


def _fix_builder_highlighter(builder: StandaloneHTMLBuilder) -> None:
    # remove dark_highlighter
    builder.dark_highlighter = None

    default_style = ShibuyaPygmentsBridge.light_style_name
    dark_style = None

    if builder.config.pygments_style is not None:
        default_style = builder.config.pygments_style
    elif getattr(builder, "theme", None):
        dark_style = builder.theme.pygments_style_dark
        default_style = builder.theme.pygments_style_default or "none"

    highlighter = ShibuyaPygmentsBridge("html", default_style)
    if dark_style:
        highlighter.dark_style_name = dark_style

    builder.highlighter = highlighter


def _fix_builder_globals(builder: StandaloneHTMLBuilder, context: Dict[str, Any]) -> None:
    builder.templates.environment.globals.update(_add_readthedocs_context())
    builder.templates.environment.globals.update(context)


def _fix_context_pageurl(app: Sphinx, context: Dict[str, Any]) -> None:
    pageurl: str = context.get("pageurl")
    if not pageurl:
        return

    if pageurl.endswith("/index.html"):
        context["pageurl"] = re.sub(r"index\.html$", "", pageurl)
    if isinstance(app.builder, DirectoryHTMLBuilder) and pageurl.endswith(".html"):
        context["pageurl"] = re.sub(r"\.html$", "/", pageurl)


def _fix_context_toc(context: Dict[str, Any]):
    toc: str = context.get("toc")
    if not toc:
        return

    root = ET.fromstring(toc)
    if len(root) == 1:
        child = root[0]
        if len(child) == 2 and child[1].tag == "ul":
            toc = ET.tostring(child[1]).decode("utf-8")
            context["toc"] = toc


def _patch_section_navigation(app: Sphinx, context: Dict[str, Any]) -> None:
    """Inject section-scoped navigation data into the template context.

    When ``navigation_scope`` is ``"section"``, this function:
    - Generates the full global toctree
    - Extracts L1 items for the top navbar (``section_nav_items``)
    - Extracts L2+ subtree for the active section (``section_toctree``)
    """
    toctree_func = context.get("toctree")
    if toctree_func is None:
        return

    # Generate the full global toctree with the same options used by default.html
    collapse = context.get("theme_toctree_collapse", "")
    maxdepth = int(context.get("theme_toctree_maxdepth", 4) or 4)
    titles_only = context.get("theme_toctree_titles_only", True)
    includehidden = context.get("theme_toctree_includehidden", True)

    full_toc = toctree_func(
        collapse=collapse,
        maxdepth=maxdepth,
        titles_only=titles_only,
        includehidden=includehidden,
    )

    if not full_toc:
        context["section_nav_items"] = []
        context["section_toctree"] = ""
        return

    context["section_nav_items"] = _get_section_nav_items(full_toc)
    context["section_toctree"] = _get_section_toctree(full_toc)


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
            if _classname:
                el.set("class", _classname + " _expand")

    result = ET.tostring(root).decode("utf-8")[5:-6]
    # fix for accessibility
    return result.replace('role="heading">', 'role="heading" aria-level="3">')



def _check_toctree_contains_page(li_element, pagename: str) -> bool:
    """Check if a toctree <li> element or any of its descendants links to the given pagename."""
    for a in li_element.iter("a"):
        href = a.get("href", "")
        # Normalize: strip anchors, trailing slashes, and .html extension
        href_clean = href.split("#")[0].rstrip("/")
        if href_clean.endswith(".html"):
            href_clean = href_clean[:-5]
        # Also strip leading path segments like ../ for relative links
        href_clean = href_clean.rsplit("/", 1)[-1] if "/" in href_clean else href_clean
        page_clean = pagename.rsplit("/", 1)[-1] if "/" in pagename else pagename
        if href_clean == page_clean:
            return True
    # Also check "current" class which Sphinx adds to the active item
    classname = li_element.get("class", "")
    if "current" in classname:
        return True
    return False


def _get_section_nav_items(toc: str) -> List[Dict[str, str]]:
    """Extract L1 navigation items from the global toctree HTML.

    Returns a list of dicts with 'title', 'url', and 'current' keys.
    """
    if not toc:
        return []

    root = ET.fromstring("<div>" + toc.strip() + "</div>")
    items = []
    # Find all top-level <li> elements (toctree-l1)
    for li in root.findall('.//li[@class]'):
        classname = li.get("class", "")
        if not classname.startswith("toctree-l1"):
            continue
        # Get the first <a> child for the link
        a = li.find("a")
        if a is None:
            continue
        title = a.text or ""
        # If the <a> has child elements (e.g. <span>), get full text
        if not title:
            title = "".join(a.itertext())
        url = a.get("href", "")
        is_current = "current" in classname
        items.append({
            "title": title.strip(),
            "url": url,
            "current": is_current,
        })
    return items


def _get_section_toctree(toc: str) -> str:
    """Extract the L2+ subtree for the currently active L1 section.

    Returns the inner HTML of the active section's <ul> subtree,
    or an empty string if no section is active.
    """
    if not toc:
        return ""

    root = ET.fromstring("<div>" + toc.strip() + "</div>")
    # Find the L1 <li> that has the "current" class
    for li in root.findall('.//li[@class]'):
        classname = li.get("class", "")
        if not classname.startswith("toctree-l1"):
            continue
        if "current" not in classname:
            continue
        # Found the active section — get its child <ul> (L2+ items)
        sub_ul = li.find("ul")
        if sub_ul is None:
            return ""
        # Re-wrap as a top-level toctree so the existing CSS classes work.
        # Remap toctree-l2 -> toctree-l1, toctree-l3 -> toctree-l2, etc.
        for sub_li in sub_ul.iter("li"):
            sub_class = sub_li.get("class", "")
            for level in range(9, 1, -1):
                sub_class = sub_class.replace(
                    f"toctree-l{level}", f"toctree-l{level - 1}"
                )
            sub_li.set("class", sub_class)
        return ET.tostring(sub_ul).decode("utf-8")
    return ""


def _create_edit_source_link(context: Dict[str, Any]):
    source_type = context.get("source_type")
    source_user = context.get("source_user")
    source_repo = context.get("source_repo")
    source_docs_path = context.get("source_docs_path", "/docs/")
    source_version = context.get("source_version", "main")
    source_edit_template = context.get("source_edit_template")

    def edit_source_link(filename: str) -> Optional[str]:
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


def _create_view_source_link(config: Config):
    site_url = config.html_baseurl
    copy_source = config.html_copy_source

    context = config.html_context
    source_type = context.get("source_type")
    source_user = context.get("source_user")
    source_repo = context.get("source_repo")
    source_docs_path = context.get("source_docs_path", "/docs/")
    source_version = context.get("source_version", "main")
    source_view_template = context.get("source_view_template")

    def view_source_link(filename: str) -> Optional[str]:
        if site_url and copy_source:
            return site_url.rstrip("/") + "/_sources/" + filename

        if source_view_template:
            return source_view_template.format(filename)

        if not source_user or not source_repo:
            return

        if source_type == "github":
            url = f"https://raw.githubusercontent.com/{source_user}/{source_repo}/refs/heads"
        elif source_type == "gitlab":
            url = f"https://gitlab.com/{source_user}/{source_repo}/-/raw"
        elif source_type == "bitbucket":
            url = f"https://bitbucket.org/{source_user}/{source_repo}/raw"
        else:
            return

        return f"{url}/{source_version}{source_docs_path}{filename}"

    return view_source_link


def _add_readthedocs_context():
    context: Dict[str, Any] = {}
    project_slug = os.environ.get("READTHEDOCS_PROJECT")
    if project_slug:
        context["theme_readthedocs_url"] = f"https://readthedocs.org/projects/{project_slug}"
    return context
