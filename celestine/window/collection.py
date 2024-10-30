""""""

import collections.abc

from celestine.typed import (
    IT,
    A,
    B,
    D,
    F,
    K,
    N,
    Object,
    T,
    V,
    S,
    Z,
    ignore,
)
from celestine.window.cardinal import Dyad
from celestine.literal import FULL_STOP, NONE


class Point(Dyad):
    """"""

    one: F
    two: F

    @property
    def value(self) -> T[Z, Z]:
        """"""
        one = int(self.one)
        two = int(self.two)
        result = (one, two)
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
        one = self.one
        two = self.two
        return Point(one.length, two.length)

    def __contains__(self, item: K) -> B:
        one = item.one in self.one
        two = item.two in self.two
        return one and two


class Area(Object):
    """"""

    local: Plane
    world: Plane

    def __contains__(self, item: Point) -> B:
        return item in self.world

    @classmethod
    def fast(cls, width: Z, height: Z) -> K:
        """"""
        local = Plane.create(width, height)
        world = Plane.create(width, height)
        return cls(local, world)

    def __init__(self, local: Plane, world: Plane) -> N:
        self.local = local.copy()
        self.world = world.copy()
        super().__init__(self.local, self.world)

    def __repr__(self):
        return f"Area({self.local}, {self.world})"

    def __str__(self):
        return f"({self.local}, {self.world})"


class Dictionary[X](collections.abc.MutableMapping[S, A]):
    """"""

    dictionary: D[S, X]

    def copy(self) -> K:
        """"""
        return self.echo(self)

    @classmethod
    def echo(cls, self: K) -> K:
        """"""
        return cls(self.dictionary)

    @classmethod
    def make(cls, dictionary: V[D[S, X]] = None) -> K:
        """"""
        return cls(dictionary)

    def __delitem__(self, key: S) -> N:
        del self.dictionary[key]

    def __getitem__(self, key: S) -> X:
        a, b = key.split("::")

        if not a:
            result = self.dictionary[b]
        else:
            c = a.split(FULL_STOP)
            add = NONE
            for e in c:
                add += e
                cow = f"{add}{FULL_STOP}{b}"
                if cow in self.dictionary:
                    result = self.dictionary[cow]
                    break
                add += FULL_STOP
        return result

    def __init__(self, dictionary: V[D[S, X]] = None) -> N:
        self.dictionary = dictionary or {}

    def __iter__(self) -> IT[S]:
        return iter(self.dictionary)

    def __len__(self) -> Z:
        return len(self.dictionary)

    def __setitem__(self, key: S, value: X) -> N:
        self.dictionary[key] = value

    def __or__(self, other: K) -> K:
        if not isinstance(other, Dictionary):
            return NotImplemented

        result = self.make(self.dictionary)
        result.dictionary.update(other.dictionary)
        return result

    def __ror__(self, other: K) -> K:
        if not isinstance(other, Dictionary):
            return NotImplemented

        result = self.make(self.dictionary)
        result.dictionary.update(self.dictionary)
        return result

    def __ior__(self, other: K) -> K:
        self.dictionary.update(other.dictionary)
        return self
