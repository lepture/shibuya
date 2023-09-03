:description: Well designed code highlights on Shibuya Sphinx theme.

Code blocks
===========

``code-block`` directive
------------------------

The ``code-block`` directive is defined by Sphinx, the syntax looks like:

.. code-block:: none

    .. code-block:: language
       :linenos:
       :caption: text for caption
       :emphasize-lines: 2,10-15

       code content here, please keep a blank line above

`code-block`_ directive accepts several options:

.. _`code-block`: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block

- **caption**: to display a caption of the code block
- **linenos**: to show line numbers of the code block
- **lineno-start**: to set the first line number of the code block
- **emphasize-lines**: to emphasize particular lines of the code block
- **name**: to define a reference target
- **class**: to add extra class names for the code block
- **dedent**: to strip indentation for the code block

Here shows some of the use cases for ``code-block`` directive.

Highlight
~~~~~~~~~

The ``code-block`` directive accepts a program language after its directive name:

.. container:: demo

   .. code-block:: none
      :caption: Highlight with a language
      :class: demo-code

      .. code-block:: python

         import mistune

         def render_markdown(text: str) -> str:
             """A simple function to render text in markdown format."""
             return mistune.html(text)

         render_markdown("Hello **Shibuya**.")

   .. code-block:: python
      :class: demo-result

      import mistune

      def render_markdown(text: str) -> str:
          """A simple function to render text in markdown format."""
          return mistune.html(text)

      render_markdown("Hello **Shibuya**.")

Captions
~~~~~~~~

It is also possible to add a ``caption`` option in ``code-block``. For example,
here displays the code of ``markdown.py``::

    .. code-block:: python
        :caption: markdown.py

And the final result on Shibuya theme:

.. code-block:: python
    :caption: markdown.py

    import mistune

    def render_markdown(text: str) -> str:
        """A simple function to render text in markdown format."""
        return mistune.html(text)

    render_markdown("Hello **Shibuya**.")


Line numbers
~~~~~~~~~~~~

Adding a ``linenos`` option to show the code block's line numbers::

    .. code-block:: python
        :linenos:

This is how it looks with Shibuya theme:

.. code-block:: python
    :linenos:

    import mistune

    class Shibuya:
        def render_markdown(self, text: str) -> str:
            """A simple function to render text in markdown format."""
            return mistune.html(text)

If both ``caption`` and ``linenos`` options are added:

.. code-block:: python
    :caption: markdown.py
    :linenos:

    import mistune

    class Shibuya:
        def render_markdown(self, text: str) -> str:
            """A simple function to render text in markdown format."""
            return mistune.html(text)

Emphasize lines
~~~~~~~~~~~~~~~

The ``code-block`` directive offers an ``emphasize-lines`` option to highlight
the chosen lines::

    .. code-block:: python
        :emphasize-lines: 1,5-6,24-29

.. code-block:: python
    :caption: markdown.py
    :linenos:
    :emphasize-lines: 3-5

    import mistune

    def render_markdown(text: str) -> str:
        """A simple function to render text in markdown format."""
        return mistune.html(text)

    render_markdown("Hello **Shibuya**.")

``code`` directive
------------------

The code_ is a built-in directive in reStructuredText. When using
rst as the markup format in Sphinx, ``code`` directive can also be
used.

.. _code: https://docutils.sourceforge.io/docs/ref/rst/directives.html#code

.. code-block:: none

   .. code:: python

      import mistune

      mistune.html("Hello **Shibuya**")

.. code:: python

    import mistune

    mistune.html("Hello **Shibuya**")


``parsed-literal`` directive
----------------------------

The `parsed-literal`_ is a built-in directive in reStructuredText. It constructs
a literal block where the text is parsed for inline markup.

For example:

.. code-block:: ReST

  .. parsed-literal::

     $ pip install shibuya==\ |version|


.. _`parsed-literal`: https://docutils.sourceforge.io/docs/ref/rst/directives.html#parsed-literal

Above markup will turn into:

.. parsed-literal::

    $ pip install shibuya==\ |version|

.. _block-dark-code:

Dark code
---------

Dark code block can be defined with a class ``dark-code``::

  .. code-block:: python
     :class: dark-code

     html_theme_options = {
         "dark_code": True
     }

.. code-block:: python
    :class: dark-code

    html_theme_options = {
        "dark_code": True
    }

It is also possible to enable **dark code mode** for :ref:`the whole page <page-dark-code>`.
You can even enable **dark code mode** for :ref:`the whole site <global-dark-code>`.

.. important:: This ``:class:`` option does not work well together with caption.
