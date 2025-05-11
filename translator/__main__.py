""""""

import importlib
import os
import sys

if __name__ == "__main__":
    parent, name = os.path.split(sys.path[0])
    sys.path.insert(0, parent)
    importlib.import_module(name)
