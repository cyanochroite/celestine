"""
Define types here.

Generator[YieldType, SendType, ReturnType]
"""

# TODO: Replace all this with 'type' after python 3.12 and mypy support.

import io
import pathlib
import types
import typing
from collections.abc import Callable as C
from collections.abc import Generator as G
from typing import Dict as D
from typing import Iterator as IT
from typing import List as L
from typing import Literal
from typing import Optional as V
from typing import Self as K
from typing import Tuple as T
from typing import Type as TY


class Star(typing.TypedDict):
    """The global Star object."""

    # TODO: Figure out how to map this to the R type.


type A = typing.Any
type B = bool
# type C = collections.abc.Callable
# type D = typing.Dict
# type E = typing.Any  # Unused # Enum?
type F = float
# type G = collections.abc.Generator
# type H = typing.Any  # Unused
# type I = typing.Any  # Ambiguous variable name.
type J = object
# type K = typing.Self
# type L = typing.List
type M = types.ModuleType
type N = None
# type O = typing.Any  # Ambiguous variable name.
type P = pathlib.Path
# type Q = typing.Any  # Unused
type R = typing.Any  # Future star type.
type S = str
# type T = typing.Tuple
# type U = typing.Any  # Unused  # Union?
# type V = typing.Optional  # Void like type.
# type W = typing.Any  # Unused
# type X = typing.Type  # Primary type variable.
# type Y = typing.Type  # Secondary type variable.
type Z = int  # Set of Integers Symbol ℤ.

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


def override(function: A) -> A:
    """Used so earlier Python wont fail when using @override."""
    # TODO: Remove this once we drop Python 3.11.
    # Also, nothing seems to support this, so keeping it in for now.
    return function


def string(*characters: S) -> S:
    """A simple utility for joining together a series of strings."""
    buffer = io.StringIO()
    for character in characters:
        buffer.write(character)
    value = buffer.getvalue()
    return value


class _Typing:
    """Hides all the "unused-import" erros."""

    @staticmethod
    def _iterator() -> IT[A]:
        return iter([])

    def _self(self) -> K:
        """"""
        return self

    @staticmethod
    def _tuple() -> T[Z, Z]:
        return (0, 0)

    @staticmethod
    def _type() -> TY[A]:
        return str


_Typing()
