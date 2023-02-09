Code Blocks
===========

Highlight
---------

The ``code-block`` directive accepts a program language after its directive name::

    .. code-block:: language

Here is an example of how Python code looks like in Shibuya theme:

.. code-block:: python

    import mistune

    def render_markdown(text: str) -> str:
        """A simple function to render text in markdown format."""
        return mistune.html(text)

    render_markdown("Hello **world**.")


Captions
--------

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

    render_markdown("Hello **world**.")


Line Numbers
------------

Adding a ``linenos`` option to show the code block's line numbers::

    .. code-block:: python
        :linenos:

This is how it looks with Shibuya theme:

.. code-block:: python
    :linenos:

    import mistune

    def render_markdown(text: str) -> str:
        """A simple function to render text in markdown format."""
        return mistune.html(text)

    render_markdown("Hello **world**.")

If both ``caption`` and ``linenos`` options are added:

.. code-block:: python
    :caption: markdown.py
    :linenos:

    import mistune

    def render_markdown(text: str) -> str:
        """A simple function to render text in markdown format."""
        return mistune.html(text)

    render_markdown("Hello **world**.")
