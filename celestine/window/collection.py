""""""

from celestine.typed import (
    GF,
    B,
    F,
    K,
    N,
    T,
    Z,
)

# monad
# dyad
# triad
# tetrad

# Monad
# Dyad
# Triad
# Tetrad
# Pentad
# Hexad


class Dyad:
    """"""

    _one: F
    _two: F

    @property
    def one(self) -> F:
        """"""
        return self._one

    @property
    def two(self) -> F:
        """"""
        return self._two

    @property
    def value(self) -> T[Z, Z]:
        """"""
        return (int(self._one), int(self._two))

###

    @classmethod
    def clone(cls, self: K) -> K:
        """"""
        return cls(self._one, self._two)

    def copy(self) -> K:
        """"""
        return self.clone(self)

    @property
    def length(self) -> Z:
        """"""
        return self._two - self._one

    @property
    def midpoint(self) -> Z:
        """"""
        return (self._one + self._two) // 2

###

    def __add__(self, other: K) -> K:
        one = self._one + other._one
        two = self._two + other._two
        return type(self)(one, two)

    def __contains__(self, item: Z) -> B:
        return self.minimum <= item <= self.maximum

    def __iadd__(self, other: F) -> K:
        self._one += other
        self._two += other
        return self

    def __imul__(self, other: F) -> K:
        self._one *= other
        self._two *= other
        return self

    def __init__(self, _one: F, _two: F) -> N:
        self._one = _one
        self._two = _two
        self.minimum = min(_one, _two)
        self.maximum = max(_one, _two)

    def __isub__(self, other: F) -> K:
        self._one -= other
        self._two -= other
        return self

    def __iter__(self) -> GF:
        yield self._one
        yield self._two

    def __itruediv__(self, other: F) -> K:
        self._one /= other
        self._two /= other
        return self

    def __mul__(self, other: K) -> K:
        one = self._one * other._one
        two = self._two * other._two
        return type(self)(one, two)

    def __repr__(self):
        return f"Dyad({repr(self._one)}, {repr(self._two)})"

    def __str__(self):
        return f"({str(self._one)}, {str(self._two)})"

    def __sub__(self, other: K) -> K:
        one = self._one - other._one
        two = self._two - other._two
        return type(self)(one, two)

    def __truediv__(self, other: K) -> K:
        one = self._one / other._one
        two = self._two / other._two
        return type(self)(one, two)


class Plane:
    """"""

    _one: Dyad
    _two: Dyad

    @property
    def one(self) -> Dyad:
        """"""
        return self._one

    @property
    def two(self) -> Dyad:
        """"""
        return self._two

    def center(self, other: K) -> N:
        """"""
        self += other.centroid - self.centroid

    @property
    def centroid(self) -> Dyad:
        """"""
        _one = self._one.midpoint
        _two = self._two.midpoint
        return Dyad(_one, _two)

    def copy(self) -> K:
        """"""
        return Plane(self._one, self._two)

    @property
    def value(self) -> T[Z, Z, Z, Z]:
        """"""
        xmin = int(self._one.minimum)
        ymin = int(self._two.minimum)
        xmax = int(self._one.maximum)
        ymax = int(self._two.maximum)
        return (xmin, ymin, xmax, ymax)

    @classmethod
    def make(cls, width: Z, height: Z) -> K:
        """"""
        _one = Dyad(0, width)
        _two = Dyad(0, height)
        return cls(_one, _two)

    @property
    def origin(self) -> Dyad:
        """"""
        return Dyad(self._one.minimum, self._two.minimum)

    def scale_to_max(self, other: K) -> N:
        """"""
        self *= max(other.size / self.size)

    def scale_to_min(self, other: K) -> N:
        """"""
        self *= min(other.size / self.size)

    @property
    def size(self) -> Dyad:
        """"""
        return Dyad(self._one.length, self._two.length)

    def __contains__(self, item: Dyad) -> B:
        _one = item.one in self._one
        _two = item.two in self._two
        return _one and _two

    def __iadd__(self, other: Dyad) -> K:
        self._one += other.one
        self._two += other.two
        return self

    def __imul__(self, other: Z) -> K:
        self._one *= other
        self._two *= other
        return self

    def __init__(self, _one: Dyad, _two: Dyad) -> N:
        self._one = _one.copy()
        self._two = _two.copy()

    def __isub__(self, other: Dyad) -> K:
        self._one -= other.one
        self._two -= other.two
        return self

    def __repr__(self):
        return f"Plane({repr(self._one)}, {repr(self._two)})"

    def __str__(self):
        return f"({str(self._one)}, {str(self._two)})"


class Area:
    """"""

    local: Plane
    world: Plane

    def __contains__(self, item: Dyad) -> B:
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
