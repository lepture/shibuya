:description: Shibuya is a modern, responsive, customizable theme for Sphinx.

Shibuya
=======

Make your documentation stand out with our modern, customizable theme.
Shibuya theme works well with Sphinx documentation generator.

Features
--------

- **Beautiful Design:**
  A visually stunning and modern design that makes your documentation
  look professional and appealing.
- **Responsive Layout:**
  The theme is designed to look great on all devices, from desktops to
  smartphones, without compromising on readability or functionality.
- **Three-Column Layout:**
  With a three-column layout, you can easily organize your content and make
  it more accessible to your users.
- **Light and Dark Mode:**
  Users can switch between light and dark modes according to their
  preference, making it easy to read in any lighting condition.
- **Customizable Colors:**
  You can easily customize the colors to match your brand or personal
  preferences, making it unique to your documentation.
- **SEO Optimized:**
  Built-in support for Twitter Card and Open Graph, ensuring your
  documentation looks great when shared on social media and is easily
  discoverable by search engines

If you're already familiar with Sphinx, start using our theme by
installing it with:

.. code-block:: shell

    pip install shibuya

Don't forget to update the ``html_theme`` option in your ``conf.py`` file
to ``shibuya`` to activate the new theme:

.. code-block:: python
   :caption: conf.py

   html_theme = "shibuya"

Next
----

Explore the following sections to discover more about our theme and its features.

.. grid:: 2

    .. grid-item-card:: Tutorial
        :link: /install/

        If you're new to Python and Sphinx, this is a great place to start.

    .. grid-item-card:: Customisation
        :link: /customisation/

        Tailor configurations to meet your specific requirements with customizable settings.

    .. grid-item-card:: References
        :link: /writing/

        Learn the syntax of reStructuredText and examine how it is formatted.

    .. grid-item-card:: Contributing
        :link: /contributing/

        Your contributions can make a meaningful impact and help drive the project forward!

.. toctree::
    :caption: Getting started
    :hidden:

    install
    customisation/index
    writing/index

.. toctree::
    :caption: Extensions
    :hidden:

    extensions/sphinx-copybutton
    extensions/sphinx-design
    extensions/sphinx-tabs
    extensions/jupyter-sphinx
    extensions/sphinx-togglebutton
    extensions/nbsphinx

.. toctree::
    :caption: Development
    :hidden:

    contributing/index
    alternatives
    stability
    changelog
