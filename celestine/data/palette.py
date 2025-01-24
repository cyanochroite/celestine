""""""

import math

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


def _greys(greys: Z) -> Make:
    """"""
    for grey in range(greys):
        pixel = Triad(grey, grey, grey)
        yield pixel


def _colours(colours: Z) -> Make:
    """"""
    cutoff = math.floor(colours / 2 - 1)
    for red in range(colours):
        for green in range(colours):
            for blue in range(colours):
                pixel = Triad(red, green, blue)
                maximum = max(pixel)
                minimum = min(pixel)
                chroma = maximum - minimum
                if chroma > cutoff:
                    yield pixel


def _pixels(function, limit: Z) -> Make:
    """"""
    pixels = function(limit)
    for pixel in pixels:
        result = pixel / (limit - 1)
        yield result


def _all() -> Make:
    """"""
    yield from _pixels(_greys, 16)
    yield from _pixels(_colours, 7)


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
    pixels = _all()
    for pixel in pixels:
        triad = function(pixel)
        data = triad.data
        result.append(data)

    return result


curses_table = _table(_curses)
pillow_table = _table(_pillow)
