"""Load and save user settings from a file."""
import configparser
import os.path

from celestine.main.keyword import APPLICATION
from celestine.main.keyword import DIRECTORY
from celestine.main.keyword import LANGUAGE
from celestine.main.keyword import PACKAGE
from celestine.main.keyword import PRIVATE
from celestine.main.keyword import PYTHON


def file_mode(file, mode):
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


def save(file, session):
    with file_mode(file, "wt") as fileobject:
        session.write(fileobject, True)


def load(path):
    configuration = configparser.ConfigParser()
    configuration.read_file(file_mode(path, "rt"), path) ##CHECK
    configuration.read("celestine.ini", encoding="utf_8")
    return configuration


def make(directory):
    """A quick way to make a configuration file on disk."""
    file = os.path.join(directory, "celestine", "celestine.ini")

    configuration = configparser.ConfigParser()

    session.add_section(APPLICATION)
    session.set("Application", "name", "celestine")
    session.set(APPLICATION, LANGUAGE, "english")
    session.set(APPLICATION, PACKAGE, "celestine")
    session.set(APPLICATION, PYTHON, "python_3_10")
    save(file, session)

def more(directory, argument):
    file = os.path.join(directory, "celestine", "celestine.ini")
    configuration = load(file)
    configuration.add_section(PRIVATE)
    configuration.set(PRIVATE, DIRECTORY, directory)
    return configuration

