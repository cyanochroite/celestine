""""""

import math

import celestine
from celestine import language
from celestine.interface import View
from celestine.session.session import SuperSession
from celestine.typed import (
    GS,
    LF,
    B,
    F,
    N,
    R,
    S,
    ignore,
)
from celestine.window.decorator import (
    call,
    draw,
)


class Session(SuperSession):
    """"""


def calculate(index: F) -> LF:
    """"""
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
    two: list[F] = []
    two.append(one[3] * math.pi)
    two.append(two[0] - one[7])
    two.append(one[1] + one[5] + two[1] + one[4] + two[1] + one[5])
    two.append(round(two[2]) * 2)
    two = list(map(round, two))
    number = [*one, *two]
    number.sort()
    return number


@call
def licence(**star: R) -> B:
    """"""
    ignore(star)
    for line in printer():
        print(line)
    return True


@draw
def main(view: View) -> N:
    """"""
    with view.span("main_head") as line:
        line.label("main_title", text="Logo generation functions.")
    with view.span("main_body") as line:
        line.button(
            "main_L",
            "sizes",
            text=language.CLEAN_MAIN_VERSION,
        )
        line.button(
            "main_R",
            "licence",
            text=language.CLEAN_MAIN_LICENCE,
        )


def more1(index: F, color: S) -> GS:
    """"""
    axis = calculate(index)
    yield f'<path fill="{color}" d="'
    yield "M 2178 2178"
    yield f"m +{axis[7]} +000"
    yield f"l +{axis[8]} +{axis[8]}"
    yield f"a +{axis[2]} +{axis[2]} 0 0 0 +{axis[3]} 0"
    yield f"l +{axis[8]} -{axis[8]}"
    yield f"l -{axis[8]} -{axis[8]}"
    yield f"a +{axis[2]} +{axis[2]} 0 0 0 -{axis[3]} 0"
    yield f"l -{axis[8]} +{axis[8]}"
    yield 'Z"'
    yield "/>"
    yield f'<path fill="{color}" d="'
    yield "M 2178 2178"
    yield f"m +000 -{axis[7]}"
    yield f"l +{axis[8]} -{axis[8]}"
    yield f"a +{axis[2]} +{axis[2]} 0 0 0 0 -{axis[3]}"
    yield f"l -{axis[8]} -{axis[8]}"
    yield f"l -{axis[8]} +{axis[8]}"
    yield f"a +{axis[2]} +{axis[2]} 0 0 0 0 +{axis[3]}"
    yield f"l +{axis[8]} +{axis[8]}"
    yield 'Z"'
    yield "/>"
    yield f'<path fill="{color}" d="'
    yield "M 2178 2178"
    yield f"m -{axis[7]} -000"
    yield f"l -{axis[8]} -{axis[8]}"
    yield f"a +{axis[2]} +{axis[2]} 0 0 0 -{axis[3]} 0"
    yield f"l -{axis[8]} +{axis[8]}"
    yield f"l +{axis[8]} +{axis[8]}"
    yield f"a +{axis[2]} +{axis[2]} 0 0 0 +{axis[3]} 0"
    yield f"l +{axis[8]} -{axis[8]}"
    yield 'Z"'
    yield "/>"
    yield f'<path fill="{color}" d="'
    yield "M 2178 2178"
    yield f"m -000 +{axis[7]}"
    yield f"l -{axis[8]} +{axis[8]}"
    yield f"a +{axis[2]} +{axis[2]} 0 0 0 0 +{axis[3]}"
    yield f"l +{axis[8]} +{axis[8]}"
    yield f"l +{axis[8]} -{axis[8]}"
    yield f"a +{axis[2]} +{axis[2]} 0 0 0 0 -{axis[3]}"
    yield f"l -{axis[8]} -{axis[8]}"
    yield 'Z"'
    yield "/>"


def more2(index: F, color: S) -> GS:
    """"""
    axis = calculate(index)
    yield f'<path fill="{color}" d="'
    yield "M 2178 2178"
    yield f"m +{axis[6]} +000"
    yield f"l +{axis[9]} -{axis[9]}"
    yield f"a +{axis[4]} +{axis[4]} 0 0 1 +{axis[6]} -000"
    yield f"a +{axis[5]} +{axis[5]} 0 0 0 -{axis[6]} -{axis[6]}"
    yield f"a +{axis[5]} +{axis[5]} 0 0 0 -{axis[6]} -{axis[6]}"
    yield f"a +{axis[4]} +{axis[4]} 0 0 1 -000 +{axis[6]}"
    yield f"l -{axis[9]} +{axis[9]}"
    yield f"l -{axis[9]} -{axis[9]}"
    yield f"a +{axis[4]} +{axis[4]} 0 0 1 -000 -{axis[6]}"
    yield f"a +{axis[5]} +{axis[5]} 0 0 0 -{axis[6]} +{axis[6]}"
    yield f"a +{axis[5]} +{axis[5]} 0 0 0 -{axis[6]} +{axis[6]}"
    yield f"a +{axis[4]} +{axis[4]} 0 0 1 +{axis[6]} +000"
    yield f"l +{axis[9]} +{axis[9]}"
    yield f"l -{axis[9]} +{axis[9]}"
    yield f"a +{axis[4]} +{axis[4]} 0 0 1 -{axis[6]} +000"
    yield f"a +{axis[5]} +{axis[5]} 0 0 0 +{axis[6]} +{axis[6]}"
    yield f"a +{axis[5]} +{axis[5]} 0 0 0 +{axis[6]} +{axis[6]}"
    yield f"a +{axis[4]} +{axis[4]} 0 0 1 +000 -{axis[6]}"
    yield f"l +{axis[9]} -{axis[9]}"
    yield f"l +{axis[9]} +{axis[9]}"
    yield f"a +{axis[4]} +{axis[4]} 0 0 1 +000 +{axis[6]}"
    yield f"a +{axis[5]} +{axis[5]} 0 0 0 +{axis[6]} -{axis[6]}"
    yield f"a +{axis[5]} +{axis[5]} 0 0 0 +{axis[6]} -{axis[6]}"
    yield f"a +{axis[4]} +{axis[4]} 0 0 1 -{axis[6]} -000"
    yield f"l -{axis[9]} -{axis[9]}"
    yield 'Z"'
    yield "/>"


def printer() -> GS:
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
    yield ">"
    yield from more1(338, "#191970")
    yield from more2(338, "#191970")
    yield from more1(123, "#448822")
    yield from more2(123, "#448822")
    yield "</svg>"


@call
def sizes(**star: R) -> B:
    """"""
    ignore(star)

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


ignore(Session, licence, main, sizes)

celestine.main(__package__)
