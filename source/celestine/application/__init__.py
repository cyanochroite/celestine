""""""


from celestine.session.session import SuperSession

from celestine.typed import N

from celestine.window.page import Page


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
