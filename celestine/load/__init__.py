"""Central place for loading and importing external files."""


import importlib

from celestine.data import CELESTINE
from celestine.typed import (
    A,
    B,
    C,
    D,
    M,
    N,
    S,
)
from celestine.unicode import (
    FULL_STOP,
    LOW_LINE,
)

from . import many as _many
from . import pathway as _pathway

type FN = C[[N], N]

FUNCTION = "<function"
PACKAGE = "package"

pathway = _pathway
many = _many

########################################################################


def package(base: S, *path: S) -> M:
    """Load an external package from the system path."""
    iterable = [base, *path]
    name = FULL_STOP.join(iterable)
    file = __import__(name)
    for item in path:
        file = getattr(file, item)
    if "from" not in repr(file):
        raise ModuleNotFoundError(f"Module failed to load: {name}")
    return file


def module(*path: S) -> M:
    """Load an internal module from anywhere in the application."""
    return package(CELESTINE, *path)


def attribute(*path: S) -> A:
    """Functions like the 'from package import item' syntax."""
    iterable = [*path]
    name = iterable.pop(-1)
    item = module(*iterable)
    result = getattr(item, name)
    return result


def redirect(*path: S) -> N:
    """
    Loads a function from the specified path, and then runs it.

    :param path: The last item is the function name.
    """
    function = attribute(*path)
    function()


########################################################################


def package(base: S, *path: S) -> M:
    """Load an external package from the system path."""
    iterable = [base, *path]
    name = FULL_STOP.join(iterable)
    _package = base
    _module = importlib.import_module(name, _package)
    return _module


def module(*path: S) -> M:
    """Load an internal module from anywhere in the application."""
    return package(CELESTINE, *path)


def attribute(*path: S) -> A:
    """Functions like the 'from package import item' syntax."""
    iterable = [*path]
    name = iterable.pop(-1)
    item = module(*iterable)
    result = getattr(item, name)
    return result


def redirect(*path: S) -> N:
    """
    Loads a function from the specified path, and then runs it.

    :param path: The last item is the function name.
    """
    function = attribute(*path)
    function()


########################################################################


def functions(_module: M) -> D[S, FN]:
    """Load from module all functions and turn them into dictionary."""
    _dictionary = vars(_module)
    items = _dictionary.items()
    iterable = {
        key: value
        for key, value in items
        if repr(value).startswith(FUNCTION)
    }
    return iterable


def attempt(*path: S) -> B:
    """Attempt to load a package and return the result."""
    try:
        module(*path)
        return True
    except ModuleNotFoundError:
        pass
    return False


def module_fallback(*path: S) -> M:
    """
    Load an internal module from anywhere in the application.

    If the last item is none then load the package instead.
    """
    iterable = [*path]
    pop = iterable.pop(-1)
    fallback = module(*path) if pop else module(*iterable)
    return fallback


def dictionary(*path: S) -> D[S, S]:
    """Load from module all key value pairs and make it a dictionary."""
    _module = module(*path)
    _dictionary = vars(_module)
    mapping = {
        key: value
        for key, value in _dictionary.items()
        if not key.startswith(LOW_LINE)
    }
    return mapping


def module_to_name(_module: M) -> S:
    """"""
    string = repr(_module)
    array = string.split("'")
    name = array[1]
    split = name.split(".")
    section = split[-1]
    return section


####


def method(name: S, *path: S):
    """"""
    return getattr(module(*path), name)


####


def package_dependency(name: S, fail) -> M:
    """Attempt to make loading packages easier."""
    try:
        flag = package(CELESTINE, PACKAGE, name)
    except ModuleNotFoundError:
        flag = fail
    return flag
