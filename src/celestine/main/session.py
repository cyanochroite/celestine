"""Load and save user settings from a file."""
from celestine.keyword.main import APPLICATION
from celestine.keyword.main import DIRECTORY
from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import PACKAGE
from celestine.keyword.main import CACHE
from celestine.keyword.main import PYTHON

from celestine.keyword.main import CELESTINE
from celestine.keyword.main import CONFIGURATION_CELESTINE

from celestine.main.configuration import configuration_load
from celestine.main.configuration import configuration_save


def load_module(*paths):
    """Load an internal module from anywhere in the application."""
    iterable = ["celestine"] + list(paths)
    name = ".".join(iterable)
    item = __import__(name)
    for path in paths:
        item = getattr(item, path)
    return item


class Language():
    def __init__(self, configuration):
        self.configuration = configuration
        self.TITLE = self.configuration[APPLICATION]["title"]
        self.CURSES_EXIT = self.configuration["curses"]["exit"]
    
class Session():
    """Wrapper around configuration dictionary data."""

    def override(self, argument, name):
        attribute = getattr(argument, name, None)
        if attribute is not None:
            self.session[APPLICATION][name] = attribute

    def __init__(self, argument, directory):
        self.session = configuration_load(directory, CELESTINE, "configuration", CONFIGURATION_CELESTINE)
        self.session.add_section(CACHE)
        self.session.set(CACHE, DIRECTORY, directory)
        self.override(argument, LANGUAGE)
        self.override(argument, PACKAGE)
        self.override(argument, PYTHON)
        ###
        self.directory = self.session[CACHE][DIRECTORY]
        self.python = load_module(PYTHON, self.session[APPLICATION][PYTHON])

        self.language = Language(
            configuration_load(
                directory,
                CELESTINE,
                "configuration", 
                "language",
                F"{self.session[APPLICATION][LANGUAGE]}.ini"
            )
        )

        self.package = load_module(PACKAGE, self.session[APPLICATION][PACKAGE])
