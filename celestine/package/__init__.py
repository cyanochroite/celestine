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

    def exempt(self) -> LS:
        """"""
        ignore(self)
        return []

    def __getattr__(self, name: S) -> S:
        if name in self.exempt():
            result = getattr(self.package, name)
        else:
            result = self.local.get(name)
        if not result:
            message = f"'{self.name}' object has no attribute '{name}'"
            raise AttributeError(message)
        return result

    def functions(self) -> D[S, CN]:
        """"""
        dictionary: D[S, A] = {}
        base = f"celestine.package.{self.name}"
        modules = load.walk_package(base)
        for module in modules:
            var = vars(module)
            dictionary.update(var)

        def test(value: S) -> B:
            name = repr(value)
            class_ = name.startswith("<class ")
            function_ = name.startswith("<function ")
            module_ = name.startswith("<module ")
            important = class_ or function_ or module_

            child = self.name in name

            abstract = "abstract" in name and module_
            package = "Package" in name
            excluded = abstract or package

            result = important and child and not excluded
            result = True  # Try disable of function filter.
            return result

        items = dictionary.items()
        result = {key: value for key, value in items if test(value)}
        return result

    def __init__(self, *, pypi: VS = None, **star: R) -> N:
        self.name = self.__module__.rsplit(".", maxsplit=1)[-1]
        self.pypi = pypi or self.name
        if self.name == "blender":
            #  TODO: Remove this bypass once blender is working.
            self.local = {}
        else:
            self.local = self.functions()

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
