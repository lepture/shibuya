from docutils import nodes
from sphinx import addnodes
from sphinx.transforms.post_transforms import SphinxPostTransform
from pygments.formatters.html import HtmlFormatter


class WrapperPostTransform(SphinxPostTransform):
    formats = ("html",)
    default_priority = 500

    def run(self, **kwargs) -> None:
        """Perform the post-transform on `self.document`."""
        elements = self.document.findall(nodes.table)
        self._wrap(elements, 'table-wrapper')

        elements = self.document.findall(nodes.math_block)
        self._wrap(elements, 'math-wrapper')

        elements = self.document.findall(addnodes.toctree)
        for el in elements:
            el['titlesonly'] = True

    @staticmethod
    def _wrap(elements, classname: str):
        for node in list(elements):
            new_node = nodes.container(classes=[classname])
            new_node.update_all_atts(node)
            node.parent.replace(node, new_node)
            new_node.append(node)


class WrapLineFormatter(HtmlFormatter):
    def __init__(self, **options):
        options.setdefault('linespans', 1)
        super().__init__(**options)

    def _wrap_linespans(self, inner):
        i = self.linenostart - 1
        for t, line in inner:
            if t:
                i += 1
                yield 1, '<span data-line="%d">%s</span>' % (i, line)
            else:
                yield 0, line
