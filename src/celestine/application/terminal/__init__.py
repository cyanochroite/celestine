import configparser


from .keyword import CELESTINE


from celestine.application.terminal.keyword import APPLICATION
from celestine.application.terminal.keyword import LANGUAGE
from celestine.application.terminal.keyword import PYTHON


TERMINAL = "terminal"
ENGLISH = "english"
PYTHON_3_10 = "python_3_10"
CELESTINE = "celestine"



def argument(argument):
    configure = argument.subparser.add_parser(
        CONFIGURE,
        help="you are a fish",
    )

    configure.add_argument(
        KEY,
        action=STORE,
        help="A brief description of what the argument does.",
    )

    configure.add_argument(
        REGION,
        action=STORE,
        help="A brief description of what the argument does.",
    )

    configure.add_argument(
        URL,
        action=STORE,
        help="A brief description of what the argument does.",
    )

    report = argument.subparser.add_parser(
        REPORT,
        help="you are a fish",
    )

    translate = argument.subparser.add_parser(
        TRANSLATE,
        help="you are a fish",
    )

    return argument


def configuration(
    configuration,
    application=TERMINAL,
    language=ENGLISH,
    python=PYTHON_3_10,
):
    if not configuration.has_section(CELESTINE):
        configuration.add_section(CELESTINE)
    configuration.set(CELESTINE, APPLICATION, application)
    configuration.set(CELESTINE, LANGUAGE, language)
    configuration.set(CELESTINE, PYTHON, python)
    return configuration

