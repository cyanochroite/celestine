"""Generate configuration files for all packages."""
import argparse
import configparser
import os.path
import sys

from celestine.main.configuration import configuration_load
from celestine.main.configuration import configuration_save

from celestine.main.keyword import APPLICATION
from celestine.main.keyword import LANGUAGE
from celestine.main.keyword import ENGLISH
from celestine.main.keyword import PACKAGE
from celestine.main.keyword import CELESTINE
from celestine.main.keyword import PYTHON
from celestine.main.keyword import PYTHON_3_10
from celestine.main.keyword import CONFIGURATION_CELESTINE

from celestine_translator.keyword import AZURE
from celestine_translator.keyword import KEY
from celestine_translator.keyword import REGION
from celestine_translator.keyword import URL
from celestine_translator.keyword import FILE


directory = sys.path[0]


parser = argparse.ArgumentParser(
    prog="celestine_configuration"
)

parser.add_argument(
    "-c, --celestine",
    action="store_true",
    dest="celestine",
)

parser.add_argument(
    "-l, --language",
    action="store_true",
    dest="language",
)

parser.add_argument(
    "-t, --translator",
    dest="translator",
    nargs=3,
)

parse = parser.parse_args()

celestine = parse.celestine
if celestine:
    configuration = configparser.ConfigParser()
    configuration.add_section(APPLICATION)
    configuration.set(APPLICATION, LANGUAGE, ENGLISH)
    configuration.set(APPLICATION, PACKAGE, CELESTINE)
    configuration.set(APPLICATION, PYTHON, PYTHON_3_10)
    path = os.path.join(directory, CELESTINE, CONFIGURATION_CELESTINE)
    configuration_save(path, configuration)

language = parse.language
if language:
    configuration = configuration_load(directory, CELESTINE, LANGUAGE, "english.ini")
    path = os.path.join(directory, "celestine_translator", "language.ini")
    configuration_save(path, configuration)

translator = parse.translator
if translator:
    configuration = configparser.ConfigParser()
    (key, region, url) = translator
    configuration.add_section(AZURE)
    configuration.set(AZURE, KEY, key)
    configuration.set(AZURE, REGION, region)
    configuration.set(AZURE, URL, url)
    path = os.path.join(directory, FILE)
    configuration_save(path, configuration)
