"""This is the main file. It runs first."""
import os
import sys


path = sys.path[0]
directory = os.path.dirname(path)
sys.path.append(directory)


load = __import__("celestine")
module = load.module("session")
session = module.Session(directory)
main = session.main()
sys.exit(main)
