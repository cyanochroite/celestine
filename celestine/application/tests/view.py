""""""

from celestine import language
from celestine.data import draw
from celestine.interface import View
from celestine.typed import N


@draw
def main(view: View) -> N:
    """"""
    with view.zone("main") as line:
        line.button(
            "main_A",
            "main",
            text=language.TRANSLATOR_MAIN_BUTTON,
        )
