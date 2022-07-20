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
from celestine.main.configuration import configuration_celestine


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

    def magic(self, name):
        if self.session.has_option(APPLICATION, name):
            setattr(self, name,  self.session[APPLICATION][name])
        
    def dentist(self, default, configuration, argument, name):
        sun = default[APPLICATION][name]
        if configuration.has_option(APPLICATION, name):
            sun = configuration[APPLICATION][name]

        attribute = getattr(argument, name, None)
        if attribute is not None:
            sun = attribute

        carwash = load_module(name, sun)
        setattr(self, name, carwash)
        
    def __init__(self, argument, directory):
        self.directory = directory
        
        default = configuration_celestine()
        configuration = configuration_load(
            directory,
            CELESTINE,
            "configuration",
            CONFIGURATION_CELESTINE
        )
        
        self.dentist(default, configuration, argument, LANGUAGE)
        self.dentist(default, configuration, argument, PACKAGE)
        self.dentist(default, configuration, argument, PYTHON)
        