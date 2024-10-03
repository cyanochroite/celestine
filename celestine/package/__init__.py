""""""

import os
import sys

from celestine import load
from celestine.typed import (
    LS,
    VS,
    B,
    M,
    N,
    P,
    R,
    S,
    ignore,
)


class Abstract:
    """"""

    name: S
    package: M | N

    def main(self, package: M, path: P) -> N:
        """"""
        ignore(self)
        root = str(path)
        sys.argv.append(root)
        package.main()

    def module(self) -> LS:
        """The 'import PACKAGE.MODULE' name."""
        ignore(self)
        return []

    def run(self) -> N:
        """"""

        if not self.package:
            return

        argv = sys.argv

        path = load.project_path()
        root = str(path)
        sys.argv = [root, root]
        try:
            module = load.package(self.name, *self.module())
            self.main(module, path)
        except SystemExit:
            pass

        sys.argv = argv

    def __bool__(self) -> B:
        result = self.package is not None
        return result

    def __getattr__(self, name: S) -> S:
        result = getattr(self.package, name)
        return result

    def __init__(self, *, pypi: VS = None, **star: R) -> N:
        self.name = self.__module__.rsplit(".", maxsplit=1)[-1]
        self.pypi = pypi or self.name

        # pygame prints an anoying message on import
        # so this here to hide any messages a package may print
        # when being imported
        sys_stdout = sys.stdout

        with open(
            os.devnull,
            "w",
            encoding="utf-8",
        ) as stdout:
            sys.stdout = stdout
            try:
                self.package = load.package(self.pypi)
            except ValueError:
                #  Name was none.
                self.package = None
            except ModuleNotFoundError:
                self.package = None
                found = f"Package '{self.name}' not found."
                install = f"Install with 'pip install {self.pypi}'."
                message = f"{found} {install}"
                print(message)

        sys.stdout = sys_stdout
