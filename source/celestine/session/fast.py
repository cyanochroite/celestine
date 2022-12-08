""""""

from celestine.text.unicode import NONE
from celestine.session.configuration import Configuration

from celestine.session.argument import Argument
import argparse
import types
import typing


from celestine.session import load

from celestine.text import CELESTINE

from celestine.text.directory import APPLICATION
from celestine.text.directory import LANGUAGE

from celestine.text.unicode import QUESTION_MARK


def essential(args, exit_on_error):
    """"""

    parser = argparse.ArgumentParser(
        add_help=False,
        exit_on_error=exit_on_error,
    )

    parser.add_argument(
        APPLICATION,
        nargs=QUESTION_MARK,
    )

    parser.add_argument(
        Argument.flag(LANGUAGE),
        Argument.name(LANGUAGE),
    )

    (argument, _) = parser.parse_known_args(args)

    configuration = Configuration.make()

    override = argument.application
    database = configuration.get(CELESTINE, APPLICATION)
    fallback = "__init__"
    application = override or database or fallback

    override = argument.language
    database = configuration.get(CELESTINE, LANGUAGE)
    fallback = "__init__"
    language = override or database or fallback

    language = load.module_fallback(LANGUAGE, argument.language)

    return (application, language)
