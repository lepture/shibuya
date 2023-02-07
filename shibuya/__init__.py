from pathlib import Path

__version__ = '1.0.0'

THEME_PATH = (Path(__file__).parent / "theme" / "shibuya").resolve()


def setup(app):
    """Entry point for sphinx theming."""
    app.add_html_theme("shibuya", str(THEME_PATH))
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
