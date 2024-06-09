"""The uncompromising code formatter."""

import sys

from celestine.package import Abstract
from celestine.typed import (
    CN,
    M,
    N,
    S,
)

run: CN


class Package(Abstract):
    """"""

    def main(self, package: M, path: S) -> N:
        """"""
        sys.argv.append(path)
        package.patched_main()
