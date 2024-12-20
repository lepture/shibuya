.. _sphinx-contributors:

sphinx-contributors
===================

Sphinx extension that helps you recognize the people who have contributed to an open-source project.

- **Documentation**: https://sphinx-contributors.readthedocs.io/
- **Source Code**: https://github.com/dgarcia360/sphinx-contributors

Usage
-----

Install ``sphinx-contributors``:

.. code-block:: bash

    pip install sphinx-contributors

Add ``sphinx_contributors`` to your ``conf.py``:

.. code-block:: python

    extensions = [
        'sphinx_contributors',
    ]

Example
-------

.. code-block:: none

    .. contributors:: lepture/shibuya

.. contributors:: lepture/shibuya


.. code-block:: none

    .. contributors:: lepture/shibuya
        :avatars:

.. contributors:: lepture/shibuya
    :avatars:

.. code-block:: none

  .. container:: rounded-image
      .. contributors:: lepture/shibuya
          :avatars:

.. container:: rounded-image

  .. contributors:: lepture/shibuya
      :avatars:

.. code-block:: none

    .. contributors:: lepture/shibuya
        :contributions:

.. contributors:: lepture/shibuya
    :contributions:

.. code-block:: none

    .. contributors:: lepture/shibuya
        :avatars:
        :contributions:

.. contributors:: lepture/shibuya
    :avatars:
    :contributions:
