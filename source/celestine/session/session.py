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

from celestine.session import load

from celestine.session.argument import Argument
from celestine.session.argument import Override
from celestine.session.argument import Positional


from celestine.text.directory import APPLICATION
from celestine.text.directory import INTERFACE
from celestine.text.directory import LANGUAGE

from celestine.text.unicode import NONE

from .text import VERSION
from .text import STORE_TRUE
from .text import HELP
from .text import CONFIGURATION
from .text import EN
from .text import INIT
from .text import MAIN

Magic: TA = D[U[Argument, T[Argument]], U[AP, AG]]

AD: TA = D[str, Argument]


class Dull():
    """"""

    @staticmethod
    def dictionary(_: MT, language: MT) -> AD:
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


class Dictionary():
    """"""

    @classmethod
    def dictionary(cls, application: MT, language: MT) -> AD:
        return {}

    def __setattr__(self, name: str, value: str) -> None:
        """"""
        self.__dict__[name] = load.module_fallback(name, value)


class Application(Dictionary):
    """"""

    application: types.ModuleType

    @classmethod
    def dictionary(cls, application: MT, language: MT) -> AD:
        """"""
        return super().dictionary(application, language) | {
            APPLICATION: Override(
                NONE,
                "Choose an applicanion. They have more option.",
                load.argument(APPLICATION),
            ),
        }


class Interface(Dictionary):
    """"""

    interface: types.ModuleType

    @classmethod
    def dictionary(cls, application: MT, language: MT) -> AD:
        """"""
        return super().dictionary(application, language) | {
            INTERFACE: Override(
                load.argument_default(INTERFACE),  # TODO: change to NONE
                language.ARGUMENT_INTERFACE_HELP,
                load.argument(INTERFACE),
            ),
        }


class Language(Dictionary):
    """"""

    language: types.ModuleType

    @classmethod
    def dictionary(cls, application: MT, language: MT) -> AD:
        """"""
        return super().dictionary(application, language) | {
            LANGUAGE: Override(
                NONE,
                language.ARGUMENT_LANGUAGE_HELP,
                load.argument(LANGUAGE),
            ),
        }


class Session(Application, Interface, Language):
    """"""

    main: str

    @classmethod
    def dictionary(cls, application: MT, language: MT) -> AD:
        """"""
        return super().dictionary(application, language) | {
            MAIN: Positional(
                MAIN,
                language.ARGUMENT_LANGUAGE_HELP,
                load.function_keys(application),
            ),
        }

    def __setattr__(self, name: str, value: str) -> None:
        """"""
        match name:
            case "main":
                self.__dict__[name] = value
            case "attribute":
                self.__dict__[name] = value
            case _:
                super().__setattr__(name, value)
