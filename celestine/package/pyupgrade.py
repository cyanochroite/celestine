"""Removes unused imports and unused variables."""

from celestine import load
from celestine.typed import (
    MT,
    L,
    N,
    S,
)

from . import AbstractPackage


class Package(AbstractPackage):
    """"""

    def main(self, package: MT, path: S) -> N:
        """
        This package has no configuration file options.

        Since no way to configure exclude files, we do it ourself.
        """
        files = load.many.python(path, [], ["unicode"])

        file = map(str, files)
        argv = [*file, "--py311-plus"]
        package.main(argv)

    def module(self) -> L[S]:
        """"""
        return ["_main"]
