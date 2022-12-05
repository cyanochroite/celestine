"""Celestine Image Viewer"""

import dataclasses

from celestine.session.argument import Argument
from celestine.session.attribute import Attribute

from celestine.session import load


from celestine.text.directory import APPLICATION
from celestine.text.directory import INTERFACE
from celestine.text.directory import LANGUAGE
from celestine.text.directory import PYTHON


@dataclasses.dataclass
class Session():
    """"""

    def __init__(
        self,
        args: list[str],
        exit_on_error: bool
    ) -> None:
        """"""

        argument = Argument(args, exit_on_error)

        self.attribute = Attribute(
            argument,
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
        self.python = load.module(
            PYTHON,
            self.attribute.python,
        )
        self.task = load.module(
            APPLICATION,
            self.attribute.application,
            self.attribute.task,
        )
