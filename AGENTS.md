# Guide for AI Agents

Shibuya is a clean, responsive, and customizable Sphinx documentation theme with light/dark mode.
With great support for Jupyter extensions and AI-related features. It is built on top of the popular
Sphinx documentation generator and is compatible with Python 3.10 and above.

## Project Structure

```
shibuya/
├── LICENSE
├── AGENTS.md
├── README.md
├── pyproject.toml
├── src/
│   └── shibuya/
│       ├── locale/       # Locale files using gettext
│       ├── theme/
│       │   └── shibuya/  # Theme files in Jinja templates
│       ├── __init__.py
│       └── sponsors.py
└── docs/                 # Documentation files using reStructuredText
```

## Build documentation

Install all the dependencies using uv:

```
uv sync
```

Then build the documentation using Sphinx:

```
uv run sphinx-build docs build/_html
```

## Translations

Shibuya is a Sphinx theme, Sphinx is using gettext for translations. Shibuya uses the same approach.
All localizations are stored in the `src/shibuya/locale` directory. To add a new language, using
`pybabel` to extract the messages:

```
pybabel extract -F babel.cfg src/shibuya/theme -o src/shibuya/locale/sphinx.pot
```

Initialize the translation file:

```
pybabel init -D sphinx -i src/shibuya/locale/sphinx.pot -d src/shibuya/locale -l <language>
```

Then the new language `.po` file will be created in the `src/shibuya/locale/<language>/LC_MESSAGES` 
directory. Translate the messages in the `.po` file and compile it:

```
pybabel compile -D sphinx -d src/shibuya/locale
```
