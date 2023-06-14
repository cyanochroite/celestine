"""Python Game Development."""

import os
import sys

from celestine.file.data import (
    UTF_8,
    WRITE_TEXT,
)
from celestine.typed import A

PYGAME = None


from . import Abstract


class Package(Abstract):
    """"""

    draw: A
    display: A
    image: A
    display: A
    font: A
    event: A
    quit: A
    QUIT: A
    mouse: A
    MOUSEBUTTONDOWN: A
    transform: A


def hide():
    sys_stdout = sys.stdout
    sys.stdout = open(os.devnull, WRITE_TEXT, encoding=UTF_8)

    PYGAME = __import__("pygame")

    sys.stdout.close()
    sys.stdout = sys_stdout

    return PYGAME
