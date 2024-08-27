Icons
=====

Shibuya theme incorporates a variety of icons:

- A selection of `Lucide <https://lucide.dev/>`_ icons is used for navigation, admonitions and ect,
- and a subset of `Simple Icons <https://simpleicons.org/>`_ are employed for social networks.

Lucide Icons
------------

`Lucide <https://lucide.dev/>`_ icons are embeded in CSS, which can be used with:

.. code-block:: html

    <i class="i-lucide chevron-down"></i>

Navigations
~~~~~~~~~~~

The icons are used for navigations and other functions:

.. code-block:: html

    <i class="i-lucide chevron-left"></i>
    <i class="i-lucide chevron-right"></i>
    <i class="i-lucide chevron-down"></i>
    <i class="i-lucide chevron-up"></i>

    <i class="i-lucide menu"></i>
    <i class="i-lucide outdent"></i>
    <i class="i-lucide close"></i>
    <i class="i-lucide external-link"></i>

Theme icons
~~~~~~~~~~~

Shibuya theme supports a light and dark mode switch, and the icons
used for toggling between modes are:

.. code-block::

    --icon-url: var(--lucide-laptop-url);
    --icon-url: var(--lucide-sun-url);
    --icon-url: var(--lucide-moon-url);

Admonition icons
~~~~~~~~~~~~~~~~

These are icons used for :ref:`admonitions`:

.. code-block:: css

    :root {
      --attention-icon: var(--lucide-alert-url);
      --caution-icon: var(--lucide-zap-url);
      --danger-icon: var(--lucide-skull-url);
      --error-icon: var(--lucide-close-url);
      --hint-icon: var(--lucide-bell-url);
      --important-icon: var(--lucide-flame-url);
      --note-icon: var(--lucide-calendar-url);
      --tip-icon: var(--lucide-rocket-url);
      --warning-icon: var(--lucide-zap-url);
      --seealso-icon: var(--lucide-link-url);
      --todo-icon: var(--lucide-bookmark-url);
    }

Custom Icons
~~~~~~~~~~~~

You can customize the icons by defining CSS variables for each icon,
for example:

.. code-block:: css
    :caption: custom.css

    :root {
      --lucide-star-url:url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m12 2 3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z'/%3E%3C/svg%3E");
    }

Social icons
------------

Shibuya theme uses `Iconify Icon web component <https://iconify.design/docs/iconify-icon/>`_
for social networks. With the ``<iconify-icon>`` component, you can use any icon
available through Iconify.

.. code-block:: html

    <iconify-icon icon="simple-icons:github"></iconify-icon>

.. tip::

    You can find all the available icons through
    `Icon Sets <https://icon-sets.iconify.design/>`_.

Navbar social
~~~~~~~~~~~~~

If you need to add :ref:`social` that Shibuya theme doesn't contain in navbar,
you can custom it with ``partials/nav-socials.html``:

.. code-block:: html
    :caption: docs/_templates/partials/nav-socials.html

    <div class="sy-head-socials">
      {%- include "components/nav-socials.html" -%}
      <a href="https://t.me/your-telegram-channel" aria-label="Telegram">
        <iconify-icon icon="simple-icons:telegram"></iconify-icon>
      </a>
    </div>

Foot social
~~~~~~~~~~~

Just like navbar social networks above, you can custom it with
``partials/foot-socials.html``:

.. code-block:: html
    :caption: docs/_templates/partials/foot-socials.html

    <div class="sy-foot-socials">
      {%- include "components/foot-socials.html" -%}
      <a href="https://t.me/your-telegram-channel" aria-label="Telegram">
        <iconify-icon icon="simple-icons:telegram"></iconify-icon>
      </a>
    </div>
