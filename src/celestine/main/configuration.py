"""Load and save user settings from a file."""
import configparser
import os.path


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
    configuration = read_file(path)
    configuration.read(CONFIGURATION, encoding=ENCODING)
    return configuration
