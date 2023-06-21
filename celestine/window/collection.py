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


class Axis:
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

    def __init__(self, minimum: Z, maximum: Z) -> N:
        self.minimum = minimum
        self.maximum = maximum


class Rectangle:
    """"""

    left: Z
    upper: Z
    right: Z
    lower: Z

    def copy(self, other):
        self.left = other.left
        self.upper = other.upper
        self.right = other.right
        self.lower = other.lower

    def within(self, dox_x: Z, dot_y: Z) -> B:
        test_x = self.left <= dox_x < self.right
        test_y = self.upper <= dot_y < self.lower
        return test_x and test_y

    @property
    def origin(self) -> T[Z, Z]:
        return (self.left, self.upper)

    @property
    def size(self) -> T[Z, Z]:
        """"""
        return (self.right - self.left, self.lower - self.upper)

    @property
    def value(self) -> T[Z, Z, Z, Z]:
        """"""
        return (self.left, self.upper, self.right, self.lower)

    def __init__(self, left: Z, upper: Z, right: Z, lower: Z) -> N:
        """"""
        self.left = left
        self.upper = upper
        self.right = right
        self.lower = lower


class Item(Object):
    """"""

    area: Rectangle
    name: S  # The key to use to find this in the window dictionary.

    def draw(self, ring, view, **star):
        """"""
        raise NotImplementedError(area)

    def poke(self, x_dot: Z, y_dot: Z, **star) -> B:
        """"""
        return self.area.within(x_dot, y_dot)

    def spot(self, area: Rectangle):
        """"""
        raise NotImplementedError(area)

    def __init__(self, name: S, area: Rectangle, **star) -> N:
        super().__init__(**star)
        self.area = Rectangle(*area.value)
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

    def __iter__(self) -> GE[S, N, N]:
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
