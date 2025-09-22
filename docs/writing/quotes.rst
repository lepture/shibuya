Block quotes
============

Indented quotes
---------------

A text block that is indented relative to the preceding text,
without preceding markup indicating it to be a literal block
or other content, is a block quote.

.. code-block:: none

   This is an ordinary paragraph, introducing a block quote.

       "It is my business to know things.  That is my trade."

       -- Sherlock Holmes

A block quote may end with an attribution: a text block beginning with
``--``, ``---``, or a true em-dash, flush left within the block quote.
If the attribution consists of multiple lines, the left edges of the
second and subsequent lines must align.

.. hint::
   Use empty comments to separate block quotes. For example:

   .. code-block:: none

      - list item

      ..

          quote content

   Without empty comments of ``..``, the **quote content** will be treated
   as the content of the list item.

No attribution
~~~~~~~~~~~~~~

.. code-block:: none

   This is an ordinary paragraph, introducing a block quote.

       "It is my business to know things.  That is my trade."

This is an ordinary paragraph, introducing a block quote.

    "It is my business to know things.  That is my trade."

With attribution
~~~~~~~~~~~~~~~~

.. code-block:: none

   This is an ordinary paragraph, introducing a block quote.

       "It is my business to know things.  That is my trade."

       -- Sherlock Holmes

This is an ordinary paragraph, introducing a block quote.

    "It is my business to know things.  That is my trade."

    -- Sherlock Holmes


Multiple attributions
~~~~~~~~~~~~~~~~~~~~~

It is also possible to add multiple attributions to the quote:

.. code-block:: none

   This is an ordinary paragraph, introducing a block quote.

       "This is a quote message."

       -- Author 1,
          Author 2

..

    "This is a quote message."

    -- Author 1,
       Author 2

Multiple quotes
~~~~~~~~~~~~~~~

Empty comments may also be used to separate block quotes:

.. code-block:: none

       Block quote.

   ..

       Another block quote.

..

    Block quote.

..

    Another block quote.

Epigraph
--------

An epigraph_ is an apposite (suitable, apt, or pertinent) short
inscription, often a quotation or poem, at the beginning of a
document or section.

.. _epigraph: https://docutils.sourceforge.io/docs/ref/rst/directives.html#epigraph

No attribution
~~~~~~~~~~~~~~

.. code-block::

  .. epigraph::

     | Why, you may take the most gallant sailor,
     | the most intrepid airman or the most audacious soldier,
     | put them at a table together – what do you get?
     | The sum of their fears.

.. epigraph::

   | Why, you may take the most gallant sailor,
   | the most intrepid airman or the most audacious soldier,
   | put them at a table together – what do you get?
   | The sum of their fears.

With attribution
~~~~~~~~~~~~~~~~

.. code-block::

  .. epigraph::

     | Why, you may take the most gallant sailor,
     | the most intrepid airman or the most audacious soldier,
     | put them at a table together – what do you get?
     | The sum of their fears.

     -- Winston Churchill

.. epigraph::

   | Why, you may take the most gallant sailor,
   | the most intrepid airman or the most audacious soldier,
   | put them at a table together – what do you get?
   | The sum of their fears.

   -- Winston Churchill

Highlights
----------

Highlights_ summarize the main points of a document or section,
often consisting of a list.

.. _Highlights: https://docutils.sourceforge.io/docs/ref/rst/directives.html#highlights

.. code-block:: rst

  .. highlights::

     - No matter where you go, there you are. -- *Buckaroo Banzai*.
     - I have no special talent. I am only passionately curious. -- *Albert Einstein*.

.. highlights::

   - No matter where you go, there you are. -- *Buckaroo Banzai*.
   - I have no special talent. I am only passionately curious. -- *Albert Einstein*.

Pull-Quote
----------

A pull-quote_ is a small selection of text “pulled out and quoted”,
typically in a larger typeface. Pull-quotes are used to attract attention,
especially in long articles.

.. _pull-quote: https://docutils.sourceforge.io/docs/ref/rst/directives.html#pull-quote

No attribution
~~~~~~~~~~~~~~

.. code-block:: rst

  .. pull-quote::

     No matter where you go, there you are.

.. pull-quote::

   No matter where you go, there you are.

With attribution
~~~~~~~~~~~~~~~~

.. code-block:: rst

  .. pull-quote::

     No matter where you go, there you are.

     -- Buckaroo Banzai

.. pull-quote::

   No matter where you go, there you are.

   -- Buckaroo Banzai
