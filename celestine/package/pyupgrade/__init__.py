"""Run pyupgrade on all files in a directory recursively."""

import pathlib
import sys

import pyupgrade._main
import pyupgrade_directories

from celestine.package import run


def main():
    """"""

    def function():
        path = sys.argv[1]

        files_and_dirs = [pathlib.Path(path)]

        recursive = True

        directories = pyupgrade_directories.iter_py_files(
            files_and_dirs, recursive
        )

        atlas = map(str, directories)

        argv = [*atlas, "--py311-plus"]

        pyupgrade._main.main(argv)

    argument = []

    run(function, argument)
