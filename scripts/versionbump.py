import re
import datetime


def create_version():
    today = datetime.date.today()
    numbers = [today.year, today.month, today.day]
    return ".".join(str(i) for i in numbers)


def replace_version(version):
    filepath = "src/shibuya/__init__.py"

    with open(filepath, "r") as f:
        content = f.read()
        code = re.sub(r'__version__ = "[^"]+"', f'__version__ = "{version}"', content)

    with open(filepath, "w") as f:
        f.write(code)


def bump():
    version = create_version()
    replace_version(version)


bump()
