""""""

from celestine.typed import (
    GE,
    TA,
    N,
    T,
    Z,
)

AXIS: TA = GE[T[Z, Z], N, N]


class Object:
    """"""

    def __init__(self, **star):
        super().__init__()


class Axis(Object):
    """"""

    def get(self, partition: Z) -> AXIS:
        """"""
        if partition <= 0:
            raise ValueError("need: partition > 0")

        distance = self.maximum - self.minimum
        fragment = int(distance // partition)
        position = self.minimum

        indexer = 0
        while True:
            minimum = indexer * fragment + position
            indexer += 1
            maximum = indexer * fragment + position
            indexer %= partition
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

    def get(self, partition_x: Z, partition_y: Z) -> T[AXIS, AXIS]:
        """"""
        axis_x = self.axis_x.get(partition_x)
        axis_y = self.axis_y.get(partition_y)
        return (axis_x, axis_y)

    def set(self, x_min: Z, y_min: Z, x_max: Z, y_max: Z) -> N:
        """"""
        self.axis_x.set(x_min, x_max)
        self.axis_y.set(y_min, y_max)

    def inside(self, x_dot, y_dot):
        """"""
        x_test = self.x_min <= x_dot < self.x_max
        y_test = self.y_min <= y_dot < self.y_max
        x = f"{self.x_min}<={x_dot}<{self.x_max}={x_test}"
        y = f"{self.y_min}<={y_dot}<{self.y_max}={y_test}"
        # print(F"{x} & {y}")

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
        for _, item in self.item.items():
            yield item

    def item_get(self, tag):
        """"""
        return self.item[tag]

    def item_set(self, tag, value):
        """"""
        self.item[tag] = value
        return value

    def load(self, tag):
        """"""
        return self.item[tag]

    def save(self, item):
        """"""
        tag = item.tag
        self.item[tag] = item
        return item

    def __init__(self, **star):
        self.item = {}
        super().__init__(**star)


class Rectangle(Box, Collection):
    """"""

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
