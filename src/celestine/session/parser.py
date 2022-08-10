
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
    def load_attribute(self, session, section, attribute):
        cat = getattr(session.argument, attribute)
        if cat:
            return cat

        try:
            argg = session.configuration[section][attribute]
        except KeyError:
            argg = session.default.configuration[section][attribute]
        return argg

    def parse(self, session):
        argument = session.argument.parser.parse_args()
        session.argument = argument
        session.application = self.load_attribute(session, CELESTINE, APPLICATION)
        self.application = session.application
        session.task = self.load_attribute(session, session.application, TASK)

        language = self.load_attribute(session, CELESTINE, LANGUAGE)
        session.language = module(LANGUAGE, language)

        session.python = python()
