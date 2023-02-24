Logos
=====


Same logo
---------

Shibuya will use ``html_logo`` configuration for both light and dark mode.
Adding the ``html_logo`` variable in ``conf.py``.

.. code-block::

    html_logo = "_static/logo-light.svg"

Different logos
---------------

.. code-block::

    html_static_path = ["_static"]
    html_theme_options = {
        "light_logo": "logo-light.svg",
        "dark_logo": "logo-dark.svg",
    }


Link to the logo
----------------

.. code-block::

    html_theme_options = {
        "logo_target": "https://example.com",
    }

Open Graph Image
----------------

.. code-block::

    html_theme_options = {
        "og_image_url": "https://example.com/icon.png",
    }
