SRC=benchmark src tests

.PHONY: check-format
check-format:
	ruff check --select I ${SRC}
	ruff format --diff ${SRC}

.PHONY: check-tests
check-tests:
	pytest --cov=src --cov-report=term --cov-report=html tests

.PHONY: check-lint
check-lint:
	pyrefly check ${SRC}
	ruff check --ignore I ${SRC}

.PHONY: check
check: | check-lint check-tests check-format

.PHONY: format
format:
	ruff check --select I --fix ${SRC}
	ruff format ${SRC}

.PHONY: benchmark
benchmark:
	pytest benchmark
