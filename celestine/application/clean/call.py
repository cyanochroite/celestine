""""""

import pathlib
import sys

from black import patched_main as black
from isort.main import main as isort


def run(package):
    """"""
    try:
        package()
    except SystemExit:
        pass


def clean(**star):
    """"""

    root = sys.path[0]
    path = pathlib.Path(root, "celestine")
    sys.argv = [root, str(path)]

    run(black)
    run(isort)

    print("I am a talking cow.")
