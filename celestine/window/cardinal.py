""""""

# pylint: disable=undefined-variable

import math
import typing

from celestine.literal import FULL_STOP
from celestine.typed import (
    B,
    C,
    F,
    G,
    K,
    L,
    N,
    Object,
    S,
    Z,
    ignore,
    override,
)

# type Math = typing.Union["Cardinal", F, Z]
type Math = typing.Union[F, Z]


class Cardinal[X: int](Object):
    """"""

    element: L[X]
    name: S

    @property
    @override
    def data(self) -> L[X]:
        """"""
        return self.element

    def unary(self, unary: C[[X], X]) -> L[X]:
        """Unary arithmetic operations."""
        result = list(map(unary, self.element))
        return result

    def binary(self, binary: C[[X, X], X], other: X) -> L[X]:
        """Binary arithmetic operations."""
        element: L[X]
        if isinstance(other, float | int):
            element = [other] * len(self.element)
        else:
            element = getattr(other, "element")
        result = list(map(binary, self.element, element))
        return result

    # 3.3.1. Basic Customization

    # class constructor

    def __new__(cls, *element: X) -> K:
        ignore(element)
        new = super().__new__(cls)
        name = repr(cls)
        index = name.rindex(FULL_STOP) + 1
        new.name = name[index:-2]
        return new

    def __init__(self, *element: X) -> N:
        super().__init__(*element)
        self.element = [*element]

    def __del__(self) -> N:
        self.element = []

    # string representation of an object

    def __repr__(self):
        element = ", ".join(map(repr, self.element))
        result = f"{self.name}({element})"
        return result

    def __str__(self):
        element = ", ".join(map(str, self.element))
        result = f"({element})"
        return result

    #  rich comparison methods

    def __lt__(self, other: X) -> B:
        one = float(self)
        two = float(other)
        result = one < two
        return result

    def __le__(self, other: X) -> B:
        one = float(self)
        two = float(other)
        result = one <= two
        return result

    def __eq__(self, other: object) -> B:
        if not isinstance(other, Cardinal):
            return False
        one = float(self)
        two = float(other)
        result = math.isclose(one, two)
        return result

    def __ne__(self, other: object) -> B:
        if not isinstance(other, Cardinal):
            return True
        one = float(self)
        two = float(other)
        result = not math.isclose(one, two)
        return result

    def __gt__(self, other: X) -> B:
        one = float(self)
        two = float(other)
        result = one > two
        return result

    def __ge__(self, other: X) -> B:
        one = float(self)
        two = float(other)
        result = one >= two
        return result

    # 3.3.7. Emulating container types

    def __iter__(self) -> G[X, N, N]:
        yield from self.element

    def __reversed__(self) -> G[X, N, N]:
        yield from reversed(self.element)

    def __contains__(self, item: X) -> B:
        return any(item == element for element in self.element)

    # 3.3.8. Emulating numeric types

    @staticmethod
    def add(one: X, two: X) -> X:
        """"""
        result = one + two
        return result

    @staticmethod
    def mul(one: X, two: X) -> X:
        """"""
        result = one * two
        return result

    @staticmethod
    def sub(one: X, two: X) -> X:
        """"""
        result = one - two
        return result

    @staticmethod
    def truediv(one: X, two: X) -> X:
        """"""
        result = one / two
        return result

    @staticmethod
    def neg(one: X) -> X:
        """"""
        result = -one
        return result

    @staticmethod
    def pos(one: X) -> X:
        """"""
        result = +one
        return result

    # binary arithmetic operations

    def _arithmetic(self, other: X, binary: C[[X, X], X]) -> K:
        element = self.binary(binary, other)
        return self.make(*element)

    def __add__(self, other: X) -> K:
        return self._arithmetic(other, self.add)

    def __mul__(self, other: X) -> K:
        return self._arithmetic(other, self.mul)

    def __sub__(self, other: X) -> K:
        return self._arithmetic(other, self.sub)

    def __truediv__(self, other: X) -> K:
        return self._arithmetic(other, self.truediv)

    # binary arithmetic operations with reflected operands

    def __radd__(self, other: X) -> K:
        return self._arithmetic(other, self.add)

    def __rmul__(self, other: X) -> K:
        return self._arithmetic(other, self.mul)

    def __rsub__(self, other: X) -> K:
        return self._arithmetic(other, self.sub)

    def __rtruediv__(self, other: X) -> K:
        return self.__truediv__(other)

    # augmented arithmetic assignments

    def _augmented(self, other: X, binary: C[[X, X], X]) -> K:
        self.element = self.binary(binary, other)
        return self

    def __iadd__(self, other: X) -> K:
        return self._augmented(other, self.add)

    def __imul__(self, other: X) -> K:
        return self._augmented(other, self.mul)

    def __isub__(self, other: X) -> K:
        return self._augmented(other, self.sub)

    def __itruediv__(self, other: X) -> K:
        return self._augmented(other, self.truediv)

    # unary arithmetic operations

    def __neg__(self) -> K:
        self.element = self.unary(self.neg)
        return self

    def __pos__(self) -> K:
        self.element = self.unary(self.pos)
        return self

    def __int__(self) -> Z:
        element = map(int, self.element)
        result = sum(element)
        return result

    def __float__(self) -> F:
        element = map(float, self.element)
        result = sum(element)
        return result


class Monad[X](Object):
    """"""
    __slots__ = ["_one"]

    @property
    @override
    def data(self) -> L[X]:
        """"""
        return [self._one]

    @property
    def one(self) -> X:
        """"""
        return self._one

    def __init__(self, one: X) -> N:
        super().__init__(one)
        self._one = one


class Dyad[X](Object):
    """"""
    __slots__ = ["_one", "_two"]

    @property
    @override
    def data(self) -> L[X]:
        """"""
        return [self._one, self._two]

    @property
    def one(self) -> X:
        """"""
        return self._one

    @property
    def two(self) -> X:
        """"""
        return self._two

    def __init__(self, one: X, two: X) -> N:
        super().__init__(one, two)
        self._one = one
        self._two = two


class Triad[X](Object):
    """"""
    __slots__ = ["_one", "_two", "_tri"]

    @property
    @override
    def data(self) -> L[X]:
        """"""
        return [self._one, self._two, self._tri]

    @property
    def one(self) -> X:
        """"""
        return self._one

    @property
    def two(self) -> X:
        """"""
        return self._two

    @property
    def tri(self) -> X:
        """"""
        return self._tri

    def __init__(self, one: X, two: X, tri: X) -> N:
        super().__init__(one, two, tri)
        self._one = one
        self._two = two
        self._tri = tri


class Tetrad[X](Object):
    """"""

    __slots__ = ["_one", "_two", "_tri", "_tet"]

    @property
    @override
    def data(self) -> L[X]:
        """"""
        return [self._one, self._two, self._tri, self._tet]

    @property
    def one(self) -> X:
        """"""
        return self._one

    @property
    def two(self) -> X:
        """"""
        return self._two

    @property
    def tri(self) -> X:
        """"""
        return self._tri

    @property
    def tet(self) -> X:
        """"""
        return self._tet

    def __init__(self, one: X, two: X, tri: X, tet: X) -> N:
        super().__init__(one, two, tri, tet)
        self._one = one
        self._two = two
        self._tri = tri
        self._tet = tet

#    def __new__(cls, one: Math, two: Math, tri: Math, tet: Math) -> K:
#        return super().__new__(cls, one, two, tri, tet)
