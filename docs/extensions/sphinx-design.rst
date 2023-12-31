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

Single card
~~~~~~~~~~~

A simple card:

.. card:: Card Title

    Card content

A full featured card:

.. card:: Card Title

    Header
    ^^^
    Card content
    +++
    Footer

Card with header:

.. card:: Card Title

    Header
    ^^^
    Card content

Card with footer:

.. card:: Card Title

    Card content
    +++
    Footer

Grid items
~~~~~~~~~~

.. grid:: 1 2 3 3
    :outline:

    .. grid-item::

        A

    .. grid-item::

        B

    .. grid-item::

        C

Grid cards
~~~~~~~~~~

.. grid:: 1 1 2 2
    :padding: 0
    :gutter: 2

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

Nesting grids
~~~~~~~~~~~~~

.. grid:: 1 1 2 2
    :padding: 0
    :gutter: 1

    .. grid-item::

        .. grid:: 1 1 1 1
            :gutter: 1

            .. grid-item-card:: Item 1.1

                Multi-line

                content

            .. grid-item-card:: Item 1.2

                Content

    .. grid-item::

        .. grid:: 1 1 1 1
            :gutter: 1

            .. grid-item-card:: Item 2.1

                Content

            .. grid-item-card:: Item 2.2

                Content

            .. grid-item-card:: Item 2.3

                Content

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

Article Info
------------

.. article-info::
    :avatar: https://sphinx-design.readthedocs.io/en/latest/_images/ebp-logo.png
    :avatar-link: https://executablebooks.org/
    :avatar-outline: muted
    :author: Executable Books
    :date: Jul 24, 2021
    :read-time: 5 min read
    :class-container: sd-p-2 sd-outline-muted sd-rounded-1

Only with Shibuya
-----------------

By adding a class of ``surface``, a card would be rendered:

.. code-block:: none

    .. grid:: 1 1 2 3
        :class-row: surface

.. grid:: 1 1 2 3
    :gutter: 2
    :padding: 0
    :class-container: surface

    .. grid-item-card:: :octicon:`star` Beautiful Design

        A visually stunning and modern design that makes your documentation
        look professional and appealing.

    .. grid-item-card:: :octicon:`zap` Responsive Layout

        Look great on all devices, from desktops to smartphones, without
        compromising on readability or functionality.

    .. grid-item-card:: :octicon:`moon` Light/Dark Mode

        Users can switch between light and dark modes according to their
        preference.

    .. grid-item-card:: :octicon:`paintbrush` Customizable Colors
        :link: /customisation/colors/

        Customize the colors to match your brand or personal preferences
        with radix colors.

    .. grid-item-card:: :octicon:`beaker` Jupyter Integration
        :link: /extensions/nbsphinx/

        Great CSS/UI for lots of Jupyter related extensions, enhance your
        AI documentation.

    .. grid-item-card:: :octicon:`browser` Multiple Layouts
        :link: /writing/meta/#layout

        Layouts of landing page, simple one page, and three-column
        documentation page.
