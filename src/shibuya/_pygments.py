from typing import Dict, Any, Literal
from pygments.formatters.html import HtmlFormatter
from pygments.style import Style
from sphinx.highlighting import PygmentsBridge


class ShibuyaPygmentsBridge(PygmentsBridge):
    light_style_name = "github-light-default"
    dark_style_name = "github-dark-default"

    @classmethod
    def _wrap_line_html_formatter(cls):
        class WrapLineFormatter(cls.html_formatter):
            def wrap(self, source):
                output = source
                if not self.linespans:
                    output = self._wrap_default_linespans(output)

                if self.wrapcode:
                    output = self._wrap_code(output)

                output = self._wrap_pre(output)
                return output

            def _wrap_default_linespans(self, inner):
                i = self.linenostart - 1
                for t, line in inner:
                    if t:
                        i += 1
                        yield 1, '<span data-line="%d">%s</span>' % (i, line)
                    else:
                        yield 0, line

        return WrapLineFormatter

    def get_formatter(self, **kwargs: Any):
        kwargs.update(self.formatter_args)
        if self.dest == "html":
            return self._wrap_line_html_formatter()(**kwargs)
        return self.formatter(**kwargs)

    def get_stylesheet(self) -> str:
        light_formatter: HtmlFormatter = self.get_formatter()
        dark_formatter: HtmlFormatter = self.formatter(style=self.get_style(self.dark_style_name))
        css = build_highlight_style(light_formatter, "light") + build_highlight_style(dark_formatter, "dark")
        return css


def get_pygments_style_colors(style: Style) -> Dict[str, str]:
    rv: Dict[str, str] = {
        "background": style.background_color,
        "highlight": style.highlight_color,
    }
    for ttype, ndef in style:
        color = ndef["color"]
        if color:
            rv[_convert_token_type_name(ttype)] = webify(color)
    return rv


def build_highlight_style(formatter: HtmlFormatter, color_mode: Literal["light", "dark"]):
    style_vars = get_pygments_style_colors(formatter.style)

    css = ":root {\n"
    for line in _compile_syntax_variables(style_vars, f"--syntax-{color_mode}"):
        css += line + "\n"
    css += "}\n"

    token_styles = [
        (level, ttype, cls, style) for cls, (style, ttype, level) in formatter.class2style.items() if cls and style
    ]
    token_styles.sort()

    if color_mode == "light":
        prefix = formatter.get_css_prefix(["html.light .highlight"])
    else:
        prefix = formatter.get_css_prefix(["html.dark .highlight", "html.light .dark-code .highlight"])

    for _, ttype, cls, style in token_styles:
        key = _convert_token_type_name(ttype)
        if key in style_vars:
            color = style_vars[key]
            style = style.replace(f"color: {color}", f"color: var(--syntax-{color_mode}-{key})")
        css += f"{prefix(cls)} {{ {style} }}\n"
    return css


def _compile_syntax_variables(data: Dict[str, str], prefix: str):
    for key in data:
        value = data[key]
        yield f"{prefix}-{key}: {value};"


def _convert_token_type_name(ttype: Any):
    _token_types = repr(ttype).split(".")[1:]
    return "-".join(tok.lower() for tok in _token_types)


def webify(color: str):
    if color.startswith("calc") or color.startswith("var"):
        return color
    else:
        # Check if the color can be shortened from 6 to 3 characters
        color = color.upper()
        if len(color) == 6 and (color[0] == color[1] and color[2] == color[3] and color[4] == color[5]):
            return f"#{color[0]}{color[2]}{color[4]}"
        else:
            return f"#{color}"
