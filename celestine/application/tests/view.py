""""""

from celestine import language
from celestine.data import scene
from celestine.interface import View
from celestine.typed import N


@scene
def main(view: View) -> N:
    """"""
    with view.zone("main") as line:
        line.button(
            "main_A",
            "main",
            text=language.TRANSLATOR_MAIN_BUTTON,
        )
