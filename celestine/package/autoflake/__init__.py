"""Removes unused imports and unused variables."""

import autoflake

from celestine.package import run


def main():
    """"""

    def function():
        autoflake.main()

    argument = [
        "-i",
        "-r",
        "--remove-all-unused-imports",
        "--remove-duplicate-keys",
        "--remove-unused-variables",
    ]

    run(function, argument)
