:description: Customize the elements that appear in the sidebar of your documentation pages.

Sidebar
=======

Shibuya allows you to customize the elements that appear in the sidebar of your
documentation pages.

Left sidebar
------------

The left sidebar contains the global table of contents tree of the documentation. It is
collapsed by default. Developers can customize the collapse behavior via ``conf.py``:

.. code-block:: python
    :caption: conf.py

    html_theme_options = {
        "globaltoc_expand_depth": 1,
    }

The above configuration will only expand the first level of the global table of contents.

Shibuya sphinx theme also provides other options to control the toctree_ function:

- toctree_collapse: equals to ``collapse``, ``False`` by default.
- toctree_titles_only: equals to ``titles_only``, ``True`` by default
- toctree_includehidden: equals to ``includehidden``, ``True`` by default

.. _toctree: https://www.sphinx-doc.org/en/master/development/templating.html#toctree

Discussion URL
~~~~~~~~~~~~~~

By default, the Shibuya theme includes a discussion link above the global TOC.
If you specify a ``discussion_url`` in ``conf.py``, the discussion link will be
added automatically. You can view an example of this in the documentation and
observe its appearance.

.. code-block:: python
    :caption: conf.py

    html_theme_options = {
        "discussion_url": "https://github.com/lepture/shibuya/discussions",
    }

Above template
~~~~~~~~~~~~~~

However, if you wish to include additional links above the global TOC, you can
create a ``partials/globaltoc-above.html`` template in your documentation templates
folder.

.. code-block:: html
    :caption: docs/_templates/partials/globaltoc-above.html

    <div class="sidebar-links">
      <ul>
        <li>
          <a class="icon-link" href="https://github.com/lepture/shibuya/discussions">
            <span class="icon">
              <svg viewBox="0 0 24 24" fill="none">
                <path fill="var(--accent-9)" fill-rule="evenodd" clip-rule="evenodd" d="M11 5a6 6 0 0 0-4.687 9.746c.215.27.315.62.231.954l-.514 2.058a1 1 0 0 0 1.485 1.1l2.848-1.71c.174-.104.374-.15.576-.148H13a6 6 0 0 0 0-12h-2Z"/>
                <circle fill="white" cx="12" cy="11" r="1"/>
                <circle fill="white" cx="9" cy="11" r="1"/>
                <circle fill="white" cx="15" cy="11" r="1"/>
              </svg>
            </span>
            <span class="text">Discussion</span>
          </a>
        </li>
      </ul>
    </div>

Right sidebar
-------------

By default, the right sidebar of documentation pages shows a table of
contents for the page. Additionally, there are several default templates
that you can include in the sidebar.

These templates are:

.. code-block:: none
   :caption: Default sidebar templates

   sidebars/localtoc.html
   sidebars/repo-stats.html
   sidebars/edit-this-page.html
   sidebars/carbon-ads.html
   sidebars/ethical-ads.html

You can include additional templates in the sidebar by adding them to the
``html_sidebars`` option. Here is an example configuration code that includes
a custom template:


.. code-block::

    html_sidebars = {
      "**": [
        "sidebars/localtoc.html",
        "your-own-template.html",
      ]
    }

In the above example, the ``sidebars/localtoc.html`` template is included by
default and shows the table of contents. The ``your-own-template.html`` file is
a custom template that you can create to show any additional elements you want
in the sidebar.

You can also remove the default templates if you do not want them to appear in
the sidebar. To remove a template from the sidebar, simply remove its entry from
the ``html_sidebars`` list.

.. hint::

   You can add ``your-own-template.html`` in your folder ``docs/_templates``, and
   add the ``_templates`` folder in ``conf.py`` to:

   .. code-block:: python

        templates_path = ["_templates"]


Edit this page
~~~~~~~~~~~~~~

Add an "Edit This Page" link to your documentation website with just a few lines of
configuration. Simply add the following to your Sphinx ``conf.py`` file:

.. code-block:: python

    html_context = {
        "source_type": "github|gitlab|bitbucket",
        "source_user": "<username>",
        "source_repo": "<repository>",
        "source_version": "master",  # Optional
        "source_docs_path": "/docs/",  # Optional
    }

With this configuration, Shibuya will automatically include an "Edit This Page" link in
the right sidebar of your documentation pages, allowing visitors to easily edit the page
on GitHub, GitLab or Bitbucket.

.. note::
  If you are using Read the Docs to host your documentation, you don't need to add the
  ``html_context`` configuration since this feature is automatically enabled.

Source code statistics
~~~~~~~~~~~~~~~~~~~~~~

Display statistics about your source code repository on your documentation website with
just a few lines of configuration. Simply add the following to your Sphinx ``conf.py`` file:

.. code-block:: python

    html_context = {
        "source_type": "github|gitlab",
        "source_user": "<username>",
        "source_repo": "<repository>",
    }

.. note::
  If you are using Read the Docs to host your documentation, you don't need to add the
  ``html_context`` configuration since this feature is automatically enabled.

With this configuration, Shibuya will automatically display your GitHub/Gitlab repository
statistics in the right sidebar of your documentation pages, including the number of
stars, and forks.
