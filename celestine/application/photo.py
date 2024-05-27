""""""

import hashlib
import os
import pathlib

from celestine import language
from celestine.data import (
    call,
    draw,
)
from celestine.interface import View
from celestine.literal import NONE
from celestine.session.session import SuperSession
from celestine.stream import Binary
from celestine.typed import (
    B,
    N,
    R,
    S,
    Z,
)

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


def encoder(binary: bytes) -> S:
    """"""
    return NONE.join(map(encode, binary))


def decoder(string: S) -> bytes:
    """"""
    return bytes(map(decode, string))


@call
def list_files(**star: R) -> B:
    """"""
    path = pathlib.Path("D:/test")
    files = os.listdir(path)
    for file in files:
        print(file)

    return True


@call
def braille_patterns(**star: R) -> B:
    """"""
    for index in range(256):
        print(index, chr(index + BRAILLE_PATTERNS))
    return True


@call
def run(**star: R) -> B:
    """"""
    root = pathlib.Path("D:/test/")
    binary = Binary(root)
    path = pathlib.Path(root, "test0.jpg")
    with binary.reader(path) as file:
        digest = hashlib.file_digest(file, hashlib.sha384)
        cat = encoder(digest.digest())
        print(cat)

    return True


@draw
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
