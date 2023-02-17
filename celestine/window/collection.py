""""""

from celestine.typed import GE
from celestine.typed import N
from celestine.typed import T
from celestine.typed import Z


class Object:
    """"""

    def __init__(self, **star):
        super().__init__()


class Axis(Object):
    """"""

    def get(self, partition: Z) -> GE[T[Z, Z], N, N]:
        """"""
        if partition <= 0:
            raise ValueError("need: partition > 0")

        distance = self.maximum - self.minimum
        step = int(distance // partition)

        maximum = self.minimum  # <- yes, setting maximum to minimum

        while True:
            minimum = maximum
            maximum += step
            yield (minimum, maximum)

    def get(self, partition: Z) -> GE[T[Z, Z], N, N]:
        """"""
        if partition <= 0:
            raise ValueError("need: partition > 0")

        distance = self.maximum - self.minimum
        step = int(distance // partition)

        maximum = self.minimum  # <- yes, setting maximum to minimum

        while maximum < self.maximum:
            minimum = maximum
            maximum += step
            yield (minimum, maximum)

        while True:
            yield (minimum, maximum)

    def set(self, minimum: Z, maximum: Z) -> N:
        """"""
        if minimum < 0:
            raise ValueError("need: minimum >= 0")
        if maximum < 0:
            raise ValueError("need: maximum >= 0")
        if minimum > maximum:
            raise ValueError("need: minimum <= maximum")

        self.minimum = minimum
        self.maximum = maximum

    def __init__(self, **star):
        self.minimum = 0
        self.maximum = 0
        super().__init__(**star)


class Box(Object):
    """"""

    def partition(self, length):
        partition = length or 1
        segment = size / partition
        return segment

    def center_float(self):
        """"""
        x_dot = (self.x_min + self.x_max) / 2
        y_dot = (self.y_min + self.y_max) / 2
        return (x_dot, y_dot)

    def inside(self, x_dot, y_dot):
        """"""
        x_test = self.x_min <= x_dot < self.x_max
        y_test = self.y_min <= y_dot < self.y_max
        x = F"{self.x_min}<={x_dot}<{self.x_max}={x_test}"
        y = F"{self.y_min}<={y_dot}<{self.y_max}={y_test}"
        print(F"{x} & {y}")

        return x_test and y_test

    def __init__(self, x_min=0, y_min=0, x_max=0, y_max=0, **star):
        self.axis_x = Axis()
        self.axis_y = Axis()
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        super().__init__(**star)


class Collection(Object):
    """"""

    def children(self):
        """"""
        for _, thing in self.item.items():
            yield thing

    def item_get(self, tag):
        """"""
        return self.item[tag]

    def item_set(self, tag, value):
        """"""
        self.item[tag] = value
        return value

    def __init__(self, **star):
        self.item = {}
        super().__init__(**star)


class Rectangle(Box, Collection):
    """"""

    def get(self):
        """"""
        x_min = self.move_x_min
        self.move_x_min += self.offset_x

        y_min = self.move_y_min
        self.move_y_min += self.offset_y

        x_max = self.move_x_min if self.offset_x else self.x_max
        y_max = self.move_y_min if self.offset_y else self.y_max

        return (x_min, y_min, x_max, y_max)

    def get(self):
        """"""
        x_min = self.axis_x.minimum

        x_min = self.move_x_min
        self.move_x_min += self.offset_x

        y_min = self.move_y_min
        self.move_y_min += self.offset_y

        x_max = self.move_x_min if self.offset_x else self.x_max
        y_max = self.move_y_min if self.offset_y else self.y_max

        return (x_min, y_min, x_max, y_max)

    def set(self, x_min, y_min, x_max, y_max):
        """"""
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def get_next(self):
        """"""
        x_min = self.move_x_min
        self.move_x_min += self.offset_x

        y_min = self.move_y_min
        self.move_y_min += self.offset_y

        x_max = self.move_x_min if self.offset_x else self.x_max
        y_max = self.move_y_min if self.offset_y else self.y_max

        return (x_min, y_min, x_max, y_max)

    def spawn(self):
        """"""
        (x_min, y_min, x_max, y_max) = self.get_next()
        return Rectangle(
            x_min=x_min,
            y_min=y_min,
            x_max=x_max,
            y_max=y_max,
            offset_x=self.offset_x,
            offset_y=self.offset_y,
        )

    def __init__(self, offset_x=0, offset_y=0, **star):
        super().__init__(**star)
        if "row" in star:
            offset_x = 300
        if "col" in star:
            offset_y = 50

        self.start_x_min = self.x_min
        self.start_y_min = self.y_min
        self.start_x_max = self.x_max
        self.start_y_max = self.y_max

        self.move_x_min = self.x_min
        self.move_y_min = self.y_min
        self.move_x_max = self.x_max
        self.move_y_max = self.y_max

        self.offset_x = offset_x
        self.offset_y = offset_y
