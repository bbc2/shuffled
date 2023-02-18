SRC=benchmark src tests

.PHONY: check-format
check-format:
	ruff check --select I ${SRC}
	black --check ${SRC}

.PHONY: check-tests
check-tests:
	pytest --cov=src --cov-report=term --cov-report=html tests

.PHONY: check-lint
check-lint:
	mypy --python-version 3.10 ${SRC}
	mypy --python-version 3.7 ${SRC}
	ruff check --ignore I ${SRC}

.PHONY: check
check: | check-lint check-tests check-format

.PHONY: format
format:
	ruff check --select I --fix ${SRC}
	black ${SRC}

.PHONY: benchmark
benchmark:
	pytest benchmark
