package(default_visibility = ["//visibility:public"])

py_library(
    name = "check",
    srcs = ["check.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":check_impl",
    ],
)

py_library(
    name = "check_impl",
    srcs = ["check_impl.py"],
    deps = [
        "//third_party:click",
        "//third_party:setuptools",
        "//guild:__init__",
        "//guild:cli",
        "//guild:plugin",
        "//guild:test",
        "//guild:uat",
        "//guild:util",
        ":tensorflow_info_main",
    ],
)

py_library(
    name = "compare",
    srcs = ["compare.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":compare_impl",
        ":runs_support",
    ],
)

py_library(
    name = "compare_impl",
    srcs = ["compare_impl.py"],
    deps = [
        "//guild:index",
        "//guild:tabview",
        "//guild:util",
        "//guild:var",
        ":runs_impl",
    ],
)

py_library(
    name = "help",
    srcs = ["help.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":help_impl",
    ],
)

py_library(
    name = "help_impl",
    srcs = ["help_impl.py"],
    deps = [
        "//third_party:click",
        "//guild:cli",
        "//guild:cmd_impl_support",
        "//guild:config",
        "//guild:help",
        "//guild:model",
        "//guild:modelfile",
    ],
)

py_library(
    name = "index",
    srcs = ["index.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":index_impl",
    ],
)

py_library(
    name = "index_impl",
    srcs = ["index_impl.py"],
    deps = [
        "//guild:cli",
        "//guild:index",
    ],
)

py_library(
    name = "install",
    srcs = ["install.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":packages_impl",
    ],
)

py_library(
    name = "label",
    srcs = ["label.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":label_impl",
    ],
)

py_library(
    name = "label_impl",
    srcs = ["label_impl.py"],
    deps = [
        "//third_party:click",
        "//guild:cmd_impl_support",
        "//guild:run",
        "//guild:var",
    ],
)

py_library(
    name = "main",
    srcs = ["main.py"],
    deps = [
        "//third_party:click",
        "//guild:__init__",
        "//guild:click_util",
        ":check",
        ":compare",
        ":help",
        ":index",
        ":install",
        ":models",
        ":operations",
        ":package",
        ":packages",
        ":resources",
        ":run",
        ":runs",
        ":search",
        ":shell",
        ":sync",
        ":tensorboard",
        ":train",
        ":uninstall",
    ]
)

py_library(
    name = "main_impl",
    srcs = ["main_impl.py"],
    deps = [
        "//guild:cli",
        "//guild:config",
        "//guild:log",
    ]
)

py_library(
    name = "models",
    srcs = ["models.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":models_impl",
    ],
)

py_library(
    name = "models_impl",
    srcs = ["models_impl.py"],
    deps = [
        "//guild:cli",
        "//guild:cmd_impl_support",
        "//guild:util",
    ],
)

py_library(
    name = "operations",
    srcs = ["operations.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":operations_impl",
    ],
)

py_library(
    name = "operations_impl",
    srcs = ["operations_impl.py"],
    deps = [
        "//guild:cli",
        "//guild:cmd_impl_support",
        "//guild:util",
    ],
)

py_library(
    name = "package",
    srcs = ["package.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":package_impl",
    ],
)

py_library(
    name = "package_impl",
    srcs = ["package_impl.py"],
    deps = [
        "//guild:cmd_impl_support",
        "//guild:config",
        "//guild:namespace",
        "//guild:package",
    ],
)

py_library(
    name = "packages",
    srcs = ["packages.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":packages_delete",
        ":packages_info",
        ":packages_list",
    ],
)

py_library(
    name = "packages_delete",
    srcs = ["packages_delete.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":packages_impl",
    ],
)

py_library(
    name = "packages_impl",
    srcs = ["packages_impl.py"],
    deps = [
        "//guild:cli",
        "//guild:cmd_impl_support",
        "//guild:package",
        "//guild:pip_util",
        "//guild:util",
    ],
)

py_library(
    name = "packages_info",
    srcs = ["packages_info.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":packages_impl",
    ],
)

py_library(
    name = "packages_list",
    srcs = ["packages_list.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":packages_impl",
    ],
)

py_library(
    name = "resources",
    srcs = ["resources.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":resources_impl",
    ],
)

py_library(
    name = "resources_impl",
    srcs = ["resources_impl.py"],
    deps = [
        "//guild:cli",
        "//guild:cmd_impl_support",
        "//guild:resource",
        "//guild:util",
    ],
)

py_library(
    name = "run",
    srcs = ["run.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":run_impl",
    ],
)

py_library(
    name = "run_impl",
    srcs = ["run_impl.py"],
    deps = [
        "//guild:cli",
        "//guild:cmd_impl_support",
        "//guild:deps",
        "//guild:model",
        "//guild:opref",
    ],
)

py_library(
    name = "runs",
    srcs = ["runs.py"],
    deps = [
        "//third_party:click",
        "//guild:cli",
        "//guild:click_util",
        ":runs_delete",
        ":runs_info",
        ":runs_list",
        ":runs_purge",
        ":runs_restore",
        ":runs_support",
    ],
)

py_library(
    name = "runs_delete",
    srcs = ["runs_delete.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":runs_impl",
        ":runs_support",
    ],
)

py_library(
    name = "runs_impl",
    srcs = ["runs_impl.py"],
    deps = [
        "//guild:cli",
        "//guild:cmd_impl_support",
        "//guild:config",
        "//guild:opref",
        "//guild:run",
        "//guild:util",
        "//guild:var",
    ],
)

py_library(
    name = "runs_info",
    srcs = ["runs_info.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":runs_impl",
        ":runs_support",
    ],
)

py_library(
    name = "runs_list",
    srcs = ["runs_list.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":runs_impl",
        ":runs_support",
    ],
)

py_library(
    name = "runs_purge",
    srcs = ["runs_purge.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":runs_impl",
        ":runs_support",
    ],
)

py_library(
    name = "runs_restore",
    srcs = ["runs_restore.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":runs_impl",
        ":runs_support",
    ],
)

py_library(
    name = "runs_support",
    srcs = ["runs_support.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
    ],
)

py_library(
    name = "search",
    srcs = ["search.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":search_impl",
    ],
)

py_library(
    name = "search_impl",
    srcs = ["search_impl.py"],
    deps = [
        "//guild:cli",
        "//guild:namespace",
        "//guild:package",
        "//guild:pip_util",
    ],
)

py_library(
    name = "shell",
    srcs = ["shell.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":shell_impl",
    ],
)

py_library(
    name = "shell_impl",
    srcs = ["shell_impl.py"],
    deps = [
        "//guild:util",
    ],
)

py_library(
    name = "sync",
    srcs = ["sync.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":runs_support",
        ":sync_impl",
    ],
)

py_library(
    name = "sync_impl",
    srcs = ["sync_impl.py"],
    deps = [
        "//guild:cli",
        "//guild:plugin",
        ":runs_impl",
    ],
)

py_library(
    name = "tensorboard",
    srcs = ["tensorboard.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":runs_support",
        ":tensorboard_impl",
    ],
)

py_library(
    name = "tensorboard_impl",
    srcs = ["tensorboard_impl.py"],
    deps = [
        "//guild:cli",
        "//guild:tensorboard",
        "//guild:util",
        ":runs_impl",
    ],
)
py_library(
    name = "train",
    srcs = ["train.py"],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":run",
    ],
)

py_library(
    name = "tensorflow_info_main",
    srcs = ["tensorflow_info_main.py"],
    deps = [
        "//third_party:click",
        # Does not depend on //third_party:tensorflow as it
        # handles cases where TF is not installed.
    ],
)

py_library(
    name = "uninstall",
    srcs = [
        "uninstall.py",
    ],
    deps = [
        "//third_party:click",
        "//guild:click_util",
        ":package",
    ],
)
