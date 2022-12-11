"""Celestine Image Viewer"""

import types
import typing

from celestine.window.page import Page

from celestine.session import load

from celestine.session.argument import Argument
from celestine.session.argument import Override
from celestine.session.argument import Positional


from celestine.text.directory import APPLICATION
from celestine.text.directory import INTERFACE
from celestine.text.directory import LANGUAGE

EN = "en"
VIEWER = "viewer"
MAIN = "main"

CHOICES = "choices"


class Session():
    """"""

    application: types.ModuleType
    interface: types.ModuleType
    language: types.ModuleType

    main: list[typing.Callable[[Page], None]]

    @staticmethod
    def dictionary(
        language,
    ) -> typing.Dict[str, Argument]:
        """"""

        return {
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
            APPLICATION: Positional(
                load.argument_default(APPLICATION),
                "Choose an applicanion. They have more option.",
                load.argument(APPLICATION),
            ),
            MAIN: Positional(
                MAIN,
                "Choose an applicanion. They have more option.",
                [MAIN],
            ),
        }

    def __setattr__(self, name, value):
        match name:
            case "main":
                main = getattr(self.application, value)
                super().__setattr__(name, main)
            case "attribute":
                super().__setattr__(name, value)
            case _:
                module = load.module(name, value)
                super().__setattr__(name, module)
