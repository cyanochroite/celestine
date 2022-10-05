import os
import sys


path = sys.path[0]
directory = os.path.dirname(path)
sys.path.append(directory)

def zero(page):
    with page.line("head") as line:
        line.label("title", "Page 0")


celestine = __import__("celestine")
argv = sys.argv[1:]
celestine.main(directory, argv, True, [zero])
