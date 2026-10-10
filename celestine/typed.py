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


from collections.abc import Callable as C
from collections.abc import Generator as G
from collections.abc import Iterator as IT
from collections.abc import Sequence as Q
from contextlib import AbstractContextManager as ACM
from importlib.machinery import ModuleSpec as MS
from lzma import LZMAFile
from pathlib import Path as P
from types import ModuleType as M
from typing import (
    IO,
)
from typing import Any as A
from typing import Dict as D
from typing import List as L
from typing import (
    Literal,
)
from typing import NotRequired as NR
from typing import Optional as V
from typing import (
    Protocol,
)
from typing import Self as K
from typing import (
    TextIO,
)
from typing import Tuple as T
from typing import Type as TY
from typing import TypedDict as TD
from typing import TypeVar as TV
from typing import Union as U
from typing import Unpack as UN
from typing import (
    cast,
    override,
)

type B = bool
type F = float
type J = object
type N = None
type R = A
type S = str
X = TV("X")
type Y = bytes
type Z = int


type BF = Literal[False]
type BT = Literal[True]

type CA = C[[A], N]
type CB = C[[B], N]
type CF = C[[F], N]
type CM = C[[M], N]
type CN = C[[N], N]
type CP = C[[P], N]
type CS = C[[S], N]
type CZ = C[[Z], N]

type DA = D[S, A]
type DB = D[S, B]
type DF = D[S, F]
type DM = D[S, M]
type DN = D[S, N]
type DP = D[S, P]
type DS = D[S, S]
type DZ = D[S, Z]

type GA = G[A, N, N]
type GB = G[B, N, N]
type GF = G[F, N, N]
type GM = G[M, N, N]
type GN = G[N, N, N]
type GP = G[P, N, N]
type GS = G[S, N, N]
type GZ = G[Z, N, N]

type LA = L[A]
type LB = L[B]
type LF = L[F]
type LM = L[M]
type LN = L[N]
type LP = L[P]
type LS = L[S]
type LZ = L[Z]


type TA = T[A, ...]
type TA1 = T[A]
type TA2 = T[A, A]
type TA3 = T[A, A, A]
type TA4 = T[A, A, A, A]

type TB = T[B, ...]
type TB1 = T[B]
type TB2 = T[B, B]
type TB3 = T[B, B, B]
type TB4 = T[B, B, B, B]

type TF = T[F, ...]
type TF1 = T[F]
type TF2 = T[F, F]
type TF3 = T[F, F, F]
type TF4 = T[F, F, F, F]

type TM = T[M, ...]
type TM1 = T[M]
type TM2 = T[M, M]
type TM3 = T[M, M, M]
type TM4 = T[M, M, M, M]

type TN = T[N, ...]
type TN1 = T[N]
type TN2 = T[N, N]
type TN3 = T[N, N, N]
type TN4 = T[N, N, N, N]

type TP = T[P, ...]
type TP1 = T[P]
type TP2 = T[P, P]
type TP3 = T[P, P, P]
type TP4 = T[P, P, P, P]

type TS = T[S, ...]
type TS1 = T[S]
type TS2 = T[S, S]
type TS3 = T[S, S, S]
type TS4 = T[S, S, S, S]

type TZ = T[Z, ...]
type TZ1 = T[Z]
type TZ2 = T[Z, Z]
type TZ3 = T[Z, Z, Z]
type TZ4 = T[Z, Z, Z, Z]

type LTA = L[TA]
type LTA1 = L[TA1]
type LTA2 = L[TA2]
type LTA3 = L[TA3]
type LTA4 = L[TA4]

type LTB = L[TB]
type LTB1 = L[TB1]
type LTB2 = L[TB2]
type LTB3 = L[TB3]
type LTB4 = L[TB4]

type LTF = L[TF]
type LTF1 = L[TF1]
type LTF2 = L[TF2]
type LTF3 = L[TF3]
type LTF4 = L[TF4]

type LTM = L[TM]
type LTM1 = L[TM1]
type LTM2 = L[TM2]
type LTM3 = L[TM3]
type LTM4 = L[TM4]

type LTN = L[TN]
type LTN1 = L[TN1]
type LTN2 = L[TN2]
type LTN3 = L[TN3]
type LTN4 = L[TN4]

type LTP = L[TP]
type LTP1 = L[TP1]
type LTP2 = L[TP2]
type LTP3 = L[TP3]
type LTP4 = L[TP4]

type LTS = L[TS]
type LTS1 = L[TS1]
type LTS2 = L[TS2]
type LTS3 = L[TS3]
type LTS4 = L[TS4]

type LTZ = L[TZ]
type LTZ1 = L[TZ1]
type LTZ2 = L[TZ2]
type LTZ3 = L[TZ3]
type LTZ4 = L[TZ4]


type VA = V[A]
type VB = V[B]
type VF = V[F]
type VM = V[M]
type VN = V[N]
type VP = V[P]
type VS = V[S]
type VZ = V[Z]

type Digest = C[[], A]
type Lzma = LZMAFile | TextIO
type Open = IO[A]
type Path = P | S
type Load = C[[Open], A] | N
type Save = C[[Open, S], N] | N


def ignore(*_: A) -> A:
    """An empty function used to hide unused variable warnings."""
    return _


ignore(
    ACM,
    BF,
    BT,
    CA,
    cast,
    CB,
    CF,
    CM,
    CN,
    CP,
    CS,
    CZ,
    DA,
    DB,
    DF,
    DM,
    DN,
    DP,
    DS,
    DZ,
    Digest,
    GA,
    GB,
    GF,
    GM,
    GN,
    GP,
    GS,
    GZ,
    IT,
    J,
    K,
    LA,
    LB,
    LF,
    LM,
    LN,
    LP,
    LS,
    LTA,
    LTA1,
    LTA2,
    LTA3,
    LTA4,
    LTB,
    LTB1,
    LTB2,
    LTB3,
    LTB4,
    LTF,
    LTF1,
    LTF2,
    LTF3,
    LTF4,
    LTM,
    LTM1,
    LTM2,
    LTM3,
    LTM4,
    LTN,
    LTN1,
    LTN2,
    LTN3,
    LTN4,
    LTP,
    LTP1,
    LTP2,
    LTP3,
    LTP4,
    LTS,
    LTS1,
    LTS2,
    LTS3,
    LTS4,
    LTZ,
    LTZ1,
    LTZ2,
    LTZ3,
    LTZ4,
    LZ,
    Lzma,
    MS,
    NR,
    Open,
    override,
    Path,
    Protocol,
    Q,
    R,
    TD,
    TY,
    U,
    UN,
    VA,
    VB,
    VF,
    VM,
    VN,
    VP,
    VS,
    VZ,
    X,
    Y,
)
