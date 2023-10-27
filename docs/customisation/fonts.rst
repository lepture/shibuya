:description: Customize the fonts to match your branding.

Fonts
=====

.. rst-class:: lead

    Adding a web font to match your branding.

----

Shibuya theme is using the "Inter" font served by Google fonts for headings
and content text. If this font doesn't match your branding, you can change
it through our partial templates.

Assuming your documentation is located in a ``docs`` folder, you can add the
partial template of ``webfonts.html`` like bellow:

.. code-block:: none
   :caption: Templates layout
   :emphasize-lines: 3-5

   docs/
     conf.py
     _templates/
       partials/
         webfonts.html
     index.rst

.. important::
    Don't forget to add the ``_templates`` folder into configuration:

    .. code-block:: python
       :caption: conf.py

       templates_path = ["_templates"]

Change web fonts
----------------

Shibuya allows you to customize the typography of your website by adding custom web fonts.
You can add web font related HTML in the webfonts.html partial template, which is included
in the header of all Shibuya documentation pages.

By default, Shibuya includes the ``Inter`` font family from Google Fonts. You can update
this font family to match your company or product's branding by modifying the HTML in the
``webfonts.html`` partial template. For example, you can replace ``Inter`` with the name
of a different font family that you prefer. You can also adjust the font weight and styles
according to your needs.

Here's an example of how the ``webfonts.html`` partial template might look with a custom
font family:

.. code-block:: html

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700&display=swap" rel="stylesheet">
    <style>
    :root {
      --sy-f-heading: 'Montserrat', var(--sy-f-sys), sans-serif;
    }
    </style>

In this example, we've replaced ``Inter`` with the ``Montserrat`` font family.

Disable web fonts
-----------------

Web fonts can sometime be a trouble, you may want to disable web fonts
totally. This is super easy, just keep the partial ``webfonts.html``
file to be empty.

Fonts CSS variables
-------------------

You can configure the font family with CSS variables, below is a list of CSS variables
that you can customize to change the fonts used in your documentation:

========================  ===========================
Variable Name              Description
========================  ===========================
``--sy-f-sys``            System font stack
``--sy-f-cjk``            CJK font stack
``--sy-f-heading``        Font stack for headings
``--sy-f-text``           Font stack for body text
``--sy-f-mono``           Monospace font stack
========================  ===========================
