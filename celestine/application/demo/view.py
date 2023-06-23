""""""

from celestine.typed import (
    N,
    R,
)
from celestine.window.container import View


def one(ring: R, view: View) -> N:
    """"""
    language = view.ring.language
    with view.zone("one_head") as line:
        line.text("one_title", language.DEMO_ONE_TITLE)
        line.text("one_action", "Feed Cow", call="cow", say="I eat you")
    with view.zone("one_body") as line:
        line.text("one_past", language.DEMO_ONE_PAST, call="main")
        line.text("one_next", language.DEMO_ONE_NEXT, call="two")


def two(ring: R, view: View) -> N:
    """"""
    language = view.ring.language
    with view.zone("two_head") as line:
        line.text("two_title", language.DEMO_TWO_TITLE)
        line.text("two_action", "Wave Cow", call="cow", say="Good Bye!")
    with view.zone("two_body") as line:
        line.text("two_past", language.DEMO_TWO_PAST, call="one")
        line.text("two_next", language.DEMO_TWO_NEXT, call="main")


def main(ring: R, view: View) -> N:
    """"""
    language = view.ring.language
    with view.zone("main_head") as line:
        line.text("main_title", language.DEMO_MAIN_TITLE)
        line.text("main_action", "Greet Cow", call="cow", say="Hello!")
    with view.zone("main_body") as line:
        line.text("main_past", language.DEMO_MAIN_PAST, call="one")
        line.text("main_next", language.DEMO_MAIN_NEXT, call="two")
