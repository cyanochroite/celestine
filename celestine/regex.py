""""""

import re

from celestine.typed import (
    B,
    S,
)


def replace(pattern: S, repl: S, string: S) -> S:
    """"""
    count = 0
    flags = 0
    result: S = re.sub(pattern, repl, string, count, flags)
    return result


def contains(pattern: S, string: S) -> B:
    """"""
    match = re.search(pattern, string, flags=0)
    result = bool(match)
    return result
