"""The uncompromising code formatter."""

import sys

from celestine.typed import (
    MT,
    N,
    S,
)

from . import Abstract


class Package(Abstract):
    """"""

    def main(self, package: MT, path: S) -> N:
        """"""
        sys.argv.append(path)
        package.patched_main()
