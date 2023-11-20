"""Central place for loading and importing external files."""


import importlib


from celestine.typed import (
    FN,
    LS,
    D,
    M,
    S,
    string,
)
from celestine.unicode import FULL_STOP
from celestine.data import CELESTINE
from celestine.typed import (
    FN,
    A,
    B,
    D,
    M,
    N,
    S,
)

from celestine.typed import string
from celestine.unicode import (
    FULL_STOP,
    LATIN_SMALL_LETTER_C,
    LATIN_SMALL_LETTER_F,
    LATIN_SMALL_LETTER_I,
    LATIN_SMALL_LETTER_N,
    LATIN_SMALL_LETTER_O,
    LATIN_SMALL_LETTER_P,
    LATIN_SMALL_LETTER_T,
    LATIN_SMALL_LETTER_U,
    LATIN_SMALL_LETTER_Y,
    LATIN_SMALL_LETTER_P,
    LATIN_SMALL_LETTER_A,
    LATIN_SMALL_LETTER_C,
    LATIN_SMALL_LETTER_K,
    LATIN_SMALL_LETTER_A,
    LATIN_SMALL_LETTER_G,
    LATIN_SMALL_LETTER_E,
    LESS_THAN_SIGN,
    SPACE,
)
from celestine.unicode import (
    FULL_STOP,
    LOW_LINE,
)
import os
import pathlib
import sys
from importlib.resources import files

from celestine.data import CELESTINE
from celestine.typed import (
    LS,
    P,
    S,
)
from celestine.unicode import NONE



FUNCTION = string(
    LESS_THAN_SIGN,
    LATIN_SMALL_LETTER_F,
    LATIN_SMALL_LETTER_U,
    LATIN_SMALL_LETTER_N,
    LATIN_SMALL_LETTER_C,
    LATIN_SMALL_LETTER_T,
    LATIN_SMALL_LETTER_I,
    LATIN_SMALL_LETTER_O,
    LATIN_SMALL_LETTER_N,
    SPACE,
)

PACKAGE = string(
    LATIN_SMALL_LETTER_P,
    LATIN_SMALL_LETTER_A,
    LATIN_SMALL_LETTER_C,
    LATIN_SMALL_LETTER_K,
    LATIN_SMALL_LETTER_A,
    LATIN_SMALL_LETTER_G,
    LATIN_SMALL_LETTER_E,
)

PYTHON_EXTENSION = string(
    FULL_STOP,
    LATIN_SMALL_LETTER_P,
    LATIN_SMALL_LETTER_Y,
)



def clamp(minimum, midterm, maximum):
    """The order of the inputs actually don't matter."""
    return sorted((minimum, midterm, maximum))[1]



########################################################################

def package(base: S, *path: S) -> M:
    """Load an external package from the system path."""
    iterable = [base, *path]
    name = FULL_STOP.join(iterable)
    result = importlib.import_module(name, package=base)
    return result


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






#######


def functions(module: M) -> D[S, FN]:
    """Load from module all functions and turn them into dictionary."""
    dictionary = vars(module)
    iterable = {
        key: value
        for key, value in dictionary.items()
        if FUNCTION in repr(value)
    }
    return iterable


def decorator_name(module: M, name: S) -> S:
    """Load from module all functions and turn them into dictionary."""
    dictionary = vars(module)
    text = string(FUNCTION, name, FULL_STOP)
    for key, value in dictionary.items():
        if text in repr(value):
            return key
    raise LookupError("No function with '@main' found.")


def decorators(module: M, name: S) -> D[S, FN]:
    """Load from module all functions and turn them into dictionary."""
    dictionary = vars(module)
    text = string(FUNCTION, name, FULL_STOP)
    iterable = {
        key: value
        for key, value in dictionary.items()
        if text in repr(value)
    }
    return iterable


def function_page(module: M) -> LS:
    """Load from module all functions and turn them into dictionary."""

    dictionary = functions(module)
    iterable = [key for key, value in dictionary.items()]
    return iterable




####

"""Central place for loading and importing external files."""

import os
import pathlib

from celestine.typed import (
    GP,
    LP,
    LS,
    G,
    N,
    P,
    S,
    T,
)


def walk(*path: S) -> G[T[S, LS, LS], N, N]:
    """Yields a 3-tuple (dirpath, dirnames, filenames)."""
    top = pathlib.Path(*path)
    topdown = True
    onerror = None
    followlinks = False
    return os.walk(top, topdown, onerror, followlinks)


def file(top: P, include: LS, exclude: LS) -> GP:
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


def python(top: P, include: LS, exclude: LS) -> LP:
    """"""
    include = [".py", *include]
    exclude = [
        ".mypy_cache",
        ".ruff_cache",
        "__pycache__",
        *exclude,
    ]
    return file(top, include, exclude)


# module

def remove_empty_directories(path: P) -> N:
    """"""
    empty = True
    for content in path.iterdir():
        if content.is_dir():
            empty &= remove_empty_directories(content)
        else:
            empty = False
    if empty:
        os.rmdir(path)
    return empty




########

def pathroot() -> P:
    """When running as a package, sys.path[0] is wrong."""
    for path in sys.path:
        directory = pathlib.Path(path, CELESTINE)
        if directory.is_dir():
            return pathlib.Path(path)
    directory = pathlib.Path(os.curdir)
    return directory


def pathfinder() -> P:
    """When running as a package, sys.path[0] is wrong."""
    for path in sys.path:
        directory = pathlib.Path(path, CELESTINE)
        if directory.is_dir():
            return directory
    directory = pathlib.Path(os.curdir)
    return directory


def safe_path(*path: S) -> P:
    """Might not be right be good for input from user."""
    root = pathfinder()

    join = os.path.join(root, *path)
    normcase = os.path.normcase(join)
    normpath = os.path.normpath(normcase)
    realpath = os.path.realpath(normpath, strict=True)

    safe = os.path.commonpath((root, realpath))

    if not os.path.samefile(root, safe):
        raise RuntimeError()

    return pathlib.Path(realpath)


def pathway(*path: S) -> P:
    """"""
    _package = pathfinder()
    return pathlib.Path(_package, *path)


def pathway_root(*path: S) -> P:
    """"""
    _package = pathroot()
    return pathlib.Path(_package, *path)


def python(*path: S) -> P:
    """"""
    base = pathway(*path)
    join = NONE.join([str(base), PYTHON_EXTENSION])
    return pathlib.Path(join)


def argument(*path: S) -> LS:
    """
    Build a path to the selected package.

    Scan all items in directory.
    Return a list of items that are not private, such as '.private' or
    '_private'. (First letter is not a symbol.)
    Strip off all file extensions, if any.
    """
    directory = pathway(*path)
    try:
        folder = os.listdir(directory)
    except FileNotFoundError:
        return []

    splitext = os.path.splitext
    result = [splitext(file)[0] for file in folder if file[0].isalpha()]

    result.sort()
    return result


#########


def asset(file: S) -> P:
    """"""
    # TODO: check if other path witchcraft needs replacing with this:
    data = "celestine.data"
    item = files(data).joinpath(file)
    return item
