Languages
=========

Shibuya supports multilingual documentation, allowing you to provide content
in multiple languages. You can configure the supported languages by using the
``html_context`` option in your Sphinx configuration file (``conf.py``).

Configuration
-------------

The ``html_context`` option allows you to define a list of languages, each
represented by a tuple containing the language name, URL pattern, and locale code.
Here's an example configuration:

.. code-block:: python
    :caption: conf.py

    html_context = {
        "languages": [
            ("English", "/en/%s/", "en"),
            ("中文", "/zh/%s/", "zh"),
        ]
    }

You can add more languages by including additional tuples in the ``languages`` list.

.. note::

    ``%s`` will be replaced by current page URL.

Examples
--------

A real example: https://jose.authlib.org/en/dev/

Country flag in language name:

.. code-block:: python
    :caption: conf.py

    html_context = {
        "languages": [
            ("🇺🇸 English", "/en/%s/", "en"),
            ("🇨🇳 中文", "/zh/%s/", "zh"),
        ]
    }


Using full URL pattern:

.. code-block:: python
    :caption: conf.py

    html_context = {
        "languages": [
            ("English", "https://en.example.com/%s/", "en"),
            ("中文", "https://zh.example.com/%s/", "zh"),
        ]
    }


Using URL pattern endswith ``.html``:

.. code-block:: python
    :caption: conf.py

    html_context = {
        "languages": [
            ("English", "/en/%s.html", "en"),
            ("中文", "/zh/%s.html", "zh"),
        ]
    }

If you prefer not to use a dynamic URL pattern and instead want to directly navigate
users to the homepage of the specific language, you can configure the language settings
as ``(Language Name, URL pattern)``:

.. code-block:: python
    :caption: conf.py

    html_context = {
        "languages": [
            ("English", "/en/"),
            ("中文", "/zh/"),
        ]
    }

This configuration simplifies the URL structure by removing the ``%s`` dynamic parameter
and eliminates the inclusion of the locale code and alternative ``hreflang`` links.
