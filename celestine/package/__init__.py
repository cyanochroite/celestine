"""Run a bunch of auto formaters."""

import os
import sys


def path():
    """"""
    return os.path.join(root(), "celestine")


def root():
    """"""
    return sys.path[0]


def run(function: None, argument: list[str]) -> None:
    """"""
    argv = sys.argv

    try:
        sys.argv = [root(), path(), *argument]
        function()
    except SystemExit:
        pass

    sys.argv = argv
