""""""

from typing import TypeAlias as TA

from celestine.typed import (
    A,
    B,
    D,
    G,
    I,
    K,
    N,
    R,
    S,
    T,
)

N: TA = None


class Object:
    """"""

    @classmethod
    def clone(cls, self: K) -> K:
        """"""
        return cls()

    def copy(self) -> K:
        """"""
        return self.clone(self)

    def __init__(self, **star) -> N:
        """This does not pass the star parameter to the real object."""
        super().__init__()


# TODO install windows-curses for python 3.12


from celestine.typed import (
    GF,
    B,
    F,
    K,
    N,
    S,
    override,
)


class Point:
    """"""

    one: F
    two: F

    @classmethod
    def clone(cls, self: K) -> K:
        """"""
        return cls(self.one, self.two)

    def copy(self) -> K:
        """"""
        return self.clone(self)

    def quantize(self) -> K:
        self.one = round(self.one)
        self.two = round(self.two)
        return self

    def __init__(self, one: F, two: F) -> N:
        self.one = float(one)
        self.two = float(two)

    def __iter__(self) -> GF:
        yield self.one
        yield self.two

    def __repr__(self) -> S:
        return f"Point({self.one}, {self.two})"

    def __str__(self) -> S:
        return f"({self.one}, {self.two})"

    def __sub__(self, other: K) -> K:
        one = self.one - other.one
        two = self.two - other.two
        return type(self)(one, two)

    def __truediv__(self, other: K) -> K:
        one = self.one / other.one
        two = self.two / other.two
        return type(self)(one, two)


class Line:
    """"""

    minimum: F
    maximum: F

    @classmethod
    def clone(cls, self: K) -> K:
        """"""
        return cls(self.minimum, self.maximum)

    def copy(self) -> K:
        """"""
        return self.clone(self)

    @property
    def length(self) -> F:
        return self.maximum - self.minimum

    @property
    def midpoint(self) -> F:
        return (self.minimum + self.maximum) / 2

    def quantize(self) -> K:
        self.minimum = round(self.minimum)
        self.maximum = round(self.maximum)
        return self

    def __add__(self, other: F) -> K:
        one = self.minimum + other
        two = self.maximum + other
        return type(self)(one, two)

    def __contains__(self, item: F) -> B:
        return self.minimum <= item <= self.maximum

    def __iadd__(self, other: F) -> K:
        self.minimum += other
        self.maximum += other
        return self

    def __imul__(self, other: F) -> K:
        self.minimum *= other
        self.maximum *= other
        return self

    def __init__(self, minimum: F, maximum: F) -> N:
        self.minimum = float(min(minimum, maximum))
        self.maximum = float(max(minimum, maximum))

    def __mul__(self, other: F) -> K:
        one = self.minimum * other
        two = self.maximum * other
        return type(self)(one, two)

    def __repr__(self) -> S:
        return f"Line({self.minimum}, {self.maximum})"

    def __str__(self) -> S:
        return f"[{self.minimum}, {self.maximum}]"


class Plane:
    """"""

    one: Line
    two: Line

    def center(self, other: K) -> N:
        self += other.centroid - self.centroid

    @property
    def centroid(self) -> Point:
        one = self.one.midpoint
        two = self.two.midpoint
        return Point(one, two)

    @classmethod
    def clone(cls, self: K) -> K:
        """"""
        one = self.one.copy()
        two = self.two.copy()
        return cls(one, two)

    def copy(self) -> K:
        """"""
        return self.clone(self)

    @classmethod
    def make(cls, width: F, height: F) -> K:
        """"""
        one = Line(0, width)
        two = Line(0, height)
        return cls(one, two)

    def scale_to_max(self, other: K) -> K:
        self *= max(other.size / self.size)
        return self

    def scale_to_min(self, other: K) -> K:
        self *= min(other.size / self.size)
        return self

    def quantize(self) -> K:
        self.one.quantize()
        self.two.quantize()
        return self

    @property
    def size(self) -> Point:
        return Point(self.one.length, self.two.length)

    def __add__(self, other: Point) -> K:
        one = self.one + other.one
        two = self.two + other.two
        return type(self)(one, two)

    def __contains__(self, item: Point) -> B:
        one = item.one in self.one
        two = item.two in self.two
        return one and two

    def __iadd__(self, other: Point) -> K:
        self.one += other.one
        self.two += other.two
        return self

    def __imul__(self, other: F) -> K:
        self.one *= other
        self.two *= other
        return self

    def __init__(self, one: Line, two: Line) -> N:
        self.one = one.copy()
        self.two = two.copy()

    def __mul__(self, other: F) -> K:
        one = self.one * other
        two = self.two * other
        return type(self)(one, two)

    def __repr__(self) -> S:
        one = repr(self.one)
        two = repr(self.two)
        return f"Plane({one}, {two})"

    def __str__(self) -> S:
        one = str(self.one)
        two = str(self.two)
        return f"({one}, {two})"


class Grid(Plane):
    """"""

    @property
    @override
    def centroid(self) -> Point:
        return super().centroid.quantize()

    @override
    def scale_to_max(self, other: K) -> K:
        return super().scale_to_max(other).quantize()

    @override
    def scale_to_min(self, other: K) -> K:
        return super().scale_to_min(other).quantize()

    @override
    def __init__(self, one: Line, two: Line) -> N:
        return super().__init__(one.quantize(), two.quantize())


class Rectangle:
    """"""

    left: I
    upper: I
    right: I
    lower: I

    def copy(self, other: K) -> N:
        """Copy the values from another object."""
        self.left = other.left
        self.upper = other.upper
        self.right = other.right
        self.lower = other.lower

    def within(self, dot_x: I, dot_y: I) -> B:
        """Test that click inside us."""
        test_x = self.left <= dot_x <= self.right
        test_y = self.upper <= dot_y <= self.lower
        return test_x and test_y

    @property
    def origin(self) -> T[I, I]:
        """"""
        return (self.left, self.upper)

    @property
    def size(self) -> T[I, I]:
        """"""
        return (self.right - self.left, self.lower - self.upper)

    @property
    def value(self) -> T[I, I, I, I]:
        """"""
        return (self.left, self.upper, self.right, self.lower)

    def __init__(self, left: I, upper: I, right: I, lower: I) -> N:
        """"""
        self.left = left
        self.upper = upper
        self.right = right
        self.lower = lower


class Item(Object):
    """"""

    area: Rectangle
    canvas: A
    hidden: B
    ring: R
    name: S  # The key to use to find this in the window dictionary.

    def draw(self, **star) -> N:
        """"""
        if self.hidden:
            return

    def make(self) -> N:
        """"""

    def poke(self, x_dot: I, y_dot: I, **star) -> B:
        """"""
        if self.hidden:
            return False

        return self.area.within(x_dot, y_dot)

    def spot(self, area: Rectangle) -> N:
        """"""
        raise NotImplementedError(area)

    def __init__(
        self, ring: R, canvas: A, name: S, area: Rectangle, **star
    ) -> N:
        super().__init__(**star)
        self.area = Rectangle(*area.value)
        self.canvas = canvas
        self.hidden = False
        self.ring = ring
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

    def __iter__(self) -> G[T[S, Item], N, N]:
        """"""
        yield from self.item.items()
