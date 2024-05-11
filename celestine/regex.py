""""""

import re

from celestine.typed import S


def replace(pattern: S, repl: S, string: S) -> S:
    """"""
    count = 0
    flags = 0
    result: S = re.sub(pattern, repl, string, count, flags)
    return result
