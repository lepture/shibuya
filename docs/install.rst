Installation
============

Shibuya is a theme for Sphinx_, a popular static site generator for documentation.
It is the default documentation generator for Python projects.

.. _Sphinx: https://www.sphinx-doc.org/

``pip install``
---------------

If you are familiar with Python, you can install **Shibuya** theme easily with ``pip``.

.. code-block:: shell

    pip install Shibuya

requirements.txt
----------------

If you are tracking dependencies in ``requirements.txt``, you may have another
requirements file for docs, maybe it is called ``requirements-docs.txt``, then
you can track ``Shibuya`` in this file.

conf.py
-------

Update Sphinx configuration file ``conf.py``:

.. code-block::

    html_theme = "shibuya"

Your documentation should be using Shibuya theme now.
