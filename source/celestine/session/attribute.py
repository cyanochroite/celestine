import dataclasses
import os

from celestine.session.configuration import Configuration


@dataclasses.dataclass
class Attribute():
    def __init__(self, argument, attribute, default):
        self.application = None
        self.interface = None
        self.language = None
        self.python = None
        self.task = None

        directory = os.getcwd()
        section = argument.application

        configuration = Configuration.make(directory)

        for (name, failover) in zip(attribute, default, strict=True):
            database = configuration.get(section, name, fallback=None)
            override = getattr(argument, name, None)
            value = override or database or failover
            setattr(self, name, value)
