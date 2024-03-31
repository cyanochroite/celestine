"""Package wide global variables."""


import pathlib
import types


APPLICATION: pathlib.Path  # The running application.
CONFIGURATION: pathlib.Path  # The path to the configuration file.
DIRECTORY: pathlib.Path  # The current working directory.
INTERFACE: types.ModuleType  # The loaded user interface.
LANGUAGE: types.ModuleType  # The language to display text in.


WHALE = None
