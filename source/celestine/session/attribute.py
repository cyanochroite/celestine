""""""

import dataclasses
import sys
import typing

from celestine.session.argument import Argument
from celestine.session.configuration import Configuration

from celestine.text.unicode import NONE


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

        for (name, fallback) in attribute.items():

            override = getattr(parse_args, name, NONE)
            database = configuration.get(application, name)
            value = override or database or fallback
            setattr(self, name, value)
            if parse_args.configuration:
                configuration.set(application, name, override)

        configuration.save()
