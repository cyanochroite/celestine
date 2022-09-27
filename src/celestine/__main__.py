import os
import sys


path = sys.path[0]
directory = os.path.dirname(path)
sys.path.append(directory)


celestine = __import__("celestine")
argv = sys.argv[1:]
celestine.main(directory, argv, True)
