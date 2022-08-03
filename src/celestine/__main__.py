"""This is the main file. It runs first."""
import os
import sys


directory = os.path.dirname(sys.path[0])
sys.path.append(directory)

load = __import__("celestine")

session = load.module("session").Session(directory)

argmain = load.module("application", session.app_name, "argument")

argmain.argument(session)

argument = session.parse(session)

module = load.module("application", session.app_name, session.task_name)

sys.exit(module.main(session))
