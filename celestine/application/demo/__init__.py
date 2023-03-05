""""""


from celestine.session.session import SuperSession
from celestine.typed import N
from celestine.window.container import Container as Page


class Session(SuperSession):
    """"""


def page_one(page: Page) -> N:
    """"""
    language = page.session.language
    with page.span("one_head") as line:
        line.label("one_title", language.DEMO_ONE_TITLE)
    with page.span("one_body") as line:
        line.button("one_past", language.DEMO_ONE_PAST, "page_main")
        line.button("one_next", language.DEMO_ONE_NEXT, "page_two")


def page_two(page: Page) -> N:
    """"""
    language = page.session.language
    with page.span("two_head") as line:
        line.label("two_title", language.DEMO_TWO_TITLE)
    with page.span("two_body") as line:
        line.button("two_past", language.DEMO_TWO_PAST, "page_one")
        line.button("two_next", language.DEMO_TWO_NEXT, "page_main")


def page_main(page: Page) -> N:
    """"""
    language = page.session.language
    with page.span("main_head") as line:
        line.label("main_title", language.DEMO_MAIN_TITLE)
        line.task("main_action", "text go here", "task_cow")
    with page.span("main_body") as line:
        line.button("main_past", language.DEMO_MAIN_PAST, "page_one")
        line.button("main_next", language.DEMO_MAIN_NEXT, "page_two")


def task_cow():
    print("cow bells")
