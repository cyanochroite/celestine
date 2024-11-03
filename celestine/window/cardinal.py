""""""

# pylint: disable=undefined-variable

import abc
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

type Math = typing.Union["Cardinal", F, Z]
type Unary = C[[Math], Math]
type Binary = C[[Math, Math], Math]


class Cardinal[Math: int](Object, abc.ABC):
    """"""

    name: S

    @abc.abstractmethod
    def _get(self) -> L[Math]:
        ignore(self)
        return []

    @abc.abstractmethod
    def _set(self, value: L[Math]) -> N:
        ignore(self)
        ignore(value)

    @abc.abstractmethod
    def _del(self) -> N:
        ignore(self)

    element = property(_get, _set, _del, "I'm the 'x' property.")

    @property
    @override
    def data(self) -> L[Math]:
        """"""
        return self.element

    def unary(self, unary: Unary) -> L[Math]:
        """Unary arithmetic operations."""
        result = list(map(unary, self.element))
        return result

    def binary(self, binary: Binary, other: Math) -> L[Math]:
        """Binary arithmetic operations."""
        element: L[Math]
        if isinstance(other, float | int):
            element = [other] * len(self.element)
        else:
            element = getattr(other, "element")
        result = list(map(binary, self.element, element))
        return result

    # 3.3.1. Basic Customization

    # class constructor

    def __new__(cls, *element: Math) -> K:
        ignore(element)
        new = super().__new__(cls)
        name = repr(cls)
        index = name.rindex(FULL_STOP) + 1
        new.name = name[index:-2]
        return new

    def __init__(self, *element: Math) -> N:
        super().__init__(*element)
        self.element = [*element]

    def __del__(self) -> N:
        del self.element

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

    def __lt__(self, other: Math) -> B:
        one = float(self)
        two = float(other)
        result = one < two
        return result

    def __le__(self, other: Math) -> B:
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

    def __gt__(self, other: Math) -> B:
        one = float(self)
        two = float(other)
        result = one > two
        return result

    def __ge__(self, other: Math) -> B:
        one = float(self)
        two = float(other)
        result = one >= two
        return result

    # 3.3.7. Emulating container types

    def __iter__(self) -> G[Math, N, N]:
        yield from self.element

    def __reversed__(self) -> G[Math, N, N]:
        yield from reversed(self.element)

    def __contains__(self, item: Math) -> B:
        return any(item == element for element in self.element)

    # 3.3.8. Emulating numeric types

    @staticmethod
    def add(one: Math, two: Math) -> Math:
        """"""
        result = one + two
        return result

    @staticmethod
    def mul(one: Math, two: Math) -> Math:
        """"""
        result = one * two
        return result

    @staticmethod
    def sub(one: Math, two: Math) -> Math:
        """"""
        result = one - two
        return result

    @staticmethod
    def truediv(one: Math, two: Math) -> Math:
        """"""
        result = one / two
        return result

    @staticmethod
    def neg(one: Math) -> Math:
        """"""
        result = -one
        return result

    @staticmethod
    def pos(one: Math) -> Math:
        """"""
        result = +one
        return result

    # binary arithmetic operations

    def _arithmetic(self, other: Math, binary: Binary) -> K:
        element = self.binary(binary, other)
        return self.make(*element)

    def __add__(self, other: Math) -> K:
        return self._arithmetic(other, self.add)

    def __mul__(self, other: Math) -> K:
        return self._arithmetic(other, self.mul)

    def __sub__(self, other: Math) -> K:
        return self._arithmetic(other, self.sub)

    def __truediv__(self, other: Math) -> K:
        return self._arithmetic(other, self.truediv)

    # binary arithmetic operations with reflected operands

    def __radd__(self, other: Math) -> K:
        return self._arithmetic(other, self.add)

    def __rmul__(self, other: Math) -> K:
        return self._arithmetic(other, self.mul)

    def __rsub__(self, other: Math) -> K:
        return self._arithmetic(other, self.sub)

    def __rtruediv__(self, other: Math) -> K:
        return self.__truediv__(other)

    # augmented arithmetic assignments

    def _augmented(self, other: Math, binary: Binary) -> K:
        self.element = self.binary(binary, other)
        return self

    def __iadd__(self, other: Math) -> K:
        return self._augmented(other, self.add)

    def __imul__(self, other: Math) -> K:
        return self._augmented(other, self.mul)

    def __isub__(self, other: Math) -> K:
        return self._augmented(other, self.sub)

    def __itruediv__(self, other: Math) -> K:
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


class Monad[X](Cardinal):
    """"""

    __slots__ = ["one"]

    one: X

    @property
    @override
    def data(self) -> L[X]:
        """"""
        return [self.one]

    @override
    def _del(self) -> N:
        del self.one

    @override
    def _get(self) -> L[X]:
        return [
            self.one,
        ]

    @override
    def _set(self, value: L[X]) -> N:
        self.one = value[0]

    element = property(_get, _set, _del)

    def __init__(self, one: X) -> N:
        super().__init__(one)
        self.one = one


class Dyad[X](Cardinal):
    """"""

    __slots__ = ["one", "two"]

    one: X
    two: X

    @property
    @override
    def data(self) -> L[X]:
        """"""
        return [self.one, self.two]

    @override
    def _del(self) -> N:
        del self.one
        del self.two

    @override
    def _get(self) -> L[X]:
        return [
            self.one,
            self.two,
        ]

    @override
    def _set(self, value: L[X]) -> N:
        self.one = value[0]
        self.two = value[1]

    element = property(_get, _set, _del)

    def __init__(self, one: X, two: X) -> N:
        super().__init__(one, two)
        self.one = one
        self.two = two


class Triad[X](Object):
    """"""

    __slots__ = ["one", "two", "tri"]

    one: X
    two: X
    tri: X

    @property
    @override
    def data(self) -> L[X]:
        """"""
        return [self.one, self.two, self.tri]

    @override
    def _del(self) -> N:
        del self.one
        del self.two
        del self.tri

    @override
    def _get(self) -> L[X]:
        return [
            self.one,
            self.two,
            self.tri,
        ]

    @override
    def _set(self, value: L[X]) -> N:
        self.one = value[0]
        self.two = value[1]
        self.tri = value[2]

    element = property(_get, _set, _del)

    def __init__(self, one: X, two: X, tri: X) -> N:
        super().__init__(one, two, tri)
        self.one = one
        self.two = two
        self.tri = tri


class Tetrad[X](Cardinal[Math]):
    """"""

    __slots__ = ["one", "two", "tri", "tet"]

    one: X
    two: X
    tri: X
    tet: X

    @property
    @override
    def data(self) -> L[X]:
        """"""
        return [self.one, self.two, self.tri, self.tet]

    @override
    def _del(self) -> N:
        del self.one
        del self.two
        del self.tri
        del self.tet

    @override
    def _get(self) -> L[X]:
        return [
            self.one,
            self.two,
            self.tri,
            self.tet,
        ]

    @override
    def _set(self, value: L[X]) -> N:
        self.one = value[0]
        self.two = value[1]
        self.tri = value[2]
        self.tet = value[3]

    element = property(_get, _set, _del)

    def __init__(self, one: X, two: X, tri: X, tet: X) -> N:
        super().__init__(one, two, tri, tet)
        self.one = one
        self.two = two
        self.tri = tri
        self.tet = tet


#    def __new__(cls, one: Math, two: Math, tri: Math, tet: Math) -> K:
#        return super().__new__(cls, one, two, tri, tet)
