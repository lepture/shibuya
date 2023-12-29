:description: Sphinx design extension looks awesome on Shibuya Sphinx theme.

.. _sphinx-design:

sphinx-design
=============

``sphinx-design`` extension add many components for Sphinx documentation.

**Documentation**: https://sphinx-design.readthedocs.io/

Install
-------

.. code-block:: bash

    pip install sphinx-design

Then, add the extension to your ``conf.py``:

.. code-block:: python
    :caption: conf.py

    extensions = [
        # ...
        "sphinx_design",
    ]

Examples
--------

Grid
~~~~

.. grid:: 2

    .. grid-item-card:: Tutorial
        :link: /install/

        If you're new to Python and Sphinx, this is a great place to start.

    .. grid-item-card:: Customisation
        :link: /customisation/

        Tailor configurations to meet your specific requirements with customizable settings.

    .. grid-item-card:: References
        :link: /writing/

        Learn the syntax of reStructuredText and examine how it is formatted.

    .. grid-item-card:: Contributing
        :link: /contributing/

        Your contributions can make a meaningful impact and help drive the project forward!

Card
~~~~~

.. card:: Card Title

    Header
    ^^^
    Card content
    +++
    Footer

Dropdown
~~~~~~~~

.. dropdown:: Dropdown title

    Dropdown content

Tabs
~~~~

.. tab-set::

    .. tab-item:: Label1

        Content 1

    .. tab-item:: Label2

        Content 2

.. tab-set-code::

    .. code-block:: python

        foo = "str"

    .. code-block:: javascript

        a = 1;

Badges
~~~~~~

:bdg:`plain badge`

:bdg-primary:`primary` :bdg-primary-line:`primary-line`

:bdg-secondary:`secondary` :bdg-secondary-line:`secondary-line`

:bdg-success:`success` :bdg-success-line:`success-line`

:bdg-info:`info` :bdg-info-line:`info-line`

:bdg-warning:`warning` :bdg-warning-line:`warning-line`

:bdg-danger:`danger` :bdg-danger-line:`danger-line`

:bdg-light:`light` :bdg-light-line:`light-line`

:bdg-muted:`muted` :bdg-muted-line:`muted-line`

:bdg-dark:`dark` :bdg-dark-line:`dark-line`

:bdg-black:`black` :bdg-black-line:`black-line`

:bdg-white:`white` :bdg-white-line:`white-line`

:bdg-link-primary:`https://example.com`

:bdg-link-primary-line:`explicit title <https://example.com>`

Buttons
~~~~~~~

.. button-link:: https://example.com

.. button-link:: https://example.com

    Button text

.. button-link:: https://example.com
    :color: primary
    :shadow:

.. button-link:: https://example.com
    :color: primary
    :outline:

.. button-link:: https://example.com
    :color: secondary
    :expand:

Octicon Icons
~~~~~~~~~~~~~

- alert: :octicon:`alert`
- bell: :octicon:`bell`
- book: :octicon:`book`
- clock: :octicon:`clock`
