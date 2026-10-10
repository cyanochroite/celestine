""""""

import hashlib
import os
import pathlib

import celestine
from celestine import language
from celestine.interface import View
from celestine.literal import join
from celestine.session.session import SuperSession
from celestine.stream import Binary
from celestine.typed import (
    B,
    N,
    R,
    S,
    Y,
    Z,
    ignore,
)
from celestine.window.decorator import (
    call,
    view,
)

BRAILLE_PATTERNS = 0x2800


class Session(SuperSession):
    """"""


def encode(binary: Z) -> S:
    """"""
    number = binary + BRAILLE_PATTERNS
    result = chr(number)
    return result


def decode(symbol: S) -> Z:
    """"""
    number = ord(symbol)
    result = number - BRAILLE_PATTERNS
    return result


def encoder(binary: Y) -> S:
    """"""
    symbol = map(encode, binary)
    iterable = list(symbol)
    result = join(*iterable)
    return result


def decoder(symbol: S) -> Y:
    """"""
    binary = map(decode, symbol)
    result = bytes(binary)
    return result


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

19850412T232030Z-0003573783B-SHA256
-6a86959c003d734261984fa6446df02ea7177a63de5b9ee36cd0c67d00d0bc17
19850412T232030Z-0003573783B
-6a86959c003d734261984fa6446df02ea7177a63de5b9ee36cd0c67d00d0bc17
19850412T232030Z-54

# 16 for time and date
# 32 for hash
# 10 for extension
444444444444444444444444444444444444444444
"""


@view
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


celestine.main(__package__)

ignore(Session, main, decoder, list_files, braille_patterns, run, NOTE)
