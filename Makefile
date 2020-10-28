SRC=src tests

.PHONY: check-format
check-format:
	black --check ${SRC}

.PHONY: check-tests
check-tests:
	pytest --cov=src --cov-report=term --cov-report=html

.PHONY: check-lint
check-lint:
	mypy ${SRC}
	flake8 ${SRC}

.PHONY: check
check: | check-lint check-tests check-format

.PHONY: format
format:
	black ${SRC}
