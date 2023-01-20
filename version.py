""""""

import os
import shutil
import itertools
import sys

from celestine import load

from celestine.typed import N
from celestine.typed import S

MYPY = ".mypy_cache"


def kill_cache(target: S) -> N:
    """Cahed files infest the project. Remove them."""
    path = load.pathfinder()
    for (directory, _, _) in os.walk(path):
        if directory.endswith(target):
            shutil.rmtree(directory)


def walk_file(top='.'):
    """"""
    file = []
    itter = os.walk(top)

    def loop(dirpath, dirnames, filenames):
        zero = "zero"
        if dirnames:
            zero = dirnames[0]
        if filenames:
            zero = filenames[0]
        return dirpath + zero

    file = itertools.starmap(loop, itter)
    cat = list(file)
    for item in cat:
        print(file)
    return file


def private(directory):
    """"""
    one = directory.startswith(".")
    two = directory.startswith("_")
    return one or two


def public(directory):
    """"""
    return not private(directory)


def walk_file(top='.'):
    """"""
    python = ["python_3_10.py", "python_3_11.py"]
    for (dirpath, dirnames, filenames) in os.walk(top):
        if "." in dirpath:
            continue
        dirname = list(filter(public, dirnames))
        if dirname:
            continue
        filename = [file for file in filenames if file in python]
        if filename:
            yield dirpath


def walk(top):
    """"""
    for item in walk_file(top):
        print(item)


car = sys.path

walk(load.pathfinder())
