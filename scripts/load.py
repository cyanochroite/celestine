""""""

import importlib.machinery
import importlib.util
import os
import pathlib
import pkgutil
from typing import TypeAlias as TA

type N = None
type P = pathlib.Path

FF: TA = importlib.machinery.FileFinder
MI: TA = pkgutil.ModuleInfo
MS: TA = importlib.machinery.ModuleSpec
# type FF = importlib.machinery.FileFinder
# type MI = pkgutil.ModuleInfo
# type MS = importlib.machinery.ModuleSpec


def clamp(minimum, midterm, maximum):
    """The order of the inputs actually don't matter."""
    return sorted((minimum, midterm, maximum))[1]


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


def modulesa(*path: S) -> L[M]:
    """Load an internal module from anywhere in the application."""

    def specs(module_info: MI) -> MS:
        (module_finder, name, _) = module_info
        finder = cast(FF, module_finder)
        spec = finder.find_spec(name)
        return cast(MS, spec)

    parent = pathlib.Path(__spec__.origin).parent
    pkgpath = pathlib.Path(parent, *path)
    paths = [str(pkgpath)]

    walk_packages = pkgutil.walk_packages(paths)
    spec = specs(walk_packages)
    module = importlib.util.module_from_spec(spec)
    return module
