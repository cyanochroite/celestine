"""Removes unused imports and unused variables."""

import sys

from celestine.load import directory
from celestine.typed import MT

from . import Package as Package_


class Package(Package_):
    """"""

    def main(self, package: MT) -> None:
        """"""
        path = sys.argv[1]

        files_and_dirs = [pathlib.Path(path)]

        recursive = True

        directories = pyupgrade_directories.iter_py_files(
            files_and_dirs, recursive
        )

        atlas = map(str, directories)

        argv = [*atlas, "--py311-plus"]
        #
        pyupgrade._main.main(argv)
        #
        package.main()

    def argument(self) -> list[str]:
        """"""
        filenames = []
        return [
            "--py311-plus",
            *filenames,
        ]

    def main(self, package: MT) -> None:
        """"""
        files = directory.python(sys.argv[1])
        atlas = map(str, files)
        argv = [*atlas, "--py311-plus"]
        package.main(argv)

    def module(self) -> list[str]:
        """"""
        return ["_main"]

    def name(self) -> str:
        """"""
        return "pyupgrade"
