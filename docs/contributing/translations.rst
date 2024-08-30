:description: Help us translating this documentation into other languages.

Translations
============

To begin translating this documentation into other languages, please
start by referring to the :ref:`development` guide, which will help
you set up a suitable development environment.

Adding a new language
---------------------

First, we need to generate the ``.po`` file in your preferred language:

.. code-block:: shell

    make babel-init lang=it

In this example, we're using the language code ``it`` to represent Italian.

Updating languages
------------------

If the language exists, you can update the ``.po`` files using the
following command:

.. code-block:: shell

    make babel-update lang=it

Writing the translations
------------------------

Following the previous command, the ``.po`` files will be generated within
the ``src/shibuya/locale/it/LC_MESSAGES`` directory. You can now edit these
files to add the Italian translations accordingly.

Compiling the translations
--------------------------

Once, the translations are completed. You need to compile the translations
before validating it.

.. code-block:: shell

    make babel-compile
