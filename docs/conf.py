
project = "Shibuya"
release = "1.0.0"
copyright = "Copyright &copy; 2023, Hsiaoming Yang"
author = "Hsiaoming Yang"

extensions = [
    "sphinx.ext.extlinks",
    "sphinx.ext.todo",
]
todo_include_todos = True

html_theme = "shibuya"
html_baseurl = "https://shibuya.lepture.com"
html_logo = "https://typlog.com/assets/logo-black.svg"

html_theme_options = {
    "logo_target": "/",
    "light_logo": "https://typlog.com/assets/logo-black.svg",
    "dark_logo": "https://typlog.com/assets/logo-white.svg",

    "twitter_url": "https://twitter.com/lepture",
    "github_url": "https://github.com/lepture/shibuya",

    "nav_links": [
        {
            "title": "Pricing",
            "url": "/pricing.html"
        },
        {
            "title": "About",
            "url": "/about.html"
        },
    ]
}
