Sidebar Elements
================

Shibuya allows you to customize the elements that appear in the right
sidebar of your documentation pages.

Customize elements
------------------

By default, the right sidebar of documentation pages shows a table of
contents for the page. Additionally, there are several default templates
that you can include in the sidebar.

These templates are:

.. code-block:: none
   :caption: Default sidebar templates

   sidebars/localtoc.html
   sidebars/editlink.html
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

Built-in elements
-----------------
