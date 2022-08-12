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
    def __init__(self, session):
        self.session = session

    def add(self, application, *iterable):
        for name in iterable:
            value = self.load_attribute(application, name)
            setattr(self, name, value)
        return self

        
    def load_attribute(self, section, attribute):
        # duplicate code
        try:
            cat = getattr(self.session.argument, attribute)
            if cat:
                return cat
        except AttributeError:
            pass

        try:
            argg = self.session.configuration[section][attribute]
        except KeyError:
            argg = self.session.default[section][attribute]
        return argg


class Session():
    def __init__(self, directory):
        self.directory = directory

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

    def load_attribute(self, session, section, attribute):
        cat = getattr(session.argument, attribute)
        if cat:
            return cat

        try:
            argg = session.configuration[section][attribute]
        except KeyError:
            argg = session.default[section][attribute]
        return argg

        
    def main(self):
        module_root = load.module(APPLICATION)
        module_celestine = load.module(APPLICATION, CELESTINE)
        module_application = load.module(APPLICATION, self.application)



        root = module_root
        modulea = module_application
        
        argument = root.argument()
        self.argument = modulea.argument(argument)

        configuration = root.Configuration(self.directory)
        self.configuration = configuration.load()

        default = configparser.ConfigParser()
        default = self.figtree(default, root, CELESTINE)
        default = self.figtree(default, modulea, self.application)
        self.default = default


        
        
        
        argument = self.argument.parser.parse_args()
        self.argument = argument


        self.application = self.load_attribute(self, CELESTINE, APPLICATION)
        self.task = self.load_attribute(self, self.application, TASK)

        language = self.load_attribute(self, CELESTINE, LANGUAGE)
        self.language = module(LANGUAGE, language)

        self.python = python()
        
        
        attribute = Attribute(self)
        attribute = module_celestine.attribute(attribute)
        attribute = module_application.attribute(attribute)
        
        self.attribute = attribute

        print(self.attribute.application)
        print(self.attribute.task)
        print(self.attribute.language)

        self.module = load.module(APPLICATION, self.application, self.task)
        return self.module.main(self)
