""""""

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
    W,
    Z,
    ignore,
    override,
)

type Math = typing.Union["Cardinal", F, Z]
type Unary = C[[Math], Math]
type Binary = C[[Math, Math], Math]


class Cardinal(Object):
    """"""

    element: L[Math]
    name: S

    @property
    @override
    def data(self) -> W:
        """"""
        return tuple(self.element)

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


class Monad(Cardinal):
    """"""

    @property
    def one(self) -> Math:
        """"""
        return self.element[0]

    def __new__(cls, one: Math) -> K:
        return super().__new__(cls, one)

    def __init__(self, one: Math) -> N:
        ignore(self)
        super().__init__(one)


class Dyad(Cardinal):
    """"""

    @property
    def one(self) -> Math:
        """"""
        return self.element[0]

    @property
    def two(self) -> Math:
        """"""
        return self.element[1]

    def __new__(cls, one: Math, two: Math) -> K:
        return super().__new__(cls, one, two)

    def __init__(self, one: Math, two: Math) -> N:
        ignore(self)
        super().__init__(one, two)


class Triad(Cardinal):
    """"""

    @property
    def one(self) -> Math:
        """"""
        return self.element[0]

    @property
    def two(self) -> Math:
        """"""
        return self.element[1]

    @property
    def tri(self) -> Math:
        """"""
        return self.element[2]

    def __new__(cls, one: Math, two: Math, tri: Math) -> K:
        return super().__new__(cls, one, two, tri)

    def __init__(self, one: Math, two: Math, tri: Math) -> N:
        ignore(self)
        super().__init__(one, two, tri)


class Tetrad(Cardinal):
    """"""

    @property
    def one(self) -> Math:
        """"""
        return self.element[0]

    @property
    def two(self) -> Math:
        """"""
        return self.element[1]

    @property
    def tri(self) -> Math:
        """"""
        return self.element[2]

    @property
    def tet(self) -> Math:
        """"""
        return self.element[3]

    def __new__(cls, one: Math, two: Math, tri: Math, tet: Math) -> K:
        return super().__new__(cls, one, two, tri, tet)

    def __init__(self, one: Math, two: Math, tri: Math, tet: Math) -> N:
        ignore(self)
        super().__init__(one, two, tri, tet)
