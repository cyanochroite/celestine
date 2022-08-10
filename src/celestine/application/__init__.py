"""Parse arguments."""
import argparse
import dataclasses

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import CELESTINE
from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import TASK
from celestine.keyword.main import application
from celestine.keyword.main import language


@dataclasses.dataclass
class Argument():
    """Argument"""
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
        self.configuration = configparser.ConfigParser()

    def load(self, path=None):
        """Load the configuration file."""
        self.configuration.read(path or self.path, encoding=UTF_8)
        return self.configuration

    def save(self, configuration, path=None):
        """Save the configuration file."""
        with open(path or self.path, WRITE, encoding=UTF_8) as file:
            self.configuration.write(file, True)



def argument():
    """argument"""
    argument = Argument()

    main = argument.subparser.add_parser(
        "main",
        help="The default main application."
    )
    
    return argument


def configuration(directory):
    """configuration"""
    return Configuration(directory)


