.. _sphinx-click:

sphinx-click
============

sphinx-click is a Sphinx plugin that allows you to automatically extract documentation
from a click-based application and include it in your docs.

- **Documentation**: https://sphinx-click.readthedocs.io/
- **Source Code**: https://github.com/click-contrib/sphinx-click

Usage
-----

Install ``sphinx-click``:

.. code-block:: bash

    pip install sphinx-click

Add ``sphinx_click`` to your ``conf.py``:

.. code-block:: python

    extensions = [
        'sphinx_click',
    ]

Example
-------

.. code-block:: none

    .. click:: click_demo:greet
        :prog: greet
        :nested: full

.. click:: click_demo:greet
   :prog: greet
   :nested: full
