:layout: landing
:description: Shibuya is a modern, responsive, customizable theme for Sphinx.

Shibuya
=======

.. rst-class:: lead

    Beautiful responsive theme for Sphinx documentation generator. Great supports
    for Jupyter extensions.

.. container:: buttons

    :doc:`Docs <install>`
    `GitHub <https://github.com/lepture/shibuya>`_

.. raw:: html
    :file: ./_templates/accent-colors.html

.. grid:: 1 1 2 3
    :gutter: 2
    :padding: 0
    :class-row: surface

    .. grid-item-card:: :octicon:`star` Beautiful Design

        A visually stunning and modern design that makes your documentation
        look professional and appealing.

    .. grid-item-card:: :octicon:`zap` Responsive Layout

        Look great on all devices, from desktops to smartphones, without
        compromising on readability or functionality.

    .. grid-item-card:: :octicon:`moon` Light/Dark Mode

        Users can switch between light and dark modes according to their
        preference.

    .. grid-item-card:: :octicon:`paintbrush` Customizable Colors
        :link: customisation/colors
        :link-type: doc

        Customize the colors to match your brand or personal preferences
        with radix colors.

    .. grid-item-card:: :octicon:`beaker` Jupyter Integration
        :link: extensions/nbsphinx
        :link-type: doc

        Great CSS/UI for lots of Jupyter related extensions, enhance your
        AI documentation.

    .. grid-item-card:: :octicon:`browser` Multiple Layouts
        :link: customisation/layouts
        :link-type: doc

        Layouts of landing page, simple one page, and three-column
        documentation page.

-----

.. rubric:: Sponsored by
   :class: centered

.. sponsors:: Gold Sponsors
    :amount: 100
    :size: 2xl
    :rounded:
    :center:
    :show-name:

.. sponsors:: Silver Sponsors
    :amount: 50, 100
    :size: xl
    :rounded:
    :center:

.. sponsors:: Sponsors
    :amount: 25, 50
    :size: md
    :rounded:
    :center:

.. sponsors:: Backers
    :amount: 10, 25
    :size: sm
    :rounded:
    :center:

Showcases
---------

Here are some examples of documentation sites that use the Shibuya theme.

.. grid:: 1 1 2 3
    :gutter: 2
    :padding: 0

    .. grid-item-card:: |emscripten|
        :link: https://emscripten.org/
        :link-type: url

        Emscripten is a complete compiler toolchain to WebAssembly, using LLVM, with
        a special focus on speed, size, and the Web platform.

    .. grid-item-card:: :iconify:`devicon:sentry` Sentry
        :link: https://getsentry.github.io/sentry-python/
        :link-type: url

        Sentry is using Shibuya theme for their Python libraries API documentation.
        Including ``sentry-python``, ``arroyo``, ``sentry-kafka-schemas``, and etc.

    .. grid-item-card:: |jupyter| Jupyter AI
        :link: https://jupyter-ai.readthedocs.io/
        :link-type: url

        An open source extension that connects AI agents to computational notebooks
        in JupyterLab.

    .. grid-item-card:: |authlib|
        :link: https://docs.authlib.org
        :link-type: url

        The ultimate Python library in building OAuth and OpenID Connect servers.
        It is designed from low level specifications implementations to high level
        frameworks integrations, to meet the needs of everyone.

    .. grid-item-card:: |joserfc|
        :link: https://jose.authlib.org
        :link-type: url

        ``joserfc`` is a Python library derived from Authlib that provides a
        comprehensive implementation of several essential JSON Object Signing
        and Encryption (JOSE) standards.

    .. grid-item-card:: |sphinx-iconify|
        :link: https://sphinx-iconify.lepture.com
        :link-type: url

        ``sphinx-iconify`` provides the ``:iconify:`` role, which allows you
        to use the ``<iconify-icon>`` web component powered by Iconify.

.. |emscripten| image:: https://emscripten.org/_images/emscripten_logo_full.svg
   :height: 20
   :target: https://emscripten.org/

.. |jupyter| image:: https://jupyter-ai.readthedocs.io/en/v3/_static/jupyter_logo.png
   :height: 20
   :target: https://jupyter-ai.readthedocs.io/

.. |authlib_light| image:: https://docs.authlib.org/en/latest/_static/light-logo.svg
   :height: 20
   :alt: Authlib
   :target: https://docs.authlib.org
   :class: light-only

.. |authlib_dark| image:: https://docs.authlib.org/en/latest/_static/dark-logo.svg
   :height: 20
   :alt: Authlib
   :target: https://docs.authlib.org
   :class: dark-only

.. |authlib| replace:: |authlib_light| |authlib_dark|

.. |joserfc_light| image:: https://jose.authlib.org/en/_static/light-logo.svg
   :height: 20
   :alt: JOSE RFC
   :target: https://jose.authlib.org
   :class: light-only

.. |joserfc_dark| image:: https://jose.authlib.org/en/_static/dark-logo.svg
   :height: 20
   :alt: JOSE RFC
   :target: https://jose.authlib.org
   :class: dark-only

.. |joserfc| replace:: |joserfc_light| |joserfc_dark|

.. |sphinx-iconify| image:: https://sphinx-iconify.lepture.com/_static/logo.svg
   :height: 20
   :alt: Sphinx Iconify
   :target: https://sphinx-iconify.lepture.com


Contributors
------------

Here are contributors generated by :ref:`sphinx-contributors`.

.. container:: rounded-image

    .. contributors:: lepture/shibuya
        :avatars:

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
    extensions/sphinx-togglebutton
    extensions/jupyter-sphinx
    extensions/nbsphinx
    extensions/numpydoc
    extensions/mermaid
    extensions/docsearch
    extensions/sphinx-click
    extensions/click-extra
    extensions/sphinx-sqlalchemy
    extensions/sphinx-contributors
    extensions/sphinx-autoapi
    extensions/sphinx-iconify
    extensions/sphinx-datatables

.. toctree::
    :caption: Development
    :hidden:

    contributing/index
    alternatives
    stability
    changelog
