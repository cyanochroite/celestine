""""""

from celestine.typed import (
    F,
    G,
    L,
    N,
    Z,
)
from celestine.window.cardinal import Triad

type Pixel = Triad[F] | Triad[Z]
type Pixels = L[Pixel]
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
                if total % 4 == 0 or total % 9 == 4 or chroma == 0:
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
    result = scale.ceil()
    return result


def _table(function) -> Pixels:
    """"""
    result = []
    pixels = _pixels()
    for pixel in pixels:
        triad = function(pixel)
        data = triad.data
        result.append(data)

    return result


curses_table = _table(_curses)
pillow_table = _table(_pillow)
