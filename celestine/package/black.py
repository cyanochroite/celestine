"""The uncompromising code formatter."""

import sys

from celestine.typed import (
    MT,
    N,
    S,
)

from . import (
    AbstractLinter,
    AbstractPackage,
)


class Linter(AbstractLinter):
    """"""

    def main(self, package: MT, path: S) -> N:
        """"""
        sys.argv.append(path)
        package.patched_main()


class Package(AbstractPackage):
    """"""
