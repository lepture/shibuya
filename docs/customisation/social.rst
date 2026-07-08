:description: Adding social networks of GitHub, Twitter, and etc. on your website.

.. _social:

Social network
==============

.. rst-class:: lead

    Connect and engage with your audience through social networks.

----

Navbar & Footer
---------------

Configure which social networks appear in your navigation bar and footer:

.. code-block:: python

    html_theme_options = {
        "nav_socials": ["github", "x"],
        "foot_socials": ["readthedocs", "github", "slack"]
    }

Alternatives
~~~~~~~~~~~~

You can also config ``nav_socials`` and ``foot_socials`` with:

.. code-block:: python

    html_theme_options = {
        "nav_socials": [
            {
                "name": "GitHub",
                "url": "https://github.com/lepture/shibuya",
                "icon": "simple-icons:github",
            }
        ],
        "foot_socials": [
            {
                "name": "X",
                "url": "https://x.com/lepture",
                "icon": "simple-icons:x",
            }
        ]
    }

In this case, you don't have to configure the bellow network urls.

Supported Networks
------------------

To activate the links, add the corresponding URLs to your ``html_theme_options`` in ``conf.py``:

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

Deprecated Options
------------------

.. deprecated:: 2026.7.8
    ``twitter_url`` is deprecated. Please use ``x_url`` instead.

.. deprecated:: 2026.7.8
    ``twitter_site`` and ``twitter_creator`` (used for Twitter cards) are deprecated and no longer supported.

Custom networks
---------------

If you need to add social networks that Shibuya theme doesn't contain, you can
custom it with ``partials/nav-socials.html`` and ``partials/foot-socials.html``:

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
