""""""

import importlib
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


def _dictionary_items(_module):
    _dictionary = vars(_module)
    _items = _dictionary.items()
    return _items


class Magic:
    """"""

    dictionary: D[S, S]

    def __getattr__(self, name: S) -> S:
        return self.dictionary.get(name)

    def __init__(self, dictionary: D[S, S]) -> N:
        self.dictionary = dictionary


class LanguageLoader(importlib.abc.Loader):
    """"""

    language: LS

    @override
    def create_module(self, spec: importlib.machinery.ModuleSpec) -> OM:
        """"""
        if spec.name == "celestine.sign":
            print("doggy", spec.name, self.module)
            return self.module

        name = "celestine.language.en"
        module = _package(name)
        print("MOO", spec.name, module)
        return module

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

    def create_module(self, spec):
        """"""
        partition = spec.name.rpartition(FULL_STOP)
        name = partition[2]
        print(f">>{name}<<")
        if name in ["en", "fr"]:
            return self.module
        module = _package("celestine.language.en")
        car = vars(module)
        pig = Magic(car)
        return pig
        # module = FrontendModule()

    @override
    def exec_module(self, module: M) -> N:
        """"""
        ignore(module)

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


""""""


class FrontendModule:
    """"""

    class Popup:
        """"""

        def __init__(self, message):
            self._message = message

        def display(self):
            """"""
            print("Popup:", self._message)


class DependencyInjectorLoader(importlib.abc.Loader):
    """"""

    _COMMON_PREFIX = "myapp.virtual."
    _name = "myapp.virtual"

    @override
    def exec_module(self, module: M) -> N:
        """"""
        ignore(module)

    def __init__(self):
        self._services = {"frontend": FrontendModule()}
        self.module = types.ModuleType(self._name)
        self.module.__path__ = []

    def create_module(self, spec):
        """"""
        truncate_name = spec.name[len(self._COMMON_PREFIX):]
        service_name = truncate_name
        if service_name not in self._services:
            # return our dummy module since at this point we're loading
            # *something* along the lines of "myapp.virtual" that's not
            # a service
            return self.module
        module = self._services[service_name]
        return module


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
        partition[2]
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
        if fullname.startswith("celestine.sign"):
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
        self._loader = DependencyInjectorLoader()
        self.language = LanguageLoader()
        self.package = PackageLoader()

    def find_spec(self, fullname, path, target=None):
        """"""

        if fullname.startswith("myapp"):
            return ModuleSpec(fullname, self._loader)

        if fullname.startswith("celestine.sign"):
            return ModuleSpec(fullname, self.language)

        if fullname.startswith("celestine.package._"):
            return None
        if fullname.startswith("celestine.package."):
            return ModuleSpec(fullname, self.package)
        return None


def loader() -> N:
    """"""
    sys.meta_path.insert(0, CelestineMetaFinder())
