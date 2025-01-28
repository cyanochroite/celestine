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
    for red in range(7):
        for green in range(7):
            for blue in range(7):
                pixel = Triad(red, green, blue)
                maximum = max(pixel)
                minimum = min(pixel)
                chroma = maximum - minimum
                if 1 <= chroma <= 2:
                    continue
                result = pixel / 6
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
