import re
from typing import Dict, Any
from pathlib import Path
from sphinx.builders.html import StandaloneHTMLBuilder
from .context import (
    BASE_CSS_VARIABLES,
    LIGHT_CSS_VARIABLES,
    DARK_CSS_VARIABLES,
    css_to_dict,
)

__version__ = '1.0.0'

THEME_PATH = (Path(__file__).parent / "theme" / "shibuya").resolve()


def _render_toc(toc: str):
    toc = re.sub(r'^<ul>\n<li>.*?</a>', '', toc)
    toc = re.sub(r'</li>\n</ul>$', '', toc)
    return toc


def _html_page_context(app, pagename: str, templatename: str, context: Dict[str, Any], doctree):
    assert isinstance(app.builder, StandaloneHTMLBuilder)
    context["shibuya_base_css_variables"] = css_to_dict(BASE_CSS_VARIABLES)
    context["shibuya_light_css_variables"] = css_to_dict(LIGHT_CSS_VARIABLES)
    context["shibuya_dark_css_variables"] = css_to_dict(DARK_CSS_VARIABLES)
    context['render_toc'] = _render_toc

    # TODO: add versions
    if 'script_files' in context:
        context['script_files'].append('_static/shibuya.js')


def setup(app):
    """Entry point for sphinx theming."""
    app.add_html_theme("shibuya", str(THEME_PATH))
    app.connect("html-page-context", _html_page_context)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
