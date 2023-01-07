""""""

import configparser

from celestine.text.stream import WRITE_TEXT
from celestine.text.stream import UTF_8

from celestine.session import load
from celestine.text import CELESTINE

from celestine.text.unicode import NONE

from celestine.typed import MT
from celestine.typed import N
from celestine.typed import S

from .text import FILE
from .session import SuperState


class Configuration(SuperState):
    """parse configuration stuff."""

    def __init__(self, application: MT, interface: MT, language: MT) -> N:
        """"""
        super().__init__(application, interface, language)

        self.path = load.pathway(FILE)

        self.configuration = configparser.ConfigParser(
            delimiters=("="),
            comment_prefixes=("#"),
            strict=True,
            empty_lines_in_values=False,
            default_section=CELESTINE,
        )

    def load(self) -> N:
        """Load the configuration file."""
        self.configuration.read(self.path, encoding=UTF_8)

    def save(self) -> N:
        """Save the configuration file."""
        with open(self.path, WRITE_TEXT, encoding=UTF_8) as file:
            self.configuration.write(file, True)

    def get(self, module: MT) -> S:
        """"""
        section = load.module_to_name(module)
        option = load.module_to_name(self._application)
        if self.configuration.has_section(section):
            if self.configuration.has_option(section, option):
                return self.configuration[section][option]

        return NONE

    def set(self, section: S, option: S, value: S) -> N:
        """"""
        if not value:
            return

        if not self.configuration.has_section(section):
            if section != CELESTINE:
                self.configuration.add_section(section)

        self.configuration[section][option] = value
