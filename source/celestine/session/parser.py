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


from .configuration import Configuration


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


def dofilt(
    argv: list[str],
    exit_on_error: bool
) -> None:
    """"""

    configuration = Configuration()
    configuration.load()

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

    add_argument = {}
    add_argument[Name] = parser
    add_argument[Flag] = parser

    feed_the_parser(
        add_argument,
        lambda: parser.parse_known_args(argv)[0],
        configuration,
        [turbo],
    )

    return turbo


def dostuff(args, exit_on_error, turbo):
    """"""

    language = turbo.attribute.language
    parser = argparse.ArgumentParser(
        add_help=False,
        prog=CELESTINE,
        exit_on_error=exit_on_error,
    )

    add_argument = {}
    add_argument[Information] = parser.add_argument_group(
        title=language.ARGUMENT_INFORMATION_TITLE,
        description=language.ARGUMENT_INFORMATION_DESCRIPTION,
    )
    add_argument[Optional] = parser.add_argument_group(
        title=language.ARGUMENT_OVERRIDE_TITLE + "MOO",
        description=language.ARGUMENT_OVERRIDE_DESCRIPTION + "COW",
    )
    add_argument[Override] = parser.add_argument_group(
        title=language.ARGUMENT_OVERRIDE_TITLE,
        description=language.ARGUMENT_OVERRIDE_DESCRIPTION,
    )
    add_argument[Positional] = parser.add_argument_group(
        title=language.ARGUMENT_OVERRIDE_TITLE + "MOO",
        description=language.ARGUMENT_OVERRIDE_DESCRIPTION + "COW",
    )

    information = parser.add_argument_group(
        title=language.ARGUMENT_INFORMATION_TITLE,
        description=language.ARGUMENT_INFORMATION_DESCRIPTION,
    )
    optional = parser.add_argument_group(
        title=language.ARGUMENT_OVERRIDE_TITLE + "MOO",
        description=language.ARGUMENT_OVERRIDE_DESCRIPTION + "COW",
    )
    override = parser.add_argument_group(
        title=language.ARGUMENT_OVERRIDE_TITLE,
        description=language.ARGUMENT_OVERRIDE_DESCRIPTION,
    )
    positional = parser.add_argument_group(
        title=language.ARGUMENT_OVERRIDE_TITLE + "MOO",
        description=language.ARGUMENT_OVERRIDE_DESCRIPTION + "COW",
    )

    add_argument = {}
    add_argument[Information] = information
    add_argument[Optional] = optional
    add_argument[Override] = override
    add_argument[Positional] = positional
    configuration = Configuration()
    configuration.load()

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

    feed_the_parser(
        add_argument,
        lambda: parser.parse_args(args),
        configuration,
        [dull_attribute, old_attribute, new_attribute],
    )

    configuration.save()

    session = old_attribute.attribute
    session.attribute = new_attribute.attribute

    return session


def feed_the_parser(
    add_argument: typing.Dict[Argument, argparse._ArgumentGroup],
    calling,
    configuration,
    attributes: list[Hippo],
) -> None:
    """"""

    for attribute in attributes:
        for (name, argument) in attribute.items():
            (args, kwargs) = argument.value(name)
            parser = add_argument[argument]
            parser.add_argument(*args, **kwargs)

    args = calling()

    for attribute in attributes:
        for (name, argument) in attribute.items():
            if not argument.use:
                continue
            override = getattr(args, name, NONE)
            database = configuration.get(attribute.application, name)
            value = override or database or argument.fallback
            setattr(attribute.attribute, name, value)
            if getattr(args, CONFIGURATION, NONE):
                configuration.set(attribute.application, name, override)


def start_session(
    argv: list[str],
    exit_on_error: bool,
) -> None:
    """"""
    turbo = dofilt(argv, exit_on_error)
    session = dostuff(argv, exit_on_error, turbo)
    return session
