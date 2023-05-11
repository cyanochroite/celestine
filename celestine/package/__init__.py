"""Run a bunch of auto formaters."""

import os
import sys

from celestine import load
from celestine.typed import (
    MT,
    L,
    N,
    S,
)

CELESTINE = "celestine"
PACKAGE = "package"


class Package:
    """"""

    def main(self, package: MT) -> N:
        """"""
        package.main()

    def module(self) -> L[S]:
        """The 'import PACKAGE.MODULE' name."""
        return []

    def pip(self) -> str:
        """"""
        return f"pip install {self.name}"

    def run(self, name: S) -> N:
        """"""
        argv = sys.argv

        root = sys.path[0]
        path = os.path.join(root, CELESTINE)
        sys.argv = [root, path]

        try:
            module = load.package(self.name, *self.module())
            self.main(module)
        except ModuleNotFoundError:
            print("Module failed to load. To install, run:")
            print(self.pip())
        except SystemExit:
            pass

        sys.argv = argv

    def __init__(self, name: S) -> N:
        self.name = name


def run(name: str) -> None:
    """"""
    module = load.module(PACKAGE, name)
    package = module.Package(name)
    package.run(name)
