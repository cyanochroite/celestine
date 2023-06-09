""""""
from celestine.package.blender import data

from . import quadrilateral


def text(collection, name, words):
    """"""
    font_curve = data.curve.font.make(collection, name, words)
    return font_curve


def _offset(numerator, denominator):
    """"""
    ratio = numerator / denominator
    unit = 1
    maximum = max(ratio, unit)
    normalization = maximum - unit
    half = 1 / 2
    halving = normalization * half
    return halving
    #  return (max(numerator / denominator, 1) - 1) / 2


def image(collection, image):
    """"""
    size = image.size
    x = size[0]
    y = size[1]
    y_to_x = _offset(y, x)
    x_to_y = _offset(x, y)
    (x, y) = (y_to_x, x_to_y)

    return quadrilateral.plane(collection, image.name, x, y)
