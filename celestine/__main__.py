""""""

import importlib
import os
import sys

sys.path[0] = os.path.dirname(sys.path[0])

celestine = importlib.import_module("celestine")
celestine.main(sys.argv[1:], True)

# -a viewer main -l en -d D:/size/
