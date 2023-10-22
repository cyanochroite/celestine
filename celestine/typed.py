"""
Define types here.

Generator[YieldType, SendType, ReturnType]
"""

import typing
import lzma
import pathlib
from collections.abc import Callable as CA
from collections.abc import Generator as GE
from collections.abc import Iterable as IT
from types import ModuleType as MT
from typing import IO
from typing import Optional as OPT
from typing import Self as SELF
from typing import TextIO
from typing import Type as TY
from typing import TypeAlias as TA
from typing import override





type OBJ = object
type hd = D[S, A]


type A = typing.Any
type B = bool
type C = 0
type D[X] = typing.Dict
type E = 0
type F = float
type G = 0
type H = 0
# type I = typing.Any  # Ambiguous variable name.
type J = 0
type K = 0
type L[X] = typing.List
type M = 0
type N = None
# type O = 0  # Ambiguous variable name.
type P = pathlib.Path
type Q = 0
type R = 0
type S = str
type T[X] = typing.Tuple
type U = 0
type V = 0
type W = 0
# type X = 0
type Y = 0
type Z = int


type OB = OPT[B]
type OF = OPT[F]
type OP = OPT[P]
type OS = OPT[S]
type OZ = OPT[Z]

type LB = L[B]
type LF = L[F]
type LP = L[P]
type LS = L[S]
type LZ = L[Z]

class Ignore:
    """"""

    _callable: CA
    _generator: GE
    _iterable: IT
    _dict: D
    _self: SELF
    _tuple: T
    _type: TY


class Ring:
    """"""

    application: MT
    attribute: LS
    code: MT
    interface: MT
    language: MT
    main: S
    package: MT
    view: MT
    window: MT

    @override
    def ignore(self):
        pass


R = Ring  # noqa: F401 pylint: disable=W0611

type FILE = IO[A]
type LZMA = lzma.LZMAFile | TextIO
type TEXT = GE[S, N, N]






