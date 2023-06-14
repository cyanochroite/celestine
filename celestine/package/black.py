"""The uncompromising code formatter."""

import sys

from celestine.typed import (
    MT,
    N,
    S,
)

from . import AbstractPackage


class Package(AbstractPackage):
    """"""

    def main(self, package: MT, path: S) -> N:
        """"""
        sys.argv.append(path)
        package.patched_main()
