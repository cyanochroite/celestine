""""""

import collections.abc

from celestine.literal import (
    FULL_STOP,
    KEY,
    NONE,
)
from celestine.typed import (
    IT,
    A,
    B,
    D,
    F,
    K,
    N,
    Object,
    S,
    T,
    V,
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


class Area(Object):
    """"""

    local: Plane
    world: Plane

    def __contains__(self, item: Point) -> B:
        result = item in self.world
        return result

    @classmethod
    def fast(cls, width: Z, height: Z) -> K:
        """"""
        local = Plane.create(width, height)
        world = Plane.create(width, height)
        result = cls(local, world)
        return result

    def __init__(self, local: Plane, world: Plane) -> N:
        self.local = local.copy()
        self.world = world.copy()
        super().__init__(self.local, self.world)

    def __repr__(self):
        result = f"Area({self.local}, {self.world})"
        return result

    def __str__(self):
        result = f"({self.local}, {self.world})"
        return result


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

    def key(self, key: S) -> S:
        """Expands short keys to full keys."""
        result = NONE
        add = NONE
        one, two = key.split(KEY)
        names = one.split(FULL_STOP)
        for name in names:
            result = add + two
            if result in self.dictionary:
                break
            add += name + FULL_STOP
        return result

    @classmethod
    def make(cls, dictionary: V[D[S, X]] = None) -> K:
        """"""
        return cls(dictionary)

    def __delitem__(self, key: S) -> N:
        index = self.key(key)
        del self.dictionary[index]

    def __getitem__(self, key: S) -> X:
        index = self.key(key)
        result = self.dictionary[index]
        return result

    def __init__(self, dictionary: V[D[S, X]] = None) -> N:
        self.dictionary = dictionary or {}

    def __iter__(self) -> IT[S]:
        return iter(self.dictionary)

    def __len__(self) -> Z:
        return len(self.dictionary)

    def __setitem__(self, key: S, value: X) -> N:
        index = self.key(key)
        self.dictionary[index] = value

    def __or__(self, other: K) -> K:
        result = self.make(self.dictionary)
        result.dictionary.update(other.dictionary)
        return result

    def __ror__(self, other: K) -> K:
        result = self.make(other.dictionary)
        result.dictionary.update(self.dictionary)
        return result

    def __ior__(self, other: K) -> K:
        self.dictionary.update(other.dictionary)
        return self


ignore(Area, Dictionary)
