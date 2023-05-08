"""Removes unused imports and unused variables."""

import sys

from celestine.package import Package as Package_
from celestine.typed import MT


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

    def main(self, package: MT) -> None:
        """"""
        print("MAKE RECURSIVE")
        sys.argv[1] += "\\__init__.py"
        package.main()

    def module(self) -> list[str]:
        """"""
        return ["_main"]

    def name(self) -> str:
        """"""
        return "pyupgrade"
