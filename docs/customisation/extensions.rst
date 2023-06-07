Extensions
==========

Here lists the Sphinx extensions which work well with Shibuya theme.

sphinx-copybutton
-----------------

Add a little “copy” button to the right of your code blocks.

.. code-block:: bash

    pip install sphinx-copybutton

Then, add the extension to your ``conf.py``:

.. code-block:: python
    :caption: conf.py

    extensions = [
        # ...
        "sphinx_copybutton",
    ]

**Documentation**: https://sphinx-copybutton.readthedocs.io/

sphinx-tabs
-----------

Sphinx tabs extension can create tabbed content.

.. code-block:: bash

    pip install sphinx-tabs

Then, add the extension to your ``conf.py``:

.. code-block:: python
    :caption: conf.py

    extensions = [
        # ...
        "sphinx_tabs.tabs",
    ]

**Documentation**: https://sphinx-tabs.readthedocs.io/


sphinx-design
-------------

Sphinx design extension add many components for Sphinx documentation.

.. code-block:: bash

    pip install sphinx-design

Then, add the extension to your ``conf.py``:

.. code-block:: python
    :caption: conf.py

    extensions = [
        # ...
        "sphinx_design",
    ]

**Documentation**: https://sphinx-design.readthedocs.io/
