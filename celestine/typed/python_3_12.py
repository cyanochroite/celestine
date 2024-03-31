""""""

import collections.abc
import io
import lzma
import pathlib
import types
import typing
from collections.abc import Callable as C
from collections.abc import Generator as G
from typing import Dict as D
from typing import List as L
from typing import Optional as O
from typing import Self as K
from typing import Tuple as T
from typing import Type as TYPE
from typing import override

type Argument = typing.Any  # Import the real one.

type A = typing.Any
type B = bool
# type C = collections.abc.Callable
# type D = typing.Dict
type E = typing.Any  # Unused.  # ENUM?
type F = float
# Generator[YieldType, SendType, ReturnType]
# type G = collections.abc.Generator
type H = typing.Any  # Unused
type I = int
type J = object
# type K = typing.Self
# type L = typing.List
type M = types.ModuleType
type N = None
# type O = typing.Optional
type P = pathlib.Path
type Q = typing.Any  # Unused.  # Queue?
type R = typing.Any  # **star
type S = str
# type T = typing.Tuple
type U = typing.Any  # Unused.
type V = typing.Any  # Unused.
type W = typing.Any  # Unused.
type X = typing.Any  # Unused.
type Y = typing.Any  # Unused.
type Z = typing.Any  # Unused.

type GB = G[B, N, N]
type GF = G[F, N, N]
type GI = G[I, N, N]
type GP = G[P, N, N]
type GS = G[S, N, N]

type OB = O[B]
type OF = O[F]
type OI = O[I]
type OP = O[P]
type OS = O[S]

type LB = L[B]
type LF = L[F]
type LI = L[I]
type LP = L[P]
type LS = L[S]

type PATH = P | S

type FN = C[[N], N]
type AXIS = G[T[I, I], N, N]
type FILE = typing.IO[A]
type AT = D[S, A]
# type TYPE[X] = typing.Type
type IMAGE = A
type APD = D[A, A]
type LZMA = lzma.LZMAFile
type TABLE = D[S, S]
type BOX = T[I, I, I, I]
type PAIR = T[I, I]
type AD = D[S, Argument]  # session.argument
type AI = collections.abc.Iterable[T[S, Argument]]  # session.argument


def string(*characters: S) -> S:
    """"""
    buffer = io.StringIO()
    for character in characters:
        buffer.write(character)
    value = buffer.getvalue()
    return value


class Star(typing.TypedDict):
    """"""


class Fix:
    """"""

    def override(self) -> N:
        """"""


class ImportNotUsed(Fix):
    """"""

    @override
    def override(self) -> N:
        print(override)

    def self(self) -> K:
        """"""
        return self

    @staticmethod
    def type_() -> TYPE[int]:
        """"""
        return int
