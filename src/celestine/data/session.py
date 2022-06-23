"""Load and save user settings from a file."""
import configparser


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



PYTHON = "python"
VERSION = "version"
APPLICATION = "Application"
DIRECTORY = "directory"

class Session():
    """Wrapper around configuration dictionary data."""
    def __init__(self, parent_directory):
        self.session = configparser.ConfigParser()
        self.session.read("celestine.ini")

        self.session.add_section(APPLICATION)
        self.session.set(APPLICATION, DIRECTORY, parent_directory)

        self.session.add_section(VERSION)
        self.session.set(VERSION, PYTHON, "3.10") # need to calculate this

    @property
    def python(self):
        """Returns the python version."""
        return float(self.session[VERSION][PYTHON])

    @property
    def directory(self):
        """Returns the current working directory."""
        return self.session[APPLICATION][DIRECTORY]
