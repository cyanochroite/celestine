""""""


from celestine.session.session import SuperSession

from celestine.typed import N

from celestine.window.container import Container as Page


class Session(SuperSession):
    """"""


def one(page: Page) -> N:
    """"""
    print("hi there oeu")
    language = page.session.language
    with page.span("one_head") as line:
        line.label("one_title", language.DEMO_ONE_TITLE)
    with page.span("one_body") as line:
        line.button("one_past", language.DEMO_ONE_PAST, "main")
        line.button("one_next", language.DEMO_ONE_NEXT, "two")


def two(page: Page) -> N:
    """"""
    print("hi there two")
    language = page.session.language
    with page.span("two_head") as line:
        line.label("two_title", language.DEMO_TWO_TITLE)
    with page.span("two_body") as line:
        line.button("two_past", language.DEMO_TWO_PAST, "one")
        line.button("two_next", language.DEMO_TWO_NEXT, "main")


def main(page: Page) -> N:
    """"""
    print("BOO")
    language = page.session.language
    with page.span("main_head") as line:
        line.label("main_title", language.DEMO_MAIN_TITLE)
    with page.span("main_body") as line:
        line.button("main_past", language.DEMO_MAIN_PAST, "one")
        line.button("main_next", language.DEMO_MAIN_NEXT, "two")


def cow(task: int):
    print("cow bells")
