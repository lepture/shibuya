.. _sphinx-autoapi:

sphinx-autoapi
==============

Sphinx AutoAPI is a Sphinx extension for generating complete API
documentation without needing to load, run, or import the project
being documented.

- **Documentation**: https://sphinx-autoapi.readthedocs.io/
- **Source Code**: https://github.com/readthedocs/sphinx-autoapi

Usage
-----

Install ``sphinx-autoapi``:

.. code-block:: bash

    pip install sphinx-autoapi

Add ``autoapi.extension`` to your ``conf.py``:

.. code-block:: python

    extensions = [
        'autoapi.extension',
    ]
