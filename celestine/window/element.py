""""""


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


class Image(Abstract):
    """"""

    def size(self):
        x_size = self.x_max - self.x_min
        y_size = self.y_max - self.y_min
        print(x_size, y_size, "MOO")
        return (x_size, y_size)

    def resize(self, x_length, y_length):
        x_size = self.x_max - self.x_min
        y_size = self.y_max - self.y_min

        x_over_y = x_length / y_length
        y_over_x = y_length / x_length

        if x_over_y > y_over_x:
            y_size = min(y_size, x_size / x_over_y)
        else:
            x_size = min(x_size, y_size / y_over_x)

        return (round(x_size), round(y_size))

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


class Label(Abstract):
    """"""

    def __init__(self, tag, text, **star):
        self.data = text
        super().__init__(tag, **star)
