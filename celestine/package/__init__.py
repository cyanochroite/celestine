"""Run a bunch of auto formaters."""

import logging
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


class Abstract:
    """"""

    ring: A
    name: S
    package: MT | N

    def main(self, package: MT, path: S) -> N:
        """"""
        sys.argv.append(path)
        package.main()

    def module(self) -> L[S]:
        """The 'import PACKAGE.MODULE' name."""
        return []

    def run(self) -> N:
        """"""

        if not self.package:
            return

        argv = sys.argv

        root = sys.path[0]
        path = os.path.join(root, CELESTINE)
        sys.argv = [root, path]

        try:
            module = load.package(self.name, *self.module())
            self.main(module, path)
        except SystemExit:
            pass

        sys.argv = argv

    def __bool__(self):
        return self.package is not None

    def __getattr__(self, name):
        return getattr(self.package, name)

    def __init__(self, ring, /, name: S, **star):
        self.ring = ring
        self.name = name

        try:
            self.package = load.package(name)
        except ModuleNotFoundError:
            self.package = None
            found = f"Module {name} not found."
            install = f"Install with 'pip install {name}'."
            message = f"{found} {install}"
            logging.warning(message)


class Package:
    """"""

    def __getattr__(self, name) -> A:
        """"""
        try:
            return self.dictionary[name]
        except KeyError as error:
            message = f"'{PACKAGE}' object has no attribute '{name}'"
            raise AttributeError(message) from error

    def __init__(self, ring, /, **star):
        self.dictionary = {}
        argument = load.pathway.argument(PACKAGE)
        for name in argument:
            attribute = load.attribute(PACKAGE, name, "Package")
            package = attribute(ring, name)
            self.dictionary[name] = package
