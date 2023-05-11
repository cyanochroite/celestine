"""A tool to automatically format Python docstrings.

It tries to follow. recommendations from PEP 8 and PEP 257.
"""

from celestine.typed import MT

from . import Package as Package_


class Package(Package_):
    """"""

    def main(self, package: MT) -> None:
        """"""
        package.run_docstring_formatter()

    def name(self) -> str:
        """"""
        return "pydocstringformatter"
