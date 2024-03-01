:description: How to customize colors for your documentation website?

Colors
======

.. rst-class:: lead

    Brand your website with your colors and captivate your audience.

----

Shibuya supports a wide range of customizations to colors via CSS variables.
By using CSS variables, you can easily modify the colors used in your documentation
without needing to manually edit CSS files.

.. _accent-colors:

Accent colors
-------------

Shibuya provides pre-defined accent colors using `Radix Colors <https://www.radix-ui.com/colors>`_,
you can choose from the colors bellow:

.. code-block:: python
    :caption: conf.py

    html_theme_options = {
      "accent_color": "violet",
    }

.. raw:: html
    :file: ../_templates/accent-colors.html

.. hint:: Click each color block for previewing.

.. _global-dark-code:

Dark code
---------

By default, code blocks in light theme will be decorated with a light background.
But it is possible to use the **dark code mode** in the light mode. To turn all
code blocks into dark mode, you can update ``dark_code`` in ``html_theme_options``:

.. code-block:: python
    :class: dark-code

    html_theme_options = {
        "dark_code": True,
    }

There is also a :ref:`page level <page-dark-code>` configuration via ``:dark_code:``
meta tag. If you don't want to enable it for the whole site, you can use the meta tag.

Color mode
----------

Shibuya theme provides both light and dark modes, allowing users to switch between
them based on their preference. By default, the theme uses the "auto" mode, which
respects the operating system's settings. However, you have the option to force the
use of either light or dark mode by adjusting the settings in ``conf.py``:

.. code-block:: python

    html_theme_options = {
        "color_mode": "dark",
    }

Choices are: ``auto``, ``light``, ``dark``.

Variable name conventions
-------------------------

.. deprecated:: 2024.1.1

    The CSS variable ``--sy-rc-theme`` is removed.

Our naming conventions for Shibuya theme-related CSS variables are as follows:

- **Prefix**: All Shibuya-related CSS variable names start with ``--sy``.
  This prefix stands for Shibuya.

- **Middle**: After the prefix, the CSS variable name should include a dash followed
  by one or more of the following segments:

  - ``-c``: This segment indicates that the CSS variable is used for color.
  - ``-s``: This segment indicates that the CSS variable is used for size.
  - ``-f``: This segment indicates that the CSS variable is used for font.

- **Specificity**: After the segments, the CSS variable name should describe
  the specific use of the variable. For example, ``--sy-c-link`` refers to
  the color of a link in your documentation.

By following these naming conventions, you can easily identify and customize
the CSS variables for your Shibuya-themed documentation.

Color variables
---------------

Below is a list of CSS variables that you can customize to change the colors used in
your documentation:

==========================  ============================================================
Variable Name               Description
==========================  ============================================================
``--sy-s-banner-height``    Height of the banner
``--sy-s-navbar-height``    Height of the navbar
``--sy-s-offset-top``       Top offset
``--sy-c-divider``          Divider color
``--sy-c-border``           Border color
``--sy-c-link``             Color for links
``--sy-c-text``             Default text color
``--sy-c-light``            Light text color
``--sy-c-bold``             Bold text color
``--sy-c-heading``          Heading text color
``--sy-c-background``       Background color for elements
``--sy-c-foot-text``        Footer text color
``--sy-c-foot-background``  Footer background color
``--sy-c-foot-divider``     Footer divider color
==========================  ============================================================


Using a ``custom.css``
----------------------

You can add a ``custom.css`` file to your document repository, and use CSS variables
to define the colors you want to use.

Create a new file called ``custom.css`` in the ``_static`` directory of your
documentation project, and add it into ``conf.py`` with::

    html_css_files = [
      'custom.css',
    ]

This will tell Sphinx to include your custom.css file in the HTML output of your
documentation.

Once you have created the ``custom.css`` file and updated it in ``conf.py``, you can use
CSS variables to define your desired colors. Here is an example of how to set the footer
background color with ``--sy-c-foot-background`` variable:

.. code-block:: css
    :caption: custom.css

    html.light {
      --sy-c-foot-background: #f0f0f0;
    }

    html.dark {
      --sy-c-foot-background: black;
    }

The CSS variables defined in the ``html.light`` block will be activated in
the light mode, while the variables defined in the ``html.dark`` block will
be activated in the dark mode.

Additional CSS Variables
------------------------

In addition to the CSS variables listed in the previous section, you can also
customize other variables that are not specific to the Shibuya theme but are used
by Shibuya theme or any other extensions.

One such variable is ``--yue-c-text``, which sets the color of the text in the your
document content. You can customize this variable in ``custom.css``:

.. code-block:: css
    :caption: custom.css

    html.light {
      --yue-c-text: #000;
    }

    html.dark {
      --yue-c-text: #fff;
    }

.. hint::

    Discover all available CSS variables by using the inspect feature
    in your web browser.
