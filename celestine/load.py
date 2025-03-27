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
    CA,
    CN,
    GM,
    GP,
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
    ignore,
)

########################################################################


def testit(module_: M, name: S) -> B:
    """Finds the named attribute from the module."""
  
    return code
    result = None
    object_: M | CA = module_
    items = name.split(FULL_STOP)
    for item in items:
        result = getattr(object_, item)
        object_ = result
    if not result:
        raise AttributeError(module_, name)
    return result


def attribute(module_: M, name: S) -> CA:
    """Finds the named attribute from the module."""
    result = None
    object_: M | CA = module_
    items = name.split(FULL_STOP)
    for item in items:
        result = getattr(object_, item)
        object_ = result
    if not result:
        raise AttributeError(module_, name)
    return result


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
    result = package(CELESTINE, *path)
    return result


def package(base: S, *path: S) -> M:
    """Load an external package from the system path."""
    iterable = [base, *filter(None, path)]
    name = FULL_STOP.join(iterable)
    result = importlib.import_module(name)
    return result


########################################################################


def attempt(*path: S) -> B:
    """Attempt to load a package and return the result."""
    try:
        module(*path)
        result = True
    except ModuleNotFoundError:
        result = False
    return result


def module_fallback(*path: S) -> M:
    """
    Load an internal module from anywhere in the application.

    If the last item is none then load the package instead.
    """
    iterable = [*path]
    pop = iterable.pop(-1)
    result = module(*path) if pop else module(*iterable)
    return result


def module_to_name(module_: M) -> S:
    """"""
    text = repr(module_)
    array = text.split("'")
    name = array[1]
    split = name.split(".")
    result = split[-1]
    return result


####


def method(name: S, *path: S):
    """"""
    result = getattr(module(*path), name)
    return result


####


def package_dependency(name: S, fail: M) -> M:
    """Attempt to make loading packages easier."""
    try:
        result = package(CELESTINE, PACKAGE, name)
    except ModuleNotFoundError:
        result = fail
    return result


########################################################################
# Dictionary stuff


def functions(module_: M) -> D[S, CN]:
    """Load from module all functions and turn them into dictionary."""

    def test(value: S) -> B:
        name = repr(value)
        result = name.startswith(FUNCTION)
        return result

    _dictionary: D[S, A] = vars(module_)
    _items = _dictionary.items()
    result = {key: value for key, value in _items if test(value)}
    return result


def dictionary(module_: M) -> D[S, CN]:
    """Load from module all key value pairs and make it a dictionary."""

    def test(value: S) -> B:
        return not value.startswith(LOW_LINE)

    _dictionary: D[S, A] = vars(module_)
    _items = _dictionary.items()
    result = {key: value for key, value in _items if test(key)}
    return result


########


def function_page(module_: M) -> LS:
    """Load from module all functions and turn them into dictionary."""
    _dictionary = functions(module_)
    result = [key for key, _ in _dictionary.items()]
    return result


########################################################################


def walk(*path: S) -> G[T[S, LS, LS], N, N]:
    """Yields a 3-tuple (dirpath, dirnames, filenames)."""
    top = pathlib.Path(*path)
    topdown = True
    onerror = None
    followlinks = False
    yield from os.walk(top, topdown, onerror, followlinks)


def walk_file(path: P, include: LS, exclude: LS) -> GP:
    """
    Item 'name_exclude': a list of directory names to exclude.

    Item 'suffix_include': a list of file name suffix to include
    if none, it ignores it.
    """
    top = str(path)
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


def walk_python(path: P, include: LS, exclude: LS) -> GP:
    """"""
    include = [".py", *include]
    exclude = [
        ".mypy_cache",
        ".ruff_cache",
        "__pycache__",
        *exclude,
    ]
    yield from walk_file(path, include, exclude)


def walk_package(base: S) -> GM:
    """Load all decorated functions from all modules found in path."""
    find = importlib.import_module(base)
    spec = find.__spec__
    if not spec:
        raise NotImplementedError("Why is your spec None?")
    if not spec.origin:
        raise NotImplementedError("Why is your spec origin also None?")
    spot = pathlib.Path(spec.origin)
    if spot.stem != INIT:
        yield find
        return

    root = spot.parent
    walked = walk_python(root, [], [])
    for file in walked:
        with_name = file.with_name(file.stem)
        # relative to what though?
        relative_to = with_name.relative_to(root)
        parts = relative_to.parts
        strip = parts[:-1] if parts[-1] == INIT else parts
        name = FULL_STOP.join((base, *strip))
        yield importlib.import_module(name)


########################################################################


def project_root() -> P:
    """When running as a package, sys.path[0] is wrong."""
    result = pathlib.Path(os.curdir)
    for path in sys.path:
        directory = pathlib.Path(path, CELESTINE)
        if directory.is_dir():
            result = pathlib.Path(path)
            break
    return result


def project_path() -> P:
    """When running as a package, sys.path[0] is wrong."""
    result = pathlib.Path(os.curdir)
    for path in sys.path:
        directory = pathlib.Path(path, CELESTINE)
        if directory.is_dir():
            result = directory
            break
    return result


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

    result = pathlib.Path(realpath)
    return result


def pathway(*path: S) -> P:
    """"""
    _package = project_path()
    result = pathlib.Path(_package, *path)
    return result


def pathway_root(*path: S) -> P:
    """"""
    _package = project_root()
    result = pathlib.Path(_package, *path)
    return result


def python(*path: S) -> P:
    """"""
    base = pathway(*path)
    join = NONE.join([str(base), PYTHON_EXTENSION])
    result = pathlib.Path(join)
    return result


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
    result = pathlib.Path(str(item))
    return result


#########


ignore(
    argument,
    asset,
    attempt,
    attribute,
    dictionary,
    function_page,
    instance,
    method,
    module_fallback,
    module_to_name,
    package_dependency,
    pathway_root,
    python,
    safe_path,
    walk_package,
)
