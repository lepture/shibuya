build-docs:
	sphinx-build docs build/_html -b dirhtml -a

build-icons:
	node scripts/genicons.js

build-static:
	cd static && npm run build

babel-extract:
	pybabel extract -F babel.cfg src/shibuya/theme -o src/shibuya/locale/sphinx.pot

lang=zh

babel-init:
	pybabel init -D sphinx -i src/shibuya/locale/sphinx.pot -d src/shibuya/locale -l ${lang}

babel-update:
	pybabel update -D sphinx -i src/shibuya/locale/sphinx.pot -d src/shibuya/locale -l ${lang}

babel-compile:
	pybabel compile -D sphinx -d src/shibuya/locale
