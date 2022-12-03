import typing
import dataclasses
import sys

from celestine.session.argument import Argument
from celestine.session.configuration import Configuration


@dataclasses.dataclass
class Attribute():
    def __init__(
        self,
        argument: Argument,
        attribute: typing.Dict[str, str],
    ):
        self.application = None
        self.interface = None
        self.language = None
        self.python = None
        self.task = None

        directory = sys.path[0]
        section = argument.application

        configuration = Configuration.make(directory)

        for (name, failover) in attribute.items():
            database = configuration.get(section, name, fallback=None)
            override = getattr(argument, name, None)
            value = override or database or failover
            setattr(self, name, value)
