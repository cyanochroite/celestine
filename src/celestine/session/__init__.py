"""Celestine Image Viewer"""
"""Load and save user settings from a file."""

import sys
import os.path

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
from celestine.application.terminal.configure import configuration_celestine


class Session():
    def __init__(self, directory):
        self.directory = directory

        self.argument = Argument()
#        self.configuration = Configuration(directory)
        self.parser = Parser(directory)
        self.python = python()

        self.app_name = sys.argv[1]

        config = Configuration(directory)
        self.configuration = config.load(directory)
        self.default = configuration_celestine()

        self.application = load_application(self.configuration)
        self.window = load.module("window", "main")

    def parse(self, session):
        argument = self.argument.parser.parse_args()
        application = self.load_attribute(argument, APPLICATION)
        task = self.load_attribute(argument, TASK)
        language = self.load_attribute(argument, LANGUAGE)

        self.task_name = task

        session.application = load.module(APPLICATION, application)
        session.task = load.module(APPLICATION, application, task)
        session.language = load.module(LANGUAGE, language)
        session.asset = sys.path[0]

    def load_attribute(self, argument, attribute):
        cat = getattr(argument, attribute)
        if cat:
            return cat

        try:
            argg = self.configuration[CELESTINE][attribute]
        except KeyError:
            argg = self.default[CELESTINE][attribute]
        return argg
