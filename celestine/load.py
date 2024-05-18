"""Central place for loading and importing external files."""

import importlib
import importlib.resources
import os
import pathlib
import sys

from celestine.literal import (
    CELESTINE,
    FULL_STOP,
    FUNCTION,
    INIT,
    LOW_LINE,
    NONE,
    PACKAGE,
    PYTHON_EXTENSION,
)
from celestine.typed import (
    FN,
    GM,
    GP,
    LP,
    LS,
    A,
    B,
    D,
    G,
    M,
    N,
    P,
    S,
    T,
    string,
)

########################################################################


def function(*path: S) -> A:
    """Functions like the 'from package import item' syntax."""
    iterable = [*path]
    name = iterable.pop(-1)
    item = module(*iterable)
    result = getattr(item, name)
    return result


def instance(*path: S) -> A:
    """Functions like the 'from package import item' syntax."""
    call = function(*path)
    result = call()
    return result


def module(*path: S) -> M:
    """Load an internal module from anywhere in the application."""
    return package(CELESTINE, *path)


def modules(*path: S) -> GM:
    """Load an internal module from anywhere in the application."""
    yield from packages(CELESTINE, *path)


def package(base: S, *path: S) -> M:
    """Load an external package from the system path."""
    iterable = [base, *path]
    name = FULL_STOP.join(iterable)
    result = importlib.import_module(name)
    return result


def packages(base: S, *path: S) -> GM:
    """Load an external package from the system path."""
    find = importlib.import_module(base)
    spec = find.__spec__
    info = spec.origin if spec else project_path()
    spot = pathlib.Path(str(info))
    root = spot.parent

    root = project_path()
    top = pathlib.Path(root, *path)

    walked = walk_python(top, [], [])
    walker = [top, *walked]
    for file in walker:
        with_name = file.with_name(file.stem)
        relative_to = with_name.relative_to(root)
        parts = relative_to.parts
        strip = parts[:-1] if parts[-1] == INIT else parts
        yield package(base, *strip)


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


def module_to_name(_module: M) -> S:
    """"""
    text = repr(_module)
    array = text.split("'")
    name = array[1]
    split = name.split(".")
    section = split[-1]
    return section


####


def method(name: S, *path: S):
    """"""
    return getattr(module(*path), name)


####


def package_dependency(name: S, fail: M) -> M:
    """Attempt to make loading packages easier."""
    try:
        flag = package(CELESTINE, PACKAGE, name)
    except ModuleNotFoundError:
        flag = fail
    return flag


########################################################################
# Dictionary stuff


def _dictionary_items(_module: M) -> T[S, A]:
    _dictionary: D[S, A] = vars(_module)
    _items = _dictionary.items()
    return _items


def functions(_module: M) -> D[S, FN]:
    """Load from module all functions and turn them into dictionary."""

    def test(value: S) -> B:
        return FUNCTION in repr(value)

    _dictionary = _dictionary_items(_module)
    mapping = {key: value for key, value in _dictionary if test(value)}
    return mapping


def dictionary(_module: M) -> D[S, FN]:
    """Load from module all key value pairs and make it a dictionary."""

    def test(value: S) -> B:
        return not value.startswith(LOW_LINE)

    _dictionary = _dictionary_items(_module)
    mapping = {key: value for key, value in _dictionary if test(key)}
    return mapping


def decorators(_module: M, name: S) -> D[S, FN]:
    """Load from module all functions and turn them into dictionary."""
    _dictionary = _dictionary_items(_module)
    text = string(FUNCTION, name, FULL_STOP)

    def test(value: S) -> B:
        return text in repr(value)

    iterable = {key: value for key, value in _dictionary if test(value)}
    return iterable


########


def function_page(_module: M) -> LS:
    """Load from module all functions and turn them into dictionary."""
    _dictionary = functions(_module)
    iterable = [key for key, _ in _dictionary.items()]
    return iterable


########################################################################


def walk(*path: S) -> G[T[S, LS, LS], N, N]:
    """Yields a 3-tuple (dirpath, dirnames, filenames)."""
    top = pathlib.Path(*path)
    topdown = True
    onerror = None
    followlinks = False
    yield from os.walk(top, topdown, onerror, followlinks)


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


########################################################################


def project_root() -> P:
    """When running as a package, sys.path[0] is wrong."""
    for path in sys.path:
        directory = pathlib.Path(path, CELESTINE)
        if directory.is_dir():
            return pathlib.Path(path)
    directory = pathlib.Path(os.curdir)
    return directory


def project_path() -> P:
    """When running as a package, sys.path[0] is wrong."""
    for path in sys.path:
        directory = pathlib.Path(path, CELESTINE)
        if directory.is_dir():
            return directory
    directory = pathlib.Path(os.curdir)
    return directory


def safe_path(*path: S) -> P:
    """Might not be right be good for input from user."""
    root = project_path()

    join: S = os.path.join(root, *path)
    normcase: S = os.path.normcase(join)
    normpath: S = os.path.normpath(normcase)
    realpath: S = os.path.realpath(normpath, strict=True)

    safe = os.path.commonpath((root, realpath))

    if not os.path.samefile(root, safe):
        raise RuntimeError()

    return pathlib.Path(realpath)


def pathway(*path: S) -> P:
    """"""
    _package = project_path()
    return pathlib.Path(_package, *path)


def pathway_root(*path: S) -> P:
    """"""
    _package = project_root()
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
        folder: LS = os.listdir(directory)
    except FileNotFoundError:
        return []

    splitext = os.path.splitext
    result = [splitext(file)[0] for file in folder if file[0].isalpha()]

    result.sort()
    return result


#########


def asset(file: S) -> P:
    """"""
    data = "celestine.data"
    item = importlib.resources.files(data).joinpath(file)
    return item
