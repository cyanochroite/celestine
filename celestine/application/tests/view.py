""""""

from celestine import bank
from celestine.data import main
from celestine.interface import View
from celestine.typed import N


@main
def app(view: View) -> N:
    """"""
    with view.zone("main") as line:
        line.button(
            "main_A",
            "main",
            text=view.hold.language.TRANSLATOR_MAIN_BUTTON,
        )
