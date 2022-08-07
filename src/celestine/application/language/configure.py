"""Load and save user settings from a file."""
import configparser

from celestine.application.language.keyword import LANGUAGE
from celestine.application.language.keyword import KEY
from celestine.application.language.keyword import REGION
from celestine.application.language.keyword import URL

from celestine.application.language.keyword import ARGUMENT
from celestine.application.language.keyword import SESSION
from celestine.application.language.keyword import NONE


def configure(
    configuration,
    key=NONE, 
    region=NONE,
    url=NONE,
    ):
    """Build up the configuration file."""
    if not configuration.has_section(LANGUAGE):
        configuration.add_section(LANGUAGE)
    configuration.set(LANGUAGE, KEY, key)
    configuration.set(LANGUAGE, REGION, region)
    configuration.set(LANGUAGE, URL, url)
    return configuration



def main(session):
    """The main function."""
    configuration = session.config.load()
    key = session.argument.key
    region = session.argument.region
    url = session.argument.url
    configuration = configure(session.configuration, key, region, url)
    session.config.save(configuration)
