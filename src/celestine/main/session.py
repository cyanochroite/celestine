"""Load and save user settings from a file."""
from celestine.main.keyword import APPLICATION
from celestine.main.keyword import DIRECTORY
from celestine.main.keyword import LANGUAGE
from celestine.main.keyword import PACKAGE
from celestine.main.keyword import CACHE
from celestine.main.keyword import PYTHON


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
        return load_module(PYTHON, self.session[APPLICATION][PYTHON])

    @property
    def language(self):
        """Returns the language."""
        return load_module(LANGUAGE, self.session[APPLICATION][LANGUAGE])

    @property
    def package(self):
        """Returns the package."""
        return load_module(PACKAGE, self.session[APPLICATION][PACKAGE])
