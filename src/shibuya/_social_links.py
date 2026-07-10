from typing import Dict, Literal, Any


SOCIAL_LABELS = {
    "x": "X (Twitter)",
    "github": "GitHub",
    "youtube": "YouTube",
}

DEFAULT_NAV_SOCIALS = DEFAULT_FOOT_SOCIALS = [
    "readthedocs",
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
    if not fields:
        fields = DEFAULT_SOCIALS[key]

    for data in fields:
        social_link = _normalize_social_link(data, context)
        if social_link:
            yield social_link


def _normalize_social_link(data: Any, context: Dict[str, Any]):
    if isinstance(data, str):
        url = context.get(f"theme_{data}_url")
        if url:
            name = SOCIAL_LABELS.get(data, data.title())
            return dict(icon=f"simple-icons:{data}", url=url, name=name)
    elif isinstance(data, dict):
        if "name" in data and "url" in data and "icon" in data:
            return data
