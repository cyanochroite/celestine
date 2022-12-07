""""""

import configparser

from celestine.text.session import CONFIGURATION

from celestine.text.stream import WRITE_TEXT
from celestine.text.stream import UTF_8

from celestine.session import load
from celestine.text import CELESTINE

from celestine.text.unicode import NONE

import typing


class Configuration():
    """parse configuration stuff."""

    def __init__(
        self,
    ) -> None:
        """"""

        self.path = load.pathway(CONFIGURATION)

        defaults: typing.Mapping[str, str] = {}

        self.configuration = configparser.ConfigParser(
            defaults=defaults,
            delimiters=("="),
            comment_prefixes=("#"),
            strict=True,
            empty_lines_in_values=False,
            default_section=CELESTINE,
        )

    def load(
        self,
    ) -> None:
        """Load the configuration file."""

        self.configuration.read(self.path, encoding=UTF_8)

    def save(
        self,
    ) -> None:
        """Save the configuration file."""

        with open(self.path, WRITE_TEXT, encoding=UTF_8) as file:
            self.configuration.write(file, True)

    def get(
        self,
        section: str,
        option: str
    ) -> str:
        """"""

        try:
            return self.configuration[section][option]
        except KeyError:
            return NONE

    def set(
        self,
        section: str,
        option: str,
        value: str,
    ) -> None:
        """"""

        if not self.configuration.has_section(section):
            self.configuration.add_section(section)

        self.configuration[section][option] = value

    def add_configuration(self, configuration, module, application):
        """Build up the configuration file."""
        if not configuration.has_section(application):
            configuration.add_section(application)
        attribute = module.attribute()
        default = module.default()
        for item in zip(attribute, default, strict=True):
            (name, value) = item
            configuration.set(application, name, value)

        return configuration
