import os
import sys


PATH = sys.path[0]
directory = os.path.dirname(PATH)
sys.path.append(directory)


celestine = __import__("celestine")
argv = sys.argv[1:]
celestine.main(argv, True)
