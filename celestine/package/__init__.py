""""""
import importlib
import importlib.abc
import importlib.machinery
import os
import pathlib
import sys
import types
import typing
from typing import override

from celestine import package
from celestine.typed import (
    GP,
    LP,
    LS,
    OS,
    B,
    D,
    G,
    M,
    N,
    P,
    R,
    S,
    T,
    ignore,
)
from celestine.unicode import FULL_STOP

from ._autoflake import Package as _autoflake
from ._black import Package as _black
from ._curses import Package as _curses
from ._dearpygui import Package as _dearpygui
from ._isort import Package as _isort
from ._pillow import Package as _pillow
from ._platformdirs import Package as _platformdirs
from ._pydocstringformatter import Package as _pydocstringformatter
from ._pygame import Package as _pygame
from ._pyupgrade import Package as _pyupgrade
from ._tkinter import Package as _tkinter

CELESTINE = "celestine"


def project_path() -> P:
    """When running as a package, sys.path[0] is wrong."""
    for path in sys.path:
        directory = pathlib.Path(path, CELESTINE)
        if directory.is_dir():
            return directory
    directory = pathlib.Path(os.curdir)
    return directory


class Abstract:
    """"""

    name: S
    package: M | N

    def main(self, package: M, path: S) -> N:
        """"""
        sys.argv.append(path)
        package.main()

    def module(self) -> LS:
        """The 'import PACKAGE.MODULE' name."""
        return []

    def run(self) -> N:
        """"""

        if not self.package:
            return

        argv = sys.argv

        path = str(project_path())
        sys.argv = [path, path]
        try:
            module = package(self.name, *self.module())
            self.main(module, path)
        except SystemExit:
            pass

        sys.argv = argv

    def __bool__(self) -> B:
        return self.package is not None

    def __getattr2__(self, name: S) -> S:
        return getattr(self.package, name)

    def __init__(self, name: S, pypi: OS = None, **star: R) -> N:
        self.name = name
        self.pypi = pypi or name

        # pygame prints an anoying message on import
        # so this here to hide any messages a package may print
        # when being imported
        sys_stdout = sys.stdout

        with open(
            os.devnull,
            "w",
            encoding="utf-8",
            #            stream.Mode.WRITE_TEXT.value,
            #            encoding=stream.Encoding.UTF_8.value,
        ) as stdout:
            sys.stdout = stdout  # as TextIO
            try:
                self.package = package(self.pypi)
            except ModuleNotFoundError:
                self.package = None
                # found = f"Package '{self.name}' not found."
                # install = f"Install with 'pip install {self.pypi}'."
                # message = f"{found} {install}"
                # logging.warning(message)

        sys.stdout = sys_stdout


class Package:
    """"""

    dictionary: D[S, M]

    def __getattr__(self, name: S) -> M:
        """"""
        try:
            return self.dictionary[name]
        except KeyError as error:
            message = f"'{PACKAGE}' object has no attribute '{name}'"
            raise AttributeError(message) from error

    def __init__(self, **star: R) -> N:
        self.dictionary = {}
        argument = load.argument(PACKAGE)
        for name in argument:
            attribute = load.attribute(PACKAGE, name, "Package")
            package = attribute(name)
            self.dictionary[name] = package


def walk(*path: S) -> G[T[S, LS, LS], N, N]:
    """Yields a 3-tuple (dirpath, dirnames, filenames)."""
    top = pathlib.Path(*path)
    topdown = True
    onerror = None
    followlinks = False
    return os.walk(top, topdown, onerror, followlinks)


def walk_file(top: P, include: LS, exclude: LS) -> GP:
    """
    Item 'name_exclude': a list of directory names to exclude.

    Item 'suffix_include': a list of file name suffix to include
    if none, it ignores it.
    """
    included = set(include)
    excluded = set(exclude)

    for dirpath, dirnames, filenames in walk(top):
        for dirname in dirnames:
            if dirname in excluded:
                dirnames.remove(dirname)

        for filename in filenames:
            path = pathlib.Path(dirpath, filename)
            suffix = path.suffix.lower()
            if not included or suffix in included:
                yield path


def walk_python(top: P, include: LS, exclude: LS) -> LP:
    """"""
    include = [".py", *include]
    exclude = [
        ".mypy_cache",
        ".ruff_cache",
        "__pycache__",
        *exclude,
    ]
    return walk_file(top, include, exclude)


def package(base: S, *path: S) -> M:
    """Load an external package from the system path."""
    iterable = [base, *path]
    name = FULL_STOP.join(iterable)
    result = importlib.import_module(name)
    return result


type SO = typing.Sequence[str] | None
type OM = types.ModuleType | None
type MS = importlib.machinery.ModuleSpec | None
type N = None


class Loader(importlib.abc.Loader):
    """"""

    @override
    def create_module(self, spec: importlib.machinery.ModuleSpec) -> OM:
        """"""
        name = spec.name[self.skip :]
        match name:
            case "autoflake":
                module = _autoflake(name)
            case "black":
                module = _black(name)
            case "curses":
                module = _curses(name)
            case "dearpygui":
                module = _dearpygui(name)
            case "isort":
                module = _isort(name)
            case "pillow":
                module = _pillow(name)
            case "platformdirs":
                module = _platformdirs(name)
            case "pydocstringformatter":
                module = _pydocstringformatter(name)
            case "pygame":
                module = _pygame(name)
            case "pyupgrade":
                module = _pyupgrade(name)
            case "tkinter":
                module = _tkinter(name)
            case _:
                module = None
        return module

    @override
    def exec_module(self, module: M) -> N:
        """"""
        ignore(module)

    def __init__(self):
        self.skip = len("celestine.package.")
