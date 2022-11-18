"""Celestine Image Viewer"""
from celestine.session.argument import Argument
from celestine.session.attribute import Attribute

from celestine.session import load


from celestine.string.all import APPLICATION
from celestine.string.all import CELESTINE

from celestine.string.all import INTERFACE
from celestine.string.all import LANGUAGE
from celestine.string.all import PYTHON


TERMINAL = "terminal"
ENGLISH = "english"
PYTHON_3_10 = "python_3_10"
CONFIGURE = "configure"
STORE = "store"
TKINTER = "tkinter"
EN = "en"
TASK = "task"


class Session():
    def __init__(self, args, exit_on_error):
        argument = Argument(args, exit_on_error)

        default = [
            load.argument_default(APPLICATION),
            load.argument_default(INTERFACE),
            EN,
            load.argument_default(PYTHON),
            "main"
        ]
        attribute = [
            APPLICATION,
            INTERFACE,
            LANGUAGE,
            PYTHON,
            "task",
        ]

        applications = load.argument(APPLICATION)
        for application in applications:
            module = load.module(APPLICATION, application)
            attribute.extend(module.attribute())
            default.extend(module.default())

        self.attribute = Attribute(
            argument.parser.parse_args(args),
            attribute,
            default,
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
