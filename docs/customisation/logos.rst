Logos
=====


Same logo for light and dark mode
---------------------------------

Shibuya will use ``html_logo`` configuration for both light and dark mode.
Adding the ``html_logo`` variable in ``conf.py``.

.. code-block::

    html_logo = "_static/logo-light.svg"

Different logos for light and dark mode
---------------------------------------

.. code-block::

    html_static_path = ["_static"]
    html_theme_options = {
        "light_logo": "logo-light.svg",
        "dark_logo": "logo-dark.svg",
    }


Link logo to a different target
-------------------------------

.. code-block::

    html_theme_options = {
        "logo_target": "https://example.com",
    }
