"""Run a bunch of auto formaters."""

import math

from celestine.data import call
from celestine.typed import (
    B,
    F,
    R,
)


@call
def sizes(**star: R) -> B:
    """"""

    def fix(numer: F) -> F:
        return abs(round(numer) - numer)

    limit = 3500
    lowest = 4.0
    for index in range(7, limit):
        major = index * math.sqrt(2)
        minor = major / (1 + math.sqrt(2))

        one = [
            major / math.sqrt(1),
            major / math.sqrt(2),
            major / math.sqrt(3),
            major / math.sqrt(4),
            minor / math.sqrt(1),
            minor / math.sqrt(2),
            minor / math.sqrt(4),
            minor / math.sqrt(8),
        ]
        error = sum(map(fix, one))
        one = list(map(round, one))

        two: list[F] = []
        two.append(one[3] * math.pi)
        two.append(two[0] - one[7])
        two.append(one[1] + one[5] + two[1] + one[4] + two[1] + one[5])
        two.append(round(two[2]) * 2)
        two = list(map(round, two))

        if error < lowest:
            lowest = error
            number = [*one, *two]
            number.sort()
            print(error, index, number)

    return True


def printer():
    """"""
    yield '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
    yield '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"'
    yield '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">'
    yield "<svg"
    yield '    width="100%"'
    yield '    height="100%"'
    yield '    viewBox="0 0 4356 4356"'
    yield '    version="1.1"'
    yield '    xmlns="http://www.w3.org/2000/svg"'
    yield '    xmlns:xlink="http://www.w3.org/1999/xlink"'
    yield '    xml:space="preserve"'
    yield '    xmlns:serif="http://www.serif.com/"'
    yield '    style="background-color:#B2FFFF;"'
    yield ">    "


@call
def licence(**star: R) -> B:
    """"""
    for line in printer():
        print(line)
    return True
