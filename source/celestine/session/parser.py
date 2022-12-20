""""""

import argparse

import typing

from celestine.session.argument import Argument
from celestine.session.argument import Optional
from celestine.session.argument import Override
from celestine.session.argument import Name
from celestine.session.argument import Flag

from celestine.session.argument import Positional


from celestine.text.unicode import NONE


from celestine.session import load

from celestine.text import CELESTINE
from celestine.text import VERSION_NUMBER

from celestine.text.directory import APPLICATION
from celestine.text.directory import LANGUAGE

from celestine.text.unicode import HYPHEN_MINUS

from .configuration import Configuration

from .text import HELP
from .text import STORE_TRUE
from .text import VERSION


CONFIGURATION = "configuration"


class Hippo():
    """"""

    def __init__(
        self,
        application: str,
        language: str,
        *path: str,
    ):

        self.application = application
        self.language = language

        module = load.module(*path)

        self.attribute = module.Session()
        self.dictionary = self.attribute.dictionary(self.language)

    def items(
        self,
    ) -> typing.Iterable[typing.Tuple[str, Argument]]:
        """"""

        return self.dictionary.items()


class Parser():
    """"""

    add_argument: typing.Dict[Argument, argparse._ArgumentGroup]

    def __init__(
        self,
        args: list[str],
        exit_on_error: bool
    ) -> None:
        """"""

    def setup(
        self,
        args: list[str],
        exit_on_error: bool
    ) -> None:
        """"""

        one = Flag("__init__").key(APPLICATION)
        two = Flag("__init__").key(LANGUAGE)

        turbo = Hippo(
            CELESTINE,
            None,
            "session",
            "turbo",
        )

        parser = argparse.ArgumentParser(
            add_help=False,
            exit_on_error=exit_on_error,
        )

        parser.add_argument(*one)
        parser.add_argument(*two)

        (parse_known_args, _) = parser.parse_known_args(args)

        self.configuration = Configuration()
        self.configuration.load()

        override = parse_known_args.application
        database = self.configuration.get(CELESTINE, APPLICATION)
        fallback = "__init__"
        application = override or database or fallback

        override = parse_known_args.language
        database = self.configuration.get(CELESTINE, LANGUAGE)
        fallback = "__init__"
        language = override or database or fallback

        language = load.module_fallback(LANGUAGE, parse_known_args.language)

        # (application, language) = self.essential(args, exit_on_error)

        self.dictionary: typing.Dict[str, str] = {}
        self.parser = argparse.ArgumentParser(
            add_help=False,
            prog=CELESTINE,
            exit_on_error=exit_on_error,
        )

        # FLAGS WITH NO PARAMETER
        self.information = self.parser.add_argument_group(
            title=language.ARGUMENT_INFORMATION_TITLE,
            description=language.ARGUMENT_INFORMATION_DESCRIPTION,
        )

        self.override = self.parser.add_argument_group(
            title=language.ARGUMENT_OVERRIDE_TITLE,
            description=language.ARGUMENT_OVERRIDE_DESCRIPTION,
        )

        self.positional = self.parser.add_argument_group(
            title=language.ARGUMENT_OVERRIDE_TITLE + "MOO",
            description=language.ARGUMENT_OVERRIDE_DESCRIPTION + "COW",
        )

        self.optional = self.parser.add_argument_group(
            title=language.ARGUMENT_OVERRIDE_TITLE + "MOO",
            description=language.ARGUMENT_OVERRIDE_DESCRIPTION + "COW",
        )

        # self.information.add_argument(
        #    self.flag(CONFIGURATION),
        #    self.name(CONFIGURATION),
        #    action=STORE_TRUE,
        #    help=language.ARGUMENT_HELP_HELP,
        # )

        # self.information.add_argument(
        #    self.flag(HELP),
        #    self.name(HELP),
        #    action=HELP,
        #    help=language.ARGUMENT_HELP_HELP,
        # )

        # self.information.add_argument(
        #    self.flag(VERSION),
        #    self.name(VERSION),
        #    action=VERSION,
        #    help=language.ARGUMENT_VERSION_HELP,
        #    version=VERSION_NUMBER,
        # )

        self.information.add_argument(
            "-h", "--help",
            action=HELP,
            help=language.ARGUMENT_HELP_HELP,
        )

        # ignore above for now

        self.add_argument = {}
        self.add_argument[Positional] = self.positional
        self.add_argument[Optional] = self.optional
        self.add_argument[Override] = self.override

        # rest of stuff
        self.application = application
        self.language = language

        return self

    def dostuff(self, args):
        """"""

        old_attribute = Hippo(
            self.application,
            self.language,
            "session",
            "session",
        )
        new_attribute = Hippo(
            self.application,
            self.language,
            APPLICATION,
            self.application,
        )

        self.head(old_attribute)
        self.head(new_attribute)
        self.parse_args = self.parser.parse_args(args)
        self.foot(old_attribute)
        self.foot(new_attribute)

        self.configuration.save()

        session = old_attribute.attribute
        session.attribute = new_attribute.attribute

        return session

    def head(  # feed the parser
        self,
        attribute: Hippo,
    ) -> None:
        """"""

        for (name, argument) in attribute.items():
            (args, kwargs) = argument.value(name)
            parser = self.add_argument[argument]
            parser.add_argument(*args, **kwargs)

    def foot(
        self,
        attribute: Hippo,
    ) -> None:
        """"""

        application = attribute.application

        for (name, fallback) in attribute.items():
            override = getattr(self.parse_args, name, NONE)
            database = self.configuration.get(application, name)
            value = override or database or fallback.fallback
            setattr(attribute.attribute, name, value)
            # if self.parse_args.configuration:
            #    self.configuration.set(application, name, override)


def start_session(
    argv: list[str],
    exit_on_error: bool,
) -> None:
    """"""

    argument = Parser(argv, exit_on_error)
    cat = argument.setup(argv, exit_on_error)
    session = argument.dostuff(argv)
    return session
