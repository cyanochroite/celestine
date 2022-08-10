"""Celestine Image Viewer"""
"""Load and save user settings from a file."""

import sys
import configparser


from celestine.core import load


from celestine.keyword.main import APPLICATION
from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import TASK

from celestine.keyword.main import CELESTINE


from celestine import module


class Parser():
    def load_attribute(self, session, section, attribute):
        cat = getattr(session.argument, attribute)
        if cat:
            return cat

        try:
            argg = session.configuration[section][attribute]
        except KeyError:
            argg = session.default[section][attribute]
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


"""Load and save user settings from a file."""
import configparser

from celestine.core import load

from celestine.keyword.main import CELESTINE
from celestine.keyword.main import CONFIGURATION
from celestine.keyword.main import WRITE
from celestine.keyword.main import UTF_8


class Configuration():
    """parse configuration stuff."""

    def __init__(self, directory):
        self.directory = directory
        self.path = load.path(directory, CELESTINE, CONFIGURATION)

    def load(self, path=None):
        """Load the configuration file."""
        configuration = configparser.ConfigParser()
        configuration.read(path or self.path, encoding=UTF_8)
        return configuration

    def save(self, configuration, path=None):
        """Save the configuration file."""
        with open(path or self.path, WRITE, encoding=UTF_8) as file:
            configuration.write(file, True)


from celestine import module

PYTHON = "python"

PYTHON_3_6 = "python_3_6"
PYTHON_3_7 = "python_3_7"
PYTHON_3_8 = "python_3_8"
PYTHON_3_9 = "python_3_9"
PYTHON_3_10 = "python_3_10"
PYTHON_3_11 = "python_3_11"


def python():
    try:
        python = module(PYTHON, PYTHON_3_6)
        python = module(PYTHON, PYTHON_3_7)
        python = module(PYTHON, PYTHON_3_8)
        python = module(PYTHON, PYTHON_3_9)
        python = module(PYTHON, PYTHON_3_10)
        python = module(PYTHON, PYTHON_3_11)
    except SyntaxError:
        pass
    return python


class Attribute():
    def __init__(self, session, items):
        for name in items:
            value = self.load_attribute(session, session.application, name)
            setattr(self, name, value)

    def load_attribute(self, session, section, attribute):
        # duplicate code
        try:
            cat = getattr(session.argument, attribute)
            if cat:
                return cat
        except AttributeError:
            pass

        try:
            argg = session.configuration[section][attribute]
        except KeyError:
            argg = session.default[section][attribute]
        return argg


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

    def figtree(self, configuration, module, application):
        """Build up the configuration file."""
        try:
            configuration.add_section(application)
        except configparser.DuplicateSectionError:
            pass
        configuration = module.default(configuration)
        configuration.set(application, "task", "main")
        return configuration

    def main(self):
        root = load.module(APPLICATION)
        module = load.module(APPLICATION, self.application)

        argument = root.argument()
        self.argument = module.argument(argument)

        configuration = root.Configuration(self.directory)
        self.configuration = configuration.load()

        default = configparser.ConfigParser()
        default = self.figtree(default, root, CELESTINE)
        default = self.figtree(default, module, self.application)
        self.default = default

        self.parser = Parser()

        temargument = self.parser.parse(self)

        self.attribute = Attribute(self, module.attribute())

        self.module = load.module(APPLICATION, self.application, self.task)
        return self.module.main(self)
