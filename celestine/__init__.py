""""""

import importlib
import sys
from importlib.abc import (
    Loader,
    MetaPathFinder,
)
from importlib.machinery import ModuleSpec

from celestine import bank
from celestine.session import begin_session
from celestine.typed import (
    LS,
    MS,
    OM,
    SS,
    B,
    N,
    R,
    S,
    ignore,
    override,
)


class CelestineMetaFinder(MetaPathFinder):
    """"""

    loader: Loader

    @override
    def find_spec(self, fullname: S, path: SS, target: OM = None) -> MS:
        """"""
        ignore(path)
        ignore(target)
        if fullname.startswith("celestine.package."):
            return ModuleSpec(fullname, self.loader)
        return None

    @override
    def __init__(self) -> None:
        package = importlib.import_module("celestine.package")
        self.loader = getattr(package, "Loader")()


def main(argument_list: LS, exit_on_error: B, **star: R) -> N:
    """Run the main program."""
    sys.meta_path.insert(0, CelestineMetaFinder())

    begin_session(argument_list, exit_on_error, **star)
    with bank.window:
        for name, function in bank.code.items():
            bank.window.code[name] = function

        for name, function in bank.view.items():
            view = bank.window.drop(name)
            function(view)
            bank.window.view[name] = view
