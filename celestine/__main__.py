"""
Run the program from the command line.

Add the parent directory to the path so we can find ourself.
"""

import importlib
import pathlib
import sys

if __name__ == "__main__":
    path = pathlib.Path(sys.path[0])
    sys.path.insert(0, str(path.parent))
    celestine = importlib.import_module("celestine")
    celestine.main("celestine.application")
