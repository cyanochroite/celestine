"""A Python utility / library to sort Python imports."""

from celestine.package import Abstract
from celestine.typed import (
    CN,
    LS,
)

run: CN


class Package(Abstract):
    """"""

    def module(self) -> LS:
        """"""
        return ["main"]
