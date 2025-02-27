"""Removes unused imports and unused variables."""

from celestine import load
from celestine.package import Abstract
from celestine.typed import (
    LS,
    M,
    N,
    P,
    ignore,
    override,
)


class Package(Abstract):
    """"""

    @override
    def main(self, package: M, path: P) -> N:
        """
        This package has no configuration file options.

        Since there is no way to configure the exclude files,
        we do it ourself.
        """
        ignore(self)

        files = load.walk_python(path, [], [])

        file = map(str, files)
        argv = [*file, "--py312-plus"]
        package.main(argv)

    @override
    def module(self) -> LS:
        """"""
        ignore(self)
        return ["_main"]


def run() -> N:
    """"""
