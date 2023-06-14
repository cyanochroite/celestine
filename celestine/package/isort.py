"""A Python utility / library to sort Python imports."""

from celestine.typed import (
    L,
    S,
)

from . import AbstractPackage


class Package(AbstractPackage):
    """"""

    def module(self) -> L[S]:
        """"""
        return ["main"]
