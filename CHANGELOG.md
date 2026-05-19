# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog], and this project adheres to [Semantic
Versioning].

## [Unreleased]

- Drop support for Python 3.7, Python 3.8 and PyPy3.8.
- Add tests with Python 3.14 and PyPy3.11.
- Improve performance by reducing the AES plaintext size. Note: this changes the
  ordering of integers for existing seeds, which may be a breaking change depending
  on the use case.
- Add support for negative indexes.
- Add support for slices.

## [1.1.0] - 2022-12-29

- Improve performance.

## [1.0.2] - 2022-06-18

- Drop support for Python 3.5, 3.6 and PyPy3.6.
- Add tests with Python 3.10 and PyPy3.8.

## [1.0.1] - 2020-10-28

- Fix release script.

## [1.0.0] - 2020-10-28

- Drop support for Python 2.7 and 3.4
- Add type hints

## [0.2] - 2016-10-09

- Add support for Python 2

## [0.1] - 2016-08-06

- Initial public release

  [Keep a Changelog]: https://keepachangelog.com/en/1.0.0/
  [Semantic Versioning]: https://semver.org/spec/v2.0.0.html
  [Unreleased]: https://github.com/bbc2/shuffled/compare/1.1.0...main
  [1.1.0]: https://github.com/bbc2/shuffled/compare/1.0.2...1.1.0
  [1.0.2]: https://github.com/bbc2/shuffled/compare/1.0.1...1.0.2
  [1.0.1]: https://github.com/bbc2/shuffled/compare/1.0.0...1.0.1
  [1.0.0]: https://github.com/bbc2/shuffled/compare/v0.2...1.0.0
  [0.2]: https://github.com/bbc2/shuffled/compare/v0.1...v0.2
  [0.1]: https://github.com/bbc2/shuffled/tree/v0.1
