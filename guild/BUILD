package(default_visibility = ["//visibility:public"])

sh_binary(
    name = "guild",
    srcs = ["//guild/scripts:guild"],
    data = [
        ":main_bootstrap",
        "//guild/plugins",
    ]
)

py_library(
    name = "__init__",
    srcs = ["__init__.py"],
)

py_library(
    name = "cli",
    srcs = ["cli.py"],
    deps = [
        "//third_party:click",
    ],
)

py_library(
    name = "click_util",
    srcs = ["click_util.py"],
    deps = [
        "//third_party:click",
    ]
)

py_library(
    name = "cmd_impl_support",
    srcs = ["cmd_impl_support.py"],
    deps = [
        ":cli",
        ":click_util",
        ":config",
        ":model",
        ":modelfile",
        ":resource",
    ],
)

py_library(
    name = "config",
    srcs = ["config.py"],
    deps = [
    ],
)

py_library(
    name = "deps",
    srcs = ["deps.py"],
    deps = [
        ":namespace",
        ":resolve",
        ":resource",
        ":util",
    ],
)

py_library(
    name = "entry_point_util",
    srcs = ["entry_point_util.py"],
    deps = [
        "//third_party:setuptools",
    ],
)

py_library(
    name = "help",
    srcs = ["help.py"],
    deps = [
        "//third_party:click",
    ],
)

py_library(
    name = "index",
    srcs = ["index.py"],
    deps = [
        "//third_party:tensorboard",
        "//third_party:whoosh",
        ":opref",
        ":util",
        ":var",
    ],
)

py_library(
    name = "log",
    srcs = ["log.py"],
    deps = [
    ],
)

py_library(
    name = "main",
    srcs = ["main.py"],
    deps = [
        "//third_party:click",
        ":click_util",
        "//guild/commands:main",
    ]
)

py_library(
    name = "main_bootstrap",
    srcs = ["main_bootstrap.py"],
    deps = [
        ":main",
    ]
)

py_library(
    name = "model",
    srcs = ["model.py"],
    deps = [
        "//third_party:setuptools",
        ":config",
        ":entry_point_util",
        ":modelfile",
        ":namespace",
        ":resource",
    ]
)

py_library(
    name = "modelfile",
    srcs = ["modelfile.py"],
    deps = [
        "//third_party:yaml",
        ":plugin",
        ":resourcedef",
        ":util",
    ]
)

py_library(
    name = "namespace",
    srcs = ["namespace.py"],
    deps = [
        ":__init__",
        ":entry_point_util",
    ],
)

py_library(
    name = "op",
    srcs = ["op.py"],
    deps = [
        ":deps",
        ":opref",
        ":plugin",
        ":run",
        ":util",
        ":var",
    ],
    data = [
        ":op_main",
    ],
)

py_library(
    name = "op_main",
    srcs = ["op_main.py"],
    deps = [
        ":log",
        ":plugin",
    ],
)

py_library(
    name = "opref",
    srcs = ["opref.py"],
    deps = [
    ],
)

py_library(
    name = "package",
    srcs = ["package.py"],
    deps = [
        "//third_party:yaml",
        ":namespace",
        ":package_main",
        ":resource",
        ":resourcedef",
        ":util",
    ],
)

py_library(
    name = "package_main",
    srcs = ["package_main.py"],
    deps = [
        "//third_party:setuptools",
        "//third_party:twine",
        "//third_party:yaml",
        ":modelfile",
        ":namespace",
        ":util",
    ],
)

py_library(
    name = "pip_util",
    srcs = ["pip_util.py"],
    deps = [
        "//third_party:pip",
        ":cli",
        ":namespace",
    ],
)

py_library(
    name = "plugin",
    srcs = ["plugin.py"],
    deps = [
        ":entry_point_util",
    ],
)

py_library(
    name = "plugin_util",
    srcs = ["plugin_util.py"],
    deps = [
        ":run",
    ],
)

py_library(
    name = "resolve",
    srcs = ["resolve.py"],
    deps = [
        ":opref",
        ":pip_util",
        ":util",
        ":var",
    ],
)

py_library(
    name = "resource",
    srcs = ["resource.py"],
    deps = [
        ":entry_point_util",
        ":namespace",
    ],
)

py_library(
    name = "resourcedef",
    srcs = ["resourcedef.py"],
    deps = [
        ":resolve",
        ":util",
    ],
)

py_library(
    name = "run",
    srcs = ["run.py"],
    deps = [
         ":util",
    ],
)

py_library(
    name = "tabview",
    srcs = ["tabview.py"],
    deps = [
        "//third_party:tabview",
    ],
)

py_library(
    name = "tensorboard",
    srcs = ["tensorboard.py"],
    deps = [
        "//third_party:setuptools",
        "//third_party:tensorboard",
        "//third_party:tensorflow",
        "//third_party:werkzeug",
    ],
)

py_library(
    name = "test",
    srcs = ["test.py"],
    data = [
        "//guild/tests",
    ],
    deps = [
        ":util",
    ],
)

py_library(
    name = "uat",
    srcs = ["uat.py"],
    deps = [
        ":test",
    ],
    data = [
        "//guild/tests/uat"
    ],
)

py_library(
    name = "util",
    srcs = ["util.py"],
    deps = [
    ],
)

py_library(
    name = "var",
    srcs = ["var.py"],
    deps = [
        ":config",
        ":run",
        ":util",
    ],
)
