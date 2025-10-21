:description: Customize webpage with meta configuration.
:dark_code: true

.. _meta:

Meta tags
=========

.. rst-class:: lead

    You can customize the webpage using the following meta tags.

-----

Layout
------

Shibuya theme offers multiple page layouts. The default layout
features a three-column design:

- the left sidebar contains the global table of contents,
- the right sidebar holds the local table of contents,
- and the center displays the main page content.

Page layout can be configured with:

.. code-block:: none

   :layout: landing

Description
-----------


A description meta tag provides a summary of the current page
content, enhancing both SEO and social sharing.

.. code-block:: rst

   :description: A description about this page.

   Page title
   ==========

The provided code will generate the following HTML:

.. code-block:: html

    <meta name="description" content="A description about this page."/>
    <meta property="og:description" content="A description about this page."/>

.. _page-cover:

Cover
-----

Utilize the ``:cover:`` tag to embed a sizable image,
creating a visually impactful image card on X (Twitter).

.. code-block:: rst

   :cover: https://example.com/a-big-cover-image.png

   Page title
   ==========

The provided code will generate the following HTML:

.. code-block:: html

    <meta name="twitter:card" content="summary_large_image"/>
    <meta property="og:image" content="https://example.com/a-big-cover-image.png"/>

.. _page-image:

Image
-----

In addition to ``:cover:``, if you prefer to showcase a smaller
image rather than a large cover, you can employ the ``:image:``
meta tag.

.. code-block:: rst

   :image: https://example.com/a-squared-image.png

   Page title
   ==========

The provided code will generate the following HTML:

.. code-block:: html

    <meta name="twitter:card" content="summary"/>
    <meta property="og:image" content="https://example.com/a-squared-image.png"/>

.. hint::

    You can configure a global :ref:`og_image_url` with ``og_image_url``.

.. _page-dark-code:

Dark code
---------

Apply ``:dark_code: true`` meta tag to enable dark mode
rendering for code blocks on the current page.

.. code-block:: rst

   :dark_code: true

   Page title
   ==========

Indeed, as evident, the code blocks on this page are displayed
in a dark theme.

Breadcrumbs
-----------

Adding ``:hide_breadcrumbs: true`` meta tag to hide the breadcrumbs
component on the current page.

.. code-block:: rst

   :hide_breadcrumbs: true

   Page title
   ==========

Max width
---------

You can customize the maximum content width for the ``landing`` and ``simple``
layouts using the ``:content_max_width:`` meta configuration.

.. code-block:: rst

   :layout: landing
   :content_max_width: 960px
