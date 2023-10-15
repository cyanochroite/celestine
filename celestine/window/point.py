""""""

from celestine.typed import (
    GE,
    SELF,
    B,
    F,
    N,
)


class Point:
    """"""

    one: F
    two: F

    @classmethod
    def clone(cls, self: SELF) -> SELF:
        """"""
        return cls(self.one, self.two)

    def copy(self) -> SELF:
        """"""
        return self.clone(self)

    def __init__(self, one: F, two: F) -> N:
        self.one = one
        self.two = two

    def __iter__(self) -> GE[F, N, N]:
        yield self.one
        yield self.two

    def __repr__(self):
        return f"Point({self.one}, {self.two})"

    def __str__(self):
        return f"({self.one}, {self.two})"

    def __sub__(self, other: SELF) -> SELF:
        one = self.one - other.one
        two = self.two - other.two
        return type(self)(one, two)

    def __truediv__(self, other: SELF) -> SELF:
        one = self.one / other.one
        two = self.two / other.two
        return type(self)(one, two)


class Line:
    """"""

    minimum: F
    maximum: F

    @classmethod
    def clone(cls, self: SELF) -> SELF:
        """"""
        return cls(self.minimum, self.maximum)

    def copy(self) -> SELF:
        """"""
        return self.clone(self)

    @property
    def length(self):
        return self.maximum - self.minimum

    @property
    def midpoint(self) -> F:
        return (self.minimum + self.maximum) / 2

    def __add__(self, other: F) -> SELF:
        one = self.minimum + other
        two = self.maximum + other
        return type(self)(one, two)

    def __contains__(self, item: F) -> B:
        return self.minimum <= item <= self.maximum

    def __iadd__(self, other: F) -> SELF:
        self.minimum += other
        self.maximum += other
        return self

    def __imul__(self, other: F) -> SELF:
        self.minimum *= other
        self.maximum *= other
        return self

    def __init__(self, minimum: F, maximum: F) -> N:
        self.minimum = min(minimum, maximum)
        self.maximum = max(minimum, maximum)

    def __mul__(self, other: F) -> SELF:
        one = self.minimum * other
        two = self.maximum * other
        return type(self)(one, two)

    def __repr__(self):
        return f"Line({self.minimum}, {self.maximum})"

    def __str__(self):
        return f"[{self.minimum}, {self.maximum}]"


class Plane:
    """"""

    one: Line
    two: Line

    def center(self, other: SELF) -> N:
        self += other.centroid - self.centroid

    @property
    def centroid(self) -> Point:
        return Point(self.one.midpoint, self.two.midpoint)

    @classmethod
    def clone(cls, self: SELF) -> SELF:
        """"""
        one = self.one.copy()
        two = self.two.copy()
        return cls(one, two)

    def copy(self) -> SELF:
        """"""
        return self.clone(self)

    @classmethod
    def make(cls, width: F, height: F) -> SELF:
        """"""
        one = Line(0, width)
        two = Line(0, height)
        return cls(one, two)

    def scale_to_max(self, other: SELF) -> N:
        print(str(other), repr(other))
        print(str(self), repr(self))
        self *= max(other.size / self.size)

    def scale_to_min(self, other: SELF) -> N:
        self *= min(other.size / self.size)

    @property
    def size(self) -> Point:
        return Point(self.one.length, self.two.length)

    def __add__(self, other: Point) -> SELF:
        one = self.one + other.one
        two = self.two + other.two
        return type(self)(one, two)

    def __contains__(self, item: Point) -> B:
        one = item.one in self.one
        two = item.two in self.two
        return one and two

    def __iadd__(self, other: Point) -> SELF:
        self.one += other.one
        self.two += other.two
        return self

    def __imul__(self, other: F) -> SELF:
        self.one *= other
        self.two *= other
        return self

    def __init__(self, one: Line, two: Line) -> N:
        self.one = one.copy()
        self.two = two.copy()

    def __mul__(self, other: F) -> SELF:
        one = self.one * other
        two = self.two * other
        return type(self)(one, two)

    def __repr__(self):
        one = repr(self.one)
        two = repr(self.two)
        return f"Plane({one}, {two})"

    def __str__(self):
        one = str(self.one)
        two = str(self.two)
        return f"({one}, {two})"
