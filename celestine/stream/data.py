"""Central place for loading and importing external files."""

import enum


class Buffering(enum.IntEnum):
    """"""

    OFF = 0
    ON = 1


class Encoding(enum.StrEnum):
    """"""

    ASCII = "ascii"
    ISO_8859_1 = "iso_8859_1"
    LATIN_1 = "latin_1"
    US_ASCII = "us_ascii"
    UTF_8 = "utf_8"
    UTF_16 = "utf_16"
    UTF_32 = "utf_32"


class Errors(enum.StrEnum):
    """"""

    BACKSLASHREPLACE = "backslashreplace"
    IGNORE = "ignore"
    NAMEREPLACE = "namereplace"
    REPLACE = "replace"
    STRICT = "strict"
    SURROGATEESCAPE = "surrogateescape"
    XMLCHARREFREPLACE = "xmlcharrefreplace"


class Mode(enum.StrEnum):
    """"""

    APPEND_BINARY = "ab"
    APPEND_TEXT = "at"
    EXCLUSIVE_BINARY = "xb"
    EXCLUSIVE_TEXT = "xt"
    READ_BINARY = "rb"
    READ_TEXT = "rt"
    TRUNCATE_BINARY = "w+b"
    TRUNCATE_TEXT = "w+t"
    UPDATE_BINARY = "r+b"
    UPDATE_TEXT = "r+t"
    WRITE_BINARY = "wb"
    WRITE_TEXT = "wt"


class Newline(enum.StrEnum):
    """"""

    APPLE = "\n"
    COMMODORE = "\r"
    MICROSOFT = "\r\n"
    UNTRANSLATED = ""
