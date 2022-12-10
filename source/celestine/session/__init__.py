"""Celestine Image Viewer"""

import types
import typing
import dataclasses

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
        new_attribute,
        attribute,
    ) -> None:
        """"""

        self.attribute = new_attribute

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
