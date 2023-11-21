"""Central place for loading and importing external files."""


import lzma

import celestine.file.lzma as _lzma
import celestine.file.text as _text
from celestine import load
from celestine.typed import (
    GS,
    N,
    S,
)

text = _text.Text()
binary = _text.Binary()
lzma = _lzma.Funny()


def module_open(*path: S) -> GS:
    """"""
    file = load.pathway.python(*path)
    with text_load(file) as document:
        yield from document


def module_save(string: S, *path: S) -> N:
    """"""
    file = load.pathway.python(*path)
    with text_save(file) as document:
        for line in string:
            document.write(line)
