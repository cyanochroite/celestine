""""""

import types
import typing

from types import ModuleType as MT
from typing import Dict as D
from typing import Type as T
from typing import Union as U
from typing import TypeAlias as TA

from argparse import _ArgumentGroup as AG
from argparse import ArgumentParser as AP

from celestine.session.argument import Information
from celestine.session.argument import Flag

from celestine.session import load

from celestine.session.argument import Argument
from celestine.session.argument import Override


from celestine.text.directory import APPLICATION
from celestine.text.directory import INTERFACE
from celestine.text.directory import LANGUAGE

from .text import VERSION
from .text import STORE_TRUE
from .text import HELP
from .text import CONFIGURATION
from .text import EN


class Session():
    """"""

    application: str
    interface: types.ModuleType
    language: types.ModuleType

    @staticmethod
    def dictionary(language) -> typing.Dict[str, Argument]:
        """"""
        return {
            APPLICATION: Override(
                "demo",
                "Choose an applicanion. They have more option.",
                load.argument(APPLICATION),
            ),
            INTERFACE: Override(
                load.argument_default(INTERFACE),
                language.ARGUMENT_INTERFACE_HELP,
                load.argument(INTERFACE),
            ),
            LANGUAGE: Override(
                EN,
                language.ARGUMENT_LANGUAGE_HELP,
                load.argument(LANGUAGE),
            ),
        }

    def __setattr__(self, name: str, value: str) -> None:
        """"""
        match name:
            case "attribute":
                super().__setattr__(name, value)
            case _:
                module = load.module(name, value)
                super().__setattr__(name, module)


class Turbo():
    """"""

    application: str
    language: str

    @staticmethod
    def dictionary(_) -> typing.Dict[str, Argument]:
        """"""
        return {
            APPLICATION: Flag(True, "__init__"),
            LANGUAGE: Flag(True, "__init__"),
        }

    def __setattr__(self, name: str, value: str) -> None:
        """"""
        match name:
            case "application":
                super().__setattr__(name, value)
            case "language":
                module = load.module(name, value)
                super().__setattr__(name, module)


class Dull():
    """"""

    @staticmethod
    def dictionary(language) -> typing.Dict[str, Argument]:
        """"""
        return {
            CONFIGURATION: Information(
                "",
                STORE_TRUE,
                language.ARGUMENT_HELP_HELP,
                False,
            ),
            HELP: Information(
                "",
                HELP,
                language.ARGUMENT_HELP_HELP,
                False,
            ),
            VERSION: Information(
                "",
                VERSION,
                language.ARGUMENT_VERSION_HELP,
                True,
            ),
        }


class Dictionary(typing.Protocol):
    """"""

    @staticmethod
    def dictionary(_: MT) -> typing.Dict[str, Argument]:
        ...


Magic: TA = D[U[Argument, T[Argument]], U[AP, AG]]
