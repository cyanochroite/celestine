""""""

from collections.abc import Collection

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
    P,
    R,
    S,
    T,
)
from celestine.unicode import NONE
from celestine.window.container import Image as Mode


class Point:
    """"""

    one: F
    two: F

    @classmethod
    def clone(cls, self: K) -> K:
        """"""
        # TODO: UNUSED
        return cls(self.one, self.two)

    def copy(self) -> K:
        """"""
        # TODO: UNUSED
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
        # TODO: UNUSED
        return f"Point({self.one}, {self.two})"

    def __str__(self) -> S:
        # TODO: UNUSED
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
        # TODO: UNUSED
        return (self.minimum, self.maximum)

    @property
    def int(self) -> T[I, I]:
        # TODO: UNUSED
        return tuple(map(round, self.float))

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

    def __isub__(self, other: F) -> K:
        self.minimum -= other
        self.maximum -= other
        return self

    def __repr__(self) -> S:
        # TODO: UNUSED
        return f"Line({self.minimum}, {self.maximum})"

    def __str__(self) -> S:
        # TODO: UNUSED
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

    @property
    def size(self) -> Point:
        return Point(self.one.length, self.two.length)

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

    def __isub__(self, other: Point) -> K:
        self.one -= other.one
        self.two -= other.two
        return self

    def __repr__(self) -> S:
        one = repr(self.one)
        two = repr(self.two)
        # TODO: UNUSED
        return f"Plane({one}, {two})"

    def __str__(self) -> S:
        one = str(self.one)
        two = str(self.two)
        # TODO: UNUSED
        return f"({one}, {two})"

    def spot(
        self, index_x: I, index_y: I, partition_x: I, partition_y: I
    ) -> N:
        """"""
        size_x = self.one.length
        size_y = self.two.length

        fragment_x = size_x // partition_x
        fragment_y = size_y // partition_y


        left = self.one.minimum
        upper = self.two.minimum

        ymin = upper + fragment_y * (index_y + 0)
        ymax = upper + fragment_y * (index_y + 1)
        xmin = left + fragment_x * (index_x + 0)
        xmax = left + fragment_x * (index_x + 1)

        one = Line(xmin, xmax)
        two = Line(ymin, ymax)

        return Plane(one, two)

class Area:
    """"""

    local: Plane
    world: Plane

    @classmethod
    def clone(cls, self: K) -> K:
        """"""
        return cls()

    def copy(self) -> K:
        """"""
        return self.clone(self)

    def __contains__(self, item: Point) -> B:
        return item in self.world

    @classmethod
    def make(cls, width: F, height: F) -> K:
        """"""
        local = Plane.make(width, height)
        world = Plane.make(width, height)
        return cls(local, world)

    def __init__(self, local: Plane, world: Plane) -> N:
        self.local = local.copy()
        self.world = world.copy()


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


class Abstract(Object):
    """"""

    keep: A  # The object that the window system interacts with.
    parent: K

    area: Area
    canvas: A
    hidden: B
    hold: H
    name: S  # The key to use to find this in the window dictionary.

    action: S  # The action to perform when the user clicks the button.
    fit: S  # The way the image scales to fit the view space.
    goto: S  # The page to go to when clicked.
    path: S  # The path to the image to use as a background.
    text: S  # Text that describes the purpose of the button's action.

    def click(self, point: Point, **star: R) -> B:
        """"""
        if self.hidden:
            return False

        if point not in self.area:
            return False

        if self.action:
            action = self.hold.window.work
            argument = self.action
            star = self.star | {"caller": self.name}
            self.hold.queue(action, argument, star)

        if self.goto:
            action = self.hold.window.turn
            argument = self.goto
            star = self.star | {}
            self.hold.queue(action, argument, star)

        return True

    def draw(self, **star: R) -> B:
        """"""
        if self.hidden:
            return False

        #  TODO: Check if other types want this here.
        if self.path:
            self.update(self.path)

        return True

    def hide(self) -> N:
        """"""
        self.hidden = True

    def can_make(self, **star: R) -> B:
        """"""
        return True

    def make(self, canvas: A) -> N:
        """"""
        self.canvas = canvas

    def show(self) -> N:
        """"""
        self.hidden = False

    def spot(self, area: Area) -> N:
        """"""
        self.area = area

    def update(self, path: P, **star: R) -> N:
        """"""
        pillow = self.hold.package.pillow

        self.path = path

        image = pillow.open(self.path)

        curent = Plane.make(image.image.width, image.image.height)
        target = Plane.make(*self.area.world.size.int)

        match self.fit:
            case Mode.FILL:
                result = curent.scale_to_min(target)
            case Mode.FULL:
                result = curent.scale_to_max(target)

        result.center(target)

        image.resize(result.size)
        self.image.paste(image, result)

    def __init__(self, hold: H, name: S, parent: K, **star: R) -> N:
        super().__init__(**star)
        self.parent = parent
        self.area = Area.make(0, 0)
        self.canvas = None
        self.hidden = False
        self.hold = hold
        self.name = name
        self.keep = None

        self.star = star
        # Contains all remaining keyword arguments.

        def make(name: S, default: S = NONE) -> N:
            value = star.pop(name, default)
            setattr(self, name, value)

        make("action")
        # The action to perform when the user triggers the button.

        make("fit", Mode.FILL)
        # The way the image scales to fit the view space.

        make("goto")
        # The page to go to when clicked.

        make("path")
        # The path to the image to use as a background.

        make("text")
        # Text that describes the purpose of the button's action.


class Tree(Object, Collection):
    """"""

    children: D[S, K]

    def get(self, name: S) -> K:
        """"""
        return self.children[name]

    def set(self, item: K) -> K:
        """"""
        self.children[item.name] = item
        return item

    def __bool__(self) -> B:
        return True

    def __contains__(self, item: S) -> B:
        return item in self.children

    def __init__(self, **star: R) -> N:
        self.children = {}
        super().__init__(**star)

    def __iter__(self) -> G[T[S, K], N, N]:
        yield from self.children.items()

    def __len__(self) -> I:
        return len(self.children)
