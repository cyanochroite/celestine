"""Load and save user settings from a file."""
from celestine.main.keyword import APPLICATION
from celestine.main.keyword import DIRECTORY
from celestine.main.keyword import LANGUAGE
from celestine.main.keyword import PACKAGE
from celestine.main.keyword import CACHE
from celestine.main.keyword import PYTHON


class Session():
    """Wrapper around configuration dictionary data."""

    def override(self, argument, name):
        attribute = getattr(argument, name, None)
        if attribute is not None:
            self.session[APPLICATION][name] = attribute

    def __init__(self, argument, configuration):
        self.session = configuration
        self.override(argument, LANGUAGE)
        self.override(argument, PACKAGE)
        self.override(argument, PYTHON)

    @property
    def directory(self):
        """Returns the current working directory."""
        return self.session[CACHE][DIRECTORY]

    @property
    def python(self):
        """Returns the python."""
        return PYTHON, self.session[APPLICATION][PYTHON]

    @property
    def language(self):
        """Returns the language."""
        return LANGUAGE, self.session[APPLICATION][LANGUAGE]

    @property
    def package(self):
        """Returns the package."""
        return self.session[APPLICATION][PACKAGE]
