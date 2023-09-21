"""
Define types here.

Generator[YieldType, SendType, ReturnType]
"""

import lzma
import pathlib
from collections.abc import (  # noqa: F401 pylint: disable=W0611
    Callable as CA,
)
from collections.abc import (  # noqa: F401 pylint: disable=W0611
    Generator as GE,
)
from collections.abc import (  # noqa: F401 pylint: disable=W0611
    Iterable as IT,
)
from types import ModuleType as MT  # noqa: F401 pylint: disable=W0611
from typing import IO  # noqa: F401 pylint: disable=W0611
from typing import Any as A  # noqa: F401 pylint: disable=W0611
from typing import Dict as D  # noqa: F401 pylint: disable=W0611
from typing import List as L  # noqa: F401 pylint: disable=W0611
from typing import Optional as OPT
from typing import TextIO
from typing import Tuple as T  # noqa: F401 pylint: disable=W0611
from typing import Type as TY  # noqa: F401 pylint: disable=W0611
from typing import TypeAlias as TA
from typing import Union as U  # noqa: F401 pylint: disable=W0611

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
