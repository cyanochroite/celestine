""""""

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
    ignore,
    override,
)


class Nomad(Struct):
    """"""

    __slots__: TS = ("name",)

    name: S

    def __del__(self) -> N:
        super().__del__()
        del self.name

    def __new__(cls, *_: A) -> K:
        new = super().__new__(cls)
        name = repr(cls)
        index = name.rindex(FULL_STOP) + 1
        new.name = name[index:-2]
        return new

    def __repr__(self):
        data = self.__str__()
        result = string(self.name, data)
        return result

    def __str__(self):
        comma = string(COMMA, SPACE)
        data = comma.join(map(repr, self.data))
        result = string(LEFT_PARENTHESIS, data, RIGHT_PARENTHESIS)
        return result


class Number(typing.Protocol):
    """"""

    def __add__(self, other: K) -> K:
        raise NotImplementedError(self, other)

    def __eq__(self, other: object) -> B:
        raise NotImplementedError(self, other)

    def __float__(self) -> F:
        raise NotImplementedError(self)

    def __ge__(self, other: K) -> B:
        raise NotImplementedError(self, other)

    def __gt__(self, other: K) -> B:
        raise NotImplementedError(self, other)

    def __hash__(self) -> Z:
        raise NotImplementedError(self)

    def __iadd__(self, other: K) -> K:
        raise NotImplementedError(self, other)

    def __imul__(self, other: K) -> K:
        raise NotImplementedError(self, other)

    def __isub__(self, other: K) -> K:
        raise NotImplementedError(self, other)

    def __itruediv__(self, other: K) -> K:
        raise NotImplementedError(self, other)

    def __le__(self, other: K) -> B:
        raise NotImplementedError(self, other)

    def __lt__(self, other: K) -> B:
        raise NotImplementedError(self, other)

    def __mul__(self, other: K) -> K:
        raise NotImplementedError(self, other)

    def __neg__(self) -> K:
        raise NotImplementedError(self)

    def __ne__(self, other: object) -> B:
        raise NotImplementedError(self, other)

    def __pos__(self) -> K:
        raise NotImplementedError(self)

    def __radd__(self, other: K) -> K:
        raise NotImplementedError(self, other)

    def __rmul__(self, other: K) -> K:
        raise NotImplementedError(self, other)

    def __rsub__(self, other: K) -> K:
        raise NotImplementedError(self, other)

    def __rtruediv__(self, other: K) -> K:
        raise NotImplementedError(self, other)

    def __sub__(self, other: K) -> K:
        raise NotImplementedError(self, other)

    def __truediv__(self, other: K) -> K:
        raise NotImplementedError(self, other)


type Float = Number
type Unary = C[[Float], Float]
type Binary = C[[Float, Float], Float]


class Math:
    """"""

    @staticmethod
    def add(one: Float, two: Float) -> Float:
        """"""
        result: Float = one + two
        return result

    @staticmethod
    def mul(one: Float, two: Float) -> Float:
        """"""
        result = one * two
        return result

    @staticmethod
    def neg(one: Float) -> Float:
        """"""
        result = -one
        return result

    @staticmethod
    def pos(one: Float) -> Float:
        """"""
        result = +one
        return result

    @staticmethod
    def sub(one: Float, two: Float) -> Float:
        """"""
        result = one - two
        return result

    @staticmethod
    def truediv(one: Float, two: Float) -> Float:
        """"""
        result = one / two
        return result


class Cardinal(Nomad):
    """"""

    __slots__: TS = ()

    def binary2(self, binary: Binary, other: Float) -> L[Float]:
        """Binary arithmetic operations."""
        data: L[Float]
        if isinstance(other, float | int):
            data = [other] * len(self.data)
        else:
            data = getattr(other, "data")
        result = list(map(binary, self.data, data))
        return result

    def binary(self, binary: Binary, other: Float) -> L[Float]:
        """Binary arithmetic operations."""
        data: L[Float]
        if isinstance(other, float | int):
            data = [other] * len(self.data)
        else:
            data = getattr(other, "data")
        result = list(map(binary, self.data, data))
        return result

    def unary(self, unary: Unary) -> L[Float]:
        """Unary arithmetic operations."""
        result = list(map(unary, self.data))
        return result

    def _arithmetic(self, other: Float, binary: Binary) -> K:
        data = self.binary(binary, other)
        return self.make(*data)

    def _augmented(self, other: Float, binary: Binary) -> K:
        self.data = self.binary(binary, other)
        return self
#######

    def __add__(self, other: Float) -> K:
        return self._arithmetic(other, Math.add)

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

    def __ge__(self, other: Float) -> B:
        one = float(self)
        two = float(other)
        result = one >= two
        return result

    def __gt__(self, other: Float) -> B:
        one = float(self)
        two = float(other)
        result = one > two
        return result

    def __hash__(self) -> Z:
        number = map(float, self.data)
        count = sum(number)
        result = hash(count)
        return result

    def __iadd__(self, other: Float) -> K:
        return self._augmented(other, Math.add)

    def __imul__(self, other: Float) -> K:
        return self._augmented(other, Math.mul)

    def __isub__(self, other: Float) -> K:
        return self._augmented(other, Math.sub)

    def __itruediv__(self, other: Float) -> K:
        return self._augmented(other, Math.truediv)

    def __le__(self, other: Float) -> B:
        one = float(self)
        two = float(other)
        result = one <= two
        return result

    def __lt__(self, other: Float) -> B:
        one = float(self)
        two = float(other)
        result = one < two
        return result

    def __mul__(self, other: Float) -> K:
        return self._arithmetic(other, Math.mul)

    def __neg__(self) -> K:
        self.data = self.unary(Math.neg)
        return self

    def __ne__(self, other: object) -> B:
        if not isinstance(other, Cardinal):
            return True
        one = float(self)
        two = float(other)
        result = not math.isclose(one, two)
        return result

    def __pos__(self) -> K:
        self.data = self.unary(Math.pos)
        return self

    def __radd__(self, other: Float) -> K:
        return self._arithmetic(other, Math.add)

    def __rmul__(self, other: Float) -> K:
        return self._arithmetic(other, Math.mul)

    def __rsub__(self, other: Float) -> K:
        return self._arithmetic(other, Math.sub)

    def __rtruediv__(self, other: Float) -> K:
        return self.__truediv__(other)

    def __sub__(self, other: Float) -> K:
        return self._arithmetic(other, Math.sub)

    def __truediv__(self, other: Float) -> K:
        return self._arithmetic(other, Math.truediv)


class Monad[X](Cardinal):
    """"""

    __slots__: T[S] = ("one",)

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

    __slots__: T[S, S] = ("one", "two")

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

    __slots__: T[S, S, S] = ("one", "two", "tri")

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

    __slots__: T[S, S, S, S] = ("one", "two", "tri", "tet")

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
