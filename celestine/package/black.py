"""The uncompromising code formatter."""

import sys

from celestine.typed import (
    MT,
    N,
    S,
)

from . import Package as Package_


class Package(Package_):
    """"""

    def main(self, package: MT, path: S) -> N:
        """"""
        sys.argv.append(path)
        package.patched_main()
