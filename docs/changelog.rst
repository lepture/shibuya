:description: Here lists the releases notes of Shibuya Sphinx theme.

Changelog
=========

Shibuya uses date based release segments. For pre-releases, it follows :pep:`440`.

2025.9.24
---------

- **New**: add a ``shibuya.sponsor`` extension.
- **Fix**: remove useless pygments css files.
- **Fix**: hide username when repository name is too long.
- **Fix**: update head backrop blur style.
- **Fix**: update base template's block ``theme_scripts`` to ``themescripts``.

2025.9.23
---------

- **Fix**: fix ``pageurl`` context when it is ``None``, via :issue:`90`.

2025.9.22
---------

- **Refactor**: Update python code structure.
- **Fix**: Support for Pygments extension, via :issue:`89`.
- **Fix**: Build pygments styles dynamically.
- **Fix**: Fix text overflow for math block and pre.
- **Fix**: Fix style for buysellads.

2025.8.16
---------

- **Update**: Use tailwindcss v4.
- **Fix**: Improve copybutton's position in code blocks.
- **Fix**: Improve style for sphinx-contributors.
- **Fix**: Fix JS errors when scrolling on landing page.

2025.7.24
---------

- **Fix**: Improve accessibility for nav links, you can now using keyboard to open sub nav links.
- **Fix**: Update sphinx-design's style for iconify-icon.

2025.7.14
---------

- **New**: Add ``data-accent-color`` style for :ref:`sphinx-iconify`.
- **New**: Add ``outline`` variant style for sphinx-design's tab-set.

2025.4.25
---------

- **New**: Add ``resource`` parameter to ``nav_links``, via :issue:`83`.

2025.3.24
---------

- **Fix**: Remove ``margin-top`` for ``dl.field-list``, via :issue:`81`.

2025.2.28
---------

- **Fix**: Fix style for ``sphinx-contributors``.

2025.2.20
---------

- **Breaking**: Set default ``source_version`` config from ``master`` to ``main``.
- **Fix**: Skip prompt when selecting code, via :pull:`80`.
- **Fix**: Add bottom margin for admonition content, via :issue:`77`.
- **Fix**: Add bottom margin for images.

2025.2.14
---------

- **Fix**: Use correct icon for gitlab in foot, via :issue:`78`.

2025.2.11
---------

- **Fix**: Improve fonts for CJK, via :issue:`76`.

2025.1.29
---------

- **New**: Add ``toctree_maxdepth`` theme option, via :pull:`74`.

2024.12.21
----------

- **Fix**: Rename css variables from ``{name}t-contrast`` to ``{name}-contrast``, via :pull:`71`.

2024.12.20
----------

- **New**: Added integration with :ref:`sphinx-contributors`.

2024.12.15
----------

- **Fix**: Add ``min-height`` for ``main`` element, via :issue:`68`.
- **Fix**: Set admonition block to be flex box, via :issue:`69`.
- **Fix**: Update icons for version related directives.

2024.12.13
----------

- **New**: Add style for ``versionremoved`` directive.

2024.10.15
----------

- **Fix**: Update integration with Read the Docs Addons.

2024.10.14
----------

- **Fix**: Set ``max-height`` for the sidebar scroller.
- **Fix**: Update background color for :ref:`jupyter-sphinx` code blocks, via :issue:`66`.

2024.8.30
---------

- **Fix**: Update translation files.
- **Fix**: Add ``min-height`` for RTD other versions.

2024.8.27
---------

- **Fix**: Update style for admonition, use block instead of flex.
- **Fix**: Use ``<iconify-icon>`` web component for social icons.

2024.8.26
---------

- **Fix**: Fix sphinx-design grid css conflict with :ref:`sphinx-togglebutton`.
- **New**: Add :ref:`buysellads` extension.

2024.8.21
---------

- **Fix**: Fix sphinx-design grid css conflict with admonition.

2024.7.13
---------

- **New**: Add ``slack_url`` theme option.
- **New**: Add ``partials/nav-socials.html`` template.
- **Fix**: Word break for right sidebar's repository stats component.

2024.6.23
---------

- **Fix**: Improve style for sphinx togglebutton.
- **Fix**: Remove prefix in local TOC for API references.
- **Fix**: Fix table style, avoid extra padding for tables.

2024.6.1
--------

- **New**: Allow customize social network with partial template.
- **New**: Add ``nav_links_align`` theme option.
- **Fix**: Improve sidebar style for mobile view.
- **Fix**: Use localStorage for theme mode state.
- **Fix**: Hide rtd injected widget on landing page.
- **Fix**: Lazy load logo to improve page speed.
- **Fix**: Improve admonition style.

2024.5.15
---------

- **Fix**: Update style for floatting image with admonition.

2024.5.14
---------

- **New**: Added integration with :ref:`sphinx-click`.
- **New**: Added style for menuselection.
- **New**: Added style for sidebar.
- **New**: Added style for align images.
- **Fix**: Updated CSS for h5, h6, and ``.rubric``.

2024.5.10
---------

- **New**: Added ``linkedin_url`` theme option
- **New**: Make theme switch a component
- **Fix**: Cleanup ``html_context`` to prevent sphinx 7.3 warnings


2024.4.27
---------

- **New**: Added integration with :ref:`sphinx-sqlalchemy`.
- **Fix**: Improve accessibility with ``aria-label``.
- **Fix**: Improve style for nav links and docsearch.
- **Breaking**: Fix typo of ``Lucide`` icons.

2024.4.15
---------

- **Breaking**: Lucide and Simple Icons are splitted
- **New**: Added ``404`` layout template
- **New**: Added ``readthedocs_url`` theme option
- **Fix**: Improve style for API autosummary tables

2024.4.8
--------

- **New**: Added integration with :ref:`docsearch`
- **New**: Added ``reddit_url`` theme option
- **New**: Added ``discussion_url`` theme option
- **Fix**: Improve style for tables
- **Fix**: Added ``external`` key for nav links

2024.4.4
--------

- **New**: Auto highlight local TOC links
- **New**: Added back to top button
- **Fix**: Improve style for code blocks in tabs
- **Fix**: Improve accent color definition
- **Fix**: Improve style for copybutton

2024.3.1
--------

- **New**: Added ``page_layout`` theme option
- **New**: Added ``color_mode`` theme option
- **New**: Added compact page layout
- **Fix**: Improve style for ``nbsphinx`` tables

2024.2.21
---------

- **New**: Added ``source_version`` html context
- **New**: Added ``source_docs_path`` html context
- **Fix**: Improve code block caption background color

2024.1.17
---------

- **New**: Added "ghost" style tables.
- **New**: Improve SEO with BreadcrumbList schema.
- **Fix**: Change ``<img>`` style to ``inline``.

2024.1.2
--------

- **Fix**: Add opengraph information for landing and simple layouts.
- **Fix**: Move ``.buttons`` container into global css.

2024.1.1
--------

- **Breaking**: ``--sy-rc-theme`` CSS variable has been removed in favor of :ref:`accent-colors`.
- **Breaking**: Several CSS variable names are changed.
- **Breaking**: ``light_css_variables`` and ``dark_css_variables`` theme option has been removed.
- **New**: Added many pre-defined :ref:`accent-colors`.
- **New**: Added style for ``sphinx-gallery`` and ``xarray``, via :issue:`20`.
- **New**: Added **simple** and **landing** layout templates.
- **New**: Added two image containers.
- **Fix**: Improve style for ``sphinx-design``, ``jupyter-sphinx``, and etc.
- **Fix**: Improve style for search page.

2023.10.26
----------

- Add ``gitlab_url`` and ``bitbucket_url``
- Update Twitter icon to X icon
- Integrate with numpydoc extension
- Improve CSS for ``sphinx.ext.autosummary`` extension
- Add ``light-only`` and ``dark-only`` class

2023.10.5
---------

- Fix deprecated links in relations.html and searchbox.html

2023.9.3
--------

- Improve sidebar CSS for compatibility
- Add an alias template of ``localtoc.html``
- Add deprecated warning templates of ``relations.html`` and ``searchbox.html``
- Improve CSS for ``nbsphinx`` extension
- New feature for global TOC configuration
- Improve CSS for global TOC

2023.7.28
---------

- Remove current ``hreflang`` link
- Fix nested TOC links, via :issue:`7`
- Use theme color for code blocks, via :issue:`5`
- Remove version parameter on assets URLs

2023.7.16
---------

- Fix multiple languages links for index pages
- Add ``hreflang`` links for SEO
- Add locale data of theme templates

2023.7.15
---------

- Change multiple languages configuration

2023.7.14
---------

- Add YouTube link
- Improve style for versions and languages
- Improve breadcrumbs style
- Add expand and collapse global TOC

2023.7.11
---------

- Fix style for genindex
- Add breadcrumbs for small screen
- Move TOC controllers to breadcrumbs block
- Move RTD versions to left sidebar
- Add multiple languages switcher

2023.6.30
---------

- Fix normalize toc with ``xml.etree``
- Fix local toc style
- Fix style of main part for large screen

2023.6.27
---------

- Fix style of copybutton for dark code mode
- Fix style for modindex page

2023.6.25
---------

- Apply ``dark_css_variables`` in templates
- Fix code block style in dark code mode for sphinx design
- Fix colors for API docs in dark code mode
- Fix stderr background for ``nbsphinx``

2023.6.21
---------

- Add support for ``sphinx-togglebutton`` extension
- Add support for ``nbsphinx`` extension
- Rename template ``partials/sidebar-links`` to ``partials/globaltoc-above``
- Add template ``extensions/buysellads``

2023.6.18
---------

- Fix edit this page link
- Fix nav links style
- Update style for :ref:`jupyter-sphinx`

2023.6.8
--------

- Add external-link icon for external nav links
- Add highlight background color for search results
- Fix search results page nav links for mobile devices
- Add native built-in carbon ads

2023.6.7
--------

- Fix ``scroll-margin-top`` for sections
- Change "edit this page" link
- Add an option to use your own Ethical Ads publisher ID
- Update navbar links style
- Add navbar children links

2023.3.19
---------

- Enable ``repo-stats`` sidebar by default
- Improve colors for dark mode

2023.3.11
---------

- Auto resize announcement banner
- Fix context for readthedocs

2023.3.7
--------

- Add "edit this page" in sidebar
- Add GitHub / Gitlab repository stats
- Fix versions on css files


2023.3.5
--------

- Add dark code mode
- Improve style for print media
- Improve style for sphinx-design


2023.3.2
--------

- Improve style for quotes
- Add github link on nav bar


2023.3.1
--------

- Fix margins for "kbd"
- Add style for sphinx-tabs
- Improve style for code blocks


2023.2.25a2
-----------

- Fix templates when ``pageurl`` is None
- Improve opengraph with more theme options
- Tweak style, fix for a11y
- Move theme switch to site head
- Add logos and colors

2023.2.23a1
-----------

Initial release.
