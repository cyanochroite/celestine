""""""

import os
import pathlib
import sys

path = pathlib.Path("COW", "DOG.TXT")
print(path.suffix)


sys.path[0] = os.path.dirname(sys.path[0])

celestine = __import__("celestine")
celestine.main(sys.argv[1:], True)
