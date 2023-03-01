build-docs:
	sphinx-build docs build/_html -b dirhtml -a

build-icons:
	node scripts/genicons.js

build-static:
	npm run build
