""""""

from celestine.typed import (
    N,
    R,
)
from celestine.window.container import View


def main(ring: R, view: View) -> N:
    """"""
    language = view.ring.language
    with view.zone("main_head") as line:
        line.new("main_title", text=language.DEMO_MAIN_TITLE)
        line.new("main_action", text="Greet Cow", code="clean")
    with view.zone("main_body") as line:
        line.new("main_L", text="Clean licence files", code="licence")
