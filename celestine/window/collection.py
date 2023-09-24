""""""

from celestine.typed import (
    GE,
    SELF,
    TA,
    A,
    B,
    D,
    N,
    R,
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

class Point:
    """Screen cordinates."""

    point_x: Z
    point_y: Z

    def __init__(self, point_x: Z, point_y: Z) -> N:
        self.point_x = abs(point_x)
        self.point_y = abs(point_y)

class Rectangle:
    """"""

    left: Z
    upper: Z
    right: Z
    lower: Z

    def copy(self, other: SELF) -> N:
        """Copy the values from another object."""
        self.left = other.left
        self.upper = other.upper
        self.right = other.right
        self.lower = other.lower

    def within(self, x: Z, y: Z) -> B:
        """Test that click inside us."""
        test_x = self.left <= dox_x <= self.right
        test_y = self.upper <= dot_y <= self.lower
        return test_x and test_y

    @property
    def origin(self) -> T[Z, Z]:
        """"""
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
    canvas: A
    name: S  # The key to use to find this in the window dictionary.
    hidden: B

    def draw(self, ring, **star) -> N:
        """"""
        if self.hidden:
            return

    def make(self, ring, **star) -> N:
        """"""

    def poke(self, ring: R, x_dot: Z, y_dot: Z, **star) -> N:
        """"""
        if self.hidden:
            return False

        return self.area.within(x_dot, y_dot)

    def spot(self, area: Rectangle) -> N:
        """"""
        raise NotImplementedError(area)

    def __init__(
        self, canvas: A, name: S, area: Rectangle, **star
    ) -> N:
        super().__init__(**star)
        self.area = Rectangle(*area.value)
        self.canvas = canvas
        self.name = name
        self.hidden = False


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
