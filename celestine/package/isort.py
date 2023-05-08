"""A Python utility / library to sort Python imports."""


from celestine.package import Package as Package_
from celestine.typed import MT


class Package(Package_):
    """"""

    def main(self, package: MT) -> None:
        """"""
        package.main.main()

    def module(self) -> str:
        """"""
        return "isort.main"
