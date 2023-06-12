"""A Python utility / library to sort Python imports."""

from celestine.typed import (
    L,
    S,
)

from . import (
    AbstractLinter,
    AbstractPackage,
)


class Linter(AbstractLinter):
    """"""

    def module(self) -> L[S]:
        """"""
        return ["main"]


class Package(AbstractPackage):
    """"""
