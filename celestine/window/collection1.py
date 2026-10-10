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


class Point(Dyad[F]):
    """"""

    @property
    def value(self) -> T[Z, Z]:
        """"""
        one = int(self.one)
        two = int(self.two)
        result = (one, two)
        return result


class Line(Dyad[F]):
    """"""

    @property
    def length(self) -> Z:
        """"""
        result = int(self.two - self.one)
        return result

    @property
    def midpoint(self) -> F:
        """"""
        result = (self.one + self.two) / 2
        return result

    def __contains__(self, item: F) -> B:
        result = self.one <= float(item) <= self.two
        return result

    def __init__(self, one: F, two: F) -> N:
        ignore(self)
        minimum = min(one, two)
        maximum = max(one, two)
        super().__init__(minimum, maximum)


class Plane(Dyad[Line]):
    """"""

    def center(self, other: K) -> N:
        """"""
        result = other.centroid - self.centroid
        self += result

    @property
    def centroid(self) -> Point:
        """"""
        one = self.one.midpoint
        two = self.two.midpoint
        result = Point(one, two)
        return result

    @property
    def value(self) -> T[Z, Z, Z, Z]:
        """"""
        xmin = int(self.one.one)
        ymin = int(self.two.one)
        xmax = int(self.one.two)
        ymax = int(self.two.two)
        result = (xmin, ymin, xmax, ymax)
        return result

    @classmethod
    def create(cls, width: Z, height: Z) -> K:
        """"""
        one = Line(0, width)
        two = Line(0, height)
        result = cls(one, two)
        return result

    @property
    def origin(self) -> Point:
        """"""
        result = Point(self.one.one, self.two.one)
        return result

    def scale_to_max(self, other: K) -> N:
        """"""
        result = max(other.size / self.size)
        self *= result

    def scale_to_min(self, other: K) -> N:
        """"""
        result = min(other.size / self.size)
        self *= result

    @property
    def size(self) -> Point:
        """"""
        one = self.one
        two = self.two
        result = Point(one.length, two.length)
        return result

    def __contains__(self, item: Point) -> B:
        one = item.one in self.one
        two = item.two in self.two
        result = one and two
        return result


ignore(Plane)
