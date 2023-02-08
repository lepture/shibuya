BASE_CSS_VARIABLES = """
--sy-f-sys: -apple-system, BlinkMacSystemFont, Segoe UI, Oxygen, Ubuntu, Droid Sans, Helvetica Neue;
--sy-f-latin: Inter, var(--sy-f-sys);
--sy-f-cjk: PingFang SC, Hiragino Sans GB, Droid Sans Fallback, Microsoft YaHei;
--sy-f-heading: var(--sy-f-latin), var(--sy-f-cjk), sans-serif;
--sy-f-text: var(--sy-f-latin), var(--sy-f-cjk), sans-serif;
--sy-c-text: rgba(var(--sy-rc-text), 0.86);
--sy-c-divider: var(--sy-rc-text, 0.1);
"""

LIGHT_CSS_VARIABLES = """
--sy-rc-bg: 255, 255, 255;
--sy-rc-text: 0, 0, 0;
--sy-c-bg: #fff;
--sy-c-bg-weak: #f9f9f9;
"""

DARK_CSS_VARIABLES = """
--sy-rc-bg: 18, 18, 18;
--sy-rc-text: 255, 255, 255;
--sy-c-bg: rgba(var(--sy-rc-bg), 0.86);
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
