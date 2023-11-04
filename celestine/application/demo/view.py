""""""

from celestine.typed import N
from celestine.window.container import View


def one(view: View) -> N:
    """"""
    language = view.ring.language
    with view.zone("one_head") as line:
        line.new("one_title", text=language.DEMO_ONE_TITLE)
        line.new(
            "one_A",
            text=language.DEMO_ONE_ACTION,
            code="cow",
            say=language.DEMO_ONE_SAY,
        )
    with view.zone("one_body") as line:
        line.new("one_past", text=language.DEMO_ONE_PAST, view="main")
        line.new("one_next", text=language.DEMO_ONE_NEXT, view="two")


def two(view: View) -> N:
    """"""
    language = view.ring.language
    with view.zone("two_head") as line:
        line.new("two_title", text=language.DEMO_TWO_TITLE)
        line.new(
            "two_A",
            text=language.DEMO_TWO_ACTION,
            code="cow",
            say=language.DEMO_TWO_SAY,
        )
    with view.zone("two_body") as line:
        line.new("two_past", text=language.DEMO_TWO_PAST, view="one")
        line.new("two_next", text=language.DEMO_TWO_NEXT, view="main")


def main(view: View) -> N:
    """"""
    language = view.ring.language
    with view.zone("main_head") as line:
        line.new("main_title", text=language.DEMO_MAIN_TITLE)
        line.new(
            "main_A",
            text=language.DEMO_MAIN_ACTION,
            code="cow",
            say=language.DEMO_MAIN_SAY,
        )
    with view.zone("main_body") as line:
        line.new("main_past", text=language.DEMO_MAIN_PAST, view="one")
        line.new("main_next", text=language.DEMO_MAIN_NEXT, view="two")
