"""A Python utility / library to sort Python imports."""

from celestine.package import Package
from celestine.typed import (
    LS,
    N,
    ignore,
    override,
)


class Self(Package):
    """"""

    @override
    def submodule(self) -> LS:
        """"""
        ignore(self)
        return ["main"]


def run() -> N:
    """"""


ignore(Package, run)
