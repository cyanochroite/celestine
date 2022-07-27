"""Load and save user settings from a file."""
import configparser

from celestine.main.configuration import configuration_save_main
from celestine.main.configuration import configuration_load_main

from celestine.application.language.keyword import LANGUAGE
from celestine.application.language.keyword import KEY
from celestine.application.language.keyword import REGION
from celestine.application.language.keyword import URL

from celestine.application.language.keyword import ARGUMENT
from celestine.application.language.keyword import SESSION
from celestine.application.language.keyword import NONE


def configure(configuration, key, region, url):
    if not configuration.has_section(LANGUAGE):
        configuration.add_section(LANGUAGE)
    configuration.set(LANGUAGE, KEY, key)
    configuration.set(LANGUAGE, REGION, region)
    configuration.set(LANGUAGE, URL, url)
    return configuration


def default():
    configuration = configparser.ConfigParser()
    key = NONE
    region = NONE
    url = NONE
    configuration = configure(configuration, key, region, url)
    return configuration


def main(**kwargs):
    argument = kwargs[ARGUMENT]
    session = kwargs[SESSION]
    directory = session.directory

    configuration = configuration_load_main(directory)
    key = argument.key
    region = argument.region
    url = argument.url
    configuration = configure(configuration, key, region, url)
    configuration_save_main(configuration, directory)
