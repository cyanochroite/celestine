"""Celestine Image Viewer"""

import typing

from celestine.session.argument import Argument
from celestine.session.argument import Flag

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
