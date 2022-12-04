"""Celestine Image Viewer"""
from celestine.session.argument import Argument
from celestine.session.attribute import Attribute

from celestine.session import load


from celestine.text.all import APPLICATION

from celestine.text.all import INTERFACE
from celestine.text.all import LANGUAGE
from celestine.text.all import PYTHON


TERMINAL = "terminal"
ENGLISH = "english"
PYTHON_3_10 = "python_3_10"
CONFIGURE = "configure"
STORE = "store"
TKINTER = "tkinter"
EN = "en"
TASK = "task"


class Session():
    def __init__(self, args: list[str], exit_on_error: bool) -> None:
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
