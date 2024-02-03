.. _sphinx-togglebutton:

sphinx-togglebutton
===================

A small sphinx extension to add “toggle button” elements to sections of your page.

**Documentation**: https://sphinx-togglebutton.readthedocs.io/

Install
-------

.. code-block:: bash

    pip install sphinx-togglebutton

Then, add the extension to your ``conf.py``:

.. code-block:: python
    :caption: conf.py

    extensions = [
        # ...
        "sphinx_togglebutton",
    ]

Usage
-----

``dropdown`` for admonitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ReST

    .. admonition:: Click the title to toggle
        :class: dropdown

        This title was made into a dropdown admonition by adding ``:class: dropdown`` to it.

.. admonition:: Click the title to toggle
    :class: dropdown

    This title was made into a dropdown admonition by adding ``:class: dropdown`` to it.


.. admonition:: Benchmark
    :class: dropdown

    .. code-block:: python
        :caption: bench.py

        print("Hello, world!")


``toggle`` class
~~~~~~~~~~~~~~~~

.. code-block:: ReST

    .. image:: https://media.giphy.com/media/FaKV1cVKlVRxC/giphy.gif
        :class: toggle

.. image:: https://media.giphy.com/media/FaKV1cVKlVRxC/giphy.gif
    :class: toggle


``toggle`` directive
~~~~~~~~~~~~~~~~~~~~

.. code-block:: ReST

    .. toggle::

        This is a toggled content block!

.. toggle::

    This is a toggled content block!
