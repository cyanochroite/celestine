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
from typing import Dict as D
from typing import List as L
from typing import Optional as O
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
# H: TA = Hold
I: TA = int
J: TA = object
K: TA = typing.Any  # Python 3.10 fix.
# L: TA = typing.List
M: TA = types.ModuleType
N: TA = None
# O: TA = typing.Optional
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
Z: TA = typing.Any

GB: TA = G[B, N, N]
GF: TA = G[F, N, N]
GI: TA = G[I, N, N]
GP: TA = G[P, N, N]
GS: TA = G[S, N, N]

OB: TA = O[B]
OF: TA = O[F]
OI: TA = O[I]
OP: TA = O[P]
OS: TA = O[S]

LB: TA = L[B]
LF: TA = L[F]
LI: TA = L[I]
LP: TA = L[P]
LS: TA = L[S]


FN: TA = C[[N], N]
AXIS: TA = G[T[I, I], N, N]
FILE: TA = typing.IO[A]
AT: TA = D[S, A]
# TYPE: TA = typing.Type
IMAGE: TA = A
APD: TA = D[A, A]
LZMA: TA = lzma.LZMAFile
TABLE: TA = D[S, S]
BOX: TA = T[I, I, I, I]
PAIR: TA = T[I, I]
AD: TA = D[S, A]
AI: TA = collections.abc.Iterable[T[S, A]]


def override(function: A) -> A:
    return function


def string(*characters: S) -> S:
    """"""
    buffer = io.StringIO()
    for character in characters:
        buffer.write(character)
    value = buffer.getvalue()
    return value


SELF: TA = A


class Star(typing.TypedDict):
    """"""


class Hold:
    """"""

    application: M
    attribute: LS
    code: M
    interface: M
    language: M
    main: S
    package: M
    view: M
    window: M

    _queue: L[T[C[..., N], A, A]]

    def queue(self, call: C[..., N], action: A, argument: A) -> N:
        """Add to event queue and call function at end of update."""
        self._queue.append((call, action, argument))

    def dequeue(self) -> N:
        """"""
        for call, action, argument in self._queue:
            call(action, **argument)
        self._queue = []

    def __init__(self) -> N:
        self._queue = []


H = Hold  # noqa: F401 pylint: disable=W0611


class ImportNotUsed:
    """"""

    def self(self) -> K:
        return self

    def type_(self) -> TYPE[int]:
        return int
