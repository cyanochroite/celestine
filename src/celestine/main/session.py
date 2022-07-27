"""Load and save user settings from a file."""
from celestine.keyword.main import APPLICATION
from celestine.keyword.main import DIRECTORY
from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import APPLICATION
from celestine.keyword.main import CACHE
from celestine.keyword.main import PYTHON

from celestine.keyword.main import CELESTINE
from celestine.keyword.main import CONFIGURATION_CELESTINE

from celestine.main.configuration import configuration_load
from celestine.main.configuration import configuration_celestine

from celestine.core import load


class Session():
    """Wrapper around configuration dictionary data."""

    def set_attribute(self, default, configuration, argument, name):
        attribute = default[CELESTINE][name]

        if configuration.has_option(CELESTINE, name):
            attribute = configuration[CELESTINE][name]

        override = getattr(argument, name, None)
        if override is not None:
            attribute = override

        module = load.module(name, attribute)
        setattr(self, name, module)

    def __init__(self, argument, directory):
        self.directory = directory
        self.asset = load.path(directory, CELESTINE)

        default = configuration_celestine()

        configuration = configuration_load(
            directory,
            CELESTINE,
            CONFIGURATION_CELESTINE
        )

        self.set_attribute(default, configuration, argument, APPLICATION)
        self.set_attribute(default, configuration, argument, LANGUAGE)
        self.set_attribute(default, configuration, argument, PYTHON)
