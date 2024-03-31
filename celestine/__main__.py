""""""

import importlib
import pathlib
import sys

CELESTINE = "celestine"

path = pathlib.Path(sys.path[0])
if path.name == CELESTINE:
    sys.path[0] = str(path.parent)

celestine = importlib.import_module(CELESTINE)
celestine.main(sys.argv[1:], True)
