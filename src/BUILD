load(
    "@shuffled_deps//:requirements.bzl",
    "requirement",
)

py_library(
    name = "shuffled",
    srcs = glob(["**/*.py"]),
    imports = ["."],
    deps = [
        requirement("cryptography"),
    ],
    visibility = ["//visibility:public"],
)
