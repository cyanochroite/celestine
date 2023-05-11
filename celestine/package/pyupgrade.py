"""Removes unused imports and unused variables."""

import sys

from celestine.load import directory
from celestine.typed import (
    MT,
    L,
    N,
    S,
)

from . import Package as Package_


class Package(Package_):
    """"""

    def main(self, package: MT) -> N:
        """"""
        files = directory.python(sys.argv[1])
        atlas = map(str, files)
        argv = [*atlas, "--py311-plus"]
        package.main(argv)

    def module(self) -> L[S]:
        """"""
        return ["_main"]
