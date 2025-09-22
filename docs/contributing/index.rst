Contributing
============

Contributions are welcome, and they are greatly appreciated!

Types of contributions
----------------------

There are many ways you can contribute.

Report bugs
~~~~~~~~~~~

You're welcome to report bugs at
`GitHub Issues <https://github.com/lepture/shibuya/issues>`_.

When reporting a bug, please including:

- Your operating system name and version.
- Your browser name and version.
- Details to reproduce the bug.

Submit fixes
~~~~~~~~~~~~

Once you found a bug that you can fix, you're welcome
to submit your pull request.

Please follow our `git commit conventions <https://www.conventionalcommits.org/en/v1.0.0/>`_.

Improve documentation
~~~~~~~~~~~~~~~~~~~~~

Everyone wants a good documentation. There may be mistakes
or things missing in the documentation, you're welcome to
help us improving the documentation.

.. _development:

Development
-----------

Once you cloned shibuya's source code, you can setup a development
environment to work on.

venv
~~~~

I strongly suggest you create a virtual environment with ``venv``:

.. code-block:: bash

    python -m venv .venv
    source .venv/bin/active

Install
~~~~~~~

Then install the Python requirements:

.. code-block:: bash

    pip install -r requirements-dev.lock
    pip install livereload

Run dev server
~~~~~~~~~~~~~~

Once all the requirements are installed, you can run a livereload
server with:

.. code-block:: bash

    python serve.py

Build static
~~~~~~~~~~~~

Open a new tab of your terminal, and ``cd`` into ``static`` folder:

.. code-block:: bash

    cd static

Then install all the dependencies with ``npm``:

.. code-block:: bash

    npm install

Watch CSS changes and build CSS files:

.. code-block:: bash

    npm run dev:css

Ready for development
~~~~~~~~~~~~~~~~~~~~~

Now, your environment is ready for development. Open your browser, and visit
``http://127.0.0.1:5500/``.

.. toctree::
   :hidden:

   translations
   roadmap
