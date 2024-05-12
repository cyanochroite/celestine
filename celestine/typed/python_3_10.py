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
from typing import Tuple as T
from typing import Type as TYPE
from typing import TypeAlias as TA

A: TA = typing.Any
B: TA = bool
# C: TA = collections.abc.Callable
# D: TA = typing.Dict
E: TA = typing.Any
F: TA = float
# G: TA = collections.abc.Generator
H: TA = typing.Any  # Unused
# I: TA = typing.Any  # Ambiguous variable name.
J: TA = object
K: TA = typing.Any  # Python 3.10 fix.
# L: TA = typing.List
M: TA = types.ModuleType
N: TA = None
# O: TA = typing.Any  # Ambiguous variable name.
P: TA = pathlib.Path
Q: TA = typing.Any
R: TA = typing.Any
S: TA = str
# T: TA = typing.Tuple
U: TA = typing.Any
V: TA = typing.Any
W: TA = typing.Any
X: TA = typing.Any
Y: TA = typing.Any
Z: TA = int

GB: TA = G[B, N, N]
GF: TA = G[F, N, N]
GZ: TA = G[Z, N, N]
GP: TA = G[P, N, N]
GS: TA = G[S, N, N]

OB: TA = OPT[B]
OF: TA = OPT[F]
OZ: TA = OPT[Z]
OM: TA = OPT[M]
OP: TA = OPT[P]
OS: TA = OPT[S]

LB: TA = L[B]
LF: TA = L[F]
LZ: TA = L[Z]
LP: TA = L[P]
LS: TA = L[S]


PATH: TA = P | S

FN: TA = C[[N], N]
AXIS: TA = G[T[Z, Z], N, N]
FILE: TA = typing.IO[A]
AT: TA = D[S, A]
# TYPE: TA = typing.Type
IMAGE: TA = A
APD: TA = D[A, A]
LZMA: TA = lzma.LZMAFile
TABLE: TA = D[S, S]
BOX: TA = T[Z, Z, Z, Z]
PAIR: TA = T[Z, Z]
AD: TA = D[S, A]
AI: TA = collections.abc.Iterable[T[S, A]]

SS: TA = Sequence[S] | N
MS: TA = ModuleSpec | N


def ignore(_: A) -> N:
    """"""


def override(function: A) -> A:
    """"""
    return function


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
