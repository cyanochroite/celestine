import os
import sys


path = sys.path[0]
directory = os.path.dirname(path)
sys.path.append(directory)


view = __import__("view")
argv = sys.argv[1:]
view.main(directory, argv, True)
