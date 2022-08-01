"""This is the main file. It runs first."""
import os
import sys


sys.path.append(os.path.dirname(sys.path[0]))

session = __import__("celestine")

sys.exit(session.application.main(session))
