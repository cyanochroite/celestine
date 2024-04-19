""""""

import importlib
import importlib.util
import importlib.abc
import importlib.machinery
import sys
import types
from importlib.abc import MetaPathFinder
from importlib.machinery import ModuleSpec

from celestine.typed import (
    LS,
    MS,
    OM,
    SS,
    M,
    D,
    A,
    S,
    N,
    S,
    ignore,
    override,
)
from celestine.unicode import FULL_STOP


def _package(base: S, *path: S) -> M:
    """Load an external package from the system path."""
    iterable = [base, *path]
    name = FULL_STOP.join(iterable)
    result = importlib.import_module(name)
    return result


class Magic:
    """"""

    dictionary: D[S, S]

    def __getattr__(self, name: S) -> S:
        return self.dictionary.get(name)

    def __init__(self, dictionary: D[S, S]) -> N:
        self.dictionary = dictionary


class LanguageLoader(importlib.machinery.SourcelessFileLoader):
    """"""

    language: LS

    @override
    def exec_module(self, module: M) -> N:
        """"""
        dictionary = vars(module)
        magic = Magic(dictionary)
        return magic

    @override
    def __init__(self) -> N:
        self.module = types.ModuleType("celestine.sign")
        self.module.__path__ = []


class PackageLoader(importlib.abc.Loader):
    """"""

    @override
    def create_module(self, spec: importlib.machinery.ModuleSpec) -> OM:
        """"""
        partition = spec.name.rpartition(FULL_STOP)
        name = f"{partition[0]}{partition[1]}_{partition[2]}"
        thing = _package(name)
        call = getattr(thing, "Package")
        module = call(partition[2])
        return module

    @override
    def exec_module(self, module: M) -> N:
        """"""
        ignore(module)

    @override
    def __init__(self) -> N:
        pass


class CelestineMetaFinder(MetaPathFinder):
    """"""

    language: LanguageLoader
    package: PackageLoader

    @override
    def find_spec(self, fullname: S, path: SS, target: OM = None) -> MS:
        """"""
        ignore(path)
        ignore(target)

        if fullname.startswith("celestine.language."):
            return ModuleSpec(fullname, self.language)

        if fullname.startswith("celestine.package._"):
            return None
        if fullname.startswith("celestine.package."):
            return ModuleSpec(fullname, self.package)
        return None

    @override
    def __init__(self) -> N:
        self.language = LanguageLoader()
        self.package = PackageLoader()


def loader() -> N:
    """"""
    sys.meta_path.insert(0, CelestineMetaFinder())
