""""""

from celestine.typed import (
    TZ3,
    C,
    F,
    G,
    L,
    N,
    Z,
)
from celestine.window.cardinal import (
    Round,
    Triad,
)

type Pixel = Triad[F] | Triad[Z]
type Pixels = L[TZ3]
type Make = G[Pixel, N, N]


def _pixels() -> Make:
    """"""
    for red in range(9):
        for green in range(9):
            for blue in range(9):
                pixel = Triad(red, green, blue)
                maximum = max(pixel)
                minimum = min(pixel)
                chroma = maximum - minimum
                total = red + green + blue
                if total % 4 == 0 or total % 15 == 0 or chroma == 0:
                    result = pixel / 8
                    yield result


def _curses(pixel: Pixel) -> Pixel:
    """"""
    scale = pixel * 1000
    result = scale.round()
    return result


def _pillow(pixel: Pixel) -> Pixel:
    """"""
    scale = pixel * 255
    result = scale.inplace(Round.positive)
    return result


def _table(function: C[[Pixel], Pixel]) -> Pixels:
    """"""
    result: Pixels = []
    pixels = _pixels()
    for pixel in pixels:
        triad = function(pixel)
        data = triad.data
        result.append(data)

    return result


curses_table = _table(_curses)
pillow_table = _table(_pillow)
COLOR_PAIRS = len(curses_table)
