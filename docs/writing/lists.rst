:description: Markup of lists in Sphinx, and how it looks like on Shibuya.

Lists
=====

There are several kinds of lists in Sphinx (reStructuredText, or rst).

Bullet list
-----------

A text block which begins with a ``*``, ``+``, ``-``, ``•``, ``‣``,
followed by whitespace, is an unordered list item.

.. code-block:: rst

    - This is the first bullet list item.  The blank line above the
      first list item is required; blank lines between list items
      (such as below this paragraph) are optional.

    - This is the first paragraph in the second item in the list.

      This is the second paragraph in the second item in the list.
      The blank line above this paragraph is required.  The left edge
      of this paragraph lines up with the paragraph above, both
      indented relative to the bullet.

      - This is a sublist.  The bullet lines up with the left edge of
        the text blocks above.  A sublist is a new list so requires a
        blank line above and below.

    - This is the third item of the main list.

    This paragraph is not part of the list.

And unlike Markdown, reStructuredText has no tight list. For example:

.. code-block:: rst

  - List item 1
  - List item 2

- List item 1
- List item 2

If you inspect the HTML in your browser, you will find there are always
``<p>`` tag in the list.

Numbered list
-------------

A text block which begins with a number, a letter or a roman numeral,
followed by a period ``.``, right bracket ``)`` or surrounded by brackets
``( )``, is an ordered (numbered, enumerated) list item.

.. code-block:: rst

   1. numbers

   A. upper-case letters
      and it goes over many lines

      with two paragraphs and all!

   a. lower-case letters

      3. with a sub-list starting at a different number
      4. make sure the numbers are in the correct sequence though!

   I. upper-case roman numerals

   i. lower-case roman numerals

   (1) numbers again

   1) and again

1. numbers

A. upper-case letters
   and it goes over many lines

   with two paragraphs and all!

a. lower-case letters

   3. with a sub-list starting at a different number
   4. make sure the numbers are in the correct sequence though!

I. upper-case roman numerals

i. lower-case roman numerals

(1) numbers again

1) and again

Nested lists
------------

Lists can contain lists, here is a more complex list demo:

- A list

  - can contain another list

    1. there are ordered list
    2. and unordered list

- The unordered list

  a. can have different style
  b. this ordered list is using ``a``, ``b``, etc
  c. instead of numbers

Definition list
---------------

.. code-block:: rst

   Term
      The definition of the term.
   Apple
      A kind of fruit, not a company.

Term
   The definition of term.
Apple
   A kind of fruit, not a company.


Field list
----------

.. code-block:: rst

    :Date: 2001-08-16
    :Version: 1
    :Authors: - Me
              - Myself
              - I

:Date: 2001-08-16
:Version: 1
:Authors: - Me
          - Myself
          - I

Option list
-----------

-a         Output all.
-b         Output both (this description is
           quite long).
-c arg     Output just arg.
--long     Output all day long.

-p         This option has two paragraphs in the description.
           This is the first.

           This is the second.  Blank lines may be omitted between
           options (as above) or left in (as here and below).

--very-long-option  A VMS-style option.  Note the adjustment for
                    the required two spaces.

--an-even-longer-option
           The description can also start on the next line.

-2, --two  This option has two variants.

-f FILE, --file=FILE  These two options are synonyms; both have
                      arguments.

/V         A VMS/DOS-style option.

Horizontal list
---------------

Using ``hlist`` directive to layout list horizontally.

.. code-block:: rst

    .. hlist::
      :columns: 3

      * A list of
      * short items
      * that should be
      * displayed
      * horizontally

.. hlist::
   :columns: 3

   * A list of
   * short items
   * that should be
   * displayed
   * horizontally
