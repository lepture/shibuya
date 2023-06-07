Markups of Extensions
=====================


sphinx-design
-------------

Grid
~~~~

.. grid:: 2

    .. grid-item-card:: Tutorial
        :link: /install/

        If you're new to Python and Sphinx, this is a great place to start.

    .. grid-item-card:: Customisation
        :link: /customisation/

        Tailor configurations to meet your specific requirements with customizable settings.

    .. grid-item-card:: References
        :link: /writing/

        Learn the syntax of reStructuredText and examine how it is formatted.

    .. grid-item-card:: Contributing
        :link: /contributing/

        Your contributions can make a meaningful impact and help drive the project forward!

Card
~~~~~

.. card:: Card Title

    Header
    ^^^
    Card content
    +++
    Footer

Dropdown
~~~~~~~~

.. dropdown:: Dropdown title

    Dropdown content

Tabs
~~~~

.. tab-set::

    .. tab-item:: Label1

        Content 1

    .. tab-item:: Label2

        Content 2

.. tab-set-code::

    .. code-block:: python

        foo = "str"

    .. code-block:: javascript

        a = 1;

Badges
~~~~~~

:bdg:`plain badge`

:bdg-primary:`primary`, :bdg-primary-line:`primary-line`

:bdg-secondary:`secondary`, :bdg-secondary-line:`secondary-line`

:bdg-success:`success`, :bdg-success-line:`success-line`

:bdg-info:`info`, :bdg-info-line:`info-line`

:bdg-warning:`warning`, :bdg-warning-line:`warning-line`

:bdg-danger:`danger`, :bdg-danger-line:`danger-line`

:bdg-light:`light`, :bdg-light-line:`light-line`

:bdg-dark:`dark`, :bdg-dark-line:`dark-line`

:bdg-link-primary:`https://example.com`

:bdg-link-primary-line:`explicit title <https://example.com>`

Buttons
~~~~~~~

.. button-link:: https://example.com

.. button-link:: https://example.com

    Button text

.. button-link:: https://example.com
    :color: primary
    :shadow:

.. button-link:: https://example.com
    :color: primary
    :outline:

.. button-link:: https://example.com
    :color: secondary
    :expand:

Octicon Icons
~~~~~~~~~~~~~

- alert: :octicon:`alert`
- bell: :octicon:`bell`
- book: :octicon:`book`
- clock: :octicon:`clock`


sphinx-tabs
-----------

`sphinx-tabs <https://github.com/executablebooks/sphinx-tabs>`_
is an extension maintained by Executable Books. Here are some examples
of the markup:

.. code-block:: none

    .. tabs::

      .. tab:: Apples

          Apples are green, or sometimes red.

      .. tab:: Pears

          Pears are green.

      .. tab:: Oranges

          Oranges are orange.

    .. tabs::

      .. group-tab:: Linux

          Linux Line 1

      .. group-tab:: Mac OSX

          Mac OSX Line 1

      .. group-tab:: Windows

          Windows Line 1

    .. tabs::

      .. group-tab:: Linux

          Linux Line 1

      .. group-tab:: Mac OSX

          Mac OSX Line 1

      .. group-tab:: Windows

          Windows Line 1


    .. tabs::

      .. code-tab:: c

            int main(const int argc, const char **argv) {
              return 0;
            }

      .. code-tab:: c++

            int main(const int argc, const char **argv) {
              return 0;
            }

      .. code-tab:: py

            def main():
                return

.. image:: /_static/screenshots/light-sphinx-tabs.png
   :class: dark-hidden
   :align: center

.. image:: /_static/screenshots/dark-sphinx-tabs.png
   :class: light-hidden
   :align: center

sphinx-inline-tabs
------------------
