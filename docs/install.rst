Installation
============

Shibuya is a theme for Sphinx_, a popular static site generator for documentation.
It is the default documentation generator for Python projects.

.. _Sphinx: https://www.sphinx-doc.org/

``pip install``
---------------

Shibuya is conveniently available as a Python package on PyPI and can be easily
installed using pip.

.. tab-set::

    .. tab-item:: Latest

        .. code-block:: shell

            pip install shibuya

    .. tab-item:: Development

        .. code-block:: shell

            pip install "shibuya @ git+https://github.com/lepture/shibuya"

.. hint::
   If you're new to Sphinx, we recommend reading the
   `official tutorial <https://www.sphinx-doc.org/en/master/tutorial/>`_
   for a solid understanding of the platform and its features.


requirements.txt
----------------

If you're tracking dependencies in ``requirements.txt``, you can create a separate
requirements file for your documentation, such as ``requirements-docs.txt``, and
add ``shibuya`` to that file to ensure it is included in your documentation build.

Using this theme
----------------

Update Sphinx configuration file ``conf.py``:

.. code-block::

    html_theme = "shibuya"

Your documentation should be using Shibuya theme now.
