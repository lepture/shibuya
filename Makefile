build-docs:
	sphinx-build docs build/_html -b dirhtml

build-icons:
	node scripts/genicons.js
