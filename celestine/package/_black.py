"""The uncompromising code formatter."""

import sys

from celestine.package._abstract import Abstract
from celestine.typed import (
    M,
    N,
    S,
)


class Package(Abstract):
    """"""

    def main(self, package: M, path: S) -> N:
        """"""
        sys.argv.append(path)
        package.patched_main()
