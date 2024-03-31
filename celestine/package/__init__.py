"""Run a bunch of auto formaters."""

import os
import sys

from celestine import (
    load,
    stream,
)
from celestine.typed import (
    LS,
    OS,
    B,
    D,
    M,
    N,
    R,
    S,
)

CELESTINE = "celestine"
PACKAGE = "package"


class Abstract:
    """"""

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

        path = str(load.project_path())
        sys.argv = [path, path]
        try:
            module = load.package(self.name, *self.module())
            self.main(module, path)
        except SystemExit:
            pass

        sys.argv = argv

    def __bool__(self) -> B:
        return self.package is not None

    def __getattr__(self, name: S) -> S:
        return getattr(self.package, name)

    def __init__(self, name: S, pypi: OS = None, **star: R) -> N:
        self.name = name
        self.pypi = pypi or name

        # pygame prints an anoying message on import
        # so this here to hide any messages a package may print
        # when being imported
        sys_stdout = sys.stdout

        with open(
            os.devnull,
            stream.Mode.WRITE_TEXT.value,
            encoding=stream.Encoding.UTF_8.value,
        ) as stdout:
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

    dictionary: D[S, M]

    def __getattr__(self, name: S) -> M:
        """"""
        try:
            return self.dictionary[name]
        except KeyError as error:
            message = f"'{PACKAGE}' object has no attribute '{name}'"
            raise AttributeError(message) from error

    def __init__(self, **star: R) -> N:
        self.dictionary = {}
        argument = load.argument(PACKAGE)
        for name in argument:
            attribute = load.attribute(PACKAGE, name, "Package")
            package = attribute(name)
            self.dictionary[name] = package
