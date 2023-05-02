"""Define types here."""

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

# Generator[YieldType, SendType, ReturnType]
from typing import Any as A  # noqa: F401 pylint: disable=W0611
from typing import Dict as D  # noqa: F401 pylint: disable=W0611
from typing import List as L  # noqa: F401 pylint: disable=W0611
from typing import Tuple as T  # noqa: F401 pylint: disable=W0611
from typing import Type as TY  # noqa: F401 pylint: disable=W0611
from typing import TypeAlias as TA
from typing import Union as U  # noqa: F401 pylint: disable=W0611

B: TA = bool
F: TA = float
N: TA = None
O: TA = object
S: TA = str
Z: TA = int
