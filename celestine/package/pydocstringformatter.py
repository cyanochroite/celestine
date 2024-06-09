"""A tool to automatically format Python docstrings."""

import os
import sys

from celestine import load
from celestine.package import Abstract
from celestine.typed import (
    CN,
    M,
    N,
    S,
)

run: CN


class Package(Abstract):
    """"""

    def main(self, package: M, path: S) -> N:
        """
        This package is troublesome.

        It can't find the pyproject file unless run from root directory.
        Exclude argument simply does not work.
        Manually feeding it files works.
        """
        location = os.getcwd()
        os.chdir(sys.path[0])

        files = load.walk_python(path, [], [])

        file = map(str, files)
        argv = [*file]
        package.run_docstring_formatter(argv)

        os.chdir(location)
