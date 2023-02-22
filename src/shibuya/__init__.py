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
from ._sphinx import WrapperPostTransform

__version__ = '1.0.0'

shibuya_version = __version__

THEME_PATH = (Path(__file__).parent / "theme" / "shibuya").resolve()


def _render_toc(toc: str):
    toc = re.sub(r'^<ul>\n<li>.*?</a>', '', toc)
    toc = re.sub(r'</li>\n</ul>$', '', toc)
    return toc


def _normalize_pageurl_dirhtml(pageurl: str):
    if pageurl.endswith('/index.html'):
        return re.sub(r'index\.html$', '', pageurl)
    elif pageurl.endswith('.html'):
        return re.sub(r'\.html$', '/', pageurl)
    return pageurl


def _html_page_context(app, pagename: str, templatename: str, context: Dict[str, Any], doctree):
    assert isinstance(app.builder, StandaloneHTMLBuilder)
    context["shibuya_base_css_variables"] = css_to_dict(BASE_CSS_VARIABLES)
    context["shibuya_light_css_variables"] = css_to_dict(LIGHT_CSS_VARIABLES)
    context["shibuya_dark_css_variables"] = css_to_dict(DARK_CSS_VARIABLES)
    context['render_toc'] = _render_toc

    # fixing pageurl, need to submit a PR to sphinx
    if 'pageurl' in context:
        pageurl = context['pageurl']
        if app.builder.name == 'dirhtml':
            context['pageurl'] = _normalize_pageurl_dirhtml(pageurl)

    if 'script_files' in context:
        script_files = context['script_files']
        script_files.append(f'_static/shibuya.js?v={shibuya_version}')
        context['script_files'] = script_files

    if 'css_files' in context:
        css_files = [f'{name}?v={shibuya_version}' for name in context['css_files']]
        context['css_files'] = css_files


def setup(app):
    """Entry point for sphinx theming."""
    app.add_html_theme("shibuya", str(THEME_PATH))
    app.add_post_transform(WrapperPostTransform)
    app.connect("html-page-context", _html_page_context)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
