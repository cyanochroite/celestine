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
        self.section = application
        map(self.load_attribute, iterable)
        return self

    def load_attribute(self, attribute):
        args = None
        try:
            cat = getattr(self.session.argument, attribute)
            if cat:
                args = cat
        except AttributeError:
            pass

        if not args:
            try:
                args = self.session.configuration[self.section][attribute]
            except KeyError:
                args = self.session.default[self.section][attribute]

        setattr(self, attribute, args)  # value


class Attribute():
    pass

    def add(self, application, *iterable):
        self.section = application
        for attribute in iterable:
            args = None
            try:
                cat = getattr(self.session.argument, attribute)
                if cat:
                    args = cat
            except AttributeError:
                pass

            if not args:
                try:
                    args = self.session.configuration[self.section][attribute]
                except KeyError:
                    args = self.session.default[self.section][attribute]

            setattr(self, attribute, args)  # value

        return self


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

    def add_configuration(self, configuration, module, application):
        """Build up the configuration file."""
        if not configuration.has_section(application):
            configuration.add_section(application)
        attribute = module.attribute()
        default = module.default()
        for item in zip(attribute, default, strict=True):
            (name, value) = item
            configuration.set(application, name, value)

        return configuration

    def add_attribute(self, application, iterable):
        self.section = application
        for attribute in iterable:
            args = None
            try:
                cat = getattr(self.argument, attribute)
                if cat:
                    args = cat
            except AttributeError:
                pass

            if not args:
                try:
                    args = self.configuration[self.section][attribute]
                except KeyError:
                    args = self.default[self.section][attribute]

            setattr(self.attribute, attribute, args)  # value

    def main(self):
        module_root = load.module(APPLICATION)
        module_celestine = load.module(APPLICATION, CELESTINE)
        module_application = load.module(APPLICATION, self.application)

        root = module_root
        modulea = module_application

        configuration = root.Configuration(self.directory)
        self.configuration = configuration.load()

        default = configparser.ConfigParser()
        default = self.add_configuration(default, module_celestine, CELESTINE)
        default = self.add_configuration(default, modulea, self.application)
        self.default = default

        argument = root.argument()
        argument = modulea.argument(argument)
        argument = argument.parser.parse_args()
        self.argument = argument

        self.attribute = Attribute()

        self.add_attribute(CELESTINE, module_celestine.attribute())
        self.add_attribute(self.application, module_application.attribute())

        self.application = load.module(
            APPLICATION,
            self.attribute.application,
        )
        self.task = load.module(
            APPLICATION,
            self.attribute.application,
            self.attribute.task,
        )
#        self.task = load.module(APPLICATION, data.application, data.task)
        self.language = module(
            LANGUAGE,
            self.attribute.language,
        )

        self.python = python()

        return self.task.main(self)
