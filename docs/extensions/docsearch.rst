:description: Shibuya theme works well with Algolia sphinx docsearch extension.

.. _docsearch:

sphinx-docsearch
================

``sphinx-docsearch`` replaces Sphinx's built-in search with Algolia DocSearch.

- **Documentation**: https://sphinx-docsearch.readthedocs.io/
- **Source Code**: https://github.com/algolia/sphinx-docsearch

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

Docsearch troubleshoots
-----------------------

If Algolia Docsearch does not show in the navbar, please check your browser's
console log. You may encounter an error of requirejs. This error is usually
caused by conflicts with other sphinx extensions.

1. If using together with :ref:`nbsphinx` extension, you can use
   ``nbsphinx_requirejs_path`` setting to resolve the issue:

   .. code-block:: python
      :caption: conf.py

      nbsphinx_requirejs_path = ''

2. If using together with :ref:`jupyter-sphinx` extension, you can
   resolve the issue with ``jupyter_sphinx_require_url`` setting:

   .. code-block:: python
      :caption: conf.py

      jupyter_sphinx_require_url = ''
