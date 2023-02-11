Admonitions
===========

Admonitions are a great way to bring the attention of readers. It
is a special kind of directives. There are many different types of
admonitions, including the reStructuredText's built-in admonitions,
and directives provided by Sphinx which looks like admonitions.

reST admonitions
----------------

The built-in `admonitions in reST`_ includes:

.. _`admonitions in reST`: https://docutils.sourceforge.io/docs/ref/rst/directives.html#admonitions

- attention
- caution
- danger
- error
- hint
- important
- note
- tip
- warning

The admonition syntax in reST accepts no arguments, and most of the
time no options:

.. code-block:: rst

    .. admonition-name::
       content in admonition

Here is an example of the ``hint`` admonition:

.. container:: demo

   .. code-block:: none
      :caption: attention
      :class: demo-code

      .. hint::
         ``hint`` is a special directive for admonition.

   .. container:: demo-result

      .. hint::
         ``hint`` is a special directive for admonition.

``attention``
~~~~~~~~~~~~~

.. attention::

Generic admonition
------------------

Admonition-like directives
--------------------------

- versionmodified
- seealso

.. note::

  There is a note

Nested admonitions
------------------

Style customisation
-------------------
