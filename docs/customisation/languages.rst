Languages
=========

Shibuya sphinx theme supports multiple languages.

Configuration
-------------

Name, URL Pattern, Locale Code.

.. code-block:: python
    :caption: conf.py

    html_context = {
        "languages": [
            ("English", "/en/%s/", "en"),
            ("中文", "/zh/%s/", "zh"),
        ]
    }
