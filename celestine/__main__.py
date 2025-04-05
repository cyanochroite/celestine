"""
Run the program from the command line.

Add the parent directory to the path so we can find ourself.
"""

import importlib
import os
import sys

if __name__ == "__main__":
    PATH = sys.path[0]
    parent = os.path.dirname(PATH)
    sys.path.insert(0, parent)
    celestine = importlib.import_module("celestine")
    celestine.main()
