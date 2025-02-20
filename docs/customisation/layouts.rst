:description: Shibuya theme offers several page layouts...

Layouts
=======

.. rst-class:: lead

    Change the page layout of your documentation.

----

The Shibuya theme provides various page layouts for your documentation. You have the
flexibility to change the layout for your entire documentation site or individual pages.

Global layout
-------------

You can customize the global page layout by adjusting the ``page_layout`` settings within
the ``html_context`` option in your Sphinx configuration file (``conf.py``):

.. code-block::
    :caption: conf.py

    html_theme_options = {
        "page_layout": "default",
    }

The default ``page_layout`` is ``default``.

Page layout
-----------

Utilize :ref:`meta` to modify the layout of individual pages:

.. code-block:: none

   :layout: default

Layout templates
----------------

Built-in layout templates that Shibuya theme offers:

Default layout
~~~~~~~~~~~~~~

The ``default`` layout features a three-column design:

- the left sidebar contains the global table of contents,
- the right sidebar holds the local table of contents,
- and the center displays the main page content.

.. image:: /_static/screenshots/layout-light-default.jpg
   :class: light-only rounded

.. image:: /_static/screenshots/layout-dark-default.jpg
   :class: dark-only rounded

.. code-block::
    :caption: conf.py

    html_theme_options = {
        "page_layout": "default",
    }

Compact layout
~~~~~~~~~~~~~~

The ``compact`` layout features a two-column design:

- the right sidebar holds the local table of contents,
- and the center displays the main page content.

.. image:: /_static/screenshots/layout-light-compact.jpg
   :class: light-only rounded

.. image:: /_static/screenshots/layout-dark-compact.jpg
   :class: dark-only rounded

.. code-block::
    :caption: conf.py

    html_theme_options = {
        "page_layout": "compact",
    }

Simple layout
~~~~~~~~~~~~~

A ``simple`` layout exclusively displays the page content without
any sidebars—ideal for generating single-page documentation.

.. image:: /_static/screenshots/layout-light-simple.jpg
   :class: light-only rounded

.. image:: /_static/screenshots/layout-dark-simple.jpg
   :class: dark-only rounded

.. code-block::
    :caption: conf.py

    html_theme_options = {
        "page_layout": "simple",
    }

Landing layout
~~~~~~~~~~~~~~

The ``landing`` layout is typically used for the home page
(``index.rst``).

.. code-block:: none

   :layout: landing

.. hint::

    Discover the appearance of the landing page by visiting the
    `Shibuya theme's homepage </>`_. Source code can be found on
    `GitHub (index.rst)`_.

.. _`GitHub (index.rst)`: https://github.com/lepture/shibuya/blob/main/docs/index.rst

This template offers a special container for buttons:

.. code-block:: none

    .. container:: buttons

        `Docs </install/>`_
        `GitHub <https://github.com/lepture/shibuya>`_

404 layout
~~~~~~~~~~

The ``404`` layout is designed for displaying "404 page not found".
Typically, you would use it in ``404.rst`` file:

.. code-block:: none
    :caption: docs/404.rst

    :layout: 404
    :orphan:

    404
    ===

    This page does not exist.

Shibuya theme has a special fix for 404 page with ``dirhtml`` builder.
