""""""

import configparser

from celestine import load

from celestine.text.directory import APPLICATION
from celestine.text.stream import UTF_8
from celestine.text.stream import WRITE_TEXT

from celestine.typed import N
from celestine.typed import S

from celestine.unicode import EQUALS_SIGN
from celestine.unicode import NONE
from celestine.unicode import POUND_SIGN

from .text import FILE


class Configuration():
    """parse configuration stuff."""

    def __init__(self) -> N:
        """"""
        self.path = load.pathway(FILE)

        self.configuration = configparser.ConfigParser(
            delimiters=(EQUALS_SIGN),
            comment_prefixes=(POUND_SIGN),
            strict=True,
            empty_lines_in_values=False,
            default_section=APPLICATION,
        )

    def load(self) -> N:
        """Load the configuration file."""
        self.configuration.read(self.path, encoding=UTF_8)

    def save(self) -> N:
        """Save the configuration file."""
        with open(self.path, WRITE_TEXT, encoding=UTF_8) as file:
            self.configuration.write(file, True)

    def get(self, section: S, option: S) -> S:
        """"""
        if section == APPLICATION:
            if self.configuration.has_option(section, option):
                return self.configuration[section][option]

        if self.configuration.has_section(section):
            if self.configuration.has_option(section, option):
                return self.configuration[section][option]

        return NONE

    def set(self, section: S, option: S, value: S) -> N:
        """"""
        if not self.configuration.has_section(section):
            if section != APPLICATION:
                self.configuration.add_section(section)

        self.configuration[section][option] = value
