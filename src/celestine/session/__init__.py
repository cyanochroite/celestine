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


class Session():
    def __init__(self, directory):
        self.directory = directory

#        self.configuration = Configuration(directory)

        self.config = Configuration(directory)
        self.configuration = self.config.load(directory)

        try:
            self.application = sys.argv[1]
        except IndexError:
            print("hack and bad default?")
            sys.argv.append("tkinter")
            self.application = sys.argv[1]

        self.window = load.module("window", "main")



    def figtree(self, configuration, application):
        """Build up the configuration file."""
        module = load.module("application", application)
        configuration.add_section(application)
        configuration = module.configuration(configuration)
        configuration.set(application, "task", "main")
        return configuration
    
    
        
    
    def main(self):
        module = load.module("application", self.application)

        argument = Argument()

        self.argument = module.argument(Argument())

        confree = load.module("application", "terminal", "configure")

        configuration = configparser.ConfigParser()
        configuration = self.figtree(configuration, "terminal")
        configuration = self.figtree(configuration, self.application)
        self.configuration = configuration
        
        self.parser = Parser(directory, configuration)

        temargument = self.parser.parse(self)

        self.module = load.module("application", self.application, self.task)
        return self.module.main(self)

