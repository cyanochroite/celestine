"""Load and save user settings from a file."""
import configparser

from celestine.application.terminal.keyword import APPLICATION
from celestine.application.terminal.keyword import DIRECTORY
from celestine.application.terminal.keyword import LANGUAGE
from celestine.application.terminal.keyword import PYTHON

from celestine.application.language.keyword import ARGUMENT
from celestine.application.language.keyword import SESSION
from celestine.application.language.keyword import NONE


TERMINAL = "terminal"
ENGLISH = "english"
PYTHON_3_10 = "python_3_10"
CELESTINE = "celestine"

def configure(configuration, key, region, url):
    """Build up the configuration file."""
    if not configuration.has_section(LANGUAGE):
        configuration.add_section(LANGUAGE)
    configuration.set(LANGUAGE, KEY, key)
    configuration.set(LANGUAGE, REGION, region)
    configuration.set(LANGUAGE, URL, url)
    return configuration


def default():
    """The default configuration with all keys."""
    configuration = configparser.ConfigParser()
    key = NONE
    region = NONE
    url = NONE
    configuration = configure(configuration, key, region, url)
    return configuration


def main(session):
    """The main function."""
    directory = session.directory
    configuration = session.configuration.load_default(directory)
    key = argument.key
    region = argument.region
    url = argument.url
    configuration = configure(configuration, key, region, url)
    session.configuration.save_default(configuration, directory)


def configuration_celestine(application=TERMINAL, language=ENGLISH, python=PYTHON_3_10):
    """The default configuration file."""
    configuration = configparser.ConfigParser()
    configuration.add_section(CELESTINE)
    configuration.set(CELESTINE, APPLICATION, application)
    configuration.set(CELESTINE, LANGUAGE, language)
    configuration.set(CELESTINE, PYTHON, python)
    return configuration
