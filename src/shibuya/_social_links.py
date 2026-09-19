from typing import Dict, Literal, Any


DEFAULT_SOCIALS_DICT = {
    "github": {
        "name": "GitHub",
        "icon": "simple-icons:github",
    },
    "gitlab": {
        "name": "GitLab",
        "icon": "simple-icons:gitlab",
    },
    "bitbucket": {
        "name": "Bitbucket",
        "icon": "simple-icons:bitbucket",
    },
    "x": {
        "name": "X (Twitter)",
        "icon": "simple-icons:x",
    },
    "bluesky": {
        "name": "Bluesky",
        "icon": "simple-icons:bluesky",
    },
    "mastodon": {
        "name": "Mastodon",
        "icon": "simple-icons:mastodon",
    },
    "slack": {
        "name": "Slack",
        "icon": "simple-icons:slack",
    },
    "discord": {
        "name": "Discord",
        "icon": "simple-icons:discord",
    },
    "youtube": {
        "name": "YouTube",
        "icon": "simple-icons:youtube",
    },
    "reddit": {
        "name": "Reddit",
        "icon": "simple-icons:reddit",
    },
    "linkedin": {
        "name": "LinkedIn",
        "icon": "simple-icons:linkedin",
    },
    "readthedocs": {
        "name": "Read the Docs",
        "icon": "simple-icons:readthedocs",
    },
}

DEFAULT_NAV_SOCIALS = [
    "github",
    "gitlab",
    "bitbucket",
    "x",
    "bluesky",
    "mastodon",
    "slack",
    "discord",
    "youtube",
    "reddit",
    "linkedin",
]

DEFAULT_FOOT_SOCIALS = ["readthedocs"] + DEFAULT_NAV_SOCIALS

DEFAULT_SOCIALS = {
    "theme_nav_socials": DEFAULT_NAV_SOCIALS,
    "theme_foot_socials": DEFAULT_FOOT_SOCIALS,
}


def patch_social_context(context: Dict[str, Any]) -> None:
    # patch twitter url
    twitter_url = context.get("theme_twitter_url")
    x_url = context.get("theme_x_url")
    if twitter_url and not x_url:
        context["theme_x_url"] = twitter_url

    # extends social links
    context["theme_nav_socials"] = list(_fix_social_links(context, "theme_nav_socials"))
    context["theme_foot_socials"] = list(_fix_social_links(context, "theme_foot_socials"))


def _fix_social_links(context: Dict[str, Any], key: Literal["theme_nav_socials", "theme_foot_socials"]):
    fields = context.get(key)
    if not fields and not isinstance(fields, list):
        fields = DEFAULT_SOCIALS[key]

    for data in fields:
        social_link = _normalize_social_link(data, context)
        if social_link:
            yield social_link


def _normalize_social_link(data: Any, context: Dict[str, Any]):
    if isinstance(data, str):
        url = context.get(f"theme_{data}_url")
        if url:
            social = DEFAULT_SOCIALS_DICT.get(data, {})
            name = context.get(f"theme_{data}_name") or social.get("name", data.title())
            icon = context.get(f"theme_{data}_icon") or social.get("icon", f"simple-icons:{data}")
            return dict(name=name, icon=icon, url=url)
    elif isinstance(data, dict):
        if "name" in data and "url" in data and "icon" in data:
            return data
