""""""

import dataclasses
import sys
import typing

from celestine.session.argument import Argument
from celestine.session.configuration import Configuration


@dataclasses.dataclass
class Attribute():
    """"""

    def __init__(
        self,
        arguments: Argument,
        args: list[str],
    ):
        """"""

        argument = arguments.parser.parse_args(args)

        self.application = None
        self.interface = None
        self.language = None
        self.python = None
        self.task = None

        directory = sys.path[0]
        application = arguments.application

        attribute: typing.Dict[str, str] = arguments.dictionary

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
