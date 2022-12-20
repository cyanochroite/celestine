"""Celestine Image Viewer"""

import typing

from celestine.session.argument import Argument
from celestine.session.argument import Flag

from celestine.session import load

from celestine.text.directory import APPLICATION
from celestine.text.directory import LANGUAGE


class Session():
    """"""

    application: str
    language: str

    @staticmethod
    def dictionary(
        _,
    ) -> typing.Dict[str, Argument]:
        """"""

        return {
            APPLICATION: Flag("__init__"),
            LANGUAGE: Flag("__init__"),
        }

    def __setattr__(self, name, value):
        match name:
            case "application":
                super().__setattr__(name, value)
            case "language":
                module = load.module(name, value)
                super().__setattr__(name, module)
