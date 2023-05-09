"""A Python utility / library to sort Python imports."""


from . import Package as Package_


class Package(Package_):
    """"""

    def module(self) -> list[str]:
        """"""
        return ["main"]

    def name(self) -> str:
        """"""
        return "isort"
