"""Run a bunch of auto formaters."""

import os
import sys

from celestine import load

CELESTINE = "celestine"
PACKAGE = "package"


from celestine.typed import MT


class Package:
    """"""

    def argument(self) -> list[str]:
        """"""
        return []

    def main(module: MT) -> None:
        """"""
        raise NotImplementedError

    def module(self) -> str:
        """The 'import PACKAGE.MODULE' name."""
        return self.name

    def pip(self) -> str:
        """"""
        return f"pip install {self.name}"

    def run(self) -> None:
        """"""
        argv = sys.argv

        root = sys.path[0]
        path = os.path.join(root, CELESTINE)
        argument = self.argument()
        sys.argv = [root, path, *argument]

        try:
            module = load.package(self.module())
            self.main(module)
        except ModuleNotFoundError:
            print("Module failed to load. To install, run:")
            print(self.pip())
        except SystemExit:
            pass

        sys.argv = argv

    def __init__(self, name: str) -> None:
        """"""
        self.name = name


def run(name: str) -> None:
    """"""
    module = load.module(PACKAGE, name)
    package = module.Package(name)
    package.run()
