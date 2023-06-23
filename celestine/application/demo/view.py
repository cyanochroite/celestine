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
        line.new("one_title", text=language.DEMO_ONE_TITLE)
        line.new("one_A", text="Feed Cow", call="cow", say="I eat you")
    with view.zone("one_body") as line:
        line.new("one_past", text=language.DEMO_ONE_PAST, call="main")
        line.new("one_next", text=language.DEMO_ONE_NEXT, call="two")


def two(ring: R, view: View) -> N:
    """"""
    language = view.ring.language
    with view.zone("two_head") as line:
        line.new("two_title", text=language.DEMO_TWO_TITLE)
        line.new("two_A", text="Wave Cow", call="cow", say="Good Bye!")
    with view.zone("two_body") as line:
        line.new("two_past", text=language.DEMO_TWO_PAST, call="one")
        line.new("two_next", text=language.DEMO_TWO_NEXT, call="main")


def main(ring: R, view: View) -> N:
    """"""
    language = view.ring.language
    with view.zone("main_head") as line:
        line.new("main_title", text=language.DEMO_MAIN_TITLE)
        line.new("main_A", text="Greet Cow", call="cow", say="Hello!")
    with view.zone("main_body") as line:
        line.new("main_past", text=language.DEMO_MAIN_PAST, call="one")
        line.new("main_next", text=language.DEMO_MAIN_NEXT, call="two")
