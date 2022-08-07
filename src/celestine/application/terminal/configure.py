"""Load and save user settings from a file."""
import configparser


from .keyword import CELESTINE


from celestine.application.terminal.keyword import APPLICATION
from celestine.application.terminal.keyword import LANGUAGE
from celestine.application.terminal.keyword import PYTHON


TERMINAL = "terminal"
ENGLISH = "english"
PYTHON_3_10 = "python_3_10"
CELESTINE = "celestine"


def configure(
    configuration,
    application=TERMINAL,
    language=ENGLISH,
    python=PYTHON_3_10,
):
    """Build up the configuration file."""
    if not configuration.has_section(CELESTINE):
        configuration.add_section(CELESTINE)
    configuration.set(CELESTINE, APPLICATION, application)
    configuration.set(CELESTINE, LANGUAGE, language)
    configuration.set(CELESTINE, PYTHON, python)
    return configuration




def main(session):
    """The main function."""
    directory = session.directory
    configuration = session.configuration.load_default(directory)
    key = argument.key
    region = argument.region
    url = argument.url
    configuration = configure(configuration, key, region, url)
    session.configuration.save_default(configuration, directory)

