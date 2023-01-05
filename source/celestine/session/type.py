"""Define types here."""
from argparse import _ArgumentGroup as AG
from argparse import ArgumentParser as AP

from typing import Dict as D
from typing import Iterable as IT
from types import ModuleType as MT
from typing import Self as SELF
from typing import Type as T
from typing import TypeAlias as TA
from typing import Tuple as TU
from typing import Union as U


class Argument:
    ...


S: TA = str
"""string"""

SL: TA = list[str]
"""string list"""


B: TA = bool
"""bool"""

I: TA = int
"""int"""

N: TA = None
"""none"""

AT: TA = D[S, S | SL]
"""attribute table"""

APD: TA = D[U[Argument, T[Argument]], U[AP, AG]]
"""argument parser dictionary"""


AD: TA = D[S, Argument]
"""argument dictionary"""

ADI: TA = IT[TU[S, Argument]]
"""
argument dictionary items

ADI: typing.TypeAlias = typing.Iterable[typing.Tuple[str, Argument]]
"""
