SRC=setup.py src tests

.PHONY: check-format
check-format:
	black --check ${SRC}

.PHONY: check-tests
check-tests:
	pytest --cov=src --cov-report=term --cov-report=html

.PHONY: check
check: | check-tests check-format

.PHONY: format
format:
	black ${SRC}
