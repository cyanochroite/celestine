"""
Define types here.

Generator[YieldType, SendType, ReturnType]
"""

import collections.abc
import pathlib
import types
import typing
from typing import Self as K
from typing import override

type X = typing.Any
type Y = typing.Any
type Z = typing.Any

type A = typing.Any
type B = bool
type C[X] = collections.abc.Callable[..., X]
type D[X, Y] = typing.Dict[X, Y]
# type E = 0 enum?
type F = float
type G[X, Y, Z] = collections.abc.Generator[X, Y, Z]
# type H = 0 hash?
type I = int
type J = object
# type K = typing.Self  # "Self" is not valid in this context.
type L[X] = typing.List[X]
type M = types.ModuleType
type N = None
type O[X] = typing.Optional[X]
type P = pathlib.Path
# type Q = 0
# type R = 0
type S = str
type T[X] = typing.Tuple[X]
# type U = 0
# type V = 0
# type W = 0


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


class Fix:
    """"""

    def override(self) -> N:
        pass


class ImportNotUsed(Fix):
    """"""

    @override
    def override(self) -> N:
        pass

    def self(self) -> K:
        return self
