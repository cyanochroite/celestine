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
from typing import Optional as O
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

OB: TA = O[B]
OF: TA = O[F]
OP: TA = O[P]
OS: TA = O[S]
OZ: TA = O[Z]

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


R = Ring  # noqa: F401 pylint: disable=W0611

FILE: TA = IO[A]
LZMA: TA = U[lzma.LZMAFile, TextIO]
