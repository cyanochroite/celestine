"""Run a bunch of auto formaters."""

import os
import pathlib
import sys

import autoflake
import black
import isort.main
import pydocstringformatter
import pyupgrade._main
import pyupgrade_directories


def root():
    return sys.path[0]


def path():
    return os.path.join(root(), "celestine")


def _pydocstringformatter():
    sys.argv = [root(), path(), "-w"]

    pydocstringformatter.run_docstring_formatter()


def _autoflake():
    sys.argv = [
        root(),
        path(),
        "-i",
        "-r",
        "--remove-all-unused-imports",
        "--remove-duplicate-keys",
        "--remove-unused-variables",
    ]
    autoflake.main()


def _black():
    try:
        sys.argv = [root(), path()]
        black.patched_main()
    except SystemExit:
        pass


def _isort():
    sys.argv = [root(), path()]
    isort.main.main()


def _pyupgrade_directories():
    sys.argv = [root(), path()]

    files_and_dirs = [pathlib.Path(path())]
    recursive = True
    directories = pyupgrade_directories.iter_py_files(
        files_and_dirs, recursive
    )

    atlas = map(str, directories)

    argv = [*atlas, "--py311-plus"]
    pyupgrade._main.main(argv)


def run(package, argv=None):
    """"""
    try:
        root = sys.path[0]
        path = os.path.join(root, "celestine")
        args = argv if argv else []
        sys.argv = [root, path, *args]
        package()
    except SystemExit:
        pass


def clean(**star):
    """"""

    _pyupgrade_directories()

    _autoflake()

    _pydocstringformatter()

    _isort()

    _black()

    print("I am a talking cow.")
