import re


BASE_CSS_VARIABLES = """
--sy-f-sys: -apple-system, BlinkMacSystemFont, Segoe UI, Oxygen, Ubuntu, Droid Sans, Helvetica Neue;
--sy-f-cjk: PingFang SC, Hiragino Sans GB, Droid Sans Fallback, Microsoft YaHei;
--sy-f-heading: var(--sy-f-sys), var(--sy-f-cjk), sans-serif;
--sy-f-text: var(--sy-f-sys), var(--sy-f-cjk), sans-serif;
--sy-f-mono: Menlo, Monaco, Consolas, "Courier New", monospace;
--sy-c-divider: rgba(var(--sy-rc-text), 0.1);
--sy-c-divider-weak: rgba(var(--sy-rc-text), 0.05);
--sy-c-border: rgba(var(--sy-rc-text), 0.14);
--sy-s-banner-height: 0rem;
--sy-s-navbar-height: 4rem;
--sy-s-offset-top: calc(var(--sy-s-navbar-height) + var(--sy-s-banner-height));
--sy-rc-link: var(--sy-rc-theme);
--sy-c-link: rgb(var(--sy-rc-theme));
"""

LIGHT_CSS_VARIABLES = """
--sy-rc-theme: 143, 118, 214;
--sy-rc-bg: 255, 255, 255;
--sy-rc-invert: 0, 0, 0;
--sy-rc-text: 0, 0, 0;
--sy-c-bg: #fff;
--sy-c-bg-weak: #f9f9f9;
--sy-c-text: #374151;
--sy-c-text-weak: #6b7280;
--sy-c-text-strong: #111;
--sy-c-heading: #111827;
--sy-c-bold: #111827;
--sy-c-pre-bg: rgba(143, 118, 214, 0.06);
--sy-c-cap-bg: rgba(143, 118, 214, 0.1);
--sy-c-foot-text: #232226;
--sy-c-foot-bg: #fafafa;
--sy-c-foot-divider: #f0f0f0;
"""

DARK_CSS_VARIABLES = """
--sy-rc-theme: 143, 118, 214;
--sy-rc-bg: 18, 18, 18;
--sy-rc-invert: 255, 255, 255;
--sy-rc-text: 255, 255, 255;
--sy-c-bg: #121212;
--sy-c-bg-weak: #212833;
--sy-c-text: #a9b9cc;
--sy-c-text-weak: #77889f;
--sy-c-text-strong: #d9ebfd;
--sy-c-heading: #fff;
--sy-c-bold: #fff;
--sy-c-pre-bg: rgba(143, 118, 214, 0.16);
--sy-c-cap-bg: rgba(143, 118, 214, 0.24);
--sy-c-foot-text: #eee;
--sy-c-foot-bg: #000;
--sy-c-foot-divider: #000;
"""

def css_to_dict(text: str):
    css_vars = {}
    for line in text.strip().splitlines():
        if not line:
            continue
        line = line.rstrip(";")
        key, value = line.split(':')
        css_vars[key.strip()] = value.strip()
    return css_vars


def normalize_pageurl(pageurl: str, builder: str):
    if pageurl.endswith('/index.html'):
        return re.sub(r'index\.html$', '', pageurl)
    if builder == 'dirhtml' and pageurl.endswith('.html'):
        return re.sub(r'\.html$', '/', pageurl)
    return pageurl


def normalize_toc(toc: str):
    toc = re.sub(r'^<ul>\n<li>.*?</a>', '', toc)
    toc = re.sub(r'</li>\n</ul>$', '', toc)
    return toc
