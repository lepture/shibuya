:description: How to customize colors for your documentation website?

Colors
======

.. rst-class:: lead

    Brand your website with your colors and captivate your audience.

----

Shibuya supports an easy way of customizations to colors via settings and CSS variables.

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

Your own color
--------------

If the predefined radix colors do not align with your branding, you can further customize
them using CSS variables like ``--accent-9``. Begin by selecting a color that closely
resembles your branding from the provided radix colors, such as "blue":

.. code-block:: python
    :caption: conf.py

    html_theme_options = {
      "accent_color": "blue",
    }

However, the provided "blue" may not perfectly match your branding blue. In such cases,
you may need to adjust its color. Typically, updating ``--accent-9`` is sufficient, as
it is the most commonly used accent color.

.. code-block:: css
    :caption: custom.css

    html[data-accent-color='blue'] {
      --accent-9: #3e7fcb;
    }

If desired, you can also customize other accent colors. Below are the CSS variables
utilized by the Shibuya theme:

.. code-block:: none

    --accent-a2: rgba(62, 127, 203, 0.15)
    --accent-a3: rgba(62, 127, 203, 0.27)
    --accent-a9: rgba(62, 127, 203, 0.81)
    --accent-a11: rgba(62, 127, 203, 0.92)

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
