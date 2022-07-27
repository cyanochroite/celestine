"""Load and save user settings from a file."""

from celestine.main.configuration import configuration_save_main
from celestine.main.configuration import configuration_load_main

from celestine.application.language.keyword import LANGUAGE
from celestine.application.language.keyword import KEY
from celestine.application.language.keyword import REGION
from celestine.application.language.keyword import URL
from celestine.application.language.keyword import FILE


def configure(directory, key="", region="", url=""):
    configuration = configuration_load_main(directory)

    if not configuration.has_section(LANGUAGE):
        configuration.add_section(LANGUAGE)
    configuration.set(LANGUAGE, KEY, key)
    configuration.set(LANGUAGE, REGION, region)
    configuration.set(LANGUAGE, URL, url)

    configuration_save_main(configuration, directory)

