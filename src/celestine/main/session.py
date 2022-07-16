"""Load and save user settings from a file."""
from celestine.main.keyword import APPLICATION
from celestine.main.keyword import DIRECTORY
from celestine.main.keyword import LANGUAGE
from celestine.main.keyword import PACKAGE
from celestine.main.keyword import CACHE
from celestine.main.keyword import PYTHON

from celestine.main.keyword import CELESTINE
from celestine.main.keyword import CONFIGURATION

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


class Session():
    """Wrapper around configuration dictionary data."""

    def override(self, argument, name):
        attribute = getattr(argument, name, None)
        if attribute is not None:
            self.session[APPLICATION][name] = attribute

    def __init__(self, argument, directory):
        self.session = configuration_load(directory, CELESTINE, CONFIGURATION)
        self.session.add_section(CACHE)
        self.session.set(CACHE, DIRECTORY, directory)
        self.override(argument, LANGUAGE)
        self.override(argument, PACKAGE)
        self.override(argument, PYTHON)
        ###
        self.directory = self.session[CACHE][DIRECTORY]
        self.python = load_module(PYTHON, self.session[APPLICATION][PYTHON])
        self.language = load_module(LANGUAGE, self.session[APPLICATION][LANGUAGE])
        self.package = load_module(PACKAGE, self.session[APPLICATION][PACKAGE])
