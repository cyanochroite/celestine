""""""

import collections.abc
import math
import re

from celestine.literal import (
    NONE,
    VERTICAL_LINE,
)
from celestine.typed import (
    IT,
    TS,
    A,
    B,
    D,
    G,
    K,
    N,
    S,
    T,
    V,
    Z,
    ignore,
)
from celestine.window.cardinal import (
    Dyad,
    Monad,
)


class Digit(Monad[Z]):
    """"""

    def negative(self) -> N:
        """"""
        self.one = -abs(self.one)

    def positive(self) -> N:
        """"""
        self.one = +abs(self.one)

    def __init__(self, one: Z) -> N:
        ignore(self)
        super().__init__(one)


class Point(Dyad[Digit]):
    """"""

    __slots__: TS = ()

    @classmethod
    def create(cls, width: Z, height: Z) -> K:
        """"""
        one = Digit(width)
        two = Digit(height)
        result = cls(one, two)
        return result

    def __init__(self, one: Digit, two: Digit) -> N:
        ignore(self)
        super().__init__(one, two)


class Line(Dyad[Digit]):
    """"""

    __slots__: TS = ()

    @classmethod
    def create(cls, width: Z, height: Z) -> K:
        """"""
        one = Digit(width)
        two = Digit(height)
        result = cls(one, two)
        return result

    @property
    def length(self) -> Digit:
        """"""
        result = self.two - self.one
        result.positive()
        result += 1
        return result

    @property
    def midpoint(self) -> Digit:
        """
        Center point biased to the right.

        (-4, -4) = (-5, -2) = -7 = -3.5 = -4 <<
        (+0, +0) = (-1, +2) = +1 = +0.5 = +0 <<
        (+4, +4) = (+3, +6) = +9 = +4.5 = +4 <<

        (-5, -4) = (-6, -2) = -8 = -4.0 = -4 <<
        (+0, +0) = (-1, +2) = +1 = +0.5 = +0 <<
        (+3, +4) = (+2, +6) = +8 = +4.0 = +4 <<
        """
        one = self.one - 1
        two = self.two + 2
        tri = one + two
        number = tri / 2
        result = math.floor(number)
        return result

    def __contains__(self, item: Digit) -> B:
        result = self.one <= item <= self.two
        return result

    def __init__(self, one: Digit, two: Digit) -> N:
        ignore(self)
        data = [one, two]
        data.sort()
        super().__init__(*data)

    def __iter__(self) -> IT[Digit]:
        def iterator() -> G[Digit, N, N]:
            for index in range(self.one.one, self.two.one + 1):
                yield Digit(index)

        return iter(iterator())


class Plane(Dyad[Line]):
    """"""

    __slots__: TS = ()

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

    @classmethod
    def create(cls, width: Z, height: Z) -> K:
        """"""
        one = Line.create(0, width)
        two = Line.create(0, height)
        result = cls(one, two)
        return result

    def index(self, point: Point) -> Digit:
        """"""
        orgin = point - self.origin
        result = orgin.two.one * self.one.length + orgin.one.one
        return result

    @property
    def length(self) -> Digit:
        """"""
        result = self.one.length * self.two.length
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

    def __iter__(self) -> IT[Point]:
        def iterator() -> G[Point, N, N]:
            for two in self.two:
                for one in self.one:
                    yield Point(one, two)

        return iter(iterator())


class Dictionary[X](collections.abc.MutableMapping[S, A]):
    """"""

    mapping: D[S, X]

    def copy(self) -> K:
        """"""
        return self.echo(self)

    @classmethod
    def echo(cls, self: K) -> K:
        """"""
        return cls(self.mapping)

    def key(self, key: S) -> S:
        """Expands short keys to full keys."""
        if VERTICAL_LINE not in key:
            return key
        add = NONE
        result = NONE
        one, two = key.split(VERTICAL_LINE)
        names = re.split(r"(\w+)", one)
        for name in names:
            add += name
            result = add + two
            if result in self.mapping:
                break
        return result

    @classmethod
    def make(cls, mapping: V[D[S, X]] = None) -> K:
        """"""
        return cls(mapping)

    def __delitem__(self, key: S) -> N:
        index = self.key(key)
        del self.mapping[index]

    def __getitem__(self, key: S) -> X:
        index = self.key(key)
        result = self.mapping[index]
        return result

    def __init__(self, mapping: V[D[S, X]] = None) -> N:
        self.mapping = mapping or {}

    def __iter__(self) -> IT[S]:
        return iter(self.mapping)

    def __len__(self) -> Z:
        return len(self.mapping)

    def __setitem__(self, key: S, value: X) -> N:
        index = self.key(key)
        self.mapping[index] = value

    def __or__(self, other: K) -> K:
        result = self.make(self.mapping)
        result.mapping.update(other.mapping)
        return result

    def __ror__(self, other: K) -> K:
        result = self.make(other.mapping)
        result.mapping.update(self.mapping)
        return result

    def __ior__(self, other: K) -> K:
        self.mapping.update(other.mapping)
        return self


ignore(Plane, Dictionary)
