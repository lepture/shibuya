:description: How to add links on navbar for your documentation website?

.. _nav-links:

Navbar links
============

.. rst-class:: lead

    Elevate navigation with custom navbar links.

----

The ``nav_links`` option allows you to add custom links to the navbar
of your documentation with Shibuya theme. Each link consists of a title
and a URL. Here is an example configuration code:

.. code-block:: python
    :caption: conf.py

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

Nested links
------------

The ``nav_links`` can also contain ``children`` links:

.. code-block:: python
    :caption: conf.py

    html_theme_options = {
        "nav_links": [
            {
                "title": "Examples",
                "url": "writing",
                "children": [
                    {
                        "title": "Admonitions",
                        "url": "writing/admonition",
                    },
                    {
                        "title": "Code Blocks",
                        "url": "writing/code",
                    },
                    {
                        "title": "Autodoc",
                        "url": "writing/api",
                    },
                ]
            },
        ]
    }

Link summary
------------

The children links has an extra (optional) ``summary`` field, which is a short description
of the link:

.. code-block:: python
    :caption: conf.py

    html_theme_options = {
        "nav_links": [
            {
                "title": "Examples",
                "url": "writing",
                "children": [
                    {
                        "title": "Admonitions",
                        "url": "writing/admonition",
                        "summary": "Bring the attention of readers",
                    },
                ]
            },
        ]
    }

External link
-------------

You can add an extra ``external`` field to display an external link icon:

.. code-block:: python
    :caption: conf.py

    html_theme_options = {
        "nav_links": [
            {
                "title": "Sponsor me",
                "url": "https://github.com/sponsors/lepture",
                "external": True,
            },
        ]
    }

Align nav links
---------------

The ``nav_links`` are aligned left by default, you can change the align to
``center`` or ``right`` with:

.. code-block:: python
    :caption: conf.py

    # align center
    html_theme_options = {
        "nav_links_align": "center",
    }

    # align right
    html_theme_options = {
        "nav_links_align": "right",
    }
