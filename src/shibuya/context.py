BASE_CSS_VARIABLES = """
--sy-f-sys: -apple-system, BlinkMacSystemFont, Segoe UI, Oxygen, Ubuntu, Droid Sans, Helvetica Neue;
--sy-f-latin: Inter, var(--sy-f-sys);
--sy-f-cjk: PingFang SC, Hiragino Sans GB, Droid Sans Fallback, Microsoft YaHei;
--sy-f-heading: var(--sy-f-latin), var(--sy-f-cjk), sans-serif;
--sy-f-text: var(--sy-f-latin), var(--sy-f-cjk), sans-serif;
--sy-c-divider: rgba(var(--sy-rc-text), 0.1);
--sy-c-divider-weak: rgba(var(--sy-rc-text), 0.05);
--sy-s-navbar-height: 4rem;
--sy-rc-link: var(--sy-rc-theme);
--sy-c-link: rgb(var(--sy-rc-theme));
"""

LIGHT_CSS_VARIABLES = """
--sy-rc-theme: 143, 118, 214;
--sy-rc-bg: 255, 255, 255;
--sy-rc-text: 0, 0, 0;
--sy-c-bg: #fff;
--sy-c-bg-weak: #f9f9f9;
--sy-c-text: #374151;
--sy-c-text-weak: #6b7280;
--sy-c-heading: #111827;
--sy-c-bold: #111827;
--sy-c-bg-pre: rgba(var(--sy-rc-theme), 0.06);
--sy-c-bg-cap: rgba(var(--sy-rc-theme), 0.1);
--sy-c-foot-text: #232226;
--sy-c-foot-bg: #f1f1f1;
"""

DARK_CSS_VARIABLES = """
--sy-rc-theme: 143, 118, 214;
--sy-rc-bg: 18, 18, 18;
--sy-rc-bg-pre: 23, 29, 36;
--sy-rc-text: 255, 255, 255;
--sy-c-bg: rgba(var(--sy-rc-bg), 0.86);
--sy-c-bg-weak: #243144;
--sy-c-text: #d1d5db;
--sy-c-text-weak: #8d91a7;
--sy-c-heading: #fff;
--sy-c-bold: #fff;
--sy-c-bg-pre: rgba(var(--sy-rc-theme), 0.06);
--sy-c-bg-cap: rgba(var(--sy-rc-theme), 0.1);
--sy-c-foot-text: #eee;
--sy-c-foot-bg: #000;
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
