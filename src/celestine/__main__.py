"""This is the main file. It runs first."""
import os.path
import sys

directory = os.path.dirname(sys.path[0])
sys.path.append(directory)


import argparse

from celestine.keyword.main import CELESTINE

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import application

from celestine.keyword.main import application
from celestine.core import load




from celestine.core import load


session = __import__(CELESTINE)

session.directory = directory

session.application.main(session)

sys.exit()
