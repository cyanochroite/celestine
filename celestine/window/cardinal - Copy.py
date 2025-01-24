""""""

import itertools
import math
import typing

from celestine.literal import (
    COMMA,
    FULL_STOP,
    LEFT_PARENTHESIS,
    RIGHT_PARENTHESIS,
    SPACE,
    string,
)
from celestine.typed import (
    TS,
    TS1,
    TS2,
    TS3,
    TS4,
    VZ,
    A,
    B,
    C,
    F,
    K,
    L,
    N,
    S,
    Struct,
    T,
    Z,
    cast,
    ignore,
    override,
)

type Nomad = typing.Union["Cardinal", F, Z]
type Unary = C[[Nomad], Nomad]
type Binary = C[[Nomad, Nomad], Nomad]


class Math(Struct):
    """"""

    @staticmethod
    def add(one: Nomad, two: Nomad) -> Nomad:
        """"""
        result = one + two
        return result

    @staticmethod
    def ceil(one: Nomad) -> Nomad:
        """"""
        value = math.ceil(one)
        result = cast(Nomad, value)
        return result

    @staticmethod
    def floor(one: Nomad) -> Nomad:
        """"""
        value = math.floor(one)
        result = cast(Nomad, value)
        return result

    @staticmethod
    def mul(one: Nomad, two: Nomad) -> Nomad:
        """"""
        result = one * two
        return result

    @staticmethod
    def neg(one: Nomad) -> Nomad:
        """"""
        result = -one
        return result

    @staticmethod
    def pos(one: Nomad) -> Nomad:
        """"""
        result = +one
        return result

    @staticmethod
    def round(one: Nomad, ndigits: VZ = None) -> Nomad:
        """"""
        result = round(one, ndigits)
        return result

    @staticmethod
    def sub(one: Nomad, two: Nomad) -> Nomad:
        """"""
        result = one - two
        return result

    @staticmethod
    def truediv(one: Nomad, two: Nomad) -> Nomad:
        """"""
        result = one / two
        return result

    @staticmethod
    def trunc(one: Nomad) -> Nomad:
        """"""
        value = math.trunc(one)
        result = cast(Nomad, value)
        return result


class Cardinal(Struct):
    """"""

    __slots__: TS = ("name",)

    name: S

    def binary(self, binary: Binary, other: Nomad) -> L[Nomad]:
        """Binary arithmetic operations."""
        data: L[Nomad]
        if isinstance(other, float | int):
            data = [other] * len(self.data)
        else:
            # TODO: What happens when lists have differnt lengths?
            # Bigger worry is when SELF is longer and gets cropped.
            data = getattr(other, "data")
        result = list(map(binary, self.data, data))
        return result

    def ceil(self) -> K:
        """"""
        result = self._inplace(Math.ceil)
        return result

    def floor(self) -> K:
        """"""
        result = self._inplace(Math.floor)
        return result

    def round(self, ndigits: VZ = None) -> K:
        """"""
        other = itertools.repeat(ndigits)
        data = list(map(Math.round, self.data, other))
        result = self.make(*data)
        return result

    def unary(self, unary: Unary) -> L[Nomad]:
        """Unary arithmetic operations."""
        result = list(map(unary, self.data))
        return result

    def _arithmetic(self, other: Nomad, binary: Binary) -> K:
        data = self.binary(binary, other)
        result = self.make(*data)
        return result

    def _augmented(self, other: Nomad, binary: Binary) -> K:
        self.data = self.binary(binary, other)
        return self

    def _inplace(self, unary: Unary) -> K:
        data = self.unary(unary)
        result = self.make(*data)
        return result

    def __add__(self, other: Nomad) -> K:
        result = self._arithmetic(other, Math.add)
        return result

    def __ceil__(self) -> K:
        result = self.ceil()
        return result

    def __del__(self) -> N:
        super().__del__()
        del self.name

    def __eq__(self, other: object) -> B:
        if not isinstance(other, Cardinal):
            return False
        one = float(self)
        two = float(other)
        result = math.isclose(one, two)
        return result

    def __float__(self) -> F:
        data = map(float, self.data)
        result = sum(data)
        return result

    def __floor__(self) -> K:
        result = self.floor()
        return result

    def __ge__(self, other: Nomad) -> B:
        one = float(self)
        two = float(other)
        result = one >= two
        return result

    def __gt__(self, other: Nomad) -> B:
        one = float(self)
        two = float(other)
        result = one > two
        return result

    def __hash__(self) -> Z:
        number = map(float, self.data)
        count = sum(number)
        result = hash(count)
        return result

    def __iadd__(self, other: Nomad) -> K:
        result = self._augmented(other, Math.add)
        return result

    def __imul__(self, other: Nomad) -> K:
        result = self._augmented(other, Math.mul)
        return result

    def __isub__(self, other: Nomad) -> K:
        return self._augmented(other, Math.sub)

    def __itruediv__(self, other: Nomad) -> K:
        result = self._augmented(other, Math.truediv)
        return result

    def __le__(self, other: Nomad) -> B:
        one = float(self)
        two = float(other)
        result = one <= two
        return result

    def __lt__(self, other: Nomad) -> B:
        one = float(self)
        two = float(other)
        result = one < two
        return result

    def __mul__(self, other: Nomad) -> K:
        return self._arithmetic(other, Math.mul)

    def __neg__(self) -> K:
        result = self._inplace(Math.neg)
        return result

    def __new__(cls, *_: A) -> K:
        new = super().__new__(cls)
        name = repr(cls)
        index = name.rindex(FULL_STOP) + 1
        new.name = name[index:-2]
        return new

    def __ne__(self, other: object) -> B:
        if not isinstance(other, Cardinal):
            return True
        one = float(self)
        two = float(other)
        result = not math.isclose(one, two)
        return result

    def __pos__(self) -> K:
        result = self._inplace(Math.pos)
        return result

    def __radd__(self, other: Nomad) -> K:
        result = self._arithmetic(other, Math.add)
        return result

    def __repr__(self):
        data = self.__str__()
        result = string(self.name, data)
        return result

    def __rmul__(self, other: Nomad) -> K:
        result = self._arithmetic(other, Math.mul)
        return result

    def __round__(self, ndigits: VZ = None) -> K:
        result = self.round(ndigits)
        return result

    def __rsub__(self, other: Nomad) -> K:
        result = self._arithmetic(other, Math.sub)
        return result

    def __rtruediv__(self, other: Nomad) -> K:
        result = self.__truediv__(other)
        return result

    def __str__(self):
        comma = string(COMMA, SPACE)
        data = comma.join(map(repr, self.data))
        result = string(LEFT_PARENTHESIS, data, RIGHT_PARENTHESIS)
        return result

    def __sub__(self, other: Nomad) -> K:
        result = self._arithmetic(other, Math.sub)
        return result

    def __truediv__(self, other: Nomad) -> K:
        result = self._arithmetic(other, Math.truediv)
        return result

    def __trunc__(self) -> K:
        result = self._inplace(Math.trunc)
        return result


class Monad[X](Cardinal):
    """"""

    __slots__: TS1 = ("one",)

    one: X

    @override
    def _del(self) -> N:
        del self.one

    @override
    def _get(self) -> T[X]:
        return (self.one,)

    @override
    def _set(self, value: T[X]) -> N:
        self.one = value[0]

    def __init__(self, one: X) -> N:
        ignore(self)
        super().__init__(one)

    def __new__(cls, one: X) -> K:
        return super().__new__(cls, one)

    data = property(_get, _set, _del)


class Dyad[X](Cardinal):
    """"""

    __slots__: TS2 = ("one", "two")

    one: X
    two: X

    @override
    def _del(self) -> N:
        del self.one
        del self.two

    @override
    def _get(self) -> T[X, X]:
        return (self.one, self.two)

    @override
    def _set(self, value: T[X, X]) -> N:
        self.one = value[0]
        self.two = value[1]

    def __init__(self, one: X, two: X) -> N:
        ignore(self)
        super().__init__(one, two)

    def __new__(cls, one: X, two: X) -> K:
        return super().__new__(cls, one, two)

    data = property(_get, _set, _del)


class Triad[X](Cardinal):
    """"""

    __slots__: TS3 = ("one", "two", "tri")

    one: X
    two: X
    tri: X

    @override
    def _del(self) -> N:
        del self.one
        del self.two
        del self.tri

    @override
    def _get(self) -> T[X, X, X]:
        return (self.one, self.two, self.tri)

    @override
    def _set(self, value: T[X, X, X]) -> N:
        self.one = value[0]
        self.two = value[1]
        self.tri = value[2]

    def __init__(self, one: X, two: X, tri: X) -> N:
        ignore(self)
        super().__init__(one, two, tri)

    def __new__(cls, one: X, two: X, tri: X) -> K:
        return super().__new__(cls, one, two, tri)

    data = property(_get, _set, _del)


class Tetrad[X](Cardinal):
    """"""

    __slots__: TS4 = ("one", "two", "tri", "tet")

    one: X
    two: X
    tri: X
    tet: X

    @override
    def _del(self) -> N:
        del self.one
        del self.two
        del self.tri
        del self.tet

    @override
    def _get(self) -> T[X, X, X, X]:
        return (self.one, self.two, self.tri, self.tet)

    @override
    def _set(self, value: T[X, X, X, X]) -> N:
        self.one = value[0]
        self.two = value[1]
        self.tri = value[2]
        self.tet = value[3]

    def __init__(self, one: X, two: X, tri: X, tet: X) -> N:
        ignore(self)
        super().__init__(one, two, tri, tet)

    def __new__(cls, one: X, two: X, tri: X, tet: X) -> K:
        return super().__new__(cls, one, two, tri, tet)

    data = property(_get, _set, _del)


#######

from celestine.typed import Z, TF3, G
import colorsys
import math
import PIL
import PIL.Image

type PIXELS = L[TF3]
type Make = G[Triad, N, N]
type PIXEL = Triad[F, F, F]


def add_greys(greys: Z) -> Make:
    """"""
    for grey in range(greys):
        pixel = Triad(grey, grey, grey)
        yield pixel


def add_colours(colours: Z) -> Make:
    """"""
    cutoff = math.floor(colours / 2 - 1)
    for red in range(colours):
        for green in range(colours):
            for blue in range(colours):
                pixel = Triad(red, green, blue)
                maximum = max(pixel)
                minimum = min(pixel)
                chroma = maximum - minimum
                if chroma > cutoff:
                    yield pixel


def add_pixels(function, limit: Z) -> Make:
    """"""
    pixels = function(limit)
    for pixel in pixels:
        result = pixel / (limit - 1)
        yield result


def add_all() -> Make:
    """"""
    yield from add_pixels(add_greys, 16)
    yield from add_pixels(add_colours, 7)


def _curses(pixel: PIXEL) -> PIXEL:
    """"""
    scale = pixel * 1000
    result = scale.round()
    return result


def _pillow(pixel: PIXEL) -> PIXEL:
    """"""
    scale = pixel * 255
    result = scale.ceil()
    return result


def _table(function) -> PIXELS:
    """"""
    result = []
    pixels = add_all()
    for pixel in pixels:
        triad = function(pixel)
        data = triad.data
        result.append(data)

    return result


curses_table = _table(_curses)
pillow_table = _table(_pillow)


crayola = list(set(pillow_table))
length = len(crayola) - 1
image = PIL.Image.new("RGB", (1024, 1024))
for y in range(1024):
    for x in range(1024):
        xx = x // 4
        yy = min(xx, length)
        colour = crayola[yy]
        image.putpixel((x, y), colour)

image.show()
