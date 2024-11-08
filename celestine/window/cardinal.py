""""""

# pylint: disable=undefined-variable

import math
import typing

from celestine.typed import (
    B,
    C,
    F,
    G,
    K,
    L,
    N,
)


class Float(typing.Protocol):
    """"""

    def __add__(self, other: K) -> K:
        raise NotImplementedError(self, other)

    def __float__(self) -> F:
        raise NotImplementedError(self)

    def __mul__(self, other: K) -> K:
        raise NotImplementedError(self, other)

    def __neg__(self) -> K:
        raise NotImplementedError(self)

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


class Cardinal:
    """"""

    def unary(self, unary: Unary) -> L[Float]:
        """Unary arithmetic operations."""
        result = list(map(unary, self.data))
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

    # 3.3.1. Basic Customization

    # string representation of an object

    def __repr__(self):
        data = ", ".join(map(repr, self.data))
        result = f"{self.name}({data})"
        return result

    def __str__(self):
        data = ", ".join(map(str, self.data))
        result = f"({data})"
        return result

    #  rich comparison methods

    def __lt__(self, other: Float) -> B:
        one = float(self)
        two = float(other)
        result = one < two
        return result

    def __le__(self, other: Float) -> B:
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

    def __gt__(self, other: Float) -> B:
        one = float(self)
        two = float(other)
        result = one > two
        return result

    def __ge__(self, other: Float) -> B:
        one = float(self)
        two = float(other)
        result = one >= two
        return result

    # 3.3.7. Emulating container types

    def __iter__(self) -> G[Float, N, N]:
        yield from self.data

    def __reversed__(self) -> G[Float, N, N]:
        yield from reversed(self.data)

    def __contains__(self, item: Float) -> B:
        return any(item == data for data in self.data)

    # binary arithmetic operations

    def _arithmetic(self, other: Float, binary: Binary) -> K:
        data = self.binary(binary, other)
        return self.make(*data)

    def __add__(self, other: Float) -> K:
        return self._arithmetic(other, Math.add)

    def __mul__(self, other: Float) -> K:
        return self._arithmetic(other, Math.mul)

    def __sub__(self, other: Float) -> K:
        return self._arithmetic(other, Math.sub)

    def __truediv__(self, other: Float) -> K:
        return self._arithmetic(other, Math.truediv)

    # binary arithmetic operations with reflected operands

    def __radd__(self, other: Float) -> K:
        return self._arithmetic(other, Math.add)

    def __rmul__(self, other: Float) -> K:
        return self._arithmetic(other, Math.mul)

    def __rsub__(self, other: Float) -> K:
        return self._arithmetic(other, Math.sub)

    def __rtruediv__(self, other: Float) -> K:
        return self.__truediv__(other)

    # augmented arithmetic assignments

    def _augmented(self, other: Float, binary: Binary) -> K:
        self.data = self.binary(binary, other)
        return self

    def __iadd__(self, other: Float) -> K:
        return self._augmented(other, Math.add)

    def __imul__(self, other: Float) -> K:
        return self._augmented(other, Math.mul)

    def __isub__(self, other: Float) -> K:
        return self._augmented(other, Math.sub)

    def __itruediv__(self, other: Float) -> K:
        return self._augmented(other, Math.truediv)

    # unary arithmetic operations

    def __neg__(self) -> K:
        self.data = self.unary(Math.neg)
        return self

    def __pos__(self) -> K:
        self.data = self.unary(Math.pos)
        return self

    def __float__(self) -> F:
        data = map(float, self.data)
        result = sum(data)
        return result
