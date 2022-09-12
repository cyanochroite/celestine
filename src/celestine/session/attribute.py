import dataclasses

from celestine.session.configuration import Configuration


@dataclasses.dataclass
class Attribute():
    def __init__(self, argument, directory, module, section):
        configuration = Configuration.make(directory)

        attribute = module.attribute()
        default = module.default()

        for (name, failover) in zip(attribute, default, strict=True):
            database = configuration.get(section, name, fallback=None)
            override = getattr(argument, name, None)
            value = override or database or failover
            setattr(self, name, value)



