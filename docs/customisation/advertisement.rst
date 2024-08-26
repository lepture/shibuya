:description: Monetize your content without compromising on design or user experience.

Advertisement
=============

Shibuya theme integrates advertisements seamlessly into your documentation. The theme supports
popular ad networks, including Carbon Ads, Ethical Ads, and BuySellAds, allowing you to monetize
your content without compromising on design or user experience.

Carbon Ads
----------

Shibuya theme offers built-in support for `Carbon Ads <https://www.carbonads.net/>`_, a popular
ad network focused on displaying unobtrusive and highly relevant ads to your audience.

By defining the Carbon Ads credentials in ``conf.py``, Shibuya theme will display ads on the
right sidebar.

.. code-block:: python

    html_theme_options = {
        # ...
        "carbon_ads_code": "your-carbon-code",
        "carbon_ads_placement": "your-carbon-placement",
    }


Ethical Ads
-----------

When using Read the Docs to host your documentation, Ethical Ads will be injected automatically.
The default publisher for **Ethical Ads** is ``readthedocs``, you can also use your own publisher:

.. code-block:: python

    html_theme_options = {
        # ...
        "ethical_ads_publisher": "your-publisher-id",
    }

Shibuya theme will display the Ethical Ads on the right sidebar.

BuySellAds
----------

For those looking to connect with a broader range of advertisers, BuySellAds provides a
platform to display ads from a wide variety of advertisers. Instead of displaying it in
the right sidebar, Shibuya theme offers a way to place the Ad with a CSS selector.

Templates
~~~~~~~~~

BuySellAds is not enabled by default, so you'll need to include the template manually.
For example, you can add it to the ``partials/page-bottom.html`` template.

.. code-block:: jinja
    :caption: docs/_templates/partials/page-bottom.html

    {% include "extensions/buysellads.html" %}

Context
~~~~~~~

You'll also need to add the BuySellAds configuration to the ``html_context`` configuration.
Here is an example of this (Shibuya) documentation's ``conf.py``:

.. code-block:: python
    :caption: conf.py

    html_context = {
        "buysellads_code": "CE7DKK3M",
        "buysellads_placement": "shibuya",
        "buysellads_container_selector": ".yue > section > section",
    }
