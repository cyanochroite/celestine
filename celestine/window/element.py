""""""

import math

from celestine.typed import (
    BOX,
    PAIR,
    A,
    H,
    I,
    N,
    P,
    R,
    S,
    T,
)
from celestine.window.collection import (
    Item,
    Plane,
)


class Abstract(Item):
    """"""

    item: A  # The object that the window system interacts with.

    # TODO combine abstract and container into item clas

    def spot(self, area: Plane) -> N:
        """"""
        self.area = area.copy()

    def __init__(self, hold: H, canvas: A, name: S, **star: R) -> N:
        super().__init__(hold, canvas, name, **star)
        self.item = None


class Button(Abstract):
    """"""

    def click_action(self) -> N:
        """"""
        self.hold.queue(self.call, self.action, self.argument)

    def __init__(
        self,
        hold: H,
        canvas,
        name,
        text,
        *,
        call,
        action,
        argument,
        **star: R,
    ):
        self.action = action
        self.argument = argument
        self.call = call
        self.data = text
        super().__init__(hold, canvas, name, **star)


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


class Picture:
    def scale_to_any(self, frame: Plane, crop=False):
        """"""
        (size_x, size_y) = self.size
        (area_x, area_y) = area

        down_x = math.floor(area_y * size_x / size_y)
        down_y = math.floor(area_x * size_y / size_x)

        if crop:
            best_x = max(area_x, down_x)
            best_y = max(area_y, down_y)
        else:
            best_x = min(area_x, down_x)
            best_y = min(area_y, down_y)

        return (best_x, best_y)

    def __init__(self):
        self.area = Area(axis_x, axis_y)


class Image(Abstract):
    """"""

    path: P  # The location of the image on disk.
    image: A  # The image object after being loaded from disk.
    size: T[I, I]  # The width and height of the image.

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

    def update(self, path: P, **star: R) -> N:
        """"""
        self.path = path

    def resize(self, size):
        """"""
        (size_x, size_y) = size
        (area_x, area_y) = self.area.size

        down_x = math.floor(area_y * size_x / size_y)
        down_y = math.floor(area_x * size_y / size_x)

        best_x = min(area_x, down_x)
        best_y = min(area_y, down_y)

        return (best_x, best_y)

    def scale_to_fit(self, area):
        """"""
        (size_x, size_y) = self.size
        (area_x, area_y) = area

        down_x = math.floor(area_y * size_x / size_y)
        down_y = math.floor(area_x * size_y / size_x)

        best_x = min(area_x, down_x)
        best_y = min(area_y, down_y)

        return (best_x, best_y)

    def __init__(self, hold: H, canvas, name, path, **star: R):
        self.path = path
        self.image = None

        super().__init__(hold, canvas, name, **star)

        minimum = 2**6
        maximum = 2**16

        minimum = 2**5
        maximum = 2**8
        self.unit_x = Unit(minimum, maximum)
        self.unit_y = Unit(minimum, maximum)

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

    def resize_(self, size):
        # TODO this is old
        x_size, y_size = self.size
        return (math.floor(x_size), math.floor(y_size))

    def crop(_self, source_length: PAIR, target_length: PAIR) -> BOX:
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


class Label(Abstract):
    """"""

    def __init__(self, hold: H, canvas, name, text, **star: R):
        self.data = text
        super().__init__(hold, canvas, name, **star)
