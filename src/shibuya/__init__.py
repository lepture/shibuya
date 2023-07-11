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

__version__ = "2023.7.11"

shibuya_version = __version__

THEME_PATH = (Path(__file__).parent / "theme" / "shibuya").resolve()


def _add_version(name: str):
    return name + "?v=" + shibuya_version


def _html_page_context(app: Sphinx, pagename: str, templatename: str, context: Dict[str, Any], doctree):
    assert isinstance(app.builder, StandaloneHTMLBuilder)

    # fixing pageurl, need to submit a PR to sphinx
    if "pageurl" in context:
        pageurl = context["pageurl"]
        context["pageurl"] = normalize_pageurl(pageurl, app.builder.name)

    if "toc" in context:
        context["toc"] = normalize_toc(context['toc'])


def _initialize_builder(app: Sphinx):
    css_files = []
    for filename in app.builder.css_files:
        if filename.endswith(("shibuya.css", "pygments.css")):
            css_files.append(_add_version(filename))
        else:
            css_files.append(filename)
    app.builder.css_files = css_files

    app.add_js_file(_add_version("shibuya.js"))
    app.add_css_file(_add_version("print.css"), media='print')

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
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
