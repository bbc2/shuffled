SRC=setup.py src tests

.PHONY: check-format
check-format:
	black --check ${SRC}

.PHONY: check-tests
check-tests:
	nosetests --with-coverage --cover-erase --cover-html --cover-package src tests

.PHONY: check
check: | check-tests check-format

.PHONY: format
format:
	black ${SRC}
