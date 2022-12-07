"""Celestine Image Viewer"""

import types
import typing
import dataclasses

from celestine.session.argument import Argument
from celestine.session.attribute import Attribute
from celestine.window.page import Page

from celestine.session import load

from celestine.text.directory import APPLICATION
from celestine.text.directory import INTERFACE
from celestine.text.directory import LANGUAGE


@dataclasses.dataclass
class Session():
    """"""

    attribute: Attribute

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

        self.attribute = Attribute(
            Argument(args, exit_on_error),
            args,
        )

        self.application = load.module(
            APPLICATION,
            self.attribute.application,
        )
        self.interface = load.module(
            INTERFACE,
            self.attribute.interface,
        )
        self.language = load.module(
            LANGUAGE,
            self.attribute.language,
        )

        self.main = getattr(
            self.application,
            self.attribute.main,
        )


