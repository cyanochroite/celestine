"""This is the main file. It runs first."""
import os
import sys


directory = os.path.dirname(sys.path[0])
sys.path.append(directory)

load = __import__("celestine")

session = load.module("session").Session(directory)

sys.exit(session.application.main(session))
