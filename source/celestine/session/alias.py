""""""

from argparse import ArgumentParser
from argparse import _ArgumentGroup

from types import ModuleType as MT
from typing import TypeAlias as TA
from typing import Callable as C
from typing import Dict as D
from typing import Type as T
from typing import Union as U


from celestine.window.page import Page
from celestine.session.argument import Argument


Magic: TA = D[U[Argument, T[Argument]], U[ArgumentParser, _ArgumentGroup]]


S: TA = str
B: TA = bool
N: TA = None

SL = list[str]

Dictionary: TA = D

Module: TA = MT
Function = C


Main: TA = list[C[[Page], None]]


AttributeDictionary: TA = D[S, U[S | SL]]
