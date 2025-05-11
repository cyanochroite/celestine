"""The uncompromising code formatter."""

import sys

from celestine.package import Package
from celestine.typed import (
    M,
    N,
    P,
    ignore,
    override,
)


class Self(Package):
    """"""

    @override
    def main(self, package: M, path: P) -> N:
        """"""
        ignore(self)
        root = str(path)
        sys.argv.append(root)
        package.patched_main()


def run() -> N:
    """"""


ignore(Package, run)
