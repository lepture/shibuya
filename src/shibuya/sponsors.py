import json
import typing as t
from urllib.request import urlopen
from functools import cache
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective


class SponsorData(t.TypedDict):
    name: str
    login: str
    avatar: str
    amount: int
    link: str
    org: bool


@cache
def fetch_sponsors_data(url: str):
    with urlopen(url) as response:
        data = json.load(response)
    return data


class SponsorsDirective(SphinxDirective):
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "show-name": directives.flag,
        "center": directives.flag,
        "rounded": directives.flag,
        "url": directives.uri,
        "container-class": directives.unchanged,
        "amount": directives.positive_int_list,
        "size": directives.unchanged,
    }
    default_class_name = "sphinx-sponsors"

    def build_sponsors(self, sponsors: t.List[SponsorData]):
        list_nodes = nodes.bullet_list(classes=[self.default_class_name + '_container'])
        for sponsor in sponsors:
            item_node = nodes.list_item(classes=[self.default_class_name + '_item'])
            for node in self.build_sponsor(sponsor):
                item_node.append(node)
            list_nodes.append(item_node)
        yield list_nodes

    def build_sponsor(self, sponsor: SponsorData):
        link_node = nodes.reference(
            "", "",
            internal=False,
            refuri=sponsor["link"],
            classes=[self.default_class_name + '_avatar'],
        )
        avatar_image = nodes.image(
            uri=sponsor["avatar"],
            alt=sponsor["name"],
        )
        link_node += avatar_image
        yield link_node

        if "show-name" in self.options:
            yield nodes.inline(
                sponsor["name"],
                sponsor["name"],
                classes=[self.default_class_name + "_name"],
            )

    def run(self):
        amount = self.options["amount"]
        if 'url' in self.options:
            url = self.options['url']
            all_sponsors = fetch_sponsors_data(url)
        else:
            all_sponsors = fetch_sponsors_data(self.config.sponsors_json_url)

        if not amount:
            sponsors = [item for item in all_sponsors if item["amount"] <= 0]
        elif len(amount) == 1:
            sponsors = [item for item in all_sponsors if item["amount"] >= amount[0]]
        else:
            start, end = amount
            sponsors = [
                item for item in all_sponsors
                if item["amount"] >= start and item["amount"] < end
            ]

        if not sponsors:
            return []

        size = self.options.get("size", "base")
        classes = [self.default_class_name, self.default_class_name + f'--{size}']

        if "show-name" in self.options:
            classes.append(self.default_class_name + "--show-name")
        if "center" in self.options:
            classes.append(self.default_class_name + "--center")
        if "rounded" in self.options:
            classes.append(self.default_class_name + "--rounded")

        if "container-class" in self.options:
            classes.append(self.options["container-class"])

        container = nodes.container(
            "",
            has_title=len(self.arguments) > 0,
            classes=classes,
        )
        self.set_source_info(container)
        if self.arguments:
            textnodes, messages = self.state.inline_text(self.arguments[0], self.lineno)
            title_node = nodes.rubric(self.arguments[0], "", *textnodes)
            container += title_node
            container += messages
            self.add_name(title_node)
        else:
            self.add_name(container)
        for node in self.build_sponsors(sponsors):
            container.append(node)
        return [container]


def setup(app: Sphinx):
    # Add directive
    app.add_config_value("sponsors_json_url", "", "env")
    app.add_directive("sponsors", SponsorsDirective)
