:description: Shibuya theme works well with Algolia sphinx docsearch extension.

.. _docsearch:

sphinx-docsearch
================

``sphinx-docsearch`` replaces Sphinx's built-in search with Algolia DocSearch.

**Documentation**: https://sphinx-docsearch.readthedocs.io/

Install
-------

.. code-block:: bash

    pip install sphinx-docsearch

Then, add the extension to your ``conf.py``:

.. code-block:: python
    :caption: conf.py

    extensions = [
        # ...
        "sphinx_docsearch",
    ]

    docsearch_app_id = "<DOCSEARCH_APP_ID>"
    docsearch_api_key = "<DOCSEARCH_SEARCH_API_KEY>"
    docsearch_index_name = "<DOCSEARCH_INDEX_NAME>"

Screenshots
-----------

``sphinx-docsearch`` looks great in both light and dark mode with Shibuya theme.

.. figure:: /_static/screenshots/docsearch-light.jpg
    :class: rounded
    :align: center

    DocSearch modal in **light** mode.

.. figure:: /_static/screenshots/docsearch-dark.jpg
    :class: rounded
    :align: center

    DocSearch modal in **dark** mode.
