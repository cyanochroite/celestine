"""The uncompromising code formatter."""

import sys

from celestine.package import Abstract
from celestine.typed import (
    CN,
    M,
    N,
    P,
    ignore,
    override,
)

run: CN


class Package(Abstract):
    """"""

    @override
    def main(self, package: M, path: P) -> N:
        """"""
        ignore(self)
        root = str(path)
        sys.argv.append(root)
        package.patched_main()
