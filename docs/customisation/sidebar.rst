:description: Customize the elements that appear in the sidebar of your documentation pages.

Sidebar
=======

Shibuya allows you to customize the elements that appear in the sidebar of your
documentation pages.

.. _globaltoc:

Global TOC
----------

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

Customize elements
------------------

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
--------------

Add an "Edit This Page" link to your documentation website with just a few lines of
configuration. Simply add the following to your Sphinx ``conf.py`` file:

.. code-block:: python

    html_context = {
        "source_type": "github|gitlab|bitbucket",
        "source_user": "<username>",
        "source_repo": "<repository>",
    }

With this configuration, Shibuya will automatically include an "Edit This Page" link in
the right sidebar of your documentation pages, allowing visitors to easily edit the page
on GitHub, GitLab or Bitbucket.

.. note::
  If you are using Read the Docs to host your documentation, you don't need to add the
  ``html_context`` configuration since this feature is automatically enabled.

Source code statistics
----------------------

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

Carbon Ads
----------

Shibuya has built-in native support for `Carbon Ads <https://www.carbonads.net/>`_. By defining
the Carbon Ads credentials in ``conf.py``, Shibuya theme will display ads on the sidebar.

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
