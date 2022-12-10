""""""

import typing
import types
import os

from celestine.session.attribute import Optional
from celestine.session.attribute import Override
from celestine.session.attribute import Positional

from celestine.session.attribute import Attribute

from .main import window
from .text import DIRECTORY

NONE = ""


class Attribute2:
    """"""

    def __init__(
        self,
        application,
        language,
        parser,
        args,
        configuration,
    ) -> None:
        """"""

        self.application = application
        self.language = language
        self.parser = parser
        self.args = args
        self.configuration = configuration

    def hippo(self):
        """"""""

    @staticmethod
    def attribute(
        language: types.ModuleType
    ) -> typing.Dict[str, Attribute]:
        """"""

        return {
            DIRECTORY: Optional(
                os.getcwd(),
                "pick your nose",
            ),
            "ape": Override(
                "four",
                "moo",
                [],
            ),
            "you": Positional(
                language.ARGUMENT_OVERRIDE_TITLE,
                "cow",
                [],
            ),
        }

    def __enter__(self):
        # super().__enter__()
        return {
            DIRECTORY: Optional(
                os.getcwd(),
                "pick your nose",
            ),
            "ape": Override(
                "four",
                "moo",
                [],
            ),
            "you": Positional(
                self.language.ARGUMENT_OVERRIDE_TITLE,
                "cow",
                [],
            ),
        }

    def __exit__(self, exc_type, exc_value, traceback):
        # super().__exit__(exc_type, exc_value, traceback)

        dictionary = self.attribute(self.language)
        parse_args = self.parser.parse_args(self.args)

        for (name, fallback) in dictionary.items():
            override = getattr(parse_args, name, NONE)
            database = self.configuration.get(self.application, name)
            value = override or database or fallback
            setattr(self, name, value)
            if parse_args.configuration:
                self.configuration.set(self.application, name, override)

        return False


def main(_):
    """"""
    return [
        window,
    ]
