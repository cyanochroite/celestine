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
