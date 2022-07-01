"""Load and save user settings from a file."""
import configparser
import os.path
from celestine.core import load


def make(parent_directory):
    """A quick way to make a configuration file on disk."""
    session = configparser.ConfigParser()

    session.add_section("Application")
    session.set("Application", "name", "celestine")
    session.set("Application", "directory", parent_directory)

    with open("celestine.ini", "w", encoding="utf_8") as file:
        session.write(file)

    session.read("celestine.ini")

    return session


APPLICATION = "Application"

PYTHON = "python"
PACKAGE = "package"
LANGUAGE = "language"


PRIVATE = "Private"

DIRECTORY = "directory"


VERSION = "version"


class File():
    @classmethod
    def read(cls, file):
        return cls.text(file, "rt")

    @classmethod
    def write(cls, file):
        return cls.text(file, "wt")

    @staticmethod
    def text(file, mode):
        buffering = 1
        encoding = "utf_8"
        errors = "strict"
        newline = None
        closefd = True
        opener = None
        return open(
            file,
            mode,
            buffering,
            encoding,
            errors,
            newline,
            closefd,
            opener
        )


class Session():
    """Wrapper around configuration dictionary data."""

    def override(self, parse, name):
        attribute = getattr(parse, name, None)
        if attribute is not None:
            self.session[APPLICATION][name] = attribute

    def save_me(self):
        file = os.path.join(parent_directory, "celestine", "celestine.ini")
        self.session.write(File.write(file), True)

    @staticmethod
    def save_new(parent_directory):
        file = os.path.join(parent_directory, "celestine", "celestine.ini")
        session = configparser.ConfigParser()
        session.add_section(APPLICATION)
        session.set(APPLICATION, LANGUAGE, "english")
        session.set(APPLICATION, PACKAGE, "celestine")
        session.set(APPLICATION, PYTHON, "python_3_10")
        session.write(File.write(file), True)

    def __init__(self, parent_directory, parse):
        file = os.path.join(parent_directory, "celestine", "celestine.ini")
        self.session = configparser.ConfigParser()
        self.session.read_file(File.read(file), file)
        self.session.read("celestine.ini", encoding="utf_8")

        self.override(parse, LANGUAGE)
        self.override(parse, PACKAGE)
        self.override(parse, PYTHON)

        self.session.add_section(PRIVATE)
        self.session.set(PRIVATE, DIRECTORY, parent_directory)

    @property
    def _python(self):
        """Returns the python version."""
        return Version(self.session[VERSION][PYTHON])

    @property
    def directory(self):
        """Returns the current working directory."""
        return self.session[PRIVATE][DIRECTORY]

    @property
    def python(self):
        """Returns the python."""
        return load.module(PYTHON, self.session[APPLICATION][PYTHON])

    @property
    def language(self):
        """Returns the language."""
        return load.module(LANGUAGE, self.session[APPLICATION][LANGUAGE])

    @property
    def package(self):
        """Returns the package."""
        return self.session[APPLICATION][PACKAGE]
