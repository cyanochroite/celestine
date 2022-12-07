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

        application = argument.application

        attribute: typing.Dict[str, str] = argument.dictionary

        configuration = Configuration()
        configuration.load()

        if parse_args.configuration:
            configuration.set("pig", "dig", "hole")

        configuration.save()

        for (name, failover) in attribute.items():
            database = configuration.get(application, name)
            override = getattr(parse_args, name, None)
            value = override or database or failover
            setattr(self, name, value)
