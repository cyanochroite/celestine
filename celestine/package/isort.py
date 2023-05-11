"""A Python utility / library to sort Python imports."""

from celestine.typed import (
    L,
    S,
)

from . import Package as Package_


class Package(Package_):
    """"""

    def module(self) -> L[S]:
        """"""
        return ["main"]
