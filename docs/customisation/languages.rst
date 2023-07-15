Languages
=========

Shibuya sphinx theme supports multiple languages.

Configuration
-------------

.. code-block:: python
    :caption: conf.py

    html_context = {
        "languages": [
            ("English", "/en/%s/"),
            ("中文", "/zh/%s/"),
        ]
    }
