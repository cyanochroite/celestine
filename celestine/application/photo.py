""""""

import typing
import pathlib
import os

import io
import importlib
import os
import sys
import pathlib
import hashlib

from celestine import (
    bank,
    language,
)
from celestine.data import (
    call,
    draw,
)
from celestine.interface import View
from celestine.session.session import SuperSession
from celestine.typed import (
    B,
    N,
    R,
    S,
    Z,
)
from celestine.stream import Binary

BRAILLE_PATTERNS = 0x2800


class Session(SuperSession):
    """"""


def encode(binary: Z) -> S:
    """"""
    number = binary + BRAILLE_PATTERNS
    string = chr(number)
    return string


def decode(string: S) -> Z:
    """"""
    number = ord(string)
    binary = number - BRAILLE_PATTERNS
    return binary


def encode2(data):
    items = data
    for item in items:
        print(item)


@ call
def list_files(**star: R) -> B:
    """"""
    path = pathlib.Path("D:/test")
    files = os.listdir(path)
    for file in files:
        print(file)

    return True


@ call
def braille_patterns(**star: R) -> B:
    """"""
    for index in range(256):
        print(index, chr(index + BRAILLE_PATTERNS))
    return True


@ call
def run(**star: R) -> B:
    """"""
    root = pathlib.Path("D:/test/")
    binary = Binary(root)
    path = pathlib.Path(root, "test0.jpg")
    with binary.reader(path) as file:
        for line in file:
            encode2(line)
    return True


@ draw
def main(view: View) -> N:
    """"""
    with view.span("main_head") as line:
        line.label(
            "main_title",
            text=language.CLEAN_MAIN_TITLE,
        )
        line.button(
            "main_action",
            "list_files",
            text=language.CLEAN_MAIN_CLEAN,
        )
    with view.span("main_body") as line:
        line.button(
            "main_L",
            "braille_patterns",
            text="Braille Patterns",
        )
        line.button(
            "main_R",
            "run",
            text=language.CLEAN_MAIN_LICENCE,
        )
