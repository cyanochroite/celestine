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
class Argument1():
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog=CELESTINE,
            exit_on_error=False,
        )

        self.parser.add_argument(
            APPLICATION,
            choices=application,
            help="Select which application to run.",
        )

        self.parser.add_argument(
            "ignore",
            nargs="*",
            help="Select which application to run.",
        )


@dataclasses.dataclass
class Argument2():
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog=CELESTINE,
            exit_on_error=False,
        )

        self.parser.add_argument(
            APPLICATION,
            choices=application,
            help="Select which application to run.",
        )

        self.parser.add_argument(
            "-l, --language",
            choices=language,
            help="Choose a language.",
            dest=LANGUAGE,
            metavar="language",
        )

        self.subparser = self.parser.add_subparsers(
            dest=TASK,
            required=False,
        )

        self.main = self.subparser.add_parser(
            "main",
            help="The default main application.",
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
    def __init__(self, argument, directory, module, section):
        configuration = Configuration(directory)
        configuration = configuration.load()

        attribute = module.attribute()
        default = module.default()

        for (name, failover) in zip(attribute, default, strict=True):
            database = configuration.get(section, name, fallback=None)
            override = getattr(argument, name, None)
            value = override or database or failover
            setattr(self, name, value)


class Session():
    def __init__(self, directory, args):
        args = args or ["tkinter"]

        argument = Argument1()

        attribute = Attribute(
            argument.parser.parse_args(args),
            directory,
            load.module("internal"),
            CELESTINE,
        )

        module = load.module(APPLICATION, attribute.application)

        argument = Argument2()
        argument = module.argument(argument)
        attribute = Attribute(
            argument.parser.parse_args(args),
            directory,
            load.module("internal"),
            CELESTINE,
        )

        self.application = load.module(
            APPLICATION,
            attribute.application,
        )
        self.attribute = Attribute(
            argument.parser.parse_args(args),
            directory,
            module,
            attribute.application,
        )
        self.directory = directory  # me no like
        self.image_format = module.image_format()
        self.language = load.module(
            LANGUAGE,
            attribute.language,
        )
        self.python = self.python(
        )
        self.task = load.module(
            APPLICATION,
            attribute.application,
            attribute.task,
        )
        self.window = []
        #self.window.append(load.module("window", "main"))
        self.window.append(load.module("window", "zero"))
        self.window.append(load.module("window", "one"))
        self.window.append(load.module("window", "two"))

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
