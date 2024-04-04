CSS Variables
=============

.. rst-class:: lead

    Customize your website with Shibuya provided CSS variables.

----

Shibuya supports a wide range of customizations to colors, fonts, and sizes
via CSS variables. By using CSS variables, you can easily modify the fonts,
and colors used in your documentation without needing to manually edit CSS files.

Variable name conventions
-------------------------

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

Default variables
-----------------

Below is a list of CSS variables that you can customize to change fonts and colors
used in your documentation:

==========================  ============================================================
Variable Name               Description
==========================  ============================================================
``--sy-f-heading``          Font family for headings
``--sy-f-text``             Font family for text
``--sy-f-mono``             Font family for code
``--sy-s-banner-height``    Height of the banner
``--sy-s-navbar-height``    Height of the navbar
``--sy-c-divider``          Divider color
``--sy-c-border``           Border color
``--sy-c-text``             Default text color
``--sy-c-light``            Light text color
``--sy-c-bold``             Bold text color
``--sy-c-heading``          Heading text color
``--sy-c-link``             Color for links
``--sy-c-link-hover``       Color for links when hovering
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
