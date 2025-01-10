"""Python Game Development."""

import re
from celestine import bank
from celestine.package import Abstract
from celestine.package.pygame import (
    event,
    font,
    image,
    mouse,
    transform,
)
from celestine.package.pygame.abstract import Surface
from celestine.typed import (
    A,
    TZ2,
    B,
    N,
    Protocol,
    R,
    S,
    Z,
    ignore,
)

ignore(event)
ignore(font)
ignore(image)
ignore(mouse)
ignore(Surface)
ignore(transform)
MOUSEBUTTONDOWN: Z
QUIT: Z

NAME = "pygame"

from celestine import regex, load


class Code(Protocol):
    """Type for code functions."""

    def __call__(self, **star: R) -> B:
        raise NotImplementedError(self, star)


def stub(function: Code) -> Code:
    """"""
    cache = None

    def decorator(self, *data: A, **star: R) -> A:
        nonlocal cache
        if not cache:
            pattern = r"<function ([\w\.]+) "
            string = repr(function)
            name = regex.match(pattern, string)

            source = bank.package[NAME].package
            cache = load.find_function(source, name)

        try:
            result = function(self, *data, **star)
        except NotImplementedError:
            result = cache(*data, **star)

        return result

    return decorator


class Package(Abstract):
    """"""


def quit() -> N:  # pylint: disable=redefined-builtin
    """"""


class display:  # pylint: disable=invalid-name
    """"""

    @staticmethod
    def flip() -> N:
        """"""
        raise NotImplementedError()

    @staticmethod
    def set_caption(title: S) -> N:
        """"""
        raise NotImplementedError(title)

    @staticmethod
    def set_icon(surface: Surface) -> N:
        """"""
        raise NotImplementedError(surface)

    @stub
    def set_mode(self, size: TZ2) -> Surface:
        """"""
        raise NotImplementedError(self, size)
