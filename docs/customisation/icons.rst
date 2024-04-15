Icons
=====

Lucid Icons
-----------

Shibuya theme uses a subset of `Lucid <https://lucide.dev/>`_ icons.
The icons are used for navigations, admonitions, and etc:

.. code-block:: none

    --lucid-alert-url
    --lucid-arrows-url
    --lucid-award-url
    --lucid-bell-url
    --lucid-bookmark-url
    --lucid-calendar-url
    --lucid-check-url
    --lucid-chevron-url
    --lucid-close-url
    --lucid-external-link-url
    --lucid-flame-url
    --lucid-git-fork-url
    --lucid-help-url
    --lucid-languages-url
    --lucid-laptop-url
    --lucid-link-url
    --lucid-menu-url
    --lucid-milestone-url
    --lucid-moon-url
    --lucid-outdent-url
    --lucid-rocket-url
    --lucid-skull-url
    --lucid-star-url
    --lucid-sun-url
    --lucid-zap-url

Simple Icons
------------

Shibuya theme uses a subset of `Simple Icons <https://simpleicons.org/>`_
for social networks. These icons include:

- GitHub: ``--simpleicons-github-url``
- Gitlab: ``--simpleicons-gitlab-url``
- Bitbucket: ``--simpleicons-bitbucket-url``
- Discord: ``--simpleicons-discord-url``
- Mastodon: ``--simpleicons-mastodon-url``
- YouTube: ``--simpleicons-youtube-url``
- X (Twitter): ``--simpleicons-x-twitter-url``
- Reddit: ``--simpleicons-reddit-url``

Custom Icons
------------

You can customize the icons by defining CSS variables for each icon,
for example:

.. code-block:: css
    :caption: custom.css

    :root {
      --lucid-star-url:url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m12 2 3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z'/%3E%3C/svg%3E");
    }
