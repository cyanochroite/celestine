"""Central place for loading and importing external files."""

import os
import pathlib

from celestine import load
from celestine.typed import (
    GE,
    L,
    N,
    S,
    T,
)


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


def walk(top):
    """"""
    path = []
    file = []
    for dirpath, dirnames, filenames in os.walk(top):
        for dirname in dirnames:
            path.append((dirpath, dirname))
        for filename in filenames:
            file.append((dirpath, filename))
    return (path, file)


def walk_module(top: S) -> GE[T[S, L[S], L[S]], N, N]:
    """"""
    for dirpath, dirnames, filenames in os.walk(top):
        if ".mypy_cache" in dirnames:
            dirnames.remove(".mypy_cache")
        if "__pycache__" in dirnames:
            dirnames.remove("__pycache__")
        yield (dirpath, dirnames, filenames)


def walk_directory(top: S) -> GE[S, N, N]:
    """"""
    for dirpath, dirnames, _ in walk_module(top):
        for dirname in dirnames:
            yield os.path.join(dirpath, dirname)


def walk_file(top: S) -> GE[S, N, N]:
    """"""
    for dirpath, _, filenames in os.walk(top):
        for filename in filenames:
            yield os.path.join(dirpath, filename)
