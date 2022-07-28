"""Load and save user settings from a file."""
import dataclasses

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import PYTHON

from celestine.keyword.main import CELESTINE
from celestine.keyword.main import CONFIGURATION_CELESTINE

from celestine.main.configuration import configuration_load
from celestine.main.configuration import configuration_celestine

from celestine.core import load


@dataclasses.dataclass
class Session():
    """Wrapper around configuration dictionary data."""

    def _attribute(self, default, configuration, argument, name):
        """Combine several sources to set a final value."""
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

        self._attribute(default, configuration, argument, APPLICATION)
        self._attribute(default, configuration, argument, LANGUAGE)
        self._attribute(default, configuration, argument, PYTHON)
