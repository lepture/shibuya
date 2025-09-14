from pathlib import Path
from sphinx.application import Sphinx
from ._patch import (
    patch_app_builder,
    patch_html_page_context,
)
from ._wrapper import WrapperPostTransform

__version__ = "2025.8.16"

shibuya_version = __version__

ROOT_PATH = Path(__file__).parent
THEME_PATH = (ROOT_PATH / "theme" / "shibuya").resolve()


def _initialize_builder(app: Sphinx):
    app.add_js_file("shibuya.js")
    app.add_css_file("print.css", media="print")
    patch_app_builder(app)


def setup(app: Sphinx):
    """Entry point for sphinx theming."""
    app.add_html_theme("shibuya", str(THEME_PATH))
    app.add_post_transform(WrapperPostTransform)
    app.connect("builder-inited", _initialize_builder)
    app.connect("html-page-context", patch_html_page_context)
    app.add_message_catalog("sphinx", ROOT_PATH / "locale")
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
