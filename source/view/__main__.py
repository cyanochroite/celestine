import os
import sys


PATH = sys.path[0]
print(sys.path)
directory = os.path.dirname(PATH)
sys.path.append(directory)


view = __import__("view")
argv = sys.argv[1:]
view.main(directory, argv, True)
