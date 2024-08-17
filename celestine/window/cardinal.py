""""""

import math
import typing

from celestine.literal import FULL_STOP
from celestine.typed import (
    GF,
    LF,
    B,
    C,
    F,
    K,
    N,
    S,
    Z,
)

Other: typing.TypeAlias = F | K | Z


class Math:
    """"""

    @staticmethod
    def lt(one: F, two: F) -> B:
        """"""
        result = one < two
        return result

    @staticmethod
    def le(one: F, two: F) -> B:
        """"""
        result = one < two or math.isclose(one, two)
        return result

    @staticmethod
    def eq(one: F, two: F) -> B:
        """"""
        result = math.isclose(one, two)
        return result

    @staticmethod
    def ne(one: F, two: F) -> B:
        """"""
        result = not math.isclose(one, two)
        return result

    @staticmethod
    def gt(one: F, two: F) -> B:
        """"""
        result = one > two
        return result

    @staticmethod
    def ge(one: F, two: F) -> B:
        """"""
        result = one > two or math.isclose(one, two)
        return result

    @staticmethod
    def add(one: F, two: F) -> F:
        """"""
        result = one + two
        return result

    @staticmethod
    def mul(one: F, two: F) -> F:
        """"""
        result = one * two
        return result

    @staticmethod
    def sub(one: F, two: F) -> F:
        """"""
        result = one - two
        return result

    @staticmethod
    def truediv(one: F, two: F) -> F:
        """"""
        result = one / two
        return result


class Cardinal:
    """"""

    element: LF
    name: S

    @classmethod
    def make(cls, element: LF) -> K:
        """"""
        return cls(*element)

    def math(self, function: C[[F, F], F], other: Other) -> LF:
        """Do math stuff."""
        if isinstance(other, float | int):
            element = [other] * len(self.element)
        else:
            element = other.element
        result = list(map(function, self.element, element))
        return result

    # 3.3.1. Basic Customization

    # class constructor

    def __new__(cls, *element: F) -> K:
        new = super().__new__(cls)
        name = repr(cls)
        index = name.rindex(FULL_STOP) + 1
        new.name = name[index:-2]
        return new

    def __init__(self, *element: F) -> N:
        self.element = [*element]

    def __del__(self) -> N:
        self.element = []

    # string representation of an object

    def __repr__(self):
        result = f"{self.name}{str(self)}"
        return result

    def __str__(self):
        element = ", ".join(map(str, self.element))
        result = f"({element})"
        return result

    # rich comparison methods

    def __lt__(self, other: K) -> B:
        element = self.math(Math.lt, other)
        result = all(element)
        return result

    def __le__(self, other: K) -> B:
        element = self.math(Math.le, other)
        result = all(element)
        return result

    def __eq__(self, other: K) -> B:
        element = self.math(Math.eq, other)
        result = all(element)
        return result

    def __ne__(self, other: K) -> B:
        element = self.math(Math.ne, other)
        result = all(element)
        return result

    def __gt__(self, other: K) -> B:
        element = self.math(Math.gt, other)
        result = all(element)
        return result

    def __ge__(self, other: K) -> B:
        element = self.math(Math.ge, other)
        result = all(element)
        return result

    def __bool__(self) -> B:
        result = any(self.element)
        return result

    # 3.3.7. Emulating container types

    def __iter__(self) -> GF:
        yield from self.element

    def __reversed__(self) -> GF:
        yield from reversed(self.element)

    def __contains__(self, item: F) -> B:
        return any(item == element for element in self.element)

    # 3.3.8. Emulating numeric types

    # binary arithmetic operations

    def __add__(self, other: Other) -> K:
        element = self.math(Math.add, other)
        return self.make(element)

    def __mul__(self, other: Other) -> K:
        element = self.math(Math.mul, other)
        return self.make(element)

    def __sub__(self, other: Other) -> K:
        element = self.math(Math.sub, other)
        return self.make(element)

    def __truediv__(self, other: Other) -> K:
        element = self.math(Math.truediv, other)
        return self.make(element)

    # augmented arithmetic assignments

    def __iadd__(self, other: Other) -> K:
        self.element = self.math(Math.add, other)
        return self

    def __imul__(self, other: Other) -> K:
        self.element = self.math(Math.mul, other)
        return self

    def __isub__(self, other: Other) -> K:
        self.element = self.math(Math.sub, other)
        return self

    def __itruediv__(self, other: Other) -> K:
        self.element = self.math(Math.truediv, other)
        return self


class Monad(Cardinal):
    """"""

    def __new__(cls, one: F) -> K:
        return super().__new__(cls, one)

    def __init__(self, one: F) -> N:
        super().__init__(one)


class Dyad(Cardinal):
    """"""

    def __new__(cls, one: F, two: F) -> K:
        return super().__new__(cls, one, two)

    def __init__(self, one: F, two: F) -> N:
        super().__init__(one, two)


class Triad(Cardinal):
    """"""

    def __new__(cls, one: F, two: F, three: F) -> K:
        return super().__new__(cls, one, two, three)

    def __init__(self, one: F, two: F, three: F) -> N:
        super().__init__(one, two, three)


class Tetrad(Cardinal):
    """"""

    def __new__(cls, one: F, two: F, three: F, four: F) -> K:
        return super().__new__(cls, one, two, three, four)

    def __init__(self, one: F, two: F, three: F, four: F) -> N:
        super().__init__(one, two, three, four)
