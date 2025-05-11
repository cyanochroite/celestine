""""""

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


class Package:
    """"""

    name: S
    package: M | N

    def attribute(self, name: S) -> N:
        """"""
        if self:
            package = load.package(self.pypi, name)
            setattr(self, name, package)

    def main(self, package: M, path: P) -> N:
        """"""
        ignore(self)
        root = str(path)
        sys.argv.append(root)
        package.main()

    def submodule(self) -> LS:
        """The 'import PACKAGE.MODULE' name."""
        ignore(self)
        return []

    def run(self, terminate: B = False) -> N:
        """
        Run the package as if from the command line.

        Catch the SystemExit calls that the package may throw.
        """

        if not self.package:
            return

        argv = sys.argv

        path = load.project_root()
        root = str(path)
        sys.argv = [root, root]
        try:
            submodule = load.package(self.name, *self.submodule())
            self.main(submodule, path)
        except SystemExit as exception:
            if terminate:
                raise exception

        sys.argv = argv

    def __bool__(self) -> B:
        result = self.package is not None
        return result

    def __getattr__(self, name: S) -> S:
        result = getattr(self.package, name)
        return result

    def __init__(self, *, pypi: VS = None, **star: R) -> N:
        ignore(star)
        self.name = self.__module__.rsplit(".", maxsplit=1)[-1]
        self.pypi = pypi or self.name

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


ignore(Package)
