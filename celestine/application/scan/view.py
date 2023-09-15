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
        line.new("main_title", text=language.SCAN_MAIN_TITLE)
        line.new("main_A", text=language.SCAN_MAIN_BUTTON,
                 code="cow", say="Hello!")
