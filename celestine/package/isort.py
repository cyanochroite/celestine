"""A Python utility / library to sort Python imports."""

from celestine.package import Abstract
from celestine.typed import (
    CN,
    LS,
    ignore,
    override,
)

run: CN


class Package(Abstract):
    """"""

    @override
    def module(self) -> LS:
        """"""
        ignore(self)
        return ["main"]
