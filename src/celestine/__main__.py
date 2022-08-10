"""This is the main file. It runs first."""
import os
import sys


directory = os.path.dirname(sys.path[0])
sys.path.append(directory)

load = __import__("celestine")
module = load.module("session")
session = module.Session(directory)
main = session.main()
sys.exit(main)
