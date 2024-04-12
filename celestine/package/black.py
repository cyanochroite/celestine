"""The uncompromising code formatter."""

import sys

from celestine.typed import (
    M,
    N,
    S,
)

from celestine.session import Abstract


class Package(Abstract):
    """"""

    def main(self, package: M, path: S) -> N:
        """"""
        sys.argv.append(path)
        package.patched_main()
