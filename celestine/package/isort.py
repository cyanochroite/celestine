"""A Python utility / library to sort Python imports."""

from celestine.package import Abstract
from celestine.typed import (
    LS,
    N,
    ignore,
    override,
)


class Package(Abstract):
    """"""

    @override
    def module(self) -> LS:
        """"""
        ignore(self)
        return ["main"]


def run() -> N:
    """"""


ignore(Package, run)
