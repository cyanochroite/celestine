""""""

import configparser

from celestine import stream
from celestine.literal import CELESTINE

# from celestine.package import platformdirs
from celestine.typed import (
    OP,
    N,
    S,
)
from celestine.unicode import (
    EQUALS_SIGN,
    NONE,
    POUND_SIGN,
)


class Configuration:
    """Parse configuration stuff."""

    def get(self, section: S, option: S) -> S:
        """"""
        return self.configuration.get(section, option, fallback=NONE)

    def load(self, path: OP = None) -> N:
        """Load the configuration file."""
        filenames = path or self.path
        encoding = stream.Encoding.UTF_8.value
        self.configuration.read(filenames, encoding)

    def save(self) -> N:
        """Save the configuration file."""
        configuration = self.configuration
        with stream.text.writer(self.path) as fileobject:
            space_around_delimiters = True
            configuration.write(fileobject, space_around_delimiters)

    def set(self, section: S, option: S, value: S) -> N:
        """"""
        if not self.configuration.has_section(section):
            self.configuration.add_section(section)

        self.configuration[section][option] = value

    def __init__(self) -> N:
        """"""
        self.path = "."
        # if platformdirs:
        #    self.path = os.path.join(platformdirs.directory, FILE)

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
