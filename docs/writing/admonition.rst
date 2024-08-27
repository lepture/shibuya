:description: Admonitions are a great way to bring the attention of readers.

.. _admonitions:

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

.. code-block:: ReST

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

.. attention:: Shibuya is a well designed Sphinx theme.

``caution``
~~~~~~~~~~~~~

.. caution:: Livereload_ is using tornado for the server.

.. _Livereload: https://github.com/lepture/python-livereload

``danger``
~~~~~~~~~~~~~

.. danger:: A non-sustainable project is no trustworthy to use.

``error``
~~~~~~~~~~~~~

.. error:: One can not be divided by zero.

``hint``
~~~~~~~~~~~~~

.. hint:: Authlib_ helps you build an OpenID Connect server.

``important``
~~~~~~~~~~~~~

.. important:: I sometimes write blog posts on https://lepture.com

``note``
~~~~~~~~~~~~~

.. note:: Typlog_ is created by me.

``tip``
~~~~~~~~~~~~~

.. tip:: Become a sponsor to keep this project sustainable.

``warning``
~~~~~~~~~~~~~

.. warning:: Do not ask your own questions in GitHub issues.


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

.. code-block:: python
   :caption: conf.py

   extensions = [
       "sphinx.ext.todo",
   ]
   todo_include_todos = True

.. todo::

   Fix this UI issue later.


Versions directives
-------------------

Here lists the version related directives. These directives are not
admonitions, but in Shibuya theme, they look like admonitions.

``versionadded``
~~~~~~~~~~~~~~~~

.. container:: demo

   .. code-block:: none
      :caption: versionadded
      :class: demo-code

      .. versionadded:: v3
         Built-in reST renderer is added in Mistune.

   .. container:: demo-result

      .. versionadded:: v3
         Built-in reST renderer is added in Mistune_.

``versionchanged``
~~~~~~~~~~~~~~~~~~

.. container:: demo

   .. code-block:: none
      :caption: versionchanged
      :class: demo-code

      .. versionchanged:: v2
         The ``jose`` module is moved out of Authlib.

   .. container:: demo-result

      .. versionchanged:: v2
         The ``jose`` module is moved out of Authlib_.

``deprecated``
~~~~~~~~~~~~~~

.. container:: demo

   .. code-block:: none
      :caption: deprecated
      :class: demo-code

      .. deprecated:: 2.7
         This version is no longer maintained, please upgrade to v3.

   .. container:: demo-result

      .. deprecated:: 2.7
         This version is no longer maintained, please upgrade to v3.

Nesting admonitions
-------------------

It is possible to add admonitions into admonitions. Take an example:

.. code-block:: none

   .. note::

      An admonition can contain another admonition.

      .. warning::

         But is is not a really good idea.

         .. danger::

            It's distracting.

        It can also be confusing.

        - It can contain list.

      And it looks pretty weird.

.. note::

  An admonition can contain another admonition.

  .. warning::

    But is is not a really good idea.

    .. danger::

      It's distracting.

    It can also be confusing.

    - It can contain list.

  And it looks pretty weird.



.. _Authlib: https://authlib.org
.. _Mistune: https://mistune.lepture.com
.. _Typlog: https://typlog.com
