"""A tool to automatically format Python docstrings.

It tries to follow. recommendations from PEP 8 and PEP 257.
"""
import os
import sys

from celestine.typed import (
    MT,
    N,
)

from . import Package as Package_


class Package(Package_):
    """"""

    def main(self, package: MT) -> N:
        """"""
        directory = os.getcwd()
        path = sys.path[0]

        # The "exclude" option is extra broken in current directory.
        os.chdir(path)

        package.run_docstring_formatter()

        # Revert to old working directory.
        os.chdir(directory)
