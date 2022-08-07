
from celestine.session.argument import Argument
from celestine.session.configuration import Configuration
from celestine.session.python import python

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import TASK

from celestine.keyword.main import CELESTINE

import sys

from celestine import module
class Parser():
    def __init__(self, directory, default):
        self.argument = Argument()
        config = Configuration(directory)
        self.configuration = config.load()
        self.default = default


    def load_attribute(self, argument, attribute):
        cat = getattr(argument, attribute)
        if cat:
            return cat
                
        try:
            argg = self.configuration[CELESTINE][attribute]
        except KeyError:
            argg = self.default[CELESTINE][attribute]
        return argg

    def parse(self, session):
        argument = session.argument.parser.parse_args()
        session.argument = argument
        session.application = self.load_attribute(argument, APPLICATION)
        session.task = self.load_attribute(argument, TASK)
        session.language =self.load_attribute(argument, LANGUAGE)

