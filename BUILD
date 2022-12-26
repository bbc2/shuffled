load(
    "@shuffled_deps//:requirements.bzl",
    "requirement",
)

py_test(
    name = "runtests",
    srcs = (
        ["runtests.py"]
        + glob(["tests/**/*.py"])
    ),
    deps = [
        "//src:shuffled",
        requirement("pytest"),
        requirement("pytest-cov"),
    ],
)
