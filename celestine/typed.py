"""
Define types here.

Generator[YieldType, SendType, ReturnType]

A: typing.Any
B: bool
C: collections.abc.Callable
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
Q: typing.Any  # Unused  # Queue? Sequence?
R: typing.Any  # Future star type.
S: str
T: typing.Tuple
U: typing.Any  # Unused  # Union?
V: typing.Optional  # Void like type.
W: T[A, ...]  # Self data for __init__ call.
X: typing.Type  # Primary type variable.
Y: typing.Type  # Secondary type variable.
Z: int  # Set of Integers Symbol ℤ.
"""

import abc
import io
from collections.abc import Callable as C
from collections.abc import Generator as G
from collections.abc import Iterator as IT
from pathlib import Path as P
from types import ModuleType as M
from typing import Any as A
from typing import Dict as D
from typing import List as L
from typing import Literal
from typing import Optional as V
from typing import Self as K
from typing import Tuple as T
from typing import Type as TY
from typing import TypedDict as TD
from typing import override


class R(TD):
    """The global Star object."""

    # TODO: Figure out how to map this to the R type.


type W = T[A, ...]

type B = bool
type F = float
type J = object
type N = None
type S = str
type Z = int

type BF = Literal[False]
type BT = Literal[True]

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

type VA = V[A]
type VB = V[B]
type VF = V[F]
type VM = V[M]
type VP = V[P]
type VS = V[S]
type VZ = V[Z]

type TZ2 = T[Z, Z]
type TZ3 = T[Z, Z, Z]


def ignore(_: A) -> N:
    """An empty function used to hide unused variable warnings."""


def string(*characters: S) -> S:
    """A simple utility for joining together a series of strings."""
    buffer = io.StringIO()
    for character in characters:
        buffer.write(character)
    value = buffer.getvalue()
    return value


class Object(abc.ABC):
    """"""

    star: D[S, R]

    @property
    def data(self) -> W:
        """"""
        ignore(self)
        result: W = ()
        return result

    def copy(self) -> K:
        """"""
        return self.echo(self)

    @classmethod
    def echo(cls, self: K) -> K:
        """"""
        return cls(*self.data, **self.star)

    @classmethod
    def make(cls, *data: A, **star: R) -> K:
        """"""
        return cls(*data, **star)

    def pull(self, name: S, cast: TY[A] = str, default: A = None) -> A:
        """Extracts keyword arguments from star object and returns."""
        try:
            pop = self.star.pop(name)
            value = cast(pop)
        except KeyError:
            value = default
        return value

    def warp(self, name: S, cast: TY[A] = str, default: A = None) -> N:
        """Extracts keyword arguments from star object and saves."""
        try:
            pop = self.star.pop(name)
            value = cast(pop)
        except KeyError:
            value = default
        setattr(self, name, value)

    def __init__(self, *data: A, **star: R) -> N:
        super().__init__()
        ignore(self)
        ignore(data)
        self.star = star


class _Override:
    """"""

    def _override(self) -> K:
        """"""
        return self


class _Typing(_Override):
    """Hides all the "unused-import" erros."""

    @staticmethod
    def _iterator() -> IT[A]:
        return iter([])

    @override
    def _override(self) -> K:
        """"""
        return self


_Typing()
