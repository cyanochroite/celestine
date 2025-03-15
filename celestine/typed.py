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
U: typing.Union
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
from collections.abc import Iterator as IT
from collections.abc import Sequence as Q
from pathlib import Path as P
from types import ModuleType as M
from typing import Any as A
from typing import Dict as D
from typing import List as L
from typing import Literal
from typing import NotRequired as NR
from typing import Optional as V
from typing import Protocol
from typing import Self as K
from typing import Tuple as T
from typing import Type as TY
from typing import TypedDict as TD
from typing import TypeVar as TV
from typing import Union as U
from typing import Unpack as UN
from typing import TypeAlias
from typing import (
    cast,
)

ANY: TypeAlias = A
B: TypeAlias = bool
F: TypeAlias = float
J: TypeAlias = object
N: TypeAlias = None
R: TypeAlias = A
S: TypeAlias = str
X = TV("X")
Y: TypeAlias = bytes
Z: TypeAlias = int


BF: TypeAlias = Literal[False]
BT: TypeAlias = Literal[True]

CA: TypeAlias = C[..., A]
CN: TypeAlias = C[[N], N]

DA: TypeAlias = D[S, A]
DB: TypeAlias = D[S, B]
DF: TypeAlias = D[S, F]
DM: TypeAlias = D[S, M]
DP: TypeAlias = D[S, P]
DS: TypeAlias = D[S, S]
DZ: TypeAlias = D[S, Z]

GA: TypeAlias = G[A, N, N]
GB: TypeAlias = G[B, N, N]
GF: TypeAlias = G[F, N, N]
GM: TypeAlias = G[M, N, N]
GP: TypeAlias = G[P, N, N]
GS: TypeAlias = G[S, N, N]
GZ: TypeAlias = G[Z, N, N]

LA: TypeAlias = L[A]
LB: TypeAlias = L[B]
LF: TypeAlias = L[F]
LM: TypeAlias = L[M]
LP: TypeAlias = L[P]
LS: TypeAlias = L[S]
LZ: TypeAlias = L[Z]


TA: TypeAlias = T[A, ...]
TA1: TypeAlias = T[A]
TA2: TypeAlias = T[A, A]
TA3: TypeAlias = T[A, A, A]
TA4: TypeAlias = T[A, A, A, A]

TB: TypeAlias = T[B, ...]
TB1: TypeAlias = T[B]
TB2: TypeAlias = T[B, B]
TB3: TypeAlias = T[B, B, B]
TB4: TypeAlias = T[B, B, B, B]

TF: TypeAlias = T[F, ...]
TF1: TypeAlias = T[F]
TF2: TypeAlias = T[F, F]
TF3: TypeAlias = T[F, F, F]
TF4: TypeAlias = T[F, F, F, F]

TM: TypeAlias = T[M, ...]
TM1: TypeAlias = T[M]
TM2: TypeAlias = T[M, M]
TM3: TypeAlias = T[M, M, M]
TM4: TypeAlias = T[M, M, M, M]

TP: TypeAlias = T[P, ...]
TP1: TypeAlias = T[P]
TP2: TypeAlias = T[P, P]
TP3: TypeAlias = T[P, P, P]
TP4: TypeAlias = T[P, P, P, P]

TS: TypeAlias = T[S, ...]
TS1: TypeAlias = T[S]
TS2: TypeAlias = T[S, S]
TS3: TypeAlias = T[S, S, S]
TS4: TypeAlias = T[S, S, S, S]

TZ: TypeAlias = T[Z, ...]
TZ1: TypeAlias = T[Z]
TZ2: TypeAlias = T[Z, Z]
TZ3: TypeAlias = T[Z, Z, Z]
TZ4: TypeAlias = T[Z, Z, Z, Z]


VA: TypeAlias = V[A]
VB: TypeAlias = V[B]
VF: TypeAlias = V[F]
VM: TypeAlias = V[M]
VP: TypeAlias = V[P]
VS: TypeAlias = V[S]
VZ: TypeAlias = V[Z]


def override(_) -> A:
    pass


def ignore(*_: A) -> N:
    """An empty function used to hide unused variable warnings."""
    cast(ANY, _)


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

    def __init__(self, *data: A) -> N:
        ignore(self)
        self.data = data

    def __iter__(self) -> GA:
        yield from self.data

    def __reversed__(self) -> GA:
        yield from reversed(self.data)

    data = property(_get, _set, _del)


ignore(
    ANY,
    BF,
    BT,
    CA,
    cast,
    CN,
    DA,
    DB,
    DF,
    DM,
    DP,
    DS,
    DZ,
    GB,
    GF,
    GM,
    GP,
    GS,
    GZ,
    IT,
    J,
    LB,
    LF,
    LM,
    LP,
    LS,
    LZ,
    NR,
    Object,
    override,
    Protocol,
    Q,
    string,
    Struct,
    TA1,
    TA2,
    TA3,
    TA4,
    TB,
    TB1,
    TB2,
    TB3,
    TB4,
    TD,
    TF,
    TF1,
    TF2,
    TF3,
    TF4,
    TM,
    TM1,
    TM2,
    TM3,
    TM4,
    TP,
    TP1,
    TP2,
    TP3,
    TP4,
    TS1,
    TS2,
    TS3,
    TS4,
    TZ,
    TZ1,
    TZ2,
    TZ3,
    TZ4,
    U,
    UN,
    VA,
    VB,
    VF,
    VM,
    VP,
    VS,
    VZ,
    X,
    Y,
)
