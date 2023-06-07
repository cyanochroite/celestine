""""""

import configparser

from celestine import load
from celestine.data.directory import APPLICATION
from celestine.file.data import (
    UTF_8,
    WRITE_TEXT,
)
from celestine.typed import (
    B,
    N,
    S,
)
from celestine.unicode import (
    EQUALS_SIGN,
    NONE,
    POUND_SIGN,
)

from .data import FILE


class Configuration:
    """Parse configuration stuff."""

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

    def has_section(self, section: S, option: S) -> B:
        """Also checks if using default section name."""
        has_section = self.configuration.has_section(section)

        if option == APPLICATION:
            section = APPLICATION

        if section == APPLICATION:
            has_section = True

        return has_section

    def get(self, section: S, option: S) -> S:
        """"""
        if self.has_section(section, option):
            if self.configuration.has_option(section, option):
                return self.configuration[section][option]

        return NONE

    def set(self, section: S, option: S, value: S) -> N:
        """"""
        if not self.has_section(section, option):
            self.configuration.add_section(section)

        self.configuration[section][option] = value
