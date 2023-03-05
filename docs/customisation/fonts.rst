:description: Adding a web font to match your branding.

Web Fonts
=========

Shibuya theme is using the "Inter" font served by Google fonts for headings.
If this font doesn't match your branding, you can change it through our
partial templates.

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


Disable web fonts
-----------------

Web fonts can sometime be a trouble, you may want to disable web fonts
totally. This is super easy, just keep the partial ``webfonts.html``
file to be empty.
