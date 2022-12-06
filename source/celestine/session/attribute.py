""""""

import dataclasses
import sys
import typing

from celestine.session.argument import Argument
from celestine.session.configuration import Configuration


@dataclasses.dataclass
class Attribute():
    """"""

    application: str
    interface: str
    language: str
    main: str
    python: str

    def __init__(
        self,
        argument: Argument,
        args: list[str],
    ):
        """"""

        parse_args = argument.parser.parse_args(args)

        directory = sys.path[0]
        application = argument.application

        attribute: typing.Dict[str, str] = argument.dictionary

        configuration = Configuration.make(directory)

        for (name, failover) in attribute.items():
            database = configuration.get(
                application,
                name,
                fallback=None,
            )
            override = getattr(parse_args, name, None)
            value = override or database or failover
            setattr(self, name, value)
