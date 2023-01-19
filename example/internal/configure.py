"""Load and save user settings from a file."""

from celestine.application.terminal.keyword import CELESTINE
from celestine.application.terminal.keyword import APPLICATION
from celestine.application.terminal.keyword import LANGUAGE
from celestine.application.terminal.keyword import PYTHON

from celestine.keyword.main import application
from celestine.keyword.main import language
from celestine.keyword.main import python


def main(session):
    """The main function."""
    configuration = session.configuration
    application = session.argument._application
    language = session.argument.language
    python = session.argument.python
    figtree = hippo(configuration, application, language, python)
    session.config.save(figtree)


def hippo(configuration, application, language, python):
    """Build up the configuration file."""
    if not configuration.has_section(CELESTINE):
        configuration.add_section(CELESTINE)
    configuration.set(CELESTINE, APPLICATION, application)
    configuration.set(CELESTINE, LANGUAGE, language)
    configuration.set(CELESTINE, PYTHON, python)
    return configuration
