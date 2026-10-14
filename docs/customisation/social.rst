:description: Adding social networks of GitHub, Twitter, and etc. on your website.

.. _social:

Social networks
===============

.. rst-class:: lead

    Connect and engage with your audience through social networks.

----

Navbar & Footer
---------------

Social networks can be shown in two places: the navigation bar and the footer.
Use ``nav_socials`` and ``foot_socials`` to choose which networks to display:

.. code-block:: python

    html_theme_options = {
        "nav_socials": ["github", "x"],
        "foot_socials": ["readthedocs", "github", "slack"],
    }

Each item refers to a built-in network (see :ref:`supported-networks`). Only
networks whose URL is configured are rendered. When these options are left
unset, the theme falls back to its default list.

.. _supported-networks:

Supported networks
------------------

To activate a network, set its URL in ``html_theme_options`` in ``conf.py``:

.. code-block:: python

    html_theme_options = {
        # Development platforms
        "github_url": "https://github.com/lepture/shibuya",
        "gitlab_url": "https://gitlab.com/gitlab-org/gitlab",
        "bitbucket_url": "https://bitbucket.org/sonarsource/sonarqube-scan",

        # Chat & Community
        "discord_url": "https://discord.gg/example",
        "slack_url": "https://example.com/join/slack",

        # Social & Microblogging
        "x_url": "https://x.com/lepture",
        "mastodon_url": "https://mas.to/@trumpet",
        "bluesky_url": "https://bsky.app/profile/lepture.com",

        # Content & Professional
        "youtube_url": "https://youtube.com/@username",
        "reddit_url": "https://www.reddit.com/r/flask",
        "linkedin_url": "https://www.linkedin.com/company/microsoft",
    }

Custom networks
---------------

You can customize social networks in three ways, depending on how much control
you need:

Built-in options
~~~~~~~~~~~~~~~~

When a network is listed as a string, its display name and icon come from the
built-in defaults. Override them with ``<name>_name`` and ``<name>_icon``:

.. code-block:: python

    html_theme_options = {
        "github_name": "GitHub Repository",
        "github_icon": "fa-brands:github-square",
        "github_url": "https://github.com/lepture/shibuya",
    }

Dictionary entries
~~~~~~~~~~~~~~~~~~

Alternatively, list full dictionaries to bypass the URL options entirely:

.. code-block:: python

    html_theme_options = {
        "nav_socials": [
            {
                "name": "GitHub",
                "icon": "simple-icons:github",
                "url": "https://github.com/lepture/shibuya",
            }
        ],
        "foot_socials": [
            {
                "name": "X",
                "icon": "simple-icons:x",
                "url": "https://x.com/lepture",
            }
        ],
    }

Template overrides
~~~~~~~~~~~~~~~~~~

If you need to add social networks that Shibuya theme doesn't contain, directly
edit the ``partials/nav-socials.html`` and ``partials/foot-socials.html`` templates:

.. code-block:: html
    :caption: _templates/partials/nav-socials.html

    <div class="sy-head-socials">
      {%- include "components/nav-socials.html" -%}
      <a href="your-social-network-url" aria-label="Your Social network">
        <svg>...</svg>
      </a>
    </div>

.. code-block:: html
    :caption: _templates/partials/foot-socials.html

    <div class="sy-foot-socials">
      {%- include "components/foot-socials.html" -%}
      <a href="your-social-network-url" aria-label="Your Social network">
        <svg>...</svg>
      </a>
    </div>

Deprecated options
------------------

.. deprecated:: 2026.7.8
    ``twitter_url`` is deprecated. Please use ``x_url`` instead.

.. deprecated:: 2026.7.8
    ``twitter_site`` and ``twitter_creator`` (used for Twitter cards) are deprecated and no longer supported.

