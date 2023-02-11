Admonitions
===========

Admonitions are a great way to bring the attention of readers. It
is a special kind of directives. There are many different types of
admonitions, including the reStructuredText's built-in admonitions,
and directives provided by Sphinx which looks like admonitions.

reST admonitions
----------------

Here lists all the built-in `admonitions in reST`_. The admonition
syntax in reST accepts no arguments, and most of the time no options:

.. _`admonitions in reST`: https://docutils.sourceforge.io/docs/ref/rst/directives.html#admonitions

.. code-block:: rst

    .. admonition-name::
       content in admonition

Here is an example of the ``note`` admonition:

.. container:: demo

   .. code-block:: none
      :caption: note
      :class: demo-code

      .. note::
         ``note`` is a special directive for admonition.

   .. container:: demo-result

      .. note::
         ``note`` is a special directive for admonition.

``attention``
~~~~~~~~~~~~~

.. attention:: Python 2 is no longer maintained.

``caution``
~~~~~~~~~~~~~

.. caution:: Python 2 is no longer maintained.

``danger``
~~~~~~~~~~~~~

.. danger:: Python 2 is no longer maintained.

``error``
~~~~~~~~~~~~~

.. error:: Python 2 is no longer maintained.

``hint``
~~~~~~~~~~~~~

.. hint:: Python 2 is no longer maintained.

``important``
~~~~~~~~~~~~~

.. important:: Python 2 is no longer maintained.

``note``
~~~~~~~~~~~~~

.. note:: Python 2 is no longer maintained.

``tip``
~~~~~~~~~~~~~

.. tip:: Python 2 is no longer maintained.

``warning``
~~~~~~~~~~~~~

.. warning:: Python 2 is no longer maintained.


Generic admonition
------------------

A generic ``.. admonition::`` directive accepts a custom title:

.. code-block:: none

    .. admonition:: Admonition title here

       Content of the admonition

Here is an example of the generic admonition:

.. container:: demo

   .. code-block:: none
      :caption: generic admonition
      :class: demo-code

      .. admonition:: Typlog

         Typlog can help you hosting your blogs and podcasts.

   .. container:: demo-result

      .. admonition:: Typlog

         Typlog_ can help you hosting your blogs and podcasts.

By default, a generic admonition is decorated with your theme color.
But you can customize the result with a ``:class:`` option. With the
above admonitions as the class name, the result would look like the
above admonitions:

.. container:: demo

   .. code-block:: none
      :caption: custom admonition
      :class: demo-code

      .. admonition:: Typlog
         :class: hint

         Typlog can help you hosting your blogs and podcasts.

   .. container:: demo-result

      .. admonition:: Typlog
         :class: tip

         Typlog_ can help you hosting your blogs and podcasts.


Admonition-like directives
--------------------------

Here lists the directives added by Sphinx which looks like admonitions.

``seealso``
~~~~~~~~~~~

.. seealso::
   The `blog post about Shibuya`_ by lepture.

.. _`blog post about Shibuya`: https://lepture.com


``todo``
~~~~~~~~

The ``todo`` admonition is enabled by ``sphinx.ext.todo``, please add
this extension in the ``conf.py`` file.

.. todo::

   Fix this UI issue later.


Versions directives
-------------------

``versionadded``
~~~~~~~~~~~~~~~~

.. versionadded:: v2

   Built-in reST renderer is added in Mistune_.

``versionchanged``
~~~~~~~~~~~~~~~~~~

.. versionchanged:: v2

   Built-in reST renderer is added in Mistune_.

``deprecated``
~~~~~~~~~~~~~~

.. deprecated:: v2

   Built-in reST renderer is added in Mistune_.


Nested admonitions
------------------

.. note::

   Here is the note

   .. tip:: Here is a tip


.. _Mistune: https://mistune.lepture.com
.. _Typlog: https://typlog.com
