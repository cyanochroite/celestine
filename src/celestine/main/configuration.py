"""Load and save user settings from a file."""
import configparser
import os.path


from celestine.main.keyword import APPLICATION

from celestine.main.keyword import LANGUAGE
from celestine.main.keyword import ENGLISH

from celestine.main.keyword import PACKAGE
from celestine.main.keyword import CELESTINE

from celestine.main.keyword import PYTHON
from celestine.main.keyword import PYTHON_3_10

from celestine.main.keyword import CACHE
from celestine.main.keyword import DIRECTORY


from celestine.main.keyword import CONFIGURATION
from celestine.main.keyword import ENCODING
from celestine.main.keyword import ERRORS
from celestine.main.keyword import READ
from celestine.main.keyword import WRITE

def file_mode(file, mode):
    buffering = 1
    encoding = ENCODING
    errors = ERRORS
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


def configuration_save(path, configuration):
    with file_mode(path, WRITE) as file:
        configuration.write(file, True)


def read_file(path):
    configuration = configparser.ConfigParser()
    configuration.read_file(file_mode(path, READ), path) ##CHECK
    return configuration



def configuration_load(*paths):
    path = os.path.join(*paths)
    try:
        configuration = read_file(path)
    except FileNotFoundError:
        make(path)
        configuration = read_file(path)

    configuration.read(CONFIGURATION, encoding=ENCODING)
    return configuration


def make(path): # outsource
    """A quick way to make a configuration file on disk."""
    configuration = configparser.ConfigParser()

    configuration.add_section(APPLICATION)
    configuration.set(APPLICATION, LANGUAGE, ENGLISH)
    configuration.set(APPLICATION, PACKAGE, CELESTINE)
    configuration.set(APPLICATION, PYTHON, PYTHON_3_10)

    save(path, configuration)
