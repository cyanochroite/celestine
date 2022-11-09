import dataclasses

from celestine.session.configuration import Configuration


@dataclasses.dataclass
class Attribute():
    def __init__(self, argument, directory, attribute, default, section):
        self.language = None
        self.task = None
        self.interface = None

        configuration = Configuration.make(directory)

        for (name, failover) in zip(attribute, default, strict=True):
            database = configuration.get(section, name, fallback=None)
            override = getattr(argument, name, None)
            value = override or database or failover
            setattr(self, name, value)
