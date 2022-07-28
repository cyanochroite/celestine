"""Load and save user settings from a file."""
import configparser
import os.path


from celestine.keyword.main import APPLICATION
from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import ENGLISH
from celestine.keyword.main import CELESTINE
from celestine.keyword.main import TERMINAL
from celestine.keyword.main import PYTHON
from celestine.keyword.main import PYTHON_3_10
from celestine.keyword.main import CONFIGURATION_CELESTINE
from celestine.keyword.main import ENCODING
from celestine.keyword.main import WRITE
from celestine.keyword.main import UTF_8


def configuration_save(configuration, *paths):
    """Save the configuration file."""
    path = os.path.join(*paths)
    with open(path, WRITE, UTF_8) as file:
        configuration.write(file, True)


def configuration_load(*paths):
    """Load the configuration file."""
    path = os.path.join(*paths)
    configuration = configparser.ConfigParser()
    configuration.read(path, encoding=ENCODING)
    return configuration


def configuration_save_main(configuration, directory):
    """Save the default configuration file."""
    configuration_save(
        configuration,
        directory,
        CELESTINE,
        CONFIGURATION_CELESTINE,
    )


def configuration_load_main(directory):
    """Load the default configuration file."""
    return configuration_load(
        directory,
        CELESTINE,
        CONFIGURATION_CELESTINE,
    )


def configuration_celestine(application=TERMINAL, language=ENGLISH, python=PYTHON_3_10):
    """The default configuration file."""
    configuration = configparser.ConfigParser()
    configuration.add_section(CELESTINE)
    configuration.set(CELESTINE, APPLICATION, application)
    configuration.set(CELESTINE, LANGUAGE, language)
    configuration.set(CELESTINE, PYTHON, python)
    return configuration
