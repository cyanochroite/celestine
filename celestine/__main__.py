""""""

import importlib
import os
import sys

path = os.path.dirname(sys.path[0])
sys.path.insert(0, path)

celestine = importlib.import_module("celestine")
celestine.main(sys.argv[1:], True)
