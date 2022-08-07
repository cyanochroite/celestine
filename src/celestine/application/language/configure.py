"""Load and save user settings from a file."""

from celestine.application.language import configuration as hippo


def main(session):
    """The main function."""
    configuration = session.configuration
    key = session.argument.key
    region = session.argument.region
    url = session.argument.url
    figtree = hippo(configuration, key, region, url)
    session.config.save(figtree)
