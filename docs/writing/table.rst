Tables
======

There are many ways to create a table. Here are some of them.

Table fences
------------

Simple Table
~~~~~~~~~~~~

Very simple tables can be created with the syntax bellow:

.. code-block:: ReST

    =====  =====  ======
      A      B    A or B
    =====  =====  ======
    False  False  False
    True   False  True
    False  True   True
    True   True   True
    =====  =====  ======

=====  =====  ======
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

And it can be a little complex with multiple headers:

.. code-block:: ReST

    =====  =====  ======
       Inputs     Output
    ------------  ------
      A      B    A or B
    =====  =====  ======
    False  False  False
    True   False  True
    False  True   True
    True   True   True
    =====  =====  ======

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======


Grid Table
~~~~~~~~~~

The `grid table <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#grid-tables>`_
syntax can create more complex tables:

.. code-block:: ReST

  +------------+------------+-----------+
  | Header 1   | Header 2   | Header 3  |
  +============+============+===========+
  | body row 1 | column 2   | column 3  |
  +------------+------------+-----------+
  | body row 2 | Cells may span columns.|
  +------------+------------+-----------+
  | body row 3 | Cells may  | - Cells   |
  +------------+ span rows. | - contain |
  | body row 4 |            | - blocks. |
  +------------+------------+-----------+

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

Table directives
----------------

table
~~~~~

There is also a `table directive <https://docutils.sourceforge.io/docs/ref/rst/directives.html#table>`_,
which can wrap the above tables with many options.

.. code-block:: ReST

  .. table:: Truth table for "not"
     :widths: auto

     =====  =====
       A    not A
     =====  =====
     False  True
     True   False
     =====  =====

.. table:: Truth table for "not"
   :widths: auto

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====

csv-table
~~~~~~~~~

You can also use a ``csv-table`` directive to create tables:

.. code-block:: ReST

    .. csv-table:: Frozen Delights!
      :header: "Treat", "Quantity", "Description"
      :widths: 15, 10, 30

      "Albatross", 2.99, "On a stick!"
      "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
      crunchy, now would it?"
      "Gannet Ripple", 1.99, "On a stick!"

.. csv-table:: Frozen Delights!
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"

list-table
~~~~~~~~~~

Or with a ``list-table`` directive:

.. code-block:: ReST

    .. list-table:: Frozen Delights!
      :widths: 15 10 30
      :header-rows: 1

      * - Treat
        - Quantity
        - Description
      * - Albatross
        - 2.99
        - On a stick!
      * - Crunchy Frog
        - 1.49
        - If we took the bones out, it wouldn't be
          crunchy, now would it?
      * - Gannet Ripple
        - 1.99
        - On a stick!

.. list-table:: Frozen Delights!
   :widths: 15 10 30
   :header-rows: 1

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!

ghost class
~~~~~~~~~~~

With ``:class: ghost`` option, you can use the "ghost" style of a table.

.. code-block:: ReST

    .. table::
        :class: ghost
        :widths: auto

        =====  =====
          A    not A
        =====  =====
        False  True
        True   False
        =====  =====

.. table::
   :class: ghost
   :widths: auto

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====

Responsive table
----------------

Shibuya theme wraps the table html with a ``div.table-wrapper`` tag.
You can scroll the table inside it.

+------------+------------+-----------+----------+----------+----------+----------+----------+-----------------------------------------------+
| Header 1   | Header 2   | Header 3  | Header 4 | Header 5 | Header 6 | Header 7 | Header 8 | Header 9                                      |
+============+============+===========+==========+==========+==========+==========+==========+============+==================================+
| body row 1 | column 2   | column 3  | column 4 | column 5 | column 6 | column 7 |  Cells_for_column_8_and_column_9_in_both_row_1_and_row_2 |
+------------+------------+-----------+----------+----------+----------+----------+                                                          +
| body row 2 | Cells may span columns.| column 4 and 5      | column 6 and 7      |                                                          |
+------------+------------+-----------+---------------------+---------------------+----------------------------------------------------------+
