:description: Shibuya theme looks pretty for sphinx-tabs extension.

.. _sphinx-tabs:

sphinx-tabs
===========

sphinx-tab is an extension maintained by Executable Books.
This extension can create tabbed content.

- **Documentation**: https://sphinx-tabs.readthedocs.io/
- **Source Code**: https://github.com/executablebooks/sphinx-tabs

Install
-------

.. code-block:: bash

    pip install sphinx-tabs

Then, add the extension to your ``conf.py``:

.. code-block:: python
    :caption: conf.py

    extensions = [
        # ...
        "sphinx_tabs.tabs",
    ]

Markup syntax
-------------

.. code-block:: reST

    .. tabs::

      .. tab:: Apples

          Apples are green, or sometimes red.

      .. tab:: Pears

          Pears are green.

      .. tab:: Oranges

          Oranges are orange.

    .. tabs::

      .. group-tab:: Linux

          Linux Line 1

      .. group-tab:: Mac OSX

          Mac OSX Line 1

      .. group-tab:: Windows

          Windows Line 1

    .. tabs::

      .. group-tab:: Linux

          Linux Line 1

      .. group-tab:: Mac OSX

          Mac OSX Line 1

      .. group-tab:: Windows

          Windows Line 1


    .. tabs::

      .. code-tab:: c

            int main(const int argc, const char **argv) {
              return 0;
            }

      .. code-tab:: c++

            int main(const int argc, const char **argv) {
              return 0;
            }

      .. code-tab:: py

            def main():
                return

How it looks like
-----------------

.. image:: /_static/screenshots/sphinx-tabs-light.png
   :class: light-only
   :align: center

.. image:: /_static/screenshots/sphinx-tabs-dark.png
   :class: dark-only
   :align: center
