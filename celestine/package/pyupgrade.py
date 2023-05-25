"""Removes unused imports and unused variables."""

import sys

from celestine.load import directory
from celestine.typed import (
    MT,
    L,
    N,
    P,
    S,
)

from . import Package as Package_


class Package(Package_):
    """"""

    def main(self, package: MT) -> N:
        """Skip unicode files because they are so big."""
        #TODO fix security argv os walk
        #TODO add config options??
        top = sys.argv[1]
        include = [".py"]
        exclude = [".mypy_cache","__pycache__","unicode"]

        files = directory.file(top, include, exclude)
        atlas = map(str, files)
        argv = [*atlas, "--py311-plus"]
        package.main(argv)

    def module(self) -> L[S]:
        """"""
        return ["_main"]
