""""""

from celestine.typed import (
    GE,
    TA,
    B,
    D,
    N,
    S,
    T,
    Z,
)

AXIS: TA = GE[T[Z, Z], N, N]


class Object:
    """"""

    def __init__(self, **star) -> N:
        """Make sure object does not get the star parameter."""
        super().__init__()


class Item(Object):
    """"""

    name: S

    def __init__(self, name: S, **star) -> N:
        super().__init__()
        self.name = name


class Axis(Object):
    """"""

    minimum: Z
    maximum: Z

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

    def inside(self, midterm: Z) -> B:
        """"""
        return self.minimum <= midterm < self.maximum

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

    @property
    def size(self) -> Z:
        """"""
        return self.maximum - self.minimum

    def __init__(self, minimum: Z, maximum: Z, **star) -> N:
        super().__init__(**star)
        self.minimum = minimum
        self.maximum = maximum


class Box(Object):
    """"""

    axis_x: Axis
    axis_y: Axis

    def get(self, partition_x: Z, partition_y: Z) -> T[AXIS, AXIS]:
        """"""
        axis_x = self.axis_x.get(partition_x)
        axis_y = self.axis_y.get(partition_y)
        return (axis_x, axis_y)

    def inside(self, x_dot: Z, y_dot: Z) -> B:
        """"""
        return self.axis_x.inside(x_dot) and self.axis_y.inside(y_dot)

    def set(self, x_min: Z, y_min: Z, x_max: Z, y_max: Z) -> N:
        """"""
        self.axis_x.set(x_min, x_max)
        self.axis_y.set(y_min, y_max)

    @property
    def size(self) -> T[Z, Z]:
        """"""
        return (self.axis_x.size, self.axis_y.size)

    def __init__(
        self,
        x_min: Z = 0,
        y_min: Z = 0,
        x_max: Z = 0,
        y_max: Z = 0,
        **star,
    ) -> N:
        super().__init__(**star)
        self.axis_x = Axis(x_min, x_max)
        self.axis_y = Axis(y_min, y_max)


class Collection(Object):
    """"""

    item: D[S, Item]

    def item_get(self, name: S) -> Item:
        """"""
        return self.item[name]

    def item_set(self, name: S, item: Item) -> Item:
        """"""
        self.item[name] = item
        return item

    def load(self, name: S) -> Item:
        """"""
        return self.item[name]

    def save(self, item: Item) -> N:
        """"""
        self.item[item.name] = item

    def __init__(self, **star) -> N:
        self.item = {}
        super().__init__(**star)

    def __iter__(self) -> GE[T[S, Item], N, N]:
        """"""
        yield from self.item.items()


class Collection2:
    """"""

    item: D[S, Item]

    def children(self) -> GE[Item, N, N]:
        """"""
        for _, item in self.item.items():
            yield item

    def get(self, name: S) -> Item:
        """"""
        return self.item[name]

    def set(self, name: S, item: Item) -> Item:
        """"""
        self.item[name] = item
        return item

    def __init__(self) -> N:
        self.item = {}


class Rectangle(Box, Collection):
    """"""

    begin_x_min: Z
    begin_y_min: Z
    begin_x_max: Z
    begin_y_max: Z

    move_x_min: Z
    move_y_min: Z
    move_x_max: Z
    move_y_max: Z

    offset_x: Z
    offset_y: Z

    def get_next(self) -> T[Z, Z, Z, Z]:
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

    def __init__(self, offset_x: Z = 0, offset_y: Z = 0, **star) -> N:
        super().__init__(**star)
        if "row" in star:
            offset_x = 300
        if "col" in star:
            offset_y = 50

        self.begin_x_min = self.axis_x.minimum
        self.begin_y_min = self.axis_y.minimum
        self.begin_x_max = self.axis_x.maximum
        self.begin_y_max = self.axis_y.maximum

        self.move_x_min = self.axis_x.minimum
        self.move_y_min = self.axis_y.minimum
        self.move_x_max = self.axis_x.maximum
        self.move_y_max = self.axis_y.maximum

        self.offset_x = offset_x
        self.offset_y = offset_y
