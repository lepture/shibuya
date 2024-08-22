Images and videos
=================

.. rst-class:: lead

    Here are the examples of images and videos in Shibuya sphinx theme.

-----

Images
------

.. image:: https://img.shields.io/pypi/v/shibuya?style=for-the-badge
    :alt: PyPI
    :target: https://pypi.python.org/pypi/shibuya
.. image:: https://img.shields.io/pypi/l/shibuya?color=12A594&style=for-the-badge
    :alt: PyPI - License
    :target: https://github.com/lepture/shibuya/blob/master/LICENSE
.. image:: https://img.shields.io/github/sponsors/lepture?color=8F76D6&style=for-the-badge
    :alt: GitHub Sponsors
    :target: https://github.com/sponsors/lepture

image directive
~~~~~~~~~~~~~~~

A simple image with ``image`` directive:

.. container:: demo

   .. code-block:: none
      :class: demo-code

      .. image:: /_static/images/cat.jpg

   .. container:: demo-result

      .. image:: /_static/images/cat.jpg


align image
~~~~~~~~~~~

With ``:align:`` option, you can make the image float to left or right:

.. code-block:: ReST

    .. image:: /_static/icon-light.svg
      :align: left
      :height: 200
      :width: 200

.. image:: /_static/icon-light.svg
   :align: left
   :height: 200
   :width: 200

This is a lot of text to go along with a left-aligned image, that is
helping make this content feel less linear. It is important to have such
a body of text, since the image is meant to be "floated" to the right,
which would interfere with the rest of the document otherwise.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis
sapiente veritatis doloribus accusantium molestiae modi recusandae
excepturi facere, corrupti expedita sit.

.. image:: /_static/icon-light.svg
   :align: right
   :height: 200
   :width: 200

.. hint::

    You can use ``:align: right`` to float image to the right side.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis
sapiente veritatis doloribus accusantium molestiae modi recusandae
excepturi facere, corrupti expedita sit.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis
sapiente veritatis doloribus accusantium molestiae modi recusandae
excepturi facere, corrupti expedita sit.

figure with captions
~~~~~~~~~~~~~~~~~~~~

The ``figure`` directive will wrap the image with ``<figure>`` tag, content
if ``figure`` directive will be converted to ``<figcaption>``.

.. container:: demo

   .. code-block:: none
      :caption: Image with a caption
      :class: demo-code

      .. figure:: /_static/images/dog.jpg
         :width: 800
         :align: center

         This is the ``caption``, *it can* contain **other markups**.

   .. container:: demo-result

      .. figure:: /_static/images/dog.jpg
         :width: 800
         :align: center

         This is the ``caption``, *it can* contain **other markups**.

Containers
~~~~~~~~~~

We offer several container classes to decorate images:


.. container:: demo

   .. code-block:: none
      :class: demo-code

      .. container:: image-1

          .. image:: /_static/images/cat.jpg

   .. container:: demo-result

      .. container:: image-1

          .. image:: /_static/images/cat.jpg


.. container:: demo

   .. code-block:: none
      :class: demo-code

      .. container:: image-2

          .. image:: /_static/images/cat.jpg

   .. container:: demo-result

      .. container:: image-2

          .. image:: /_static/images/cat.jpg

Light and Dark
--------------

You can utilize the ``light-only`` and ``dark-only`` classes to specify
which media to display in light or dark mode. For instance, in the
example below, it will show a dog in light mode and a cat in dark mode.

.. container:: demo

   .. code-block:: none
      :caption: light and dark mode images
      :class: demo-code

      .. figure:: /_static/images/cat.jpg
         :figclass: light-only
         :width: 800
         :align: center

      .. figure:: /_static/images/dog.jpg
         :figclass: dark-only
         :width: 800
         :align: center

   .. container:: demo-result

      .. figure:: /_static/images/cat.jpg
         :figclass: light-only
         :width: 800
         :align: center

      .. figure:: /_static/images/dog.jpg
         :figclass: dark-only
         :width: 800
         :align: center

Videos
------

There is no built-in ``video`` directive for Sphinx. But you can use these extensions instead:

- `sphinxcontrib-video <https://sphinxcontrib-video.readthedocs.io/>`_
- `sphinxcontrib-youtube <https://sphinxcontrib-youtube.readthedocs.io/>`_

Video
~~~~~

Here is an example of ``video`` directive:

.. container:: demo

   .. code-block:: none
      :class: demo-code

      .. video:: https://sphinxcontrib-video.readthedocs.io/en/latest/_images/video.mp4

   .. container:: demo-result

      .. video:: https://sphinxcontrib-video.readthedocs.io/en/latest/_images/video.mp4

YouTube
~~~~~~~

Here is an example of ``youtube`` directive:

.. container:: demo

   .. code-block:: none
      :class: demo-code

      .. youtube:: j2BdNDTlWbo
         :width: 100%

   .. container:: demo-result

      .. youtube:: j2BdNDTlWbo
         :width: 100%

Containers
~~~~~~~~~~

We offer several container classes to decorate videos:

.. code-block:: ReST

    .. container:: video-1

      .. youtube:: j2BdNDTlWbo
          :width: 100%

    .. container:: video-1

      .. video:: https://sphinxcontrib-video.readthedocs.io/en/latest/_images/video.mp4

.. container:: video-1

  .. youtube:: j2BdNDTlWbo
      :width: 100%

.. container:: video-1

  .. video:: https://sphinxcontrib-video.readthedocs.io/en/latest/_images/video.mp4


.. code-block:: ReST

    .. container:: video-2

      .. youtube:: j2BdNDTlWbo
          :width: 100%

    .. container:: video-2

      .. video:: https://sphinxcontrib-video.readthedocs.io/en/latest/_images/video.mp4

.. container:: video-2

  .. youtube:: j2BdNDTlWbo
      :width: 100%

.. container:: video-2

  .. video:: https://sphinxcontrib-video.readthedocs.io/en/latest/_images/video.mp4
