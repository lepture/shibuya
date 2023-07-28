from typing import Dict, Any
from pathlib import Path
from sphinx.application import Sphinx
from sphinx.builders.html import StandaloneHTMLBuilder
from .context import (
    css_to_dict,
    normalize_pageurl,
    normalize_toc,
    create_edit_source_link,
)
from ._sphinx import (
    WrapperPostTransform,
    WrapLineFormatter,
)

__version__ = "2023.7.28"

shibuya_version = __version__

ROOT_PATH = Path(__file__).parent
THEME_PATH = (ROOT_PATH / "theme" / "shibuya").resolve()


def _html_page_context(app: Sphinx, pagename: str, templatename: str, context: Dict[str, Any], doctree):
    assert isinstance(app.builder, StandaloneHTMLBuilder)

    # fixing pageurl, need to submit a PR to sphinx
    if "pageurl" in context:
        pageurl = context["pageurl"]
        context["pageurl"] = normalize_pageurl(pageurl, app.builder.name)

    if "toc" in context:
        context["toc"] = normalize_toc(context['toc'])

    def create_i18n_link(pattern: str):
        url = pattern.replace("%s", pagename)
        if pagename == "index" or pagename.endswith("/index"):
            if url.endswith("/index/"):
                url = url.replace("/index/", "/")
            elif url.endswith("/index.html"):
                url = url.replace("/index.html", "/")
        return url

    context["i18n_link"] = create_i18n_link


def _initialize_builder(app: Sphinx):
    app.add_js_file("shibuya.js")
    app.add_css_file("print.css", media='print')

    edit_source_link = create_edit_source_link(app.config.html_context)
    app.config.html_context.update({
        "shibuya_base_css_variables": css_to_dict("base.css"),
        "shibuya_light_css_variables": css_to_dict("light.css"),
        "shibuya_dark_css_variables": css_to_dict("dark.css"),
        "edit_source_link": edit_source_link,
    })

    app.builder.highlighter.formatter = WrapLineFormatter


def setup(app: Sphinx):
    """Entry point for sphinx theming."""
    app.add_html_theme("shibuya", str(THEME_PATH))
    app.add_post_transform(WrapperPostTransform)
    app.connect("builder-inited", _initialize_builder)
    app.connect("html-page-context", _html_page_context)
    app.add_message_catalog("sphinx", ROOT_PATH / "locale")
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
