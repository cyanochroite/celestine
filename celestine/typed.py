"""
Define types here.

Generator[YieldType, SendType, ReturnType]
"""

import lzma
import pathlib
from collections.abc import Callable as CA
from collections.abc import Generator as GE
from collections.abc import Iterable as IT
from types import ModuleType as MT
from typing import IO
from typing import Any as A
from typing import Dict as D
from typing import List as L
from typing import Optional as OPT
from typing import TextIO
from typing import Tuple as T
from typing import Type as TY
from typing import TypeAlias as TA
from typing import Union as U

try:  # Fix for Python 3.10 not having Self.
    from typing import Self as SELF
except ImportError:
    SELF: TA = A

N: TA = None
OBJ: TA = object

B: TA = bool
F: TA = float
P: TA = pathlib.Path
S: TA = str
Z: TA = int

OB: TA = OPT[B]
OF: TA = OPT[F]
OP: TA = OPT[P]
OS: TA = OPT[S]
OZ: TA = OPT[Z]

LB: TA = L[B]
LF: TA = L[F]
LP: TA = L[P]
LS: TA = L[S]
LZ: TA = L[Z]


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


R = Ring  # noqa: F401 pylint: disable=W0611

FILE: TA = IO[A]
LZMA: TA = U[lzma.LZMAFile, TextIO]
