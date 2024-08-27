:description: Adding social networks of GitHub, Twitter, and etc. on your website.

.. _social:

Social network
==============

.. rst-class:: lead

    Connect and engage with your audience through social networks.

----

Connect with visitors by including links to your social media profiles,
making it easy for them to find and follow you on other platforms.


Source code
-----------

A link directs you to the repository where you can access the project's
source code. These links will be visible in both the website's navbar and
footer.

.. important::

    The shibuya theme will only display one source code link.

GitHub
~~~~~~

The GitHub icon will be displayed on the navbar and footer.

.. code-block:: python

    html_theme_options = {
      "github_url": "https://github.com/lepture/shibuya"
    }

Gitlab
~~~~~~

The Gitlab icon will be displayed on the navbar and footer.

.. code-block:: python

    html_theme_options = {
      "gitlab_url": "https://gitlab.com/gitlab-org/gitlab"
    }

Bitbucket
~~~~~~~~~

The Bitbucket icon will be displayed on the navbar and footer.

.. code-block:: python

    html_theme_options = {
      "bitbucket_url": "https://bitbucket.org/sonarsource/sonarqube-scan"
    }

Community
---------

You can also provide links to various social platforms where you can
interact with the documentation's community, exchange ideas, and stay
informed about the latest developments.

Discord
~~~~~~~

The Discord icon will be displayed on the navbar and footer.

.. code-block:: python

    html_theme_options = {
      "discord_url": "https://discord.gg/example/"
    }

Slack
~~~~~~~

The Slack icon will be displayed on the navbar and footer.

.. code-block:: python

    html_theme_options = {
      "slack_url": "https://example.com/join/slack"
    }

X (Twitter)
~~~~~~~~~~~

The X icon will be displayed only on the footer.

.. code-block:: python

    html_theme_options = {
      "twitter_url": "https://twitter.com/lepture"
    }

The Shibuya theme also includes support for Twitter cards,
allowing you to include additional Twitter information:

.. code-block:: python

    html_theme_options = {
      "twitter_site": "typlog",
      "twitter_creator": "lepture",
    }

Mastodon
~~~~~~~~

The Mastodon icon will be displayed only on the footer.

.. code-block:: python

    html_theme_options = {
      "mastodon_url": "https://mas.to/@trumpet"
    }


YouTube
~~~~~~~

The YouTube icon will be displayed only on the footer.

.. code-block:: python

    html_theme_options = {
      "youtube_url": "https://youtube.com/@username"
    }

Reddit
~~~~~~

The Reddit icon will be displayed only on the footer.

.. code-block:: python

    html_theme_options = {
      "reddit_url": "https://www.reddit.com/r/flask/"
    }

LinkedIn
~~~~~~~~

The LinkedIn icon will be displayed only on the footer.

.. code-block:: python

    html_theme_options = {
      "linkedin_url": "https://www.linkedin.com/company/microsoft"
    }

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
