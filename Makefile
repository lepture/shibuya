build-docs:
	sphinx-build docs build/_html -a -b dirhtml

build-icons:
	node scripts/genicons.js
