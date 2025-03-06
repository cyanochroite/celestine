""""""

import itertools
import math

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
    Q,
    S,
    Struct,
    T,
    U,
    Z,
    cast,
    ignore,
    override,
)

type Number = U["Cardinal", F, Z]
type Unary = C[[Number], Number]
type Binary = C[[Number, Number], Number]
type Nomad = U[Number, Q[F], Q[Z]]


class Round:
    """"""

    @staticmethod
    def decrease(one: Number) -> Number:
        """"""
        value = math.trunc(one)
        result = cast(Number, value)
        return result

    @staticmethod
    def increase(one: Number) -> Number:
        """"""
        negative = math.floor(one)
        positive = math.ceil(one)
        value = positive if one >= 0 else negative
        result = cast(Number, value)
        return result

    @staticmethod
    def negative(one: Number) -> Number:
        """"""
        value = math.floor(one)
        result = cast(Number, value)
        return result

    @staticmethod
    def positive(one: Number) -> Number:
        """"""
        value = math.ceil(one)
        result = cast(Number, value)
        return result

    @staticmethod
    def round(one: Number, ndigits: VZ = None) -> Number:
        """"""
        result = round(one, ndigits)
        return result


class Math(Struct):
    """"""

    @staticmethod
    def add(one: Number, two: Number) -> Number:
        """"""
        result = one + two
        return result

    @staticmethod
    def mul(one: Number, two: Number) -> Number:
        """"""
        result = one * two
        return result

    @staticmethod
    def neg(one: Number) -> Number:
        """"""
        result = -one
        return result

    @staticmethod
    def pos(one: Number) -> Number:
        """"""
        result = +one
        return result

    @staticmethod
    def radd(one: Number, two: Number) -> Number:
        """"""
        result = two + one
        return result

    @staticmethod
    def rsub(one: Number, two: Number) -> Number:
        """"""
        result = two - one
        return result

    @staticmethod
    def sub(one: Number, two: Number) -> Number:
        """"""
        result = one - two
        return result

    @staticmethod
    def truediv(one: Number, two: Number) -> Number:
        """"""
        result = one / two
        return result


class Cardinal(Struct):
    """"""

    __slots__: TS = ("name",)

    name: S

    def binary(self, binary: Binary, other: Nomad) -> L[Number]:
        """Binary arithmetic operations."""
        if isinstance(other, Cardinal):
            array = other.data
        elif isinstance(other, float | int):
            array = [other]
        else:
            array = [*other]
        iterable = itertools.repeat(array)
        data = itertools.chain.from_iterable(iterable)
        skymap = map(binary, self.data, data)
        result = list(skymap)
        return result

    def round(self, ndigits: VZ = None) -> K:
        """"""
        other = itertools.repeat(ndigits)
        data = list(map(Round.round, self.data, other))
        result = self.make(*data)
        return result

    def unary(self, unary: Unary) -> L[Number]:
        """Unary arithmetic operations."""
        result = list(map(unary, self.data))
        return result

    def _arithmetic(self, binary: Binary, other: Nomad) -> K:
        data = self.binary(binary, other)
        result = self.make(*data)
        return result

    def _augmented(self, binary: Binary, other: Nomad) -> K:
        self.data = self.binary(binary, other)
        return self

    def inplace(self, unary: Unary) -> K:
        """"""
        data = self.unary(unary)
        result = self.make(*data)
        return result

    def __add__(self, other: Nomad) -> K:
        result = self._arithmetic(Math.add, other)
        return result

    def __ceil__(self) -> K:
        result = self.inplace(Round.positive)
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
        result = self.inplace(Round.negative)
        return result

    def __getitem__(self, key: S) -> A:
        result = list(self.data)[int(key)]
        return result

    def __ge__(self, other: Number) -> B:
        one = float(self)
        two = float(other)
        result = one >= two
        return result

    def __gt__(self, other: Number) -> B:
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
        result = self._augmented(Math.add, other)
        return result

    def __imul__(self, other: Nomad) -> K:
        result = self._augmented(Math.mul, other)
        return result

    def __isub__(self, other: Nomad) -> K:
        result = self._augmented(Math.sub, other)
        return result

    def __itruediv__(self, other: Nomad) -> K:
        result = self._augmented(Math.truediv, other)
        return result

    def __le__(self, other: Number) -> B:
        one = float(self)
        two = float(other)
        result = one <= two
        return result

    def __lt__(self, other: Number) -> B:
        one = float(self)
        two = float(other)
        result = one < two
        return result

    def __mul__(self, other: Nomad) -> K:
        return self._arithmetic(Math.mul, other)

    def __neg__(self) -> K:
        result = self.inplace(Math.neg)
        return result

    def __new__(cls, *_: A) -> K:
        ignore(_)
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
        result = self.inplace(Math.pos)
        return result

    def __radd__(self, other: Nomad) -> K:
        result = self._arithmetic(Math.radd, other)
        return result

    def __repr__(self):
        data = self.__str__()
        result = string(self.name, data)
        return result

    def __rmul__(self, other: Nomad) -> K:
        result = self._arithmetic(Math.mul, other)
        return result

    def __round__(self, ndigits: VZ = None) -> K:
        result = self.round(ndigits)
        return result

    def __rsub__(self, other: Nomad) -> K:
        result = self._arithmetic(Math.rsub, other)
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
        result = self._arithmetic(Math.sub, other)
        return result

    def __truediv__(self, other: Nomad) -> K:
        result = self._arithmetic(Math.truediv, other)
        return result

    def __trunc__(self) -> K:
        result = self.inplace(Round.decrease)
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


ignore(Monad, Dyad, Triad, Tetrad)
