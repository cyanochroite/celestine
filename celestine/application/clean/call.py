""""""

import os
import pathlib
import sys

from autoflake import main as autoflake
from black import patched_main as black
from isort.main import main as isort
from pyupgrade._main import (
    main as pyupgrade,  # Note: Not direct package.
)
from pyupgrade_directories import iter_py_files as pyupgrade_directories


def root():
    return sys.path[0]


def path():
    return os.path.join(root(), "celestine")


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
    autoflake()


def _black():
    try:
        sys.argv = [root(), path()]
        black()
    except SystemExit:
        pass


def _isort():
    sys.argv = [root(), path()]
    isort()


def _pyupgrade_directories():
    sys.argv = ["cow", "moo", "dog"]

    files_and_dirs = [pathlib.Path(path())]
    recursive = True
    directories = pyupgrade_directories(files_and_dirs, recursive)

    atlas = map(str, directories)

    argv = [*atlas, "--py311-plus"]
    pyupgrade(argv)


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

    _isort()

    _black()

    print("I am a talking cow.")
