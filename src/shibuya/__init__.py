from typing import Dict, Any
from pathlib import Path
from sphinx.application import Sphinx
from sphinx.builders.html import StandaloneHTMLBuilder
from .context import (
    BASE_CSS_VARIABLES,
    LIGHT_CSS_VARIABLES,
    DARK_CSS_VARIABLES,
    css_to_dict,
    normalize_pageurl,
    normalize_toc,
)
from ._sphinx import WrapperPostTransform, WrapLineFormatter

__version__ = '2023.2.23a1'

shibuya_version = __version__

THEME_PATH = (Path(__file__).parent / "theme" / "shibuya").resolve()


def _html_page_context(app: Sphinx, pagename: str, templatename: str, context: Dict[str, Any], doctree):
    assert isinstance(app.builder, StandaloneHTMLBuilder)
    context["shibuya_base_css_variables"] = css_to_dict(BASE_CSS_VARIABLES)
    context["shibuya_light_css_variables"] = css_to_dict(LIGHT_CSS_VARIABLES)
    context["shibuya_dark_css_variables"] = css_to_dict(DARK_CSS_VARIABLES)

    # fixing pageurl, need to submit a PR to sphinx
    if 'pageurl' in context:
        pageurl = context['pageurl']
        context['pageurl'] = normalize_pageurl(pageurl, app.builder.name)

    if 'toc' in context:
        context['toc'] = normalize_toc(context['toc'])

    if 'script_files' in context:
        script_files = context['script_files']
        script_files.append(f'_static/shibuya.js?v={shibuya_version}')
        context['script_files'] = script_files

    if 'css_files' in context:
        css_files = [f'{name}?v={shibuya_version}' for name in context['css_files']]
        context['css_files'] = css_files


def _initialize_builder(app: Sphinx):
    app.builder.highlighter.formatter = WrapLineFormatter


def setup(app: Sphinx):
    """Entry point for sphinx theming."""
    app.add_html_theme("shibuya", str(THEME_PATH))
    app.add_post_transform(WrapperPostTransform)
    app.connect('builder-inited', _initialize_builder)
    app.connect("html-page-context", _html_page_context)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
