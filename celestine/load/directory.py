"""Central place for loading and importing external files."""

import os

from celestine.typed import GE
from celestine.typed import N
from celestine.typed import S


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


def walk_directory(top: S) -> GE[S, N, N]:
    """"""
    for (dirpath, dirnames, _) in os.walk(top):
        for dirname in dirnames:
            yield os.path.join(dirpath, dirname)


def walk_file(top: S) -> GE[S, N, N]:
    """"""
    for (dirpath, _, filenames) in os.walk(top):
        for filename in filenames:
            yield os.path.join(dirpath, filename)
