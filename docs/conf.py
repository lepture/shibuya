
project = "Shibuya"
copyright = "Copyright &copy; 2023, Hsiaoming Yang"
author = "Hsiaoming Yang"

extensions = [
    "sphinx.ext.extlinks",
    "sphinx.ext.todo",
]

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
