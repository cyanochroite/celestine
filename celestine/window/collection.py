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


class Area(Object):
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

    def set(self, axis_x: Axis, axis_y: Axis) -> N:
        """"""
        self.axis_x.set(axis_x.minimum, axis_x.maximum)
        self.axis_y.set(axis_y.minimum, axis_y.maximum)

    @property
    def size(self) -> T[Z, Z]:
        """"""
        return (self.axis_x.size, self.axis_y.size)

    def __init__(self, axis_x: Axis, axis_y: Axis, **star) -> N:
        """"""
        super().__init__(**star)
        self.axis_x = Axis(axis_x.minimum, axis_x.maximum)
        self.axis_y = Axis(axis_y.minimum, axis_y.maximum)


class Item(Object):
    """"""

    name: S

    def __init__(self, name: S, area: Area, **star) -> N:
        super().__init__(**star)
        self.area = area
        self.name = name


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
