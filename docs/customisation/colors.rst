:description: How to customize colors for your documentation website?

Colors
======

Shibuya supports a wide range of customizations to colors via CSS variables.
By using CSS variables, you can easily modify the colors used in your documentation
without needing to manually edit CSS files.

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

Variable Name Conventions
-------------------------

Our naming conventions for Shibuya theme-related CSS variables are as follows:

- **Prefix**: All Shibuya-related CSS variable names start with ``--sy``.
  This prefix stands for Shibuya.

- **Middle**: After the prefix, the CSS variable name should include a dash followed
  by one or more of the following segments:

  - ``-c``: This segment indicates that the CSS variable is used for color.
  - ``-rc``: This segment indicates that the CSS variable is used for RGB color.
  - ``-s``: This segment indicates that the CSS variable is used for size.
  - ``-f``: This segment indicates that the CSS variable is used for font.

- **Specificity**: After the segments, the CSS variable name should describe
  the specific use of the variable. For example, ``--sy-c-link`` refers to
  the color of a link in your documentation.

By following these naming conventions, you can easily identify and customize
the CSS variables for your Shibuya-themed documentation.

In conf.py, you have the ability to change the CSS variables for both
light and dark modes::

    html_theme_options = {
        "light_css_variables": {
          "--sy-rc-theme": "143, 118, 214",
        },
        "dark_css_variables": {
          "--sy-rc-theme": "130, 80, 223",
        },
    }

Available CSS Variables
-----------------------

Below is a list of CSS variables that you can customize to change the colors used in
your documentation:

========================  ============================================================
Variable Name              Description
========================  ============================================================
``--sy-f-sys``            System font stack
``--sy-f-cjk``            CJK font stack
``--sy-f-heading``        Font stack for headings
``--sy-f-text``           Font stack for body text
``--sy-f-mono``           Monospace font stack
``--sy-c-divider``        Divider color
``--sy-c-divider-weak``   Weak divider color
``--sy-c-border``         Border color
``--sy-s-banner-height``  Height of the banner
``--sy-s-navbar-height``  Height of the navbar
``--sy-s-offset-top``     Top offset
``--sy-c-link``           Color for links
``--sy-rc-theme``         Theme color in RGB
``--sy-rc-bg``            Background color in RGB
``--sy-rc-invert``        Inverted color in RGB
``--sy-rc-text``          Text color in RGB
``--sy-c-bg``             Background color for elements
``--sy-c-bg-weak``        Weak background color for elements
``--sy-c-text``           Default text color
``--sy-c-text-weak``      Weak text color
``--sy-c-heading``        Heading text color
``--sy-c-bold``           Bold text color
``--sy-c-foot-text``      Footer text color
``--sy-c-foot-bg``        Footer background color
``--sy-c-foot-divider``   Footer divider color
========================  ============================================================


Using a ``custom.css``
----------------------

Besides the ``light_css_variables`` and ``dark_css_variables`` in ``html_theme_options``,
you can also add a ``custom.css`` file to your document repository, and use CSS variables
to define the colors you want to use.

Create a new file called ``custom.css`` in the ``_static`` directory of your
documentation project, and add it into ``conf.py`` with::

    html_css_files = [
      'custom.css',
    ]

This will tell Sphinx to include your custom.css file in the HTML output of your
documentation.

Once you have created the ``custom.css`` file and updated it in ``conf.py``, you can use
CSS variables to define your desired colors. Here is an example of how to set the
``--sy-rc-theme`` variable to a red RGB color:

.. code-block:: css
    :caption: custom.css

    html.light {
      --sy-rc-theme: 245, 85, 153;
    }

    html.dark {
      --sy-rc-theme: 222, 114, 160;
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
