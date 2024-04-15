""""""
import importlib
import importlib.abc
import importlib.machinery

from celestine.typed import (
    M,
    OM,
    N,
    S, override,
    ignore,
)
from celestine.unicode import FULL_STOP


def package(base: S, *path: S) -> M:
    """Load an external package from the system path."""
    iterable = [base, *path]
    name = FULL_STOP.join(iterable)
    result = importlib.import_module(name)
    return result


class Loader(importlib.abc.Loader):
    """"""

    @override
    def create_module(self, spec: importlib.machinery.ModuleSpec) -> OM:
        """"""
        partition = spec.name.rpartition(FULL_STOP)
        name = f"{partition[0]}{partition[1]}_{partition[2]}"
        thing = package(name)
        call = getattr(thing, "Package")
        module = call(partition[2])
        return module

    @override
    def exec_module(self, module: M) -> N:
        """"""
        ignore(module)
