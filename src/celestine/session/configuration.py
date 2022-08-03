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

    def load(self, *paths):
        """Load the configuration file."""
        path = load.path(*paths)
        configuration = configparser.ConfigParser()
        configuration.read(path, encoding=UTF_8)
        return configuration

    def load_default(self, directory):
        """Load the default configuration file."""
        return self.load(
            directory,
            CELESTINE,
            CONFIGURATION,
        )

    def save(self, configuration, *paths):
        """Save the configuration file."""
        path = load.path(*paths)
        with open(path, WRITE, encoding=UTF_8) as file:
            configuration.write(file, True)

    def save_default(self, configuration, directory):
        """Save the default configuration file."""
        self.save(
            configuration,
            directory,
            CELESTINE,
            CONFIGURATION,
        )
