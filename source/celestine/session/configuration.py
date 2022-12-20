""""""

import configparser

from celestine.session.text import CONFIGURATION

from celestine.text.stream import WRITE_TEXT
from celestine.text.stream import UTF_8

from celestine.session import load
from celestine.text import CELESTINE

from celestine.text.unicode import NONE


class Configuration():
    """parse configuration stuff."""

    def __init__(
        self,
    ) -> None:
        """"""

        self.path = load.pathway(CONFIGURATION)

        self.configuration = configparser.ConfigParser(
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

        if self.configuration.has_section(section):
            if self.configuration.has_option(section, option):
                return self.configuration[section][option]

        return NONE

    def set(
        self,
        section: str,
        option: str,
        value: str,
    ) -> None:
        """"""

        if not value:
            return

        if not self.configuration.has_section(section):
            if section != CELESTINE:
                self.configuration.add_section(section)

        self.configuration[section][option] = value
