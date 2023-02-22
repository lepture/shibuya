
project = "Shibuya"
release = "1.0.0"
copyright = "Copyright &copy; 2023, Hsiaoming Yang"
author = "Hsiaoming Yang"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
]
todo_include_todos = True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

templates_path = ["_templates"]
html_static_path = ["_static"]

html_theme = "shibuya"
html_baseurl = "https://shibuya.lepture.com"

html_copy_source = False
html_show_sourcelink = False

html_additional_pages = {
    "branding": "branding.html",
}

# html_link_suffix = ""

# html_logo = "_static/logo-light.svg"

html_theme_options = {
    "logo_target": "/",
    "light_logo": "_static/logo-light.svg",
    "dark_logo": "_static/logo-dark.svg",

    "twitter_url": "https://twitter.com/lepture",
    "github_url": "https://github.com/lepture/shibuya",

    "nav_links": [
        {
            "title": "Branding",
            "url": "/branding"
        },
    ]
}

html_context = {}

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
