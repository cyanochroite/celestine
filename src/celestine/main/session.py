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


PYTHON = "python"

PYTHON_3_6 = "python_3_6"
PYTHON_3_7 = "python_3_7"
PYTHON_3_8 = "python_3_8"
PYTHON_3_9 = "python_3_9"
PYTHON_3_10 = "python_3_10"
PYTHON_3_11 = "python_3_11"

@dataclasses.dataclass
class Session():
    """Wrapper around configuration dictionary data."""

    def _attribute(self, default, configuration, value, name):
        """Combine several sources to set a final value."""
        attribute = default[CELESTINE][name]

        if configuration.has_option(CELESTINE, name):
            attribute = configuration[CELESTINE][name]

        if value is not None:
            attribute = value

        module = load.module(name, attribute)
        setattr(self, name, module)

    def __init__(self, directory, application):
        self.directory = directory
        self.asset = load.path(directory, CELESTINE)

        default = configuration_celestine()

        configuration = configuration_load(
            directory,
            CELESTINE,
            CONFIGURATION_CELESTINE
        )

        self._attribute(default, configuration, application, APPLICATION)
        self._attribute(default, configuration, None, LANGUAGE)

      
        try:
            self.python = load.module(PYTHON, PYTHON_3_6)
            self.python = load.module(PYTHON, PYTHON_3_7)
            self.python = load.module(PYTHON, PYTHON_3_8)
            self.python = load.module(PYTHON, PYTHON_3_9)
            self.python = load.module(PYTHON, PYTHON_3_10)
            self.python = load.module(PYTHON, PYTHON_3_11)
        except SyntaxError:
            pass
        