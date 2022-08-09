
from celestine.session.argument import Argument
from celestine.session.configuration import Configuration
from celestine.session.python import python

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import TASK

from celestine.keyword.main import CELESTINE

import sys

from celestine.session.python import python


from celestine import module


class Parser():
    def __init__(self, directory, default):
        self.argument = Argument()
        config = Configuration(directory)
        self.configuration = config.load()
        self.default = default

    def load_attribute(self, argument, section, attribute):
        cat = getattr(argument, attribute)
        if cat:
            return cat

        try:
            argg = self.configuration[section][attribute]
        except KeyError:
            argg = self.default[section][attribute]
        return argg

    def parse(self, session):
        argument = session.argument.parser.parse_args()
        session.argument = argument
        session.application = self.load_attribute(argument, CELESTINE, APPLICATION)
        self.application = session.application
        session.task = self.load_attribute(argument, session.application, TASK)

        language = self.load_attribute(argument, CELESTINE, LANGUAGE)
        session.language = module(LANGUAGE, language)

        session.python = python()
