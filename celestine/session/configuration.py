""""""

import configparser
import os

from celestine import load
from celestine.data import CELESTINE
from celestine.data.directory import APPLICATION
from celestine.file import text_save
from celestine.file.data import UTF_8
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

    def get(self, section: S, option: S) -> S:
        """"""
        if self.has_section(section, option):
            if self.configuration.has_option(section, option):
                return self.configuration[section][option]

        return NONE

    def has_section(self, section: S, option: S) -> B:
        """Also checks if using default section name."""
        has_section = self.configuration.has_section(section)

        if option == APPLICATION:
            section = APPLICATION

        if section == APPLICATION:
            has_section = True

        return has_section

    def load(self) -> N:
        """Load the configuration file."""
        filenames = self.path
        encoding = UTF_8
        self.configuration.read(filenames, encoding)

    def save(self) -> N:
        """Save the configuration file."""
        configuration = self.configuration
        with text_save(self.path) as fileobject:
            space_around_delimiters = True
            configuration.write(fileobject, space_around_delimiters)

    def set(self, section: S, option: S, value: S) -> N:
        """"""
        if not self.has_section(section, option):
            self.configuration.add_section(section)

        self.configuration[section][option] = value

    def __init__(self) -> N:
        """"""
        module = load.module("package", "platformdirs")
        path = os.path.join(module.directory, FILE)
        self.path = path

        defaults = None  # Default.
        dict_type = dict  # Default.
        allow_no_value = False  # Default.
        delimiters = EQUALS_SIGN
        comment_prefixes = POUND_SIGN
        inline_comment_prefixes = None  # Default.
        strict = True  # Important.
        empty_lines_in_values = False
        default_section = CELESTINE
        interpolation = configparser.BasicInterpolation()  # Default.
        converters = {}  # Default.
        self.configuration = configparser.ConfigParser(
            defaults,
            dict_type,
            allow_no_value,
            delimiters=delimiters,
            comment_prefixes=comment_prefixes,
            inline_comment_prefixes=inline_comment_prefixes,
            strict=strict,
            empty_lines_in_values=empty_lines_in_values,
            default_section=default_section,
            interpolation=interpolation,
            converters=converters,
        )
