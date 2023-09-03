:description: Adding social networks of GitHub, Twitter, and etc. on your website.

Social network
==============

.. rst-class:: lead

    Connect and engage with your audience through social networks.

----

Connect with visitors by including links to your social media profiles,
making it easy for them to find and follow you on other platforms.


GitHub
------

The GitHub icon will be displayed on the navbar and footer.

.. code-block:: python

    html_theme_options = {
      "github_url": "https://github.com/lepture"
    }

Discord
-------

The Discord icon will be displayed on the navbar and footer.

.. code-block:: python

    html_theme_options = {
      "discord_url": "https://discord.gg/example/"
    }

Twitter
-------

The Twitter icon will be displayed only on the footer.

.. code-block:: python

    html_theme_options = {
      "twitter_url": "https://twitter.com/lepture"
    }

.. code-block:: python

    html_theme_options = {
      "twitter_site": "typlog",
      "twitter_creator": "lepture",
    }

Mastodon
--------

The Mastodon icon will be displayed only on the footer.

.. code-block:: python

    html_theme_options = {
      "mastodon_url": "https://mas.to/@trumpet"
    }


YouTube
-------

The YouTube icon will be displayed only on the footer.

.. code-block:: python

    html_theme_options = {
      "youtube_url": "https://youtube.com/@username"
    }
