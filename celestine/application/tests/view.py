""""""

from celestine.typed import (
    N,
    R,
)
from celestine.window.container import View


def main(ring: R, view: View) -> N:
    """"""
    with view.zone("main") as line:
        line.new(
            "main_A",
            text=ring.language.TRANSLATOR_MAIN_BUTTON,
            code="main",
        )
