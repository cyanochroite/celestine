import configparser

from celestine.core import load
from celestine.keyword.all import CELESTINE
from celestine.keyword.all import CONFIGURATION
from celestine.keyword.all import WRITE
from celestine.keyword.all import UTF_8


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

    @staticmethod
    def make(directory):
        """Make a new configuration file."""
        configuration = Configuration(directory)
        return configuration.load()

    def save(self, configuration, path=None):
        """Save the configuration file."""
        with open(path or self.path, WRITE, encoding=UTF_8) as file:
            configuration.write(file, True)


