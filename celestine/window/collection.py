""""""

from celestine.typed import (
    GZ,
    B,
    F,
    K,
    N,
    T,
    Z,
)


class Point:
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

    def __init__(self, _one: F, _two: F) -> N:
        self._one = _one
        self._two = _two

    def __iter__(self) -> GZ:
        yield self._one
        yield self._two

    def __sub__(self, other: K) -> K:
        one = self._one - other._one
        two = self._two - other._two
        return type(self)(one, two)

    def __truediv__(self, other: K) -> K:
        one = self._one / other._one
        two = self._two / other._two
        return type(self)(one, two)

    def __repr__(self):
        return f"Point({repr(self._one)}, {repr(self._two)})"

    def __str__(self):
        return f"({str(self._one)}, {str(self._two)})"


class Line:
    """"""

    minimum: Z
    maximum: Z

    @classmethod
    def clone(cls, self: K) -> K:
        """"""
        return cls(self.minimum, self.maximum)

    def copy(self) -> K:
        """"""
        return self.clone(self)

    @property
    def length(self) -> Z:
        """"""
        return self.maximum - self.minimum

    @property
    def midpoint(self) -> Z:
        """"""
        return (self.minimum + self.maximum) // 2

    def __contains__(self, item: Z) -> B:
        return self.minimum <= item <= self.maximum

    def __iadd__(self, other: Z) -> K:
        self.minimum += other
        self.maximum += other
        return self

    def __imul__(self, other: Z) -> K:
        self.minimum *= other
        self.maximum *= other
        return self

    def __init__(self, minimum: Z, maximum: Z) -> N:
        self.minimum = min(minimum, maximum)
        self.maximum = max(minimum, maximum)

    def __isub__(self, other: Z) -> K:
        self.minimum -= other
        self.maximum -= other
        return self

    def __repr__(self):
        return f"Line({repr(self.minimum)}, {repr(self.maximum)})"

    def __str__(self):
        return f"({str(self.minimum)}, {str(self.maximum)})"


class Plane:
    """"""

    _one: Line
    _two: Line

    @property
    def one(self) -> Line:
        """"""
        return self._one

    @property
    def two(self) -> Line:
        """"""
        return self._two

    def center(self, other: K) -> N:
        """"""
        self += other.centroid - self.centroid

    @property
    def centroid(self) -> Point:
        """"""
        _one = self._one.midpoint
        _two = self._two.midpoint
        return Point(_one, _two)

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
        _one = Line(0, width)
        _two = Line(0, height)
        return cls(_one, _two)

    @property
    def origin(self) -> Point:
        """"""
        return Point(self._one.minimum, self._two.minimum)

    def scale_to_max(self, other: K) -> K:
        """"""
        self *= max(other.size / self.size)
        return self

    def scale_to_min(self, other: K) -> K:
        """"""
        self *= min(other.size / self.size)
        return self

    @property
    def size(self) -> Point:
        """"""
        return Point(self._one.length, self._two.length)

    def __contains__(self, item: Point) -> B:
        _one = item.one in self._one
        _two = item.two in self._two
        return _one and _two

    def __iadd__(self, other: Point) -> K:
        self._one += other.one
        self._two += other.two
        return self

    def __imul__(self, other: Z) -> K:
        self._one *= other
        self._two *= other
        return self

    def __init__(self, _one: Line, _two: Line) -> N:
        self._one = _one.copy()
        self._two = _two.copy()

    def __isub__(self, other: Point) -> K:
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
