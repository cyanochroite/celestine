"""Run a bunch of auto formaters."""

import os
import sys

from celestine import load
from celestine.typed import MT

CELESTINE = "celestine"
PACKAGE = "package"


class Package:
    """"""

    def argument(self) -> list[str]:
        """"""
        return []

    def main(self, package: MT) -> None:
        """"""
        package.main()

    def module(self) -> list[str]:
        """The 'import PACKAGE.MODULE' name."""
        return []

    def name(self) -> str:
        """The 'import PACKAGE' name."""
        raise NotImplementedError

    def pip(self) -> str:
        """"""
        return f"pip install {self.name()}"

    def run(self) -> None:
        """"""
        argv = sys.argv

        root = sys.path[0]
        path = os.path.join(root, CELESTINE)
        argument = self.argument()
        sys.argv = [root, path, *argument]

        try:
            module = load.package(self.name(), *self.module())
            self.main(module)
        except ModuleNotFoundError:
            print("Module failed to load. To install, run:")
            print(self.pip())
        except SystemExit:
            pass

        sys.argv = argv


def run(name: str) -> None:
    """"""
    module = load.module("application", "clean", "package", name)
    package = module.Package()
    package.run()
