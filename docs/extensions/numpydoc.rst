:description: Shibuya theme has built-in integration with numpydoc extension.

.. _numpydoc:

numpydoc
========

Numpy's Sphinx extensions to power Numpy's docstring syntax.

**Documentation**: https://numpydoc.readthedocs.io/

Install
-------

.. code-block:: bash

    pip install numpydoc

Then, add the extension to your ``conf.py``:

.. code-block:: python
    :caption: conf.py

    extensions = [
        # ...
        "numpydoc",
    ]

Examples
--------

.. automodule:: numpydoc_example
    :members:
