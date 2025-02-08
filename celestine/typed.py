"""
Define types here.

Generator[YieldType, SendType, ReturnType]

A: typing.Any
B: bool
C: collections.abc.Callable  # Callable[[int], str]
D: typing.Dict
E: typing.Any  # Unused  # Enum?
F: float
G: collections.abc.Generator
H: typing.Any  # Unused  # Hash?
I: typing.Any  # Ambiguous variable name.
J: object
K: typing.Self
L: typing.List
M: types.ModuleType
N: None
O: typing.Any  # Ambiguous variable name.
P: pathlib.Path
Q: collections.abc.Sequence
R: typing.Any  # Future star type.
S: str
T: typing.Tuple
U: typing.Any  # Unused  # Union?
V: typing.Optional  # Void like type.
W: typing.Any  # Unused  # self.data()? warp?
X: typing.TypeVar("X")  # Primary type variable.
Y: bytes
Z: int  # Set of Integers Symbol ℤ.
"""

# pylint: disable=invalid-name


import abc
from collections.abc import Callable as C
from collections.abc import Generator as G
from collections.abc import Sequence as Q
from collections.abc import Iterator as IT
from pathlib import Path as P
from types import ModuleType as M
from typing import Any as A
from typing import Dict as D
from typing import List as L
from typing import Literal
from typing import Optional as V
from typing import Protocol
from typing import Self as K
from typing import Tuple as T
from typing import Type as TY
from typing import TypedDict as TD
from typing import TypeVar as TV
from typing import (
    cast,
    override,
)


class Star(TD):
    """The global Star object."""

    # TODO: Figure out how to map this to the R type.


type B = bool
type F = float
type J = object
type N = None
type R = A
type S = str
X = TV("X")
type Y = bytes
type Z = int


type BF = Literal[False]
type BT = Literal[True]

type CA = C[..., A]
type CN = C[[N], N]

type DA = D[S, A]
type DB = D[S, B]
type DF = D[S, F]
type DM = D[S, M]
type DP = D[S, P]
type DS = D[S, S]
type DZ = D[S, Z]

type GA = G[A, N, N]
type GB = G[B, N, N]
type GF = G[F, N, N]
type GM = G[M, N, N]
type GP = G[P, N, N]
type GS = G[S, N, N]
type GZ = G[Z, N, N]

type LA = L[A]
type LB = L[B]
type LF = L[F]
type LM = L[M]
type LP = L[P]
type LS = L[S]
type LZ = L[Z]


type TA = T[A, ...]
type TA1 = T[A]
type TA2 = T[A, A]
type TA3 = T[A, A, A]
type TA4 = T[A, A, A, A]

type TB = T[B, ...]
type TB1 = T[B]
type TB2 = T[B, B]
type TB3 = T[B, B, B]
type TB4 = T[B, B, B, B]

type TF = T[F, ...]
type TF1 = T[F]
type TF2 = T[F, F]
type TF3 = T[F, F, F]
type TF4 = T[F, F, F, F]

type TM = T[M, ...]
type TM1 = T[M]
type TM2 = T[M, M]
type TM3 = T[M, M, M]
type TM4 = T[M, M, M, M]

type TP = T[P, ...]
type TP1 = T[P]
type TP2 = T[P, P]
type TP3 = T[P, P, P]
type TP4 = T[P, P, P, P]

type TS = T[S, ...]
type TS1 = T[S]
type TS2 = T[S, S]
type TS3 = T[S, S, S]
type TS4 = T[S, S, S, S]

type TZ = T[Z, ...]
type TZ1 = T[Z]
type TZ2 = T[Z, Z]
type TZ3 = T[Z, Z, Z]
type TZ4 = T[Z, Z, Z, Z]


type VA = V[A]
type VB = V[B]
type VF = V[F]
type VM = V[M]
type VP = V[P]
type VS = V[S]
type VZ = V[Z]


def ignore(*_: A) -> N:
    """An empty function used to hide unused variable warnings."""


def string(*iterable: S) -> S:
    """A simple utility for joining together a series of strings."""
    return "".join(iterable)


class Object(abc.ABC):
    """"""

    star: D[S, R]

    def copy(self) -> K:
        """"""
        return self.echo(self)

    @property
    def data(self) -> LA:
        """"""
        ignore(self)
        result: LA = []
        return result

    @classmethod
    def echo(cls, self: K) -> K:
        """"""
        return cls(*self.data, **self.star)

    @classmethod
    def make(cls, *data: A, **star: R) -> K:
        """"""
        return cls(*data, **star)

    def pull(self, name: S, _cast: TY[A] = str, default: A = None) -> A:
        """Extracts keyword arguments from star object and returns."""
        try:
            pop = self.star.pop(name)
            value = _cast(pop)
        except KeyError:
            value = default
        return value

    def warp(self, name: S, _cast: TY[A] = str, default: A = None) -> N:
        """Extracts keyword arguments from star object and saves."""
        try:
            pop = self.star.pop(name)
            value = _cast(pop)
        except KeyError:
            value = default
        setattr(self, name, value)

    def __init__(self, *data: A, **star: R) -> N:
        ignore(self, data)
        super().__init__()
        self.star = star


class Struct:
    """"""

    __slots__: TS = ()

    def copy(self) -> K:
        """"""
        data = self.data
        result = self.__class__(*data)
        return result

    @classmethod
    def echo(cls, self: K) -> K:
        """"""
        data = self.data
        result = cls(*data)
        return result

    @classmethod
    def make(cls, *data: A) -> K:
        """"""
        result = cls(*data)
        return result

    def _del(self) -> N:
        ignore(self)

    def _get(self) -> TA:
        ignore(self)
        return ()

    def _set(self, value: TA) -> N:
        ignore(self, value)

    def __del__(self) -> N:
        del self.data

    def __init__(self, *data: A) -> N:
        ignore(self)
        self.data = data

    def __iter__(self) -> GA:
        yield from self.data

    def __reversed__(self) -> GA:
        yield from reversed(self.data)

    data = property(_get, _set, _del)


ignore(IT, Protocol, Q, cast, override)
