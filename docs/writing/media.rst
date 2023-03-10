Images and Videos
=================

Simple images
-------------

.. container:: demo

   .. code-block:: none
      :caption: Image in center
      :class: demo-code

      .. image:: https://source.unsplash.com/200x200/daily?brids
         :width: 200
         :height: 200
         :align: center

   .. container:: demo-result

      .. image:: https://source.unsplash.com/200x200/daily?birds
         :width: 200
         :height: 200
         :align: center

Image with captions
-------------------

The ``figure`` directive will wrap the image with ``<figure>`` tag, content
if ``figure`` directive will be converted to ``<figcaption>``.

.. container:: demo

   .. code-block:: none
      :caption: Image with a caption
      :class: demo-code

      .. figure:: https://source.unsplash.com/200x200/daily?birds
         :width: 200
         :height: 200
         :align: center

         This is the ``caption``, *it can* contain **other markups**.
         The photo is generated by Unsplash_ API.

   .. container:: demo-result

      .. figure:: https://source.unsplash.com/200x200/daily?birds
         :width: 200
         :height: 200
         :align: center

         This is the ``caption``, *it can* contain **other markups**.
         The photo is generated by Unsplash_ API.

.. _Unsplash: https://unsplash.com
