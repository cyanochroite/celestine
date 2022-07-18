"""Generate configuration files for all packages."""
import argparse
import configparser
import sys

from celestine.main.configuration import configuration_load
from celestine.main.configuration import configuration_save

from celestine.keyword.main import APPLICATION
from celestine.keyword.main import LANGUAGE
from celestine.keyword.main import ENGLISH
from celestine.keyword.main import PACKAGE
from celestine.keyword.main import CELESTINE
from celestine.keyword.main import PYTHON
from celestine.keyword.main import PYTHON_3_10
from celestine.keyword.main import CONFIGURATION
from celestine.keyword.main import CONFIGURATION_CELESTINE

from celestine.keyword.translator import AZURE
from celestine.keyword.translator import KEY
from celestine.keyword.translator import REGION
from celestine.keyword.translator import URL
from celestine.keyword.translator import FILE


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
    configuration_save(
        configuration,
        directory,
        CELESTINE,
        CONFIGURATION,
        CONFIGURATION_CELESTINE
    )

language = parse.language
if language:
    configuration = configuration_load(
        directory,
        CELESTINE,
        CONFIGURATION,
        LANGUAGE,
        "english.ini"
    )
    configuration_save(
        configuration,
        directory,
        CELESTINE,
        CONFIGURATION,
        "language.ini"
    )

translator = parse.translator
if translator:
    configuration = configparser.ConfigParser()
    (key, region, url) = translator
    configuration.add_section(AZURE)
    configuration.set(AZURE, KEY, key)
    configuration.set(AZURE, REGION, region)
    configuration.set(AZURE, URL, url)
    configuration_save(
        configuration,
        directory,
        CELESTINE,
        CONFIGURATION,
        FILE
    )
