""""""

import os
import sys
import PIL
import PIL.Image

sys.path[0] = os.path.dirname(sys.path[0])

celestine = __import__("celestine")
celestine.main(sys.argv[1:], True)
