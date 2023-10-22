"""
Define types here.

Generator[YieldType, SendType, ReturnType]
"""

import typing
import types
import collections.abc
import lzma
import pathlib
from collections.abc import Iterable as IT
from typing import IO
from typing import Self as SELF
from typing import TextIO
from typing import TypeAlias as TA
from typing import override
import types
import typing
from typing import (
    IO,
    TextIO,
    override,
)

type OBJ = object
type hd = D[S, A]


type A = typing.Any
type B = bool
type C[X] = collections.abc.Callable
type D[X] = typing.Dict
# type E = 0 enum?
type F = float
type G[X] = collections.abc.Generator
# type H = 0 hash?
type I = int  # Ambiguous variable name.
# type J = 0
# type K = 0
type L[X] = typing.List
type M = types.ModuleType
type N = None
type O = typing.Optional  # Ambiguous variable name.
type P = pathlib.Path
# type Q = 0
# type R = 0
type S = str
type T[X] = typing.Tuple
# type U = 0
# type V = 0
# type W = 0
# type X = 0
type Y[X] = typing.Type
# type Z = 0


type OB = O[B]
type OF = O[F]
type OP = O[P]
type OS = O[S]
type OI = O[I]

type LB = L[B]
type LF = L[F]
type LP = L[P]
type LS = L[S]
type LI = L[I]

class Ignore:
    """"""

    _callable: C
    _generator: G
    _iterable: IT
    _dict: D
    _self: SELF
    _tuple: T
    _type: Y


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

    @override
    def ignore(self):
        pass


R = Ring  # noqa: F401 pylint: disable=W0611

type FILE = IO[A]
type LZMA = lzma.LZMAFile | TextIO
type TEXT = G[S, N, N]
