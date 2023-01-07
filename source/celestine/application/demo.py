""""""

from celestine.session.argument import Argument

from celestine.session.session import SuperSession

from celestine.typed import D
from celestine.typed import N
from celestine.typed import S
from celestine.typed import TA

from celestine.window.page import Page


AD: TA = D[S, Argument]


class Session(SuperSession):
    """"""


def one(page: Page) -> N:
    """"""
    with page.line("head") as line:
        line.label("title", "Page one")
    with page.line("body") as line:
        line.button("past", "Page main", "main")
        line.button("next", "Page two", "two")


def two(page: Page) -> N:
    """"""
    with page.line("head") as line:
        line.label("title", "Page two")
    with page.line("body") as line:
        line.button("past", "Page one", "one")
        line.button("next", "Page main", "main")


def main(page: Page) -> N:
    """"""
    with page.line("head") as line:
        line.label("title", "Page main")
    with page.line("body") as line:
        line.button("past", "Page one", "one")
        line.button("next", "Page two", "two")
