import os
import sys
import shibuya

# for example source
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "example_code"))

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
    "sphinx.ext.autosummary",
    "sphinx_copybutton",
    "sphinx_design",
    "myst_parser",
    "jupyter_sphinx",
    "sphinx_togglebutton",
    "nbsphinx",
    "numpydoc",
    "sphinx_sitemap",
    "sphinxcontrib.mermaid",
    "sphinx_sqlalchemy",
]
todo_include_todos = True
autosummary_generate = True
jupyter_sphinx_thebelab_config = {
    'requestKernel': True,
}
jupyter_sphinx_require_url = ''
nbsphinx_requirejs_path = ''

extlinks = {
    'pull': ('https://github.com/lepture/shibuya/pull/%s', 'pull request #%s'),
    'issue': ('https://github.com/lepture/shibuya/issues/%s', 'issue #%s'),
}

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
    "numpy": ("https://numpy.org/devdocs/", None),
}

templates_path = ["_templates"]
html_static_path = ["_static"]
html_extra_path = ["_public"]

html_title = "Shibuya"
html_theme = "shibuya"
html_baseurl = "https://shibuya.lepture.com/"
sitemap_url_scheme = "{link}"

html_copy_source = False
html_show_sourcelink = False

html_additional_pages = {
    "branding": "branding.html",
}

if os.getenv('USE_DOCSEARCH'):
    extensions.append("sphinx_docsearch")
    docsearch_app_id = "3RU4IG0D1E"
    docsearch_api_key = "ec63fbf7ade2fa535b0b82c86e7d1463"
    docsearch_index_name = "shibuya-lepture"

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

    "discussion_url": "https://github.com/lepture/shibuya/discussions",
    "twitter_url": "https://twitter.com/lepture",
    "github_url": "https://github.com/lepture/shibuya",

    "carbon_ads_code": "CE7DKK3W",
    "carbon_ads_placement": "shibuya",

    "globaltoc_expand_depth": 1,
    "nav_links": [
        {
            "title": "Examples",
            "url": "writing",
            "children": [
                {
                    "title": "Admonitions",
                    "url": "writing/admonition",
                    "summary": "Bring the attention of readers",
                },
                {
                    "title": "Code Blocks",
                    "url": "writing/code",
                    "summary": "Display code with highlights",
                },
                {
                    "title": "Autodoc",
                    "url": "writing/api",
                    "summary": "API documentation automatically"
                },
                {
                    "title": "Jupyter Notebook",
                    "url": "extensions/nbsphinx",
                    "summary": "Rendering .ipynb files"
                },
            ]
        },
        {
            "title": "Branding",
            "url": "branding",
        },
        {
            "title": "Sponsor me",
            "url": "https://github.com/sponsors/lepture",
            "external": True,
        },
    ]
}

if "READTHEDOCS" in os.environ:
    html_theme_options["carbon_ads_code"] = ""
    html_theme_options["announcement"] = (
        "This documentation is hosted on Read the Docs only for testing. Please use "
        "<a href='https://shibuya.lepture.com/'>the main documentation</a> instead."
    )
else:
    html_context = {
        "source_type": "github",
        "source_user": "lepture",
        "source_repo": "shibuya",
    }


DEBUG_RTD = False

if DEBUG_RTD:
    os.environ['READTHEDOCS_PROJECT'] = 'shibuya'
    os.environ['READTHEDOCS_VERSION'] = 'latest'
    html_context["READTHEDOCS"] = True
    html_context["slug"] = "shibuya"
    html_css_files = [
        "https://assets.readthedocs.org/static/css/readthedocs-doc-embed.css",
        "https://assets.readthedocs.org/static/css/badge_only.css",
    ]
    html_js_files = [
        "rtd-dummy.js",
        (
            "https://assets.readthedocs.org/static/javascript/readthedocs-doc-embed.js",
            {"async": "async"},
        ),
    ]

    html_theme_options["carbon_ads_code"] = None
    html_context["current_version"] = "latest"
    html_context["versions"] = [
        ("latest", "/en/latest/"),
        ("stable", "/en/stable/"),
        ("v3", "/en/v3/"),
        ("v2.0.5", "/en/v2.0.5/"),
        ("v2.0.4", "/en/v2.0.4/"),
        ("v2", "/en/v2/"),
        ("v0.8.4", "/en/v0.8.4/"),
    ]
    html_context["languages"] = [
        ("🇺🇸 English", "/en/%s/", "en"),
        ("🇨🇳 中文", "/zh/%s/", "zh"),
    ]
