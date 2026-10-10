"""Keywords used throughout the application."""

import enum

FILE = "celestine.ini"


class Actions(enum.StrEnum):
    """"""

    STORE = "store"
    STORE_CONST = "store_const"
    STORE_TRUE = "store_true"
    APPEND = "append"
    APPEND_CONST = "append_const"
    COUNT = "count"
    HELP = "help"
    VERSION = "version"


class Attributes(enum.StrEnum):
    """"""

    ACTION = "action"
    CHOICES = "choices"
    HELP = "help"
    NARGS = "nargs"


class Parsers(enum.StrEnum):
    """"""

    ERROR = "error"


class Values(enum.StrEnum):
    """"""

    CONFIGURATION = "configuration"
    MAIN = "main"


# other
SESSION = "session"
INIT = "__init__"
