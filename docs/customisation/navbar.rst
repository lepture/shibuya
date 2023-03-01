.. _nav-links:

Navbar Links
============

The ``nav_links`` option allows you to add custom links to the navbar
of your documentation with Shibuya theme. Each link consists of a title
and a URL. Here is an example configuration code:

.. code-block:: python

    html_theme_options = {
        "nav_links": [
            {
                "title": "Sponsor me",
                "url": "https://github.com/sponsors/lepture"
            },
        ]
    }

You can add more links to the nav_links list by including additional dictionaries.
However, we recommend that you keep the number of links to a minimum to avoid
cluttering your navbar.
