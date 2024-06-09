"""Removes unused imports and unused variables."""

from celestine import load
from celestine.package import Abstract
from celestine.typed import (
    CN,
    LS,
    M,
    N,
    S,
)

run: CN


class Package(Abstract):
    """"""

    def main(self, package: M, path: S) -> N:
        """
        This package has no configuration file options.

        Since no way to configure exclude files, we do it ourself.
        """
        # TODO: This is breaking the language files. Find out why.
        files = load.walk_python(path, [], ["language"])

        file = map(str, files)
        argv = [*file, "--py311-plus"]
        package.main(argv)

    def module(self) -> LS:
        """"""
        return ["_main"]
