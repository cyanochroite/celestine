"""Define types here."""

# TODO: Replace all this with 'type' after python 3.12 and mypy support.

import io
import pathlib
import sys
import types
import typing
from collections.abc import Callable as C
from collections.abc import Generator as G
from typing import Dict as D
from typing import List as L
from typing import Literal
from typing import Optional as V  # Void
from typing import Tuple as T
from typing import TypeAlias as TA

#  TODO: Remove after Python 3.10.
_version = sys.version.split(".")
_major = _version[0]
_minor = _version[1]
if _major == "3" and _minor == "10":
    K: TA = typing.Any  # Python 3.10 fix.
else:
    from typing import Self as K


class Star(typing.TypedDict):
    """The global Star object."""

    # TODO: Figure out how to map this to the R type.


A: TA = typing.Any
B: TA = bool
# C: TA = collections.abc.Callable
# D: TA = typing.Dict
# E: TA = typing.Any  # Unused
F: TA = float
# G: TA = collections.abc.Generator
# H: TA = typing.Any  # Unused
# I: TA = typing.Any  # Ambiguous variable name.
J: TA = object
# K: TA = typing.Self  # "Self" is not valid in this context.
# L: TA = typing.List
M: TA = types.ModuleType
N: TA = None
# O: TA = typing.Any  # Ambiguous variable name.
P: TA = pathlib.Path
# Q: TA = typing.Any  # Unused
R: TA = typing.Any  # Star.
S: TA = str
# T: TA = typing.Tuple
# U: TA = typing.Any  # Unused  # Union?
# V: TA = typing.Any  # Unused
# W: TA = typing.Any  # Unused
# X: TA = typing.Any  # Unused
# Y: TA = typing.Any  # Unused
Z: TA = int  # Set of Integers Symbol ℤ.

BF: TA = Literal[False]
BT: TA = Literal[True]

CN: TA = C[[N], N]

DA: TA = D[S, A]
DB: TA = D[S, B]
DF: TA = D[S, F]
DM: TA = D[S, M]
DP: TA = D[S, P]
DS: TA = D[S, S]
DZ: TA = D[S, Z]

# Generator[YieldType, SendType, ReturnType]
GA: TA = G[A, N, N]
GB: TA = G[B, N, N]
GF: TA = G[F, N, N]
GM: TA = G[M, N, N]
GP: TA = G[P, N, N]
GS: TA = G[S, N, N]
GZ: TA = G[Z, N, N]

LA: TA = L[A]
LB: TA = L[B]
LF: TA = L[F]
LM: TA = L[M]
LP: TA = L[P]
LS: TA = L[S]
LZ: TA = L[Z]

VA: TA = V[A]
VB: TA = V[B]
VF: TA = V[F]
VM: TA = V[M]
VP: TA = V[P]
VS: TA = V[S]
VZ: TA = V[Z]


def ignore(_: A) -> N:
    """An empty function used to hide unused variable warnings."""


def override(function: A) -> A:
    """Used so earlier Python wont fail when using @override."""
    # TODO: Remove this once we drop Python 3.11.
    return function


def string(*characters: S) -> S:
    """A simple utility for joining together a series of strings."""
    buffer = io.StringIO()
    for character in characters:
        buffer.write(character)
    value = buffer.getvalue()
    return value


# TODO: Remove this once we drop Python 3.11.
class _Fix:
    """"""

    def _override(self) -> N:
        """"""


class _ImportNotUsed(_Fix):
    """"""

    @override
    def _override(self) -> N:
        # TODO: Remove this once we drop Python 3.11.
        print(override)

    def _self(self) -> K:
        """"""
        return self

    def _tuple(self) -> T[Z, Z]:
        return (0, 0)
