""""""

import configparser
import os
import pathlib

from celestine import (
    load,
    stream,
)
from celestine.literal import (
    CELESTINE,
    EQUALS_SIGN,
    NONE,
    NUMBER_SIGN,
)
from celestine.package import platformdirs
from celestine.typed import (
    VP,
    N,
    P,
    S,
)

FILE = "celestine.ini"


class Configuration:
    """Parse configuration stuff."""

    configuration: configparser.ConfigParser
    path: P
    save_it_file: stream.Text

    def get(self, section: S, option: S) -> S:
        """"""
        return self.configuration.get(section, option, fallback=NONE)

    def load(self, path: VP = None) -> N:
        """Load the configuration file."""
        filenames = path or self.path
        encoding = stream.Encoding.UTF_8.value
        self.configuration.read(filenames, encoding)

    def save(self) -> N:
        """Save the configuration file."""
        configuration = self.configuration
        path = os.path.join(self.path, FILE)
        with self.save_it_file.writer(path) as fileobject:
            space_around_delimiters = True
            configuration.write(fileobject, space_around_delimiters)

    def set(self, section: S, option: S, value: S) -> N:
        """"""
        if not self.configuration.has_section(section):
            self.configuration.add_section(section)

        self.configuration[section][option] = value

    def __init__(self) -> N:
        """"""
        if bool(platformdirs):
            user_data_dir = platformdirs.user_data_dir(
                appname="celestine",
                appauthor=False,
                version=None,
                roaming=False,
                ensure_exists=True,
            )
            self.path = pathlib.Path(user_data_dir)
        else:
            self.path = load.pathway_root()

        self.save_it_file = stream.Text(self.path)
        self.configuration = configparser.ConfigParser(
            defaults=None,
            dict_type=dict,
            allow_no_value=False,
            delimiters=EQUALS_SIGN,
            comment_prefixes=NUMBER_SIGN,
            inline_comment_prefixes=None,
            strict=True,
            empty_lines_in_values=False,
            default_section=CELESTINE,
            interpolation=configparser.BasicInterpolation(),
            converters={},
        )
