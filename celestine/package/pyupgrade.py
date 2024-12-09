"""Removes unused imports and unused variables."""

from celestine import load
from celestine.package import Abstract
from celestine.typed import (
    CN,
    LS,
    M,
    N,
    P,
    ignore,
    override,
)

run: CN


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

        # TODO: This is breaking the language files. Find out why.
        files = load.walk_python(path, [], ["language"])

        file = map(str, files)
        argv = [*file, "--py311-plus"]
        package.main(argv)

    @override
    def module(self) -> LS:
        """"""
        ignore(self)
        return ["_main"]
