""""""

import argparse
import typing


from argparse import ArgumentParser as AP
from argparse import _ArgumentGroup as AG
from types import ModuleType as MT
from typing import TypeAlias as TA
from typing import Dict as D
from typing import Type as T
from typing import Union as U

from celestine.session.argument import Argument


class Dictionary(typing.Protocol):
    """"""

    @staticmethod
    def dictionary(language: MT) -> typing.Dict[str, Argument]:
        ...


class Parser(typing.Protocol):
    """"""

    def add_argument(self, *args, **kwargs,) -> argparse._StoreAction:
        ...


Magic: TA = D[U[Argument, T[Argument]], U[AP, AG]]


