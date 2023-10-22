"""
Define types here.

Generator[YieldType, SendType, ReturnType]
"""

import collections.abc
import pathlib
import types
import typing
from typing import override

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

type A = typing.Any
type M = types.ModuleType

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


R = Ring  # noqa: F401 pylint: disable=W0611

type SELF = typing.Self


class ImportNotUsedFix:
    """"""

    @override
    def override(self):
        pass
