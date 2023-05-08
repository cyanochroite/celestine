"""Removes unused imports and unused variables."""

import autoflake

from celestine.package import run


def main():
    """"""

    def function():
        autoflake.main()

    argument =
    run(function, argument)



"""Removes unused imports and unused variables."""

from celestine import load

MODULE = "autoflake"

def argument() -> list[str]:
    """"""
    return [
        "-i",
        "-r",
        "--remove-all-unused-imports",
        "--remove-duplicate-keys",
        "--remove-unused-variables",
    ]


def main() -> None:
    """"""
    autoflake = load.module(MODULE)
    autoflake.main()


def pip() -> str:
    """"""
    return MODULE
