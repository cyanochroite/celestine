"""The uncompromising code formatter."""

import black

from celestine.package import run


def main():
    """"""

    def function():
        black.patched_main()

    argument = []

    run(function, argument)
