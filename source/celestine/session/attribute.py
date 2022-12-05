import dataclasses
import sys
import typing

from celestine.session.argument import Argument
from celestine.session.configuration import Configuration

from celestine.session import load


TERMINAL = "terminal"
ENGLISH = "english"
PYTHON_3_10 = "python_3_10"
CONFIGURE = "configure"
STORE = "store"
TKINTER = "tkinter"
EN = "en"
TASK = "task"
INTERFACE = "interface"
LANGUAGE = "language"
PYTHON = "python"


@dataclasses.dataclass
class Attribute():
    def __init__(
        self,
        arguments: Argument,
        args: list[str],
    ):

        argument = arguments.parser.parse_args(args)

        self.application = None
        self.interface = None
        self.language = None
        self.python = None
        self.task = None

        attribute: typing.Dict[str, str]
        attribute = {
            INTERFACE: load.argument_default(INTERFACE),
            LANGUAGE: EN,
            PYTHON: load.argument_default(PYTHON),
        }

        directory = sys.path[0]
        application = argument.application

        attribute |= arguments.get_argument()

        configuration = Configuration.make(directory)

        for (name, failover) in attribute.items():
            database = configuration.get(
                application,
                name,
                fallback=None,
            )
            override = getattr(argument, name, None)
            value = override or database or failover
            setattr(self, name, value)
