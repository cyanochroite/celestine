""""""

from celestine.typed import N
from celestine.window.container import Container as Page


def main(page: Page) -> N:
    """"""
    language = page.session.language
    with page.span("main_head") as line:
        line.label("main_title", language.DEMO_MAIN_TITLE)
        line.call("main_action", "Greet Cow", "clean")
    with page.span("main_body") as line:
        line.call("main_licence", "Clean licence files.", "licence")
