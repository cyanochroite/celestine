""""""

import re

from celestine.typed import S


def replace(pattern: S, repl: S, string: S) -> S:
    """"""
    count = 0
    flags = 0
    result: S = re.sub(pattern, repl, string, count, flags)
    return result


def match(pattern: S, string: S) -> S:
    """"""
    _match = re.match(pattern, string)
    if not _match:
        raise ValueError(_match)
    result = _match[1]
    return result
