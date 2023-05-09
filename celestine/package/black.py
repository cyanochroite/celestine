"""The uncompromising code formatter."""


from celestine.typed import MT

from . import Package as Package_


class Package(Package_):
    """"""

    def main(self, package: MT) -> None:
        """"""
        package.patched_main()

    def name(self) -> str:
        """"""
        return "black"
