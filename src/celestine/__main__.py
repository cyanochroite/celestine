"""This is the main file. It runs first."""
import os
import sys


sys.path.append(os.path.dirname(sys.path[0]))

load = __import__("celestine")

session = load.module("session")

sys.exit(session.application.main(session))
