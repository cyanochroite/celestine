"""Central place for loading and importing external files."""

import os

from celestine.typed import GE
from celestine.typed import N
from celestine.typed import S
from celestine.typed import L

from celestine import load


def find(target: S) -> L[S]:
    """Find all project directories with this name."""
    path = load.pathfinder()
    array = [
        os.path.relpath(directory, start=path)
        for directory in walk_directory(path)
        if directory.endswith(target)
    ]
    return array


def walk(top):
    """"""
    path = []
    file = []
    for (dirpath, dirnames, filenames) in os.walk(top):
        for dirname in dirnames:
            path.append((dirpath, dirname))
        for filename in filenames:
            file.append((dirpath, filename))
    return (path, file)


def module(top: S) -> GE[S, N, N]:
    """"""
    for (dirpath, dirnames, _) in os.walk(top):
        if ".mypy_cache" in dirnames:
            dirnames.remove(".mypy_cache")
        if "__pycache__" in dirnames:
            dirnames.remove("__pycache__")
        for dirname in dirnames:
            yield os.path.join(dirpath, dirname)


def walk_directory(top: S) -> GE[S, N, N]:
    """"""
    for (dirpath, dirnames, _) in os.walk(top):
        if ".mypy_cache" in dirnames:
            dirnames.remove(".mypy_cache")
        if "__pycache__" in dirnames:
            dirnames.remove("__pycache__")
        for dirname in dirnames:
            yield os.path.join(dirpath, dirname)


def walk_file(top: S) -> GE[S, N, N]:
    """"""
    for (dirpath, _, filenames) in os.walk(top):
        for filename in filenames:
            yield os.path.join(dirpath, filename)
