:description: Enable copy page button and open in ChatGPT, Claude, Perplexity and etc.

Copy page
=========

.. rst-class:: lead

    Show a "Copy page" button with dropdown of open in AI links.

----

A **Copy page** button is shown by default starting with version 2025.12.13.

Disable button
--------------

If you prefer not to show the **Copy page button**, you can turn it off in the
``conf.py`` file:

.. code-block:: python
    :caption: conf.py

    html_theme_options = {
      "show_ai_links": False,
    }

Source files
------------

If the **Copy page** button does not appear at all, it may be because the source file cannot
be found. The Shibuya theme will look for the source file when ``html_copy_source = True`` is
set, or when ``html_context`` is configured with source information.

Use the GitHub's raw URL for source URL:

.. code-block:: python
    :caption: conf.py

    html_context = {
        "source_type": "github",
        "source_user": "lepture",
        "source_repo": "shibuya",
    }

Use the Sphinx copy source feature for source URL:

.. code-block:: python
    :caption: conf.py

    # html_baseurl is required to create absolute URL
    html_baseurl = "https://shibuya.lepture.com/"
    html_copy_source = True

Sphinx will copy the source files into ``_sources`` folder.

Prompt template
---------------

By default, you can open the page in ChatGPT, Claude, and Perplexity using the
following prompt:

.. code-block:: text

    Read {url} so I can ask questions about it.

You can customize the prompt template in the ``conf.py`` file:

.. code-block:: python
    :caption: conf.py

    html_theme_options = {
      "ai_prompt_template": "Read {url} at first, then answer my questions about it.",
    }

Open links
----------

The **Copy page** dropdown enables **Open in** links for ChatGPT and Claude by default.
These links can be enabled or disabled via the following configuration:

.. code-block:: python
    :caption: conf.py

    html_theme_options = {
      "open_in_chatgpt": True,
      "open_in_claude": True,
      "open_in_perplexity": True,
    }
