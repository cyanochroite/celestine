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

    one: F
    two: F

    @property
    def value(self) -> T[Z, ...]:
        """"""
        result = self.unary(int)
        return result


class Line(Dyad):
    """"""

    one: F
    two: F

    @property
    def length(self) -> Z:
        """"""
        result = int(self.two - self.one)
        return result

    @property
    def midpoint(self) -> Z:
        """"""
        result = int(self.one + self.two) // 2
        return result

    def __contains__(self, item: F) -> B:
        result = self.one <= item <= self.two
        return result

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
        one = self.one.midpoint
        two = self.two.midpoint
        return Point(one, two)

    @property
    def value(self) -> T[Z, Z, Z, Z]:
        """"""
        xmin = int(self.one.one)
        ymin = int(self.two.one)
        xmax = int(self.one.two)
        ymax = int(self.two.two)
        return (xmin, ymin, xmax, ymax)

    @classmethod
    def create(cls, width: Z, height: Z) -> K:
        """"""
        one = Line(0, width)
        two = Line(0, height)
        return cls(one, two)

    @property
    def origin(self) -> Point:
        """"""
        return Point(self.one.one, self.two.one)

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

    def __contains__(self, item: K) -> B:
        one = item.one in self.one
        two = item.two in self.two
        return one and two


class Area:
    """"""

    local: Plane
    world: Plane

    def __contains__(self, item: Point) -> B:
        return item in self.world

    @classmethod
    def make(cls, width: Z, height: Z) -> K:
        """"""
        local = Plane.create(width, height)
        world = Plane.create(width, height)
        return cls(local, world)

    def __init__(self, local: Plane, world: Plane) -> N:
        self.local = local.copy()
        self.world = world.copy()

    def __repr__(self):
        return f"Area({self.local}, {self.world})"

    def __str__(self):
        return f"({self.local}, {self.world})"
