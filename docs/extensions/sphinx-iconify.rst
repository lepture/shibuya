:description: Sphinx Iconify allowing you to embed icons from over 200000 open-source vector icons for your documentation.

.. _sphinx-iconify:

sphinx-iconify
==============

``sphinx-iconify`` provides the ``:iconify:`` role, which allows you to use
the ``<iconify-icon>`` web component

- **Documentation**: https://sphinx-iconify.lepture.com/
- **Source Code**: https://github.com/lepture/sphinx-iconify

Install
-------

.. code-block:: bash

    pip install sphinx-iconify

Then, add the extension to your ``conf.py``:

.. code-block:: python
    :caption: conf.py

    extensions = [
        # ...
        "sphinx_iconify",
    ]

Examples
--------

Using the ``:iconify:`` role is very simple :iconify:`simple-icons:python`:

.. code-block:: reST

    :iconify:`simple-icons:python`

Our :ref:`install` page is using **sphinx-iconify**, the source code
for the "package install" part:

.. code-block:: reST

    .. tab-set::
        :class: outline

        .. tab-item:: :iconify:`devicon:pypi` pip

            .. code-block:: shell

                pip install shibuya

        .. tab-item:: :iconify:`material-icon-theme:uv` uv

            .. code-block:: shell

                uv add --dev shibuya


.. tab-set::
    :class: outline

    .. tab-item:: :iconify:`devicon:pypi` pip

        .. code-block:: shell

            pip install shibuya

    .. tab-item:: :iconify:`material-icon-theme:uv` uv

        .. code-block:: shell

            uv add --dev shibuya

Only with Shibuya
-----------------

Since shibuya theme has built-in accent colors, it is also possible to
decorate the icon :iconify:`simple-icons:python data-accent-color=indigo`
with a ``data-accent-color`` attribute:

.. code-block:: reST

    :iconify:`simple-icons:python data-accent-color=indigo`

You can find all the supported colors on :ref:`accent-colors`.
