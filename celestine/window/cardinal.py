""""""

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
    S,
    Z,
    ignore,
)

Math: typing.TypeAlias = F | K | Z
Function: typing.TypeAlias = C[[Math, Math], Math]


class Cardinal:
    """"""

    element: L[Math]
    name: S

    @classmethod
    def make(cls, element: L[Math]) -> K:
        """"""
        return cls(*element)

    def math(self, function: Function, other: Math) -> L[Math]:
        """Do math stuff."""
        if isinstance(other, float | int):
            element = [other] * len(self.element)
        else:
            element = other.element
        result = list(map(function, self.element, element))
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

    # binary arithmetic operations

    def __add__(self, other: Math) -> K:
        element = self.math(self.add, other)
        return self.make(element)

    def __mul__(self, other: Math) -> K:
        element = self.math(self.mul, other)
        return self.make(element)

    def __sub__(self, other: Math) -> K:
        element = self.math(self.sub, other)
        return self.make(element)

    def __truediv__(self, other: Math) -> K:
        element = self.math(self.truediv, other)
        return self.make(element)

    # augmented arithmetic assignments

    def __iadd__(self, other: Math) -> K:
        self.element = self.math(self.add, other)
        return self

    def __imul__(self, other: Math) -> K:
        self.element = self.math(self.mul, other)
        return self

    def __isub__(self, other: Math) -> K:
        self.element = self.math(self.sub, other)
        return self

    def __itruediv__(self, other: Math) -> K:
        self.element = self.math(self.truediv, other)
        return self


class Monad(Cardinal):
    """"""

    def __new__(cls, one: Math) -> K:
        return super().__new__(cls, one)

    def __init__(self, one: Math) -> N:
        ignore(self)
        super().__init__(one)


class Dyad(Cardinal):
    """"""

    def __new__(cls, one: Math, two: Math) -> K:
        return super().__new__(cls, one, two)

    def __init__(self, one: Math, two: Math) -> N:
        ignore(self)
        super().__init__(one, two)


class Triad(Cardinal):
    """"""

    def __new__(cls, one: Math, two: Math, tri: Math) -> K:
        return super().__new__(cls, one, two, tri)

    def __init__(self, one: Math, two: Math, tri: Math) -> N:
        ignore(self)
        super().__init__(one, two, tri)


class Tetrad(Cardinal):
    """"""

    def __new__(cls, one: Math, two: Math, tri: Math, tet: Math) -> K:
        return super().__new__(cls, one, two, tri, tet)

    def __init__(self, one: Math, two: Math, tri: Math, tet: Math) -> N:
        ignore(self)
        super().__init__(one, two, tri, tet)
