"""A tool to automatically format Python docstrings.

It tries to follow. recommendations from PEP 8 and PEP 257.
"""
import os
import sys

from celestine.load import directory

from celestine.typed import (
    MT,
    N,
)

from . import Package as Package_


class Package(Package_):
    """"""

    def main(self, package: MT) -> N:
        """Setting exclude in pyproject just does not work."""
        path = os.getcwd()

        # Change current directory so we can find pyproject file.
        path = sys.path[0]
        os.chdir(path)


        #TODO fix security argv os walk
        #TODO add config options??
        top = sys.argv[1]
        include = [".py"]
        exclude = [".mypy_cache","__pycache__","unicode"]

        files = directory.file(top, include, exclude)
        atlas = map(str, files)
        argv = [*atlas]
        package.run_docstring_formatter(argv)

        os.chdir(path)
