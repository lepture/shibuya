import os
import shibuya

project = "Shibuya"
copyright = "Copyright &copy; 2023, Hsiaoming Yang"
author = "Hsiaoming Yang"

version = shibuya.shibuya_version
release = version

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_design",
]
todo_include_todos = True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

templates_path = ["_templates"]
html_static_path = ["_static"]
html_extra_path = ["_public"]

html_title = "Shibuya"
html_theme = "shibuya"
html_baseurl = "https://shibuya.lepture.com"

html_copy_source = False
html_show_sourcelink = False

html_additional_pages = {
    "branding": "branding.html",
}

html_sidebars = {
    "**": [
        "sidebars/localtoc.html",
        "sidebars/repo-stats.html",
        "sidebars/edit-this-page.html",
    ]
}

if os.getenv("TRIM_HTML_SUFFIX"):
    html_link_suffix = ""

html_favicon = "_static/icon-light.svg"

html_theme_options = {
    "logo_target": "/",
    "light_logo": "_static/logo-light.svg",
    "dark_logo": "_static/logo-dark.svg",

    "og_image_url": "https://shibuya.lepture.com/icon.png",
    "twitter_creator": "lepture",
    "twitter_site": "lepture",

    "github_url": "https://github.com/lepture/shibuya",

    "nav_links": [
        {
            "title": "Branding",
            "url": "/branding"
        },
    ]
}

html_context = {
    "source_type": "github",
    "source_user": "lepture",
    "source_repo": "shibuya",
}

if "READTHEDOCS" in os.environ:
    html_theme_options["announcement"] = (
        "This documentation is hosted on Read the Docs only for testing. Please use "
        "<a href='https://shibuya.lepture.com/'>the main documentation</a> instead."
    )

DEBUG_RTD = False

if DEBUG_RTD:
    html_css_files = [
        "https://assets.readthedocs.org/static/css/readthedocs-doc-embed.css",
        "https://assets.readthedocs.org/static/css/badge_only.css",
    ]
    html_js_files = [
        "https://docs.authlib.org/en/latest/_static/jquery.js",
        "rtd-dummy.js",
        (
            "https://assets.readthedocs.org/static/javascript/readthedocs-doc-embed.js",
            {"async": "async"},
        ),
    ]
    html_context["READTHEDOCS"] = True
    html_context["current_version"] = "latest"
