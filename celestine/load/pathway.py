"""Central place for loading and importing external files."""

import os
import pathlib
import sys

from celestine.data import CELESTINE
from celestine.typed import (
    LS,
    P,
    S,
)
from celestine.unicode import NONE

from .data import PYTHON_EXTENSION


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


def asset(item: S) -> P:
    """"""
    return pathway("data", item)
