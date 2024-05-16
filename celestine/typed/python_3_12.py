"""
Define types here.

Generator[YieldType, SendType, ReturnType]
"""

import collections.abc
import io
import lzma
import pathlib
import types
import typing
from collections.abc import Callable as C
from collections.abc import Generator as G
from collections.abc import Sequence
from importlib.machinery import ModuleSpec
from typing import Dict as D
from typing import List as L
from typing import Optional as OPT
from typing import Self as K
from typing import Tuple as T
from typing import Type as TYPE
from typing import TypeAlias as TA
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
# type I = typing.Any  # Ambiguous variable name.
type J = object
# type K = typing.Self
# type L = typing.List
type M = types.ModuleType
# type N = None
N: TA = None
# type O = typing.Any  # Ambiguous variable name.
# type O = typing.Optional # Ambiguous variable name.
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
type Z = int

type GB = G[B, N, N]
type GF = G[F, N, N]
type GZ = G[Z, N, N]
type GP = G[P, N, N]
type GS = G[S, N, N]

type OB = OPT[B]
type OF = OPT[F]
type OZ = OPT[Z]
type OM = OPT[M]
type OP = OPT[P]
type OS = OPT[S]

type LB = L[B]
type LF = L[F]
type LZ = L[Z]
type LP = L[P]
type LS = L[S]

type FN = C[[N], N]
type FB = C[[N], B]
type FF = C[[N], F]
type FZ = C[[N], Z]
type FP = C[[N], P]
type FS = C[[N], S]

type PATH = P | S

type FN = C[[N], N]
type AXIS = G[T[Z, Z], N, N]
type FILE = typing.IO[A]
type AT = D[S, A]
# type TYPE[X] = typing.Type
type IMAGE = A
type APD = D[A, A]
type LZMA = lzma.LZMAFile
type TABLE = D[S, S]
type BOX = T[Z, Z, Z, Z]
type PAIR = T[Z, Z]
type AD = D[S, Argument]  # session.argument
type AI = collections.abc.Iterable[T[S, Argument]]  # session.argument

type SS = Sequence[S] | N
type MS = ModuleSpec | N


def ignore(_: A) -> N:
    """"""


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
