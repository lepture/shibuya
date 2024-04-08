:description: Embed Mermaid flowcharts, sequence diagrams, gantt diagrams and more in your documents with Shibuya theme.

.. _sphinxcontrib-mermaid:

sphinxcontrib-mermaid
=====================

This extension allows you to embed Mermaid graphs in your documents,
including general flowcharts, sequence diagrams, gantt diagrams and more.

- **Documentation**: https://sphinxcontrib-mermaid-demo.readthedocs.io/
- **Source Code**: https://github.com/mgaitan/sphinxcontrib-mermaid

Install
-------

.. code-block:: bash

    pip install sphinxcontrib-mermaid

Then, add the extension to your ``conf.py``:

.. code-block:: python
    :caption: conf.py

    extensions = [
        # ...
        "sphinxcontrib.mermaid",
    ]

Usage
-----

It adds a ``mermaid`` directive to embed mermaid markup. For example:

.. code-block:: none

    .. mermaid::

      sequenceDiagram
          participant Alice
          participant Bob
          Alice->John: Hello John, how are you?
          loop Healthcheck
              John->John: Fight against hypochondria
          end
          Note right of John: Rational thoughts <br/>prevail...
          John-->Alice: Great!
          John->Bob: How about you?
          Bob-->John: Jolly good!

.. mermaid::

   sequenceDiagram
      participant Alice
      participant Bob
      Alice->John: Hello John, how are you?
      loop Healthcheck
          John->John: Fight against hypochondria
      end
      Note right of John: Rational thoughts <br/>prevail...
      John-->Alice: Great!
      John->Bob: How about you?
      Bob-->John: Jolly good!

Mermaid not working
-------------------

You may encounter an error of::

    Uncaught ReferenceError: mermaid is not defined

Here are some possible fixes:

1. There will be a ``requirejs`` conflict with :ref:`nbsphinx` extension,
   you can use ``nbsphinx_requirejs_path`` setting to resolve the issue:

   .. code-block:: python
      :caption: conf.py

      nbsphinx_requirejs_path = ''

2. Mermaid extension is conflict with :ref:`sphinx-jupyter` too, you can
   resolve the issue with ``jupyter_sphinx_require_url`` setting:

   .. code-block:: python
      :caption: conf.py

      jupyter_sphinx_require_url = ''
