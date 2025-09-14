from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.builders.dirhtml import DirectoryHTMLBuilder
from ._pygments import ShibuyaPygmentsBridge


class ShibuyaStandaloneHTMLBuilder(StandaloneHTMLBuilder):
    shibuya = True

    def init_highlighter(self) -> None:
        print("***** init_highlighter")
        # remove dark_highlighter
        self.dark_highlighter = None

        default_style = "a11y-light"
        dark_style = None

        if self.config.pygments_style is not None:
            default_style = self.config.pygments_style
        elif getattr(self, "theme", None):
            dark_style = self.theme.pygments_style_dark
            default_style = self.theme.pygments_style_default or "none"

        highlighter = ShibuyaPygmentsBridge("html", default_style)
        if dark_style:
            highlighter.dark_style_name = dark_style

        self.highlighter = highlighter


class ShibuyaDirectoryHTMLBuilder(ShibuyaStandaloneHTMLBuilder, DirectoryHTMLBuilder):
    pass
