""""""

import re

from celestine.typed import (
    B,
    S,
)
from celestine.literal import NONE


def replace(pattern: S, repl: S, string: S) -> S:
    """"""
    count = 0
    flags = 0
    result: S = re.sub(pattern, repl, string, count, flags)
    return result


def first(pattern: S, string: S) -> S:
    """"""
    match = re.search(pattern, string, flags=0)
    if match:
        try:
            return match[1]
        except IndexError:
            pass
    return NONE
