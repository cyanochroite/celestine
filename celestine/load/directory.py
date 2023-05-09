"""Central place for loading and importing external files."""

import os
import pathlib

from celestine import load
from celestine.typed import (
    GE,
    L,
    N,
    P,
    S,
    T,
)


def walk(folder, name_exclude, suffix_include):
    """
    Name_exclude: a list of directory names to exclude.

    suffix_include: a list of file name suffix to include
    if none, it ignores it.
    """

    directory = []
    files = []

    top = folder
    topdown = True
    onerror = None
    followlinks = False
    os_walk = os.walk(top, topdown, onerror, followlinks)

    for dirpath, dirnames, filenames in os_walk:
        for dirname in dirnames:
            path = pathlib.Path(dirpath, dirname)
            if name_exclude and path.name in name_exclude:
                dirnames.remove(dirname)
            else:
                directory.append(path)

        for filename in filenames:
            path = pathlib.Path(dirpath, filename)
            suffix = path.suffix
            if not suffix_include or suffix in suffix_include:
                files.append(path)
            else:
                filenames.remove(filename)

    return (directory, files)


def file(top: P, include: L[S], exclude: L[S]) -> GE[P, N, N]:
    """"""

    include = set(include)
    exclude = set(exclude)

    for dirpath, dirnames, filenames in os.walk(top):
        for dirname in dirnames:
            if dirname in exclude:
                dirnames.remove(dirname)

        for filename in filenames:
            path = pathlib.Path(dirpath, filename)
            if not include or path.suffix in include:
                yield path


def python(path: P) -> L[P]:
    """"""

    include = [
        ".py",
    ]
    exclude = [
        ".mypy_cache",
        "__pycache__",
    ]
    files = list(file(path, include, exclude))
    return files


###################


def modularize(path: S, start: S) -> T[S, ...]:
    """"""
    relative = os.path.relpath(path, start)
    (root, _) = os.path.splitext(relative)
    pure = pathlib.PurePath(root)
    parts = pure.parts
    return parts


def find(target: S) -> L[T[S, ...]]:
    """Find all project directories with this name."""
    start = load.pathfinder()

    array = [
        modularize(directory, start)
        for directory in walk_file(start)
        if directory.endswith(target)
    ]
    return array


def walk_file_old(top: S) -> GE[S, N, N]:
    """"""
    for dirpath, _, filenames in os.walk(top):
        for filename in filenames:
            yield os.path.join(dirpath, filename)
