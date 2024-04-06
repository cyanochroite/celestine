""""""

from celestine.data import main
from celestine import bank
from celestine.interface import View
from celestine.typed import N


@main
def app(view: View) -> N:
    """"""
    with view.zone("main") as line:
        line.button(
            "main_A",
            "main",
            text=bank.language.TRANSLATOR_MAIN_BUTTON,
        )
