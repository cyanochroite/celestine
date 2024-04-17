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


class DependencyInjectorLoader(importlib.abc.Loader):
    """"""

    _COMMON_PREFIX = "myapp.virtual."

    def __init__(self):
        self._services = {}
        # create a dummy module to return when Python attempts to import
        # myapp and myapp.virtual, the :-1 removes the last "." for
        # aesthetic reasons :)
        self._dummy_module = types.ModuleType(self._COMMON_PREFIX[:-1])
        # set __path__ so Python believes our dummy module is a package
        # this is important, since otherwise Python will believe our
        # dummy module can have no submodules
        self._dummy_module.__path__ = []

    def provide(self, service_name, module):
        """"""
        self._services[service_name] = module

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
            return self._dummy_module
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
        self.language = LanguageLoader()
        self.language = DependencyInjectorLoader()
        self.package = PackageLoader()


""""""


class DependencyInjectorFinder(importlib.abc.MetaPathFinder):
    """"""

    def __init__(self, loader):
        self._loader = loader

    def find_spec(self, fullname, path, target=None):
        """"""
        print("spec", fullname, path, target)
        if self._loader.provides(fullname):
            return self._gen_spec(fullname)
        return None

    def _gen_spec(self, fullname):
        spec = importlib.machinery.ModuleSpec(fullname, self._loader)
        return spec


class DependencyInjectorLoader(importlib.abc.Loader):
    """"""

    _COMMON_PREFIX = "myapp.virtual."

    def __init__(self):
        self._services = {}
        # create a dummy module to return when Python attempts to import
        # myapp and myapp.virtual, the :-1 removes the last "." for
        # aesthetic reasons :)
        self._dummy_module = types.ModuleType(self._COMMON_PREFIX[:-1])
        # set __path__ so Python believes our dummy module is a package
        # this is important, since otherwise Python will believe our
        # dummy module can have no submodules
        self._dummy_module.__path__ = []

    def provide(self, service_name, module):
        """"""
        self._services[service_name] = module

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
            return self._dummy_module
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


class DependencyInjector:
    """"""

    def __init__(self):
        self._loader = DependencyInjectorLoader()
        self._finder = DependencyInjectorFinder(self._loader)

    def install(self):
        """"""
        sys.meta_path.append(self._finder)

    def provide(self, service_name, module):
        """"""
        self._loader.provide(service_name, module)


class FrontendModule:
    """"""

    class Popup:
        """"""

        def __init__(self, message):
            self._message = message

        def display(self):
            """"""
            print("Popup:", self._message)


def loader() -> N:
    """"""
    sys.meta_path.insert(0, CelestineMetaFinder())

    injector = DependencyInjector()
    # we could install() and then provide() if we wanted, order isn't
    # important for the below two calls
    injector.provide("frontend", FrontendModule())
    injector.install()
    # note that these last three lines could exist in any other
    # source file,
    # as long as injector.install() was called somewhere first
    import myapp.virtual.frontend as frontend

    popup = frontend.Popup("Hello World!")
    popup.display()
