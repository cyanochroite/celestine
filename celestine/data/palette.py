""""""

import math

import PIL
import PIL.Image

from celestine.typed import (
    TF3,
    G,
    Z,
)
from celestine.window.cardinal import Triad

type PIXELS = L[TF3]
type Make = G[Triad, N, N]
type PIXEL = Triad[F, F, F]


def add_greys(greys: Z) -> Make:
    """"""
    for grey in range(greys):
        pixel = Triad(grey, grey, grey)
        yield pixel


def add_colours(colours: Z) -> Make:
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


def add_pixels(function, limit: Z) -> Make:
    """"""
    pixels = function(limit)
    for pixel in pixels:
        result = pixel / (limit - 1)
        yield result


def add_all() -> Make:
    """"""
    yield from add_pixels(add_greys, 16)
    yield from add_pixels(add_colours, 7)


def _curses(pixel: PIXEL) -> PIXEL:
    """"""
    scale = pixel * 1000
    result = scale.round()
    return result


def _pillow(pixel: PIXEL) -> PIXEL:
    """"""
    scale = pixel * 255
    result = scale.ceil()
    return result


def _table(function) -> PIXELS:
    """"""
    result = []
    pixels = add_all()
    for pixel in pixels:
        triad = function(pixel)
        data = triad.data
        result.append(data)

    return result


curses_table = _table(_curses)
pillow_table = _table(_pillow)


crayola = list(set(pillow_table))
length = len(crayola) - 1
image = PIL.Image.new("RGB", (1024, 1024))
for y in range(1024):
    for x in range(1024):
        xx = x // 4
        yy = min(xx, length)
        colour = crayola[yy]
        image.putpixel((x, y), colour)

image.show()
