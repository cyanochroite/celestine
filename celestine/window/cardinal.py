""""""
from typing import Mapping

from celestine.typed import (
    GF,
    LF,
    B,
    C,
    F,
    K,
    N,
    T,
    Z,
)

# monad
# dyad
# triad
# tetrad

# 1	monad
# 2	dyad
# 3	triad
# 4	tetrad
# 5	pentad
# 6	hexad

# 7	heptad, hebdomad
# 8	octad, ogdoad
# 9	nonad, ennead
# 10	decad, decade
# 11	hendecad
# 12	dodecad, duodecade	dozen
# 1000	chiliad

# Monad
# Dyad
# Triad
# Tetrad
# Pentad
# Hexad


class Cardinal:
    """"""

    element: LF

    @staticmethod
    def add(one: F, two: F) -> F:
        """"""
        return one + two

    def math(self, function, other: F | K | Z) -> LF:
        """Do math stuff."""
        if isinstance(other, float | int):
            element = [other] * len(self.element)
        else:
            element = other.element
        result = list(map(function, self.element, element))
        return result

    @staticmethod
    def mul(one: F, two: F) -> F:
        """"""
        return one + two

    @staticmethod
    def sub(one: F, two: F) -> F:
        """"""
        return one + two

    @staticmethod
    def truediv(one: F, two: F) -> F:
        """"""
        return one + two

    def __init__(self, element: LF) -> N:
        self.element = element

    def __add__(self, other: F | K | Z) -> K:
        value = self.math(self.add, other)
        return type(self)(value)

    def __mul__(self, other: F | K | Z) -> K:
        value = self.math(self.mul, other)
        return type(self)(value)

    def __sub__(self, other: F | K | Z) -> K:
        value = self.math(self.sub, other)
        return type(self)(value)

    def __truediv__(self, other: F | K | Z) -> K:
        value = self.math(self.truediv, other)
        return type(self)(value)

    def __iadd__(self, other: F | K) -> K:
        self.value += self._other(other)
        return self

    def __imul__(self, other: K) -> K:
        self.value *= other.value
        return self

    def __isub__(self, other: K) -> K:
        self.value -= other.value
        return self

    def __itruediv__(self, other: K) -> K:
        self.value /= other.value
        return self

    ###

    def __add__(self, other: F | K) -> K:
        def function(a, b):
            return a + b
        car = map(function, self.element, other.elements, [1, 2, 3])
        return list(car)
        return self

    def __repr__(self):
        return f"Monad({repr(self.value)})"

    def __str__(self):
        return f"({str(self.value)})"

    ###

    def __iadd__(self, other: F | K) -> K:
        self.value += self._other(other)
        return self

    def __imul__(self, other: K) -> K:
        self.value *= other.value
        return self

    def __isub__(self, other: K) -> K:
        self.value -= other.value
        return self

    def __itruediv__(self, other: K) -> K:
        self.value /= other.value
        return self

    ###

    @staticmethod
    def _other(other: F | K) -> K:
        return other if isinstance(other, F) else other.value


class Monad(Cardinal):
    pass


class Dyad(Cardinal):
    """"""

    _one: F
    _two: F

    @property
    def one(self) -> F:
        """"""
        return self._one

    @property
    def two(self) -> F:
        """"""
        return self._two

    @property
    def value(self) -> T[Z, Z]:
        """"""
        return (int(self._one), int(self._two))

###

    @classmethod
    def clone(cls, self: K) -> K:
        """"""
        return cls(self._one, self._two)

    def copy(self) -> K:
        """"""
        return self.clone(self)

    @property
    def length(self) -> Z:
        """"""
        return self._two - self._one

    @property
    def midpoint(self) -> Z:
        """"""
        return (self._one + self._two) // 2

###

    @staticmethod
    def _add(one: F, two: F) -> F:
        return one + two

    @staticmethod
    def _mul(one: F, two: F) -> F:
        return one * two

    @staticmethod
    def _sub(one: F, two: F) -> F:
        return one - two

    @staticmethod
    def _truediv(one: F, two: F) -> F:
        return one / two

    def math(self, function: C[[K, F | K], K], other: F | K) -> T[F, F]:
        """Do math stuff."""
        if isinstance(other, F):
            one = function(self._one, other)
            two = function(self._one, other)
        else:
            one = function(self._one, other._one)
            two = function(self._one, other._two)
        return one, two

    def __add__(self, other: F | K) -> K:
        one, two = self.math(self._add, other)
        return type(self)(one, two)

    ##
    def __contains__(self, item: Z) -> B:
        return self.minimum <= item <= self.maximum

    def __iadd__(self, other: F | K) -> K:
        self._one += other
        self._two += other
        return self

    def __imul__(self, other: F) -> K:
        self._one *= other
        self._two *= other
        return self

    def __init__(self, _one: F, _two: F) -> N:
        self._one = _one
        self._two = _two
        self.minimum = min(_one, _two)
        self.maximum = max(_one, _two)

    def __isub__(self, other: F) -> K:
        self._one -= other
        self._two -= other
        return self

    def __iter__(self) -> GF:
        yield self._one
        yield self._two

    def __itruediv__(self, other: F) -> K:
        self._one /= other
        self._two /= other
        return self

    def __mul__(self, other: K) -> K:
        one = self._one * other._one
        two = self._two * other._two
        return type(self)(one, two)

    def __repr__(self):
        return f"Dyad({repr(self._one)}, {repr(self._two)})"

    def __str__(self):
        return f"({str(self._one)}, {str(self._two)})"

    def __sub__(self, other: K) -> K:
        one = self._one - other._one
        two = self._two - other._two
        return type(self)(one, two)

    def __truediv__(self, other: K) -> K:
        one = self._one / other._one
        two = self._two / other._two
        return type(self)(one, two)
