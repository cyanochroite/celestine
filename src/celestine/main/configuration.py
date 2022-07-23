"""Load and save user settings from a file."""
import configparser
import os.path


from celestine.keyword.main import CONFIGURATION_CELESTINE
from celestine.keyword.main import ENCODING
from celestine.keyword.main import ERRORS
from celestine.keyword.main import READ
from celestine.keyword.main import WRITE


def configuration_save(configuration, *paths):
    path = os.path.join(*paths)
    with open(path, WRITE) as file:
        configuration.write(file, True)



def configuration_load(*paths):
    path = os.path.join(*paths)
    configuration = configparser.ConfigParser()
    configuration.read(path, encoding=ENCODING)
    return configuration



from celestine.keyword.main import APPLICATION
from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import ENGLISH
from celestine.keyword.main import PACKAGE
from celestine.keyword.main import CELESTINE
from celestine.keyword.main import TERMINAL
from celestine.keyword.main import PYTHON
from celestine.keyword.main import PYTHON_3_10
from celestine.keyword.main import CONFIGURATION
from celestine.keyword.main import CONFIGURATION_CELESTINE

from celestine.keyword.translator import AZURE
from celestine.keyword.translator import KEY
from celestine.keyword.translator import REGION
from celestine.keyword.translator import URL
from celestine.keyword.translator import FILE


def configuration_celestine(application=TERMINAL, language=ENGLISH, python=PYTHON_3_10):
    configuration = configparser.ConfigParser()
    configuration.add_section(CELESTINE)
    configuration.set(CELESTINE, APPLICATION, application)
    configuration.set(CELESTINE, LANGUAGE, language)
    configuration.set(CELESTINE, PYTHON, python)
    return configuration


def configuration_translator(key, region, url):
    configuration = configparser.ConfigParser()
    configuration.add_section(AZURE)
    configuration.set(AZURE, KEY, key)
    configuration.set(AZURE, REGION, region)
    configuration.set(AZURE, URL, url)
    return configuration
