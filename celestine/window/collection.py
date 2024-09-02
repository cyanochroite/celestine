""""""

from celestine.typed import (
    B,
    F,
    K,
    N,
    T,
    Z,
    ignore,
)
from celestine.window.cardinal import Dyad


class Point(Dyad):
    """"""

    @property
    def value(self) -> T[Z, Z]:
        """"""
        return (int(self.one), int(self.two))


class Line(Dyad):
    """"""

    @property
    def minimum(self) -> F:
        """"""
        return self.element[0]

    @property
    def maximum(self) -> F:
        """"""
        return self.element[1]

    @property
    def length(self) -> Z:
        """"""
        return int(self.maximum - self.minimum)

    @property
    def midpoint(self) -> Z:
        """"""
        return int(self.minimum + self.maximum) // 2

    def __contains__(self, item: F) -> B:
        return self.minimum <= item <= self.maximum

    def __init__(self, one: F, two: F) -> N:
        ignore(self)
        minimum = min(one, two)
        maximum = max(one, two)
        super().__init__(minimum, maximum)


class Plane(Dyad):
    """"""

    one: Line
    two: Line

    def center(self, other: K) -> N:
        """"""
        self += other.centroid - self.centroid

    @property
    def centroid(self) -> Point:
        """"""
        _one = self.one.midpoint
        _two = self.two.midpoint
        return Point(_one, _two)

    @property
    def value(self) -> T[Z, Z, Z, Z]:
        """"""
        xmin = int(self.one.minimum)
        ymin = int(self.two.minimum)
        xmax = int(self.one.maximum)
        ymax = int(self.two.maximum)
        return (xmin, ymin, xmax, ymax)

    @classmethod
    def make(cls, width: Z, height: Z) -> K:
        """"""
        _one = Line(0, width)
        _two = Line(0, height)
        return cls(_one, _two)

    @property
    def origin(self) -> Point:
        """"""
        return Point(self.one.minimum, self.two.minimum)

    def scale_to_max(self, other: K) -> N:
        """"""
        self *= max(other.size / self.size)

    def scale_to_min(self, other: K) -> N:
        """"""
        self *= min(other.size / self.size)

    @property
    def size(self) -> Point:
        """"""
        return Point(self.one.length, self.two.length)

    def __contains__(self, item: Point) -> B:
        _one = item.one in self.one
        _two = item.two in self.two
        return _one and _two


class Area:
    """"""

    local: Plane
    world: Plane

    def __contains__(self, item: Point) -> B:
        return item in self.world

    @classmethod
    def make(cls, width: Z, height: Z) -> K:
        """"""
        local = Plane.make(width, height)
        world = Plane.make(width, height)
        return cls(local, world)

    def __init__(self, local: Plane, world: Plane) -> N:
        self.local = local.copy()
        self.world = world.copy()

    def __repr__(self):
        return f"Area({self.local}, {self.world})"

    def __str__(self):
        return f"({self.local}, {self.world})"
