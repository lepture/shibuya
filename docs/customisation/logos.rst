:description: Add a logo to promote your brand and make your website more recognizable.

Logos
=====

.. rst-class:: lead

    Add a logo to promote your brand and make your website more recognizable.

----

Your logo is an important element of your product's branding and identity.
Shibuya theme supports both light and dark modes, so it's important to make
sure that your logo works well in both modes.

Same logo
---------

It's great if your logo looks good in both light and dark modes. To include
your logo in your Sphinx documentation, you can add its URL to the
``html_logo`` variable in your ``conf.py`` file.

.. code-block::

    html_logo = "_static/logo.svg"

Different logos
---------------

A logo with a light-colored text on a dark background may look great in dark mode,
but it may be difficult to read or even invisible in light mode. Similarly, a logo
with a dark-colored text on a light background may look good in light mode, but it
may be hard to distinguish in dark mode.

To address this issue, you can create two different versions of your logo, each
optimized for the different modes.

.. code-block::

    html_static_path = ["_static"]
    html_theme_options = {
        "light_logo": "logo-light.svg",
        "dark_logo": "logo-dark.svg",
    }


Link to the logo
----------------

Shibuya theme will automatically add a link to your logo. By default, the link
points to the root document, but you can change it using the ``logo_target``
option in ``conf.py`` to link to a different URL. This allows you to customize
the behavior of your logo link and direct users to the destination of your choice.

.. code-block::

    html_theme_options = {
        "logo_target": "https://example.com",
    }

.. tip::

    Customize your logo link to your product's home page. Add a **Docs** link
    to :ref:`nav_links <nav-links>` to provide a link to your documentation
    and improve navigation.

Open Graph Image
----------------

Shibuya theme also supports adding an image URL for Open Graph and Twitter cards.
To add this, you can use the ``og_image_url`` option in your ``conf.py`` file.
This allows you to customize the image that appears when your documentation is
shared on social media platforms.

.. code-block::

    html_theme_options = {
        "og_image_url": "https://example.com/icon.png",
    }

.. hint::

  It's recommended to use a square image for best results, as rectangular images
  may be cropped when displayed on social media platforms.
