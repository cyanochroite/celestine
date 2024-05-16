"""The uncompromising code formatter."""

import sys

from celestine.package import Abstract
from celestine.typed import (
    FN,
    M,
    N,
    S,
)

run: FN


class Package(Abstract):
    """"""

    def main(self, package: M, path: S) -> N:
        """"""
        sys.argv.append(path)
        package.patched_main()
