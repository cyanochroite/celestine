""""""

import importlib
import importlib.abc
import importlib.machinery
import sys
from importlib.abc import MetaPathFinder
from importlib.machinery import ModuleSpec

from celestine import bank
from celestine.session import begin_session
from celestine.typed import (
    LS,
    MS,
    OM,
    SS,
    B,
    M,
    N,
    R,
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


class LanguageLoader(importlib.abc.Loader):
    """"""

    language: LS

    @override
    def create_module(self, spec: importlib.machinery.ModuleSpec) -> OM:
        """"""
        print("spec2", spec.name)
        partition = spec.name.rpartition(FULL_STOP)
        name = partition[2]
        if name in self.language:
            return None
        return None

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
        self.language = [
            "bg",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "et",
            "fi",
            "fr",
            "ga",
            "hr",
            "hu",
            "it",
            "lt",
            "lv",
            "mt",
            "nl",
            "pl",
            "pt",
            "ro",
            "sk",
            "sl",
            "sv",
        ]


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


class CelestineMetaFinder(MetaPathFinder):
    """"""

    language: LanguageLoader
    package: PackageLoader

    @override
    def find_spec(self, fullname: S, path: SS, target: OM = None) -> MS:
        """"""
        ignore(path)
        ignore(target)

        partition = fullname.rpartition(FULL_STOP)
        name = partition[2]
        language = [
            "bg",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "es",
            "et",
            "fi",
            "fr",
            "ga",
            "hr",
            "hu",
            "it",
            "lt",
            "lv",
            "mt",
            "nl",
            "pl",
            "pt",
            "ro",
            "sk",
            "sl",
            "sv",
        ]
        if name in language:
            return None

        if fullname.startswith("celestine.language._"):
            return None
        if fullname.startswith("celestine.language."):
            candy = ModuleSpec(fullname, self.language)
            print("candy", candy)
            return candy
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
