:description: Guide on customizing the appearance and functionality of your documentation website.

Configuration
=============

.. rst-class:: lead

    Customizing the appearance and functionality of your documentation website.

----

Shibuya provides various options for customizing the appearance and functionality of
your documentation website. You can customize your website using Sphinx basic settings
and Shibuya-specific options.

To customize your website using Sphinx basic settings, you can edit your Sphinx
configuration file (``conf.py``) and modify the values of Sphinx options like
``html_title``, ``html_logo``, and ``html_favicon``.


Theme options
-------------

Additionally, Shibuya provides its own set of options that you can use to customize
the appearance of your website. These options can be set using the ``html_theme_options``
option in your Sphinx configuration file.

.. grid:: 1 1 1 2
    :gutter: 2
    :padding: 0

    .. grid-item-card:: Logos
        :link: logos
        :link-type: doc

        Add a logo to promote your brand and make your website more recognizable.

    .. grid-item-card:: Colors
        :link: colors
        :link-type: doc

        Customize the color scheme to give your website a unique look and feel that
        reflects your brand or personal style.

    .. grid-item-card:: Navbar Links
        :link: navbar
        :link-type: doc

        Improve navigation by adding custom links to the navbar that direct users
        to important content on your website.

    .. grid-item-card:: Social Connections
        :link: social
        :link-type: doc

        Connect with visitors by including links to your GitHub, Twitter, Discord,
        and etc.


Templates
---------

Shibuya also provides several partial templates that you can customize to change the
appearance of specific sections of your website. These templates include the header,
footer, navbar, and sidebar.

.. grid:: 1
    :gutter: 2
    :padding: 0

    .. grid-item-card:: Web Fonts
        :link: fonts
        :link-type: doc

        Use custom web fonts to give your documentation website a unique typography
        that reflects your brand or personal style.

    .. grid-item-card:: Icons
        :link: icons
        :link-type: doc

        Add or change our default icon set to reflect your brand and enhance the
        visual appeal and user experience of your documentation website.

    .. grid-item-card:: Sidebar
        :link: sidebar
        :link-type: doc

        Customize the elements that appear in the right sidebar of your documentation
        pages; such as table of contents, advertisement, edit this page.


.. toctree::
    :hidden:

    logos
    css
    colors
    navbar
    layouts
    copypage
    announcement
    social
    fonts
    sidebar
    languages
    advertisement
    icons
    markdown
