:description: Here is the guide on how to install Shibuya Sphinx theme.

Installation
============

.. rst-class:: lead

   Install the **shibuya** theme as a Python package.

----

Shibuya is a theme for Sphinx_, a popular static site generator for documentation.
It is the default documentation generator for Python projects.

.. _Sphinx: https://www.sphinx-doc.org/

package install
---------------

Shibuya is conveniently available as a Python package on PyPI and can be easily
installed using pip and uv.

.. tab-set::

    .. tab-item:: :iconify:`devicon:pypi` pip
        :class-label: icon-pip

        .. code-block:: shell

            pip install shibuya

    .. tab-item:: :iconify:`material-icon-theme:uv` uv
        :class-label: icon-uv

        .. code-block:: shell

            uv add shibuya

.. hint::
   If you're new to Sphinx, we recommend reading the
   `official tutorial <https://www.sphinx-doc.org/en/master/tutorial/>`_
   for a solid understanding of the platform and its features.


requirements.txt
----------------

If you're tracking dependencies in ``requirements.txt``, you can create a separate
requirements file for your documentation, such as ``requirements-docs.txt``, and
add ``shibuya`` to that file to ensure it is included in your documentation build.

Using shibuya theme
-------------------

Don't forget to update your Sphinx documentation configuration file ``conf.py``:

.. code-block:: python
   :caption: conf.py

   html_theme = "shibuya"

Your documentation should be using **Shibuya** theme now.
