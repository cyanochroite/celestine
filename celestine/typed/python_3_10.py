"""Define types here."""

# Generator[YieldType, SendType, ReturnType]
from typing import Generator as GE  # noqa: F401 pylint: disable=W0611
from typing import TypeAlias as TA
from types import ModuleType as MT  # noqa: F401 pylint: disable=W0611

from typing import Callable as CA  # noqa: F401 pylint: disable=W0611
from typing import Iterable as IT  # noqa: F401 pylint: disable=W0611

# <python_3_10>
import typing

SELF = typing.TypeVar("SELF")
# </python_3_10>
from typing import Type as TY  # noqa: F401 pylint: disable=W0611

from typing import Any as A  # noqa: F401 pylint: disable=W0611
from typing import Dict as D  # noqa: F401 pylint: disable=W0611
from typing import List as L  # noqa: F401 pylint: disable=W0611
from typing import Tuple as T  # noqa: F401 pylint: disable=W0611
from typing import Union as U  # noqa: F401 pylint: disable=W0611

B: TA = bool
F: TA = float
N: TA = None
S: TA = str
Z: TA = int
