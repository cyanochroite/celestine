"""A tool to automatically format Python docstrings.

It tries to follow. recommendations from PEP 8 and PEP 257.
"""
import os
import sys

from celestine.load import directory
from celestine.typed import (
    MT,
    N,
    S,
)

from . import Package as Package_


class Package(Package_):
    """"""

    def main(self, package: MT, path: S) -> N:
        """
        This package is troublesome.

        It can't find the pyproject file unless run from root directory.
        Exclude argument simply does not work.
        Manually feeding it files works.
        """

        location = os.getcwd()
        os.chdir(sys.path[0])

        files = directory.python(path, [], ["unicode"])

        file = map(str, files)
        argv = [*file]
        package.run_docstring_formatter(argv)

        os.chdir(location)
