"""
Define types here.

Generator[YieldType, SendType, ReturnType]
"""

import collections.abc
import lzma
import pathlib
import types
import typing
from typing import TypeAlias as TA

A: TA = typing.Any
B: TA = bool
C: TA = collections.abc.Callable
D: TA = typing.Dict
E: TA = 0
F: TA = float
G: TA = collections.abc.Generator
H: TA = 0
I: TA = int
J: TA = object
K: TA = typing.Any  # Python 3.10 fix.
L: TA = typing.List
M: TA = types.ModuleType
N: TA = None
O: TA = typing.Optional
P: TA = pathlib.Path
Q: TA = 0
R: TA = 0
S: TA = str
T: TA = typing.Tuple
U: TA = 0
V: TA = 0
W: TA = 0
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
TYPE: TA = typing.Type
IMAGE: TA = A
APD: TA = D[A, A]
LZMA: TA = lzma.LZMAFile
TABLE: TA = D[S, S]
BOX: TA = T[I, I, I, I]
PAIR: TA = T[I, I]
AD: TA = D[S, A]
AI: TA = collections.abc.Iterable[T[S, A]]


def override(function):
    return function


SELF: TA = A


class Ring:
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

    _queue: L[T[C[N], A, A]]

    def queue(self, call: C[N], action: A, argument: A) -> N:
        """Add to event queue and call function at end of update."""
        self._queue.append((call, action, argument))

    def dequeue(self) -> N:
        """"""
        for call, action, argument in self._queue:
            call(action, **argument)
        self._queue = []

    def __init__(self) -> N:
        self._queue = []


R = Ring  # noqa: F401 pylint: disable=W0611


class ImportNotUsed:
    """"""

    def self(self) -> K:
        return self
