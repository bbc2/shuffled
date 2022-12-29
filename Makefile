SRC=benchmark src tests

.PHONY: check-format
check-format:
	black --check ${SRC}

.PHONY: check-tests
check-tests:
	pytest --cov=src --cov-report=term --cov-report=html tests

.PHONY: check-lint
check-lint:
	mypy --python-version 3.10 ${SRC}
	mypy --python-version 3.7 ${SRC}
	flake8 ${SRC}

.PHONY: check
check: | check-lint check-tests check-format

.PHONY: format
format:
	black ${SRC}

.PHONY: benchmark
benchmark:
	pytest benchmark
