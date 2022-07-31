"""This is the main file. It runs first."""
import os.path
import sys

directory = os.path.dirname(sys.path[0])
sys.path.append(directory)


session = __import__("celestine")

session.directory = directory # contstrure

session.application.main(session)

sys.exit()


#sys.exit(session.application.main(session))


#terminal
#language
