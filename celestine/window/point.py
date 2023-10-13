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
        return Point(self.two.midpoint, self.two.midpoint)

    @classmethod
    def clone(cls, self: SELF) -> SELF:
        """"""
        x0 = self.one.minimum
        y0 = self.two.minimum
        x1 = self.one.maximum
        y1 = self.two.maximum
        return cls(x0, y0, x1, y1)

    def copy(self) -> SELF:
        """"""
        return self.clone(self)

    def scale_to_max(self, other: SELF) -> N:
        self *= max(other.size / self.size)

    def scale_to_min(self, other: SELF) -> N:
        self *= min(other.size / self.size)

    @property
    def size(self) -> Point:
        return Point(self.one.length, self.two.length)

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

    def __init__(self, x0: F, y0: F, x1: F, y1: F) -> N:
        """"""
        self.one = Line(x0, x1)
        self.two = Line(y0, y1)

    def __repr__(self):
        x0 = self.one.minimum
        y0 = self.two.minimum
        x1 = self.one.maximum
        y1 = self.two.maximum
        return f"Plane({x0}, {y0}, {x1}, {y1})"

    def __str__(self):
        x0 = self.one.minimum
        y0 = self.two.minimum
        x1 = self.one.maximum
        y1 = self.two.maximum
        return f"({x0}, {y0}, {x1}, {y1})"
