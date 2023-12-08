""""""


from celestine.typed import (
    GF,
    A,
    B,
    D,
    F,
    G,
    H,
    I,
    K,
    N,
    R,
    S,
    T,
)


class Object:
    """"""

    @classmethod
    def clone(cls, self: K) -> K:
        """"""
        return cls()

    def copy(self) -> K:
        """"""
        return self.clone(self)

    def __init__(self, **star: R) -> N:
        """This does not pass the star parameter to the real object."""
        super().__init__()


class Point:
    """"""

    one: F
    two: F

    @classmethod
    def clone(cls, self: K) -> K:
        """"""
        return cls(self.one, self.two)

    def copy(self) -> K:
        """"""
        return self.clone(self)

    @property
    def float(self) -> T[F, F]:
        return (self.one, self.two)

    @property
    def int(self) -> T[I, I]:
        return tuple(map(round, self.float))

    def __init__(self, one: F, two: F) -> N:
        self.one = float(one)
        self.two = float(two)

    def __iter__(self) -> GF:
        yield self.one
        yield self.two

    def __repr__(self) -> S:
        return f"Point({self.one}, {self.two})"

    def __str__(self) -> S:
        return f"({self.one}, {self.two})"

    def __sub__(self, other: K) -> K:
        one = self.one - other.one
        two = self.two - other.two
        return type(self)(one, two)

    def __truediv__(self, other: K) -> K:
        one = self.one / other.one
        two = self.two / other.two
        return type(self)(one, two)


class Line:
    """"""

    minimum: F
    maximum: F

    @classmethod
    def clone(cls, self: K) -> K:
        """"""
        return cls(self.minimum, self.maximum)

    def copy(self) -> K:
        """"""
        return self.clone(self)

    @property
    def length(self) -> F:
        return self.maximum - self.minimum

    @property
    def midpoint(self) -> F:
        return (self.minimum + self.maximum) / 2

    @property
    def float(self) -> T[F, F]:
        return (self.minimum, self.maximum)

    @property
    def int(self) -> T[I, I]:
        return tuple(map(round, self.float))

    def __add__(self, other: F) -> K:
        one = self.minimum + other
        two = self.maximum + other
        return type(self)(one, two)

    def __contains__(self, item: F) -> B:
        return self.minimum <= item <= self.maximum

    def __iadd__(self, other: F) -> K:
        self.minimum += other
        self.maximum += other
        return self

    def __imul__(self, other: F) -> K:
        self.minimum *= other
        self.maximum *= other
        return self

    def __init__(self, minimum: F, maximum: F) -> N:
        self.minimum = float(min(minimum, maximum))
        self.maximum = float(max(minimum, maximum))

    def __mul__(self, other: F) -> K:
        one = self.minimum * other
        two = self.maximum * other
        return type(self)(one, two)

    def __repr__(self) -> S:
        return f"Line({self.minimum}, {self.maximum})"

    def __str__(self) -> S:
        return f"[{self.minimum}, {self.maximum}]"


class Plane:
    """"""

    one: Line
    two: Line

    def center(self, other: K) -> N:
        self += other.centroid - self.centroid

    @property
    def centroid(self) -> Point:
        one = self.one.midpoint
        two = self.two.midpoint
        return Point(one, two)

    @classmethod
    def clone(cls, self: K) -> K:
        """"""
        one = self.one.copy()
        two = self.two.copy()
        return cls(one, two)

    def copy(self) -> K:
        """"""
        return self.clone(self)

    @property
    def float(self) -> T[F, F, F, F]:
        xmin = self.one.minimum
        ymin = self.two.minimum
        xmax = self.one.maximum
        ymax = self.two.maximum
        return (xmin, ymin, xmax, ymax)

    @property
    def int(self) -> T[I, I, I, I]:
        return tuple(map(round, self.float))

    @classmethod
    def make(cls, width: F, height: F) -> K:
        """"""
        one = Line(0, width)
        two = Line(0, height)
        return cls(one, two)

    @property
    def origin(self) -> Point:
        """"""
        return Point(self.one.minimum, self.two.minimum)

    def scale_to_max(self, other: K) -> K:
        self *= max(other.size / self.size)
        return self

    def scale_to_min(self, other: K) -> K:
        self *= min(other.size / self.size)
        return self

    def quantize(self) -> K:
        self.one.quantize()
        self.two.quantize()
        return self

    @property
    def size(self) -> Point:
        return Point(self.one.length, self.two.length)

    def __add__(self, other: Point) -> K:
        one = self.one + other.one
        two = self.two + other.two
        return type(self)(one, two)

    def __contains__(self, item: Point) -> B:
        one = item.one in self.one
        two = item.two in self.two
        return one and two

    def __iadd__(self, other: Point) -> K:
        self.one += other.one
        self.two += other.two
        return self

    def __imul__(self, other: F) -> K:
        self.one *= other
        self.two *= other
        return self

    def __init__(self, one: Line, two: Line) -> N:
        self.one = one.copy()
        self.two = two.copy()

    def __mul__(self, other: F) -> K:
        one = self.one * other
        two = self.two * other
        return type(self)(one, two)

    def __repr__(self) -> S:
        one = repr(self.one)
        two = repr(self.two)
        return f"Plane({one}, {two})"

    def __str__(self) -> S:
        one = str(self.one)
        two = str(self.two)
        return f"({one}, {two})"


class Rectangle:
    """"""

    left: I
    upper: I
    right: I
    lower: I

    def copy(self, other: K) -> N:
        """Copy the values from another object."""
        self.left = other.left
        self.upper = other.upper
        self.right = other.right
        self.lower = other.lower

    def within(self, dot_x: I, dot_y: I) -> B:
        """Test that click inside us."""
        test_x = self.left <= dot_x <= self.right
        test_y = self.upper <= dot_y <= self.lower
        return test_x and test_y

    @property
    def origin(self) -> T[I, I]:
        """"""
        return (self.left, self.upper)

    @property
    def size(self) -> T[I, I]:
        """"""
        return (self.right - self.left, self.lower - self.upper)

    @property
    def value(self) -> T[I, I, I, I]:
        """"""
        return (self.left, self.upper, self.right, self.lower)

    def __init__(self, left: I, upper: I, right: I, lower: I) -> N:
        """"""
        self.left = left
        self.upper = upper
        self.right = right
        self.lower = lower


class Abstract(Object):
    """"""

    keep: A  # The object that the window system interacts with.

    area: Plane
    canvas: A
    hidden: B
    hold: H
    name: S  # The key to use to find this in the window dictionary.

    def click(self, point: Point) -> N:
        """"""
        if self.hidden:
            return

        if point in self.area:
            self.click_action()

    def click_action(self) -> N:
        pass

    def draw(self, **star: R) -> N:
        """"""
        if self.hidden:
            return

    def hide(self) -> N:
        """"""
        self.hidden = True

    def make(self) -> N:
        """"""

    def show(self) -> N:
        """"""
        self.hidden = False

    def spot(self, area: Plane) -> N:
        """"""
        self.area = area.copy()

    def __init__(self, hold: H, canvas: A, name: S, **star: R) -> N:
        super().__init__(**star)
        self.area = Plane.make(0, 0)
        self.canvas = canvas
        self.hidden = False
        self.hold = hold
        self.name = name

        self.keep = None


class Collection(Object):
    """"""

    item: D[S, Abstract]

    def item_get(self, name: S) -> Abstract:
        """"""
        return self.item[name]

    def item_set(self, name: S, item: Abstract) -> Abstract:
        """"""
        self.item[name] = item
        return item

    def load(self, name: S) -> Abstract:
        """"""
        return self.item[name]

    def save(self, item: Abstract) -> N:
        """"""
        self.item[item.name] = item

    def __init__(self, **star: R) -> N:
        self.item = {}
        super().__init__(**star)

    def __iter__(self) -> G[T[S, Abstract], N, N]:
        """"""
        yield from self.item.items()
