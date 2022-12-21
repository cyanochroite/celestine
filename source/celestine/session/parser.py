""""""

import argparse

import types
import typing

from celestine.session.argument import Argument
from celestine.session.argument import Optional
from celestine.session.argument import Override
from celestine.session.argument import Information
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
        name: str,
        *path: str,
    ):

        self.application = application
        self.language = language

        module = load.module(*path)

        session = getattr(module, name)
        self.attribute = session()
        self.dictionary = self.attribute.dictionary(self.language)

    def items(
        self,
    ) -> typing.Iterable[typing.Tuple[str, Argument]]:
        """"""

        return self.dictionary.items()


class Parser():
    """"""

    add_argument: typing.Dict[Argument, argparse._ArgumentGroup]
    configuration: Configuration
    parser: argparse.ArgumentParser

    def __init__(
        self,
        exit_on_error: bool,
        language: types.ModuleType,
    ) -> None:
        """"""
        self.configuration = Configuration()
        self.configuration.load()

        self.parser = argparse.ArgumentParser(
            add_help=False,
            prog=CELESTINE,
            exit_on_error=exit_on_error,
        )

        self.add_argument = {}
        self.add_argument[Information] = self.parser.add_argument_group(
            title=language.ARGUMENT_INFORMATION_TITLE,
            description=language.ARGUMENT_INFORMATION_DESCRIPTION,
        )
        self.add_argument[Optional] = self.parser.add_argument_group(
            title=language.ARGUMENT_OVERRIDE_TITLE + "MOO",
            description=language.ARGUMENT_OVERRIDE_DESCRIPTION + "COW",
        )
        self.add_argument[Override] = self.parser.add_argument_group(
            title=language.ARGUMENT_OVERRIDE_TITLE,
            description=language.ARGUMENT_OVERRIDE_DESCRIPTION,
        )
        self.add_argument[Positional] = self.parser.add_argument_group(
            title=language.ARGUMENT_OVERRIDE_TITLE + "MOO",
            description=language.ARGUMENT_OVERRIDE_DESCRIPTION + "COW",
        )

    @classmethod
    def dofilt(
        cls,
        args: list[str],
        exit_on_error: bool
    ) -> None:
        """"""

        configuration = Configuration()
        configuration.load()

        one = Flag(True, "__init__").key(APPLICATION)
        two = Flag(True, "__init__").key(LANGUAGE)

        turbo = Hippo(
            CELESTINE,
            "",
            "Session",
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
        #         return namespace, args

        cls.foot(turbo, parse_known_args, configuration)

        return turbo

    def dostuff(self, args, turbo):
        """"""

        dull_attribute = Hippo(
            turbo.attribute.application,
            turbo.attribute.language,
            "Session",
            "session",
            "dull",
        )
        old_attribute = Hippo(
            turbo.attribute.application,
            turbo.attribute.language,
            "Session",
            "session",
            "session",
        )
        new_attribute = Hippo(
            turbo.attribute.application,
            turbo.attribute.language,
            "Session",
            APPLICATION,
            turbo.attribute.application,
        )

        self.head(dull_attribute)
        self.head(old_attribute)
        self.head(new_attribute)

        args = self.parser.parse_args(args)

        self.foot(dull_attribute, args, self.configuration)
        self.foot(old_attribute, args, self.configuration)
        self.foot(new_attribute, args, self.configuration)

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

    @staticmethod
    def foot(
        attribute: Hippo,
        args,
        configuration,
    ) -> None:
        """"""

        application = attribute.application

        for (name, argument) in attribute.items():
            if not argument.use:
                continue
            override = getattr(args, name, NONE)
            database = configuration.get(application, name)
            value = override or database or argument.fallback
            setattr(attribute.attribute, name, value)
            if getattr(args, CONFIGURATION, NONE):
                configuration.set(application, name, override)


def start_session(
    argv: list[str],
    exit_on_error: bool,
) -> None:
    """"""
    turbo = Parser.dofilt(argv, exit_on_error)
    argument = Parser(exit_on_error, turbo.attribute.language)
    session = argument.dostuff(argv, turbo)
    return session
