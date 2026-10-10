"""Removes unused imports and unused variables."""

from celestine.package import Package
from celestine.typed import (
    N,
    ignore,
)


class Self(Package):
    """"""


def post(url, data=None, json=None, **kwargs) -> str:
    """"""
    raise NotImplementedError(url, data, json, kwargs)


def run() -> N:
    """"""


ignore(Self, post, run)
