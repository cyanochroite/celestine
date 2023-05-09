"""Removes unused imports and unused variables."""

from . import Package as Package_


class Package(Package_):
    """"""

    def argument(self) -> list[str]:
        """"""
        return [
            "-i",
            "-r",
            "--remove-all-unused-imports",
            "--remove-duplicate-keys",
            "--remove-unused-variables",
        ]

    def name(self) -> str:
        """"""
        return "autoflake"
