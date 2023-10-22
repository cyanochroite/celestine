"""Run a bunch of auto formaters."""

import os
import sys

from celestine import load
from celestine.file.data import (
    UTF_8,
    WRITE_TEXT,
)
from celestine.load import pathway
from celestine.typed import (
    LS,
    M,
    OS,
    A,
    N,
    R,
    S,
)

CELESTINE = "celestine"
PACKAGE = "package"


class Abstract:
    """"""

    ring: A
    name: S
    package: M | N

    def main(self, package: M, path: S) -> N:
        """"""
        sys.argv.append(path)
        package.main()

    def module(self) -> LS:
        """The 'import PACKAGE.MODULE' name."""
        return []

    def run(self) -> N:
        """"""

        if not self.package:
            return

        argv = sys.argv

        path = str(pathway.pathfinder())
        sys.argv = [path, path]
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

    def __init__(self, ring: R, name: S, pypi: OS = None, **star) -> N:
        self.ring = ring
        self.name = name
        self.pypi = pypi or name

        # pygame prints an anoying message on import
        # so this here to hide any messages a package may print
        # when being imported
        sys_stdout = sys.stdout

        with open(os.devnull, WRITE_TEXT, encoding=UTF_8) as stdout:
            sys.stdout = stdout  # as TextIO
            try:
                self.package = load.package(self.pypi)
            except ModuleNotFoundError:
                self.package = None
                # found = f"Package '{self.name}' not found."
                # install = f"Install with 'pip install {self.pypi}'."
                # message = f"{found} {install}"
                # logging.warning(message)

        sys.stdout = sys_stdout


class Package:
    """"""

    def __getattr__(self, name) -> A:
        """"""
        try:
            return self.dictionary[name]
        except KeyError as error:
            message = f"'{PACKAGE}' object has no attribute '{name}'"
            raise AttributeError(message) from error

    def __init__(self, ring: R, **star):
        self.dictionary = {}
        argument = load.pathway.argument(PACKAGE)
        for name in argument:
            attribute = load.attribute(PACKAGE, name, "Package")
            package = attribute(ring, name)
            self.dictionary[name] = package
