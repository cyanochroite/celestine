""""""

import abc

import math

from celestine import load
from celestine.typed import (
    TA,
    R,
    T,
    Z,
)
from celestine.window.collection import Box

BOX: TA = T[Z, Z, Z, Z]
PAIR: TA = T[Z, Z]


class Abstract(Box):
    """"""

    def poke(self, x_dot, y_dot):
        """"""
        return self.inside(x_dot, y_dot)

    def spot(self, x_min, y_min, x_max, y_max):
        """"""
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def __init__(self, tag, **star):
        self.item = None
        self.tag = tag
        super().__init__(**star)


class Button(Abstract):
    """"""

    def poke(self, x_dot, y_dot):
        """"""
        if super().poke(x_dot, y_dot):
            self.call(self.action, **self.argument)

    def __init__(self, tag, text, *, call, action, argument, **star):
        self.action = action
        self.argument = argument
        self.call = call
        self.data = text
        super().__init__(tag, **star)


class Unit:
    """"""

    @property
    def data(self):
        """"""
        return self._value

    @data.setter
    def data(self, value):
        if value < self._minimum:
            self._value = self._minimum

        if value > self._maximum:
            self._value = self._maximum

        self._value = value

    @data.deleter
    def data(self):
        del self._value

    def __init__(self, minimum, maximum):
        minimum = math.floor(minimum)
        maximum = math.ceil(maximum - 1)
        self._minimum = min(minimum, maximum)
        self._maximum = max(minimum, maximum)
        self._value = 0
        self.data = 0


class Picture(Abstract, abc.ABC):
    """
    A small version of an image.

    Terminal:
    minimum = 2**5 = 32
    maximum = 2**7 = 128

    Regular:
    minimum = 2**05 = 64
    maximum = 2**13 = 8192

    Minimum:
    Fairly good detail preservation at 64 pixels.

    Maximum
    Biggest TV is 8k and "biggest" monitors are less then 8K.
    """

    @abc.abstractmethod
    def resize(self, size):
        """"""

    def path(self):
        """"""
        return self.image or load.pathway.asset("null.png")

    def size(self):
        x_size = self.x_max - self.x_min
        y_size = self.y_max - self.y_min
        print(x_size, y_size, "MOO")
        return (x_size, y_size)

    def update(self, ring: R, image, **star):
        """"""
        if not image:
            return False

        self.image = image
        return True

    def __init__(self, tag, image, **star):
        self.cache = None
        self.image = image
        super().__init__(tag, **star)

        minimum = 2**6
        maximum = 2**16

        minimum = 2**5
        maximum = 2**8
        self.unit_x = Unit(minimum, maximum)
        self.unit_y = Unit(minimum, maximum)


class Image(Picture):
    """
    A small version of an image.

    Terminal:
    minimum = 2**5 = 32
    maximum = 2**7 = 128

    Regular:
    minimum = 2**05 = 64
    maximum = 2**13 = 8192

    Minimum:
    Fairly good detail preservation at 64 pixels.

    Maximum
    Biggest TV is 8k and "biggest" monitors are less then 8K.
    """

    def resize(self, size):
        x_size = self.x_max - self.x_min
        y_size = self.y_max - self.y_min

        return (math.floor(x_size), math.floor(y_size))

    def crop(self, source_length: PAIR, target_length: PAIR) -> BOX:
        """"""

        (source_length_x, source_length_y) = source_length
        (target_length_x, target_length_y) = target_length

        source_ratio = source_length_x / source_length_y
        target_ratio = target_length_x / target_length_y

        if source_ratio < target_ratio:
            length = round(source_length_x / target_ratio)
            offset = round((source_length_y - length) / 2)
            return (0, 0 + offset, source_length_x, length + offset)

        if source_ratio > target_ratio:
            length = round(source_length_y * target_ratio)
            offset = round((source_length_x - length) / 2)
            return (0 + offset, 0, length + offset, source_length_y)

        return (0, 0, source_length_x, source_length_y)


class Photo(Picture):
    """
    A small version of an image.

    Terminal:
    minimum = 2**4 = 16
    maximum = 2**6 = 64

    Regular:
    minimum = 2**5 = 32
    maximum = 2**8 = 256

    Minimum:
    Smallest thumbnail seems to be 40.
    Resolution of 16 too small for regular images.

    Maximum
    Largest thumbnail seems to be 250.
    Keeping it within a byte (256) a nice goal.
    """

    def resize(self, size):
        """"""
        x_length, y_length = size

        x_size = self.x_max - self.x_min
        y_size = self.y_max - self.y_min

        new_x = y_size * x_length / y_length
        new_y = x_size * y_length / x_length

        if new_y > y_size:
            done_x = new_x
            done_y = y_size
        else:
            done_x = x_size
            done_y = new_y

        return (math.floor(done_x), math.floor(done_y))


class Label(Abstract):
    """"""

    def __init__(self, tag, text, **star):
        self.data = text
        super().__init__(tag, **star)
