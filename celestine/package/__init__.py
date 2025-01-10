""""""

import sys

from celestine import load
from celestine.typed import (
    CN,
    LS,
    VS,
    A,
    B,
    D,
    M,
    N,
    P,
    R,
    S,
    ignore,
)


class Abstract:
    """"""

    local: D[S, A]  # TODO: Not ANY
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
        if name != "Surface":
            gets = self.local.get(name)
            if gets:
                return gets

        result = getattr(self.package, name)
        return result

    def functions(self, module: M) -> D[S, CN]:
        """"""
        path = f"celestine.package.{self.name}"

        def test(value: S) -> B:
            name = repr(value)
            one = name.startswith("<function ")
            two = name.startswith("<class ")
            three = path in name
            four = "Package" not in name
            result = (one or two) and three and four
            return result

        _dictionary: D[S, A] = vars(module)
        _items = _dictionary.items()
        result = {key: value for key, value in _items if test(value)}
        return result

    def __init__(self, *, pypi: VS = None, **star: R) -> N:
        self.name = self.__module__.rsplit(".", maxsplit=1)[-1]
        self.pypi = pypi or self.name
        local = load.module("package", self.name)
        self.local = self.functions(local)
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
