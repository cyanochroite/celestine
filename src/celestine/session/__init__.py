"""Celestine Image Viewer"""
"""Load and save user settings from a file."""

import sys
import os.path
import configparser
asset = sys.path[0]
directory = os.path.dirname(sys.path[0])

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import PYTHON


from celestine.keyword.main import CELESTINE
from celestine.keyword.main import CONFIGURATION


from celestine.core import load

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import TASK


from celestine.keyword.main import application as applications


def load_application(config):
    try:
        argumentation = sys.argv[1]
        if argumentation not in applications:
            parser.parse_args()
    except IndexError:
        try:
            configuration = config.load(directory, CELESTINE, CONFIGURATION)
            argumentation = configuration[CELESTINE][APPLICATION]
        except KeyError:
            configuration = config.load_default()
            argumentation = configuration[CELESTINE][APPLICATION]
    return load.module(APPLICATION, argumentation)


from celestine.session.argument import Argument
from celestine.session.configuration import Configuration
from celestine.session.parser import Parser

from celestine.session.python import python


class Session():
    def __init__(self, directory):
        self.directory = directory

#        self.configuration = Configuration(directory)
        self.python = python()

        self.config = Configuration(directory)
        self.configuration = self.config.load(directory)

        self.application = sys.argv[1]
        self.window = load.module("window", "main")


    def main(self):
        module = load.module("application", self.application)

        argument = Argument()
        configuration = configparser.ConfigParser()

        self.argument = module.argument(Argument())
        self.configuration = module.configuration(configuration)

        confree = load.module("application", "terminal", "configure")
        configuration = confree.configure(configuration)


        self.parser = Parser(directory, self.configuration)

        temargument = self.parser.parse(self)

        module = load.module("application", self.application, self.task)
        return module.main(self)

