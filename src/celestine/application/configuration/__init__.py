"""Generate configuration files for all packages."""
from celestine.application.configuration.argument import parser
from celestine.main.configuration import configuration_save
from celestine.main.configuration import configuration_celestine
from celestine.main.configuration import configuration_translator

from celestine.keyword.main import CELESTINE
from celestine.keyword.main import CONFIGURATION_CELESTINE
from celestine.keyword.main import CONFIGURATION_TRANSLATOR


def save(configuration, file):
    """Simplify the saveing of stuff."""
    configuration_save(configuration, session.directory, CELESTINE, file)


def main(**kwargs):
    """def main"""
    global session
    session = kwargs["session"]

    argument = parser.parse_args()
    configuration = argument.configuration

    if configuration == "celestine":
        save(
            configuration_celestine(
                argument.application,
                argument.language,
                argument.python,
            ),
            CONFIGURATION_CELESTINE,
        )

    if configuration == "translator":
        save(
            configuration_translator(
                argument.key,
                argument.region,
                argument.url,
            ),
            CONFIGURATION_TRANSLATOR,
        )
