# Markdown

In addition to reStructuredText, Shibuya supports writing documentation
in Markdown using the MyST parser for Sphinx.

## Install

To enable Markdown support in your Sphinx documentation, you need to
install the `myst-parser` package. You can do this using pip:

::::{tab-set}
:class: outline

:::{tab-item} {iconify}`devicon:pypi` pip
```bash
pip install myst-parser
```
:::

:::{tab-item} {iconify}`material-icon-theme:uv` uv
```bash
uv add --dev myst-parser
```
:::

::::

## MyST

After installing `myst-parser`, you need to enable it in your Sphinx
configuration file (`conf.py`). Open `conf.py` and add "myst_parser"
to the list of extensions:

```{code-block} python
:caption: conf.py

extensions = [
    # ...
    "myst_parser"
]
```

```{hint}
This documentation itself is written in Markdown. To view the source code,
click the **Edit this page** link on the right sidebar.
```
