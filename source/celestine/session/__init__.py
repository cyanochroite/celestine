"""Celestine Image Viewer"""

import types
import typing
import dataclasses

from celestine.session.argument import Argument
from celestine.window.page import Page

from celestine.session import load

from celestine.text.directory import APPLICATION
from celestine.text.directory import INTERFACE
from celestine.text.directory import LANGUAGE


@dataclasses.dataclass
class Session():
    """"""

    application: types.ModuleType
    interface: types.ModuleType
    language: types.ModuleType

    main: list[typing.Callable[[Page], None]]

    def __init__(
        self,
        args: list[str],
        exit_on_error: bool
    ) -> None:
        """"""

        # (self.attribute, attribute) = Argument.make(args, exit_on_error)

        argument = Argument(args, exit_on_error)
        argument.dostuff()

        self.attribute = argument.new_attribute
        attribute = argument.attribute

        self.application = load.module(
            APPLICATION,
            attribute.application,
        )
        self.interface = load.module(
            INTERFACE,
            attribute.interface,
        )
        self.language = load.module(
            LANGUAGE,
            attribute.language,
        )

        self.main = getattr(
            self.application,
            attribute.main,
        )

        # self.application = load.module(APPLICATION, attribute.application)
        # self.interface = load.module(INTERFACE, attribute.interface)
        # self.language = load.module(LANGUAGE, attribute.language)

        # self.main = getattr(self.application, attribute.main)


