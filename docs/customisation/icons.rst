Icons
=====

Lucid Icons
-----------

Shibuya theme uses a subset of `Lucid <https://lucide.dev/>`_ icons.
The icons are used for navigations, admonitions, and etc:

.. code-block:: none

    --i-alert-url
    --i-arrows-url
    --i-award-url
    --i-bell-url
    --i-bookmark-url
    --i-calendar-url
    --i-check-url
    --i-chevron-url
    --i-close-url
    --i-external-link-url
    --i-flame-url
    --i-git-fork-url
    --i-help-url
    --i-languages-url
    --i-laptop-url
    --i-link-url
    --i-menu-url
    --i-milestone-url
    --i-moon-url
    --i-outdent-url
    --i-rocket-url
    --i-skull-url
    --i-star-url
    --i-sun-url
    --i-zap-url

Simple Icons
------------

Shibuya theme uses a subset of `Simple Icons <https://simpleicons.org/>`_
for social networks. These icons include:

- GitHub: ``--i-github-url``
- Gitlab: ``--i-gitlab-url``
- Bitbucket: ``--i-bitbucket-url``
- Discord: ``--i-discord-url``
- Mastodon: ``--i-mastodon-url``
- YouTube: ``--i-youtube-url``
- X (Twitter): ``--i-x-twitter-url``
- Reddit: ``--i-reddit-url``

Custom Icons
------------

You can customize the icons by defining CSS variables for each icon,
for example:

.. code-block:: css
    :caption: custom.css

    :root {
      --i-star-url:url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m12 2 3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z'/%3E%3C/svg%3E");
    }
