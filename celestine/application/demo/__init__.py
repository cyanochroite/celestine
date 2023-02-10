""""""


from celestine.session.session import SuperSession

from celestine.typed import N

from celestine.window.page import Page


class Session(SuperSession):
    """"""


def one(page: Page) -> N:
    """"""
    language = page.session.language
    with page.span("head") as line:
        line.label("title", language.DEMO_ONE_TITLE)
    with page.span("body") as line:
        line.button("past", language.DEMO_ONE_PAST, "main")
        line.button("next", language.DEMO_ONE_NEXT, "two")


def two(page: Page) -> N:
    """"""
    language = page.session.language
    with page.span("head") as line:
        line.label("title", language.DEMO_TWO_TITLE)
    with page.span("body") as line:
        line.button("past", language.DEMO_TWO_PAST, "one")
        line.button("next", language.DEMO_TWO_NEXT, "main")


def main(page: Page) -> N:
    """"""
    language = page.session.language
    with page.span("head") as line:
        line.label("title", language.DEMO_MAIN_TITLE)
    with page.span("body") as line:
        line.button("past", language.DEMO_MAIN_PAST, "one")
        line.button("next", language.DEMO_MAIN_NEXT, "two")
