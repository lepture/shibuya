:description: How API documentation looks like on Shibuya Sphinx theme.

API reference
=============

Here are examples of ``automodule``, ``autoclass``, and ``autofunction`` directives.

automodule
----------

.. code-block:: rst

    .. automodule:: babel.units
        :members:
        :noindex:

.. automodule:: babel.units
    :members:

autoclass
---------

.. code-block:: rst

    .. autoclass:: babel.support.Format
        :members:
        :noindex:

.. autoclass:: babel.support.Format
    :members:

autofunction
------------

.. code-block:: rst

    .. autofunction:: babel.util.distinct

.. autofunction:: babel.util.distinct
    :noindex:
