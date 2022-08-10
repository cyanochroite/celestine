"""Load and save user settings from a file."""

from .keyword import LANGUAGE

from .keyword import KEY
from .keyword import REGION
from .keyword import URL


def hippo(configuration, key, region, url):
    """Build up the configuration file."""
    if not configuration.has_section(LANGUAGE):
        configuration.add_section(LANGUAGE)
    configuration.set(LANGUAGE, KEY, key)
    configuration.set(LANGUAGE, REGION, region)
    configuration.set(LANGUAGE, URL, url)
    return configuration


def main(session):
    """The main function."""
    configuration = session.configuration
    key = session.argument.key
    region = session.argument.region
    url = session.argument.url
    figtree = hippo(configuration, key, region, url)
    session.config.save(figtree)
