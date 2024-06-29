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
)

BRAILLE_PATTERNS = 0x2800


class Session(SuperSession):
    """"""


def encode(binary: int) -> str:
    """"""
    number = binary + BRAILLE_PATTERNS
    string = chr(number)
    return string


def decode(string: str) -> int:
    """"""
    number = ord(string)
    binary = number - BRAILLE_PATTERNS
    return binary


def encoder(binary: bytes) -> str:
    """"""
    return NONE.join(map(encode, binary))


def decoder(string: str) -> bytes:
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
    root = pathlib.Path("D:/test2/")
    binary = Binary(root)
    path = pathlib.Path(root, "test0.jpg")
    with binary.reader(path) as file:
        digest = hashlib.file_digest(file, hashlib.sha3_512)
        print(digest.hexdigest())

    stem = encoder(digest.digest())
    suffix = path.suffix.lower()
    name = f"{stem}{suffix}"
    target = path.with_name(name)
    path.rename(target)

    return True


NOTE = """
tar.lzma
WITNESS_CAMPAIGN
VBOX - EXTPACK
PSPPALETTE
PROPERTIES
MSSTYLES
TORRENT
NUMBERS
GEOJSON
MODULES
GRAPHML
blend
config
0123456789abcdef
2021 - 06 - 30T15: 20: 14Z_SHA3_512_⠩⢻⠷⠽⢔⠑⡵⢓⣖⢶⠉⣁⠫⢧⠖⢟⠠⣄⢕⠅⡤⡂⠣⢦⠜⢬⢇⠈.blend
2021 - 06 - 30T15: 20: 14Z_SHA3⠩⢻⠷⠽⢔⠑⡵⢓⣖⢶⠉⣁⠫⢧⠖⢟⠠⣄⢕⠅⡤⡂⠣⢦⠜⢬⢇⠈.html5123
20210630⠩⢻⠷⠽⢔⠑⡵⢓⣖⢶⠉⣁⠫⢧⠖⢟⠠⣄⢕⠅⡤⡂⠣⢦⠜⢬⢇⠈.html
1985 - 04 - 12T23: 20: 30Z

19850412T232030Z
SHA3⠩⢻⠷⠽⢔⠑⡵⢓⣖⢶⠉⣁⠫⢧⠖⢟⠠⣄⢕⠅⡤⡂⠣⢦⠜⢬⢇⠈
PROPERTIES

19850412T232030Z⠩⢻⠷⠽⢔⠑⡵⢓⣖⢶⠉⣁⠫⢧⠖⢟⠠⣄⢕⠅⡤⡂⠣⢦⠜⢬⢇⠈.WITNESS_CAMPAIGNsha3
19850412T232030Z⠩⢻⠷⠽⢔⠑⡵⢓⣖⢶⠉⣁⠫⢧⠖⢟⠠⣄⢕⠅⡤⡂⠣⢦⠜⢬⢇⠈.PROPERTIESsha3hhhh
19850412T232030Z_SHA3_512⠩⢻⠷⠽⢔⠑⡵⢓⣖⢶⠉⣁⠫⢧⠖⢟⠠⣄⢕⠅⡤⡂⠣⢦⠜⢬⢇⠈.PROPERTIES

m2_19850412T232030Z_SHA3⠩⢻⠷⠽⢔⠑⡵⢓⣖⢶⠉⣁⠫⢧⠖⢟⠠⣄⢕⠅⡤⡂⠣⢦⠜⢬⢇⠈.PROPERTIES
19850412T232030Z⠩⢻⠷⠽⢔⠑⡵⢓⣖⢶⠉⣁⠫⢧⠖⢟⠠⣄⢕⠅⡤⡂⠣⢦⠜⢬⢇⠈SHA3.PROPERTIES

a.o + 19850412T232030Z + SHA3⠩⢻⠷⠽⢔⠑⡵⢓⣖⢶⠉⣁⠫⢧⠖⢟⠠⣄⢕⠅⡤⡂⠣⢦⠜⢬⢇⠈.PROPERTIES

# 1985-04-12T23-20-30Z_SHA3⠩⢻⠷⠽⢔⠑⡵⢓⣖⢶⠉⣁⠫⢧⠖⢟⠠⣄⢕⠅⡤⡂⠣⢦⠜⢬⢇⠈.PROPERTIES
8888 - 88-80_SHA3⠩⢻⠷⠽⢔⠑⡵⢓⣖⢶⠉⣁⠫⢧⠖⢟⠠⣄⢕⠅⡤⡂⠣⢦⠜⢬⢇⠈.jpg
19850412T232030Z
SHA3⠩⢻⠷⠽⢔⠑⡵⢓⣖⢶⠉⣁⠫⢧⠖⢟⠠⣄⢕⠅⡤⡂⠣⢦⠜⢬⢇⠈
.PROPERTIES

# 16 for time and date
# 32 for hash
# 10 for extension
444444444444444444444444444444444444444444
"""


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
