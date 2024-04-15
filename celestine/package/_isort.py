"""A Python utility / library to sort Python imports."""

from celestine.package._abstract import Abstract
from celestine.typed import LS


class Package(Abstract):
    """"""

    def module(self) -> LS:
        """"""
        return ["main"]
