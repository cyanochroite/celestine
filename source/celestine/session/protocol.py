""""""

import argparse
import types
import typing


from argparse import ArgumentParser as AP
from argparse import _ArgumentGroup as AG
from typing import TypeAlias as TA
from typing import Dict as D
from typing import Type as T
from typing import Union as U

from celestine.session.argument import Argument
from celestine.session.argument import Argument as A


class Dictionary(typing.Protocol):
    """"""

    @staticmethod
    def dictionary(
        language: types.ModuleType,
    ) -> typing.Dict[str, Argument]:
        ...


class Parser(typing.Protocol):
    """"""

    def add_argument1(
        self,
        *args,
        **kwargs,
    ) -> argparse._StoreAction: ...


Magic: TA = D[U[A, T[A]], U[AP, AG]]


