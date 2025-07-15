.. _sphinx-sqlalchemy:

sphinx-sqlalchemy
=================

Sphinx extension for documenting SQLAlchemy ORMs.

- **Documentation**: https://sphinx-sqlalchemy.readthedocs.io/
- **Source Code**: https://github.com/sphinx-extensions2/sphinx-sqlalchemy

Usage
-----

Install ``sphinx_sqlalchemy``:

.. code-block:: bash

    pip install sphinx_sqlalchemy

Add ``sphinx_sqlalchemy`` to your ``conf.py``:

.. code-block:: python

    extensions = [
        'sphinx_sqlalchemy',
    ]

Example
-------

.. code-block:: reST

    .. sqla-model:: sqla_models.User

    .. sqla-model:: ~sqla_models.Address


.. sqla-model:: sqla_models.User

.. sqla-model:: ~sqla_models.Address
