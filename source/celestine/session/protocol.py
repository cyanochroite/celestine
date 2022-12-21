""""""

import argparse
import types
import typing

from celestine.session.argument import Argument


class Dictionary(typing.Protocol):
    """"""

    @staticmethod
    def dictionary(
        language: types.ModuleType,
    ) -> typing.Dict[str, Argument]:
        ...


class Parser(typing.Protocol):
    """"""

    def add_argument(
        self,
        *args,
        **kwargs,
    ) -> argparse._StoreAction: ...
