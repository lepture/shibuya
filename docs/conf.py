
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

html_theme = "shibuya"
html_baseurl = "https://shibuya.lepture.com"

html_static_path = ["_static"]

html_copy_source = False
html_show_sourcelink = False

# html_link_suffix = ""

html_theme_options = {
    "logo_target": "/",
    "light_logo": "/_static/logo-light.svg",
    "dark_logo": "/_static/logo-dark.svg",

    "twitter_url": "https://twitter.com/lepture",
    "github_url": "https://github.com/lepture/shibuya",

    "nav_links": [
        {
            "title": "Sponsors",
            "url": "/sponsors"
        },
        {
            "title": "About",
            "url": "/about"
        },
    ]
}
