from docutils import nodes
from sphinx.transforms.post_transforms import SphinxPostTransform


class WrapperPostTransform(SphinxPostTransform):
    formats = ("html",)
    default_priority = 500

    def run(self, **kwargs) -> None:
        """Perform the post-transform on `self.document`."""
        elements = self.document.findall(nodes.table)
        self._wrap(elements, 'table-wrapper')

        elements = self.document.findall(nodes.math_block)
        self._wrap(elements, 'math-wrapper')

    @staticmethod
    def _wrap(elements, classname: str):
        for node in list(elements):
            new_node = nodes.container(classes=[classname])
            new_node.update_all_atts(node)
            node.parent.replace(node, new_node)
            new_node.append(node)
