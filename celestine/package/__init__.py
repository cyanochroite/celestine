"""Run a bunch of auto formaters."""

import os
import sys

from celestine import load
from celestine.typed import (
    MT,
    A,
    L,
    N,
    S,
)

CELESTINE = "celestine"
PACKAGE = "package"
DICTIONARY = "dictionary"


class AbstractLinter:
    """"""

    def main(self, package: MT, path: S) -> N:
        """"""
        sys.argv.append(path)
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
            self.main(module, path)
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
    package = module.Linter(name)
    package.run(name)


class AbstractPackage:
    """"""

    def __bool__(self):
        return self.package is not None

    def __getattr__(self, name):
        return getattr(self.package, name)

    def __init__(self, ring, /, name, **star):
        self.ring = ring
        self.name = name

        try:
            self.package = load.package(self.name)
        except ModuleNotFoundError:
            self.package = None


class Package:
    """"""

    def __getattr__(self, name) -> A:
        """"""
        try:
            return self.dictionary[name]
        except KeyError:
            message = f"'{PACKAGE}' object has no attribute '{name}'"
            raise AttributeError(message)

    def __init__(self, ring, /, **star):
        self.dictionary = {}
        argument = load.pathway.argument(PACKAGE)
        for name in argument:
            attribute = load.attribute(PACKAGE, name, "Package")
            package = attribute(ring, name)
            self.dictionary[name] = package
