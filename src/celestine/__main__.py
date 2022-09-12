"""This is the main file. It runs first."""
import os
import sys


path = sys.path[0]
directory = os.path.dirname(path)
sys.path.append(directory)


module = __import__("celestine")
args = sys.argv[1:]
main = module.main(directory, args, True)
sys.exit(main)
