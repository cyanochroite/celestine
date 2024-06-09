"""
Define types here.

Generator[YieldType, SendType, ReturnType]
"""

# TODO: Replace all this with 'type' after python 3.12 and mypy support.

import collections.abc
import io
import lzma
import pathlib
import sys
import types
import typing
from collections.abc import Callable as C
from collections.abc import Generator as G
from collections.abc import Sequence
from importlib.machinery import ModuleSpec
from typing import Dict as D
from typing import List as L
from typing import Literal
from typing import Optional as V  # Void.
from typing import Tuple as T
from typing import Type as TYPE
from typing import TypeAlias as TA

_version = sys.version.split(".")
_major = _version[0]
_minor = _version[1]

if _major == "3" and _minor == "10":
    K: TA = typing.Any  # Python 3.10 fix.
else:
    from typing import Self as K

A: TA = typing.Any
B: TA = bool
# C: TA = collections.abc.Callable
# D: TA = typing.Dict
# E: TA = typing.Any  # Unused
F: TA = float
# G: TA = collections.abc.Generator
# H: TA = typing.Any  # Unused
# I: TA = typing.Any  # Ambiguous variable name.
J: TA = object
# K: TA = typing.Self  # "Self" is not valid in this context.
# L: TA = typing.List
M: TA = types.ModuleType
N: TA = None
# O: TA = typing.Any  # Ambiguous variable name.
P: TA = pathlib.Path
# Q: TA = typing.Any  # Unused
R: TA = typing.Any  # Star.
S: TA = str
# T: TA = typing.Tuple
# U: TA = typing.Any  # Unused  # Union?
# V: TA = typing.Any  # Unused
# W: TA = typing.Any  # Unused
# X: TA = typing.Any  # Unused
# Y: TA = typing.Any  # Unused
Z: TA = int

# E: TA = typing.Any
# H: TA = typing.Any  # Unused
# Q: TA = typing.Any  # Unused
# R: TA = typing.Any  # Unused
# U: TA = typing.Any  # Unused
# V: TA = typing.Any  # Unused
# W: TA = typing.Any  # Unused
# X: TA = typing.Any  # Unused
# Y: TA = typing.Any  # Unused


BF: Literal[False]
BT: Literal[True]

CN: TA = C[[N], N]

DB: TA = D[S, B]
DF: TA = D[S, F]
DM: TA = D[S, M]
DP: TA = D[S, P]
DS: TA = D[S, S]
DZ: TA = D[S, Z]

GB: TA = G[B, N, N]
GF: TA = G[F, N, N]
GM: TA = G[M, N, N]
GP: TA = G[P, N, N]
GS: TA = G[S, N, N]
GZ: TA = G[Z, N, N]

LB: TA = L[B]
LF: TA = L[F]
LM: TA = L[M]
LP: TA = L[P]
LS: TA = L[S]
LZ: TA = L[Z]

VB: TA = V[B]
VF: TA = V[F]
VM: TA = V[M]
VP: TA = V[P]
VS: TA = V[S]
VZ: TA = V[Z]


PATH: TA = P | S

AXIS: TA = G[T[Z, Z], N, N]
FILE: TA = typing.IO[A]
AT: TA = D[S, A]
# TYPE: TA = typing.Type
IMAGE: TA = A
APD: TA = D[A, A]
LZMA: TA = lzma.LZMAFile | typing.TextIO
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
