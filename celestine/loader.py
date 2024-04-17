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
import types


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
    name = "myapp.virtual"

    def __init__(self):
        self._services = {
            "frontend": FrontendModule()
        }
        self.module = types.ModuleType("myapp.virtual")
        self.module.__path__ = []

    def provides(self, fullname):
        """"""
        if self._truncate_name(fullname) in self._services:
            return True

        # this checks if we should return the dummy module,
        # since this evaluates to True when importing myapp and
        # myapp.virtual
        return self._COMMON_PREFIX.startswith(fullname)

    def create_module(self, spec):
        """"""
        service_name = self._truncate_name(spec.name)
        if service_name not in self._services:
            # return our dummy module since at this point we're loading
            # *something* along the lines of "myapp.virtual" that's not
            # a service
            return self.module
        module = self._services[service_name]
        return module

    def exec_module(self, module):
        """Execute the given module in its own namespace
        This method is required to be present by importlib.abc.Loader,
        but since we know our module object is already fully-formed,
        this method merely no-ops.
        """

    def _truncate_name(self, fullname):
        """Strip off _COMMON_PREFIX from the given module name
        Convenience method when checking if a service is provided.
        """
        return fullname[len(self._COMMON_PREFIX):]


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
        self.language = DependencyInjectorLoader()
        self.package = PackageLoader()

    def find_spec(self, fullname, path, target=None):
        """"""
        if self._loader.provides(fullname):
            return ModuleSpec(fullname, self._loader)
        if fullname.startswith("celestine.package._"):
            return None
        if fullname.startswith("celestine.package."):
            return ModuleSpec(fullname, self.package)
        return None


def loader() -> N:
    """"""
    sys.meta_path.insert(0, CelestineMetaFinder())
