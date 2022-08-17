"""Celestine Image Viewer"""
"""Load and save user settings from a file."""

import sys
import configparser


from celestine.keyword.main import APPLICATION
from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import TASK

from celestine.keyword.main import CELESTINE


"""Load and save user settings from a file."""
import configparser

from celestine.core import load

from celestine.keyword.main import CELESTINE
from celestine.keyword.main import CONFIGURATION
from celestine.keyword.main import WRITE
from celestine.keyword.main import UTF_8

"""Parse arguments."""
import argparse
import dataclasses

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import CELESTINE
from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import TASK
from celestine.keyword.main import application
from celestine.keyword.main import language


PYTHON = "python"

PYTHON_3_6 = "python_3_6"
PYTHON_3_7 = "python_3_7"
PYTHON_3_8 = "python_3_8"
PYTHON_3_9 = "python_3_9"
PYTHON_3_10 = "python_3_10"
PYTHON_3_11 = "python_3_11"


@dataclasses.dataclass
class Argument():
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog=CELESTINE
        )

        self.parser.add_argument(
            APPLICATION,
            choices=application,
            help="Select which application to run."
        )

        self.parser.add_argument(
            "-l, --language",
            choices=language,
            help="Choose a language.",
            dest=LANGUAGE,
            metavar="language"
        )

        self.subparser = self.parser.add_subparsers(
            dest=TASK,
            required=False
        )

        self.main = self.subparser.add_parser(
            "main",
            help="The default main application."
        )


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


class Attribute(Configuration):
    def __init__(self, argument, configuration, default):
        self.argument = argument
        self.configuration = configuration
        self.default = default

    def add(self, application, iterable):
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

            setattr(self, attribute, args)  # value

        return self


class Session():
    def __init__(self, directory):
        self.directory = directory  # me no like

        try:
            application = sys.argv[1]
        except IndexError:
            print("hack and bad default?")
            sys.argv.append("tkinter")
            application = sys.argv[1]

        module_celestine = load.module(APPLICATION, CELESTINE)
        module_application = load.module(APPLICATION, application)

        configuration = Configuration(directory)
        self.configuration = configuration.load()

        default = configparser.ConfigParser()
        default = self.add_configuration(default, module_celestine, CELESTINE)
        default = self.add_configuration(default, module_application, application)
        self.default = default

        argument = Argument()
        argument = module_application.argument(argument)
        argument = argument.parser.parse_args()
        self.argument = argument

        self.attribute = Attribute(self.argument, self.configuration, self.default)
        self.attribute.add(CELESTINE, module_celestine.attribute())
        self.attribute.add(application, module_application.attribute())

        self.application = load.module(
            APPLICATION,
            self.attribute.application,
        )
        self.task = load.module(
            APPLICATION,
            self.attribute.application,
            self.attribute.task,
        )
        self.language = load.module(
            LANGUAGE,
            self.attribute.language,
        )
        self.python = self.python(
        )
        self.window = load.module(
            "window",
            "main",
        )

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

    def python(self):
        try:
            python = load.module(PYTHON, PYTHON_3_6)
            python = load.module(PYTHON, PYTHON_3_7)
            python = load.module(PYTHON, PYTHON_3_8)
            python = load.module(PYTHON, PYTHON_3_9)
            python = load.module(PYTHON, PYTHON_3_10)
            python = load.module(PYTHON, PYTHON_3_11)
        except SyntaxError:
            pass
        return python

    def main(self):
        return self.task.main(self)
