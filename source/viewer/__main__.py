import os
import sys


PATH = sys.path[0]
directory = os.path.dirname(PATH)
sys.path.append(directory)


viewer = __import__("viewer")
argv = sys.argv[1:]
viewer.main(directory, argv, True)
