""""""

from celestine.data import main
from celestine.interface import View
from celestine.typed import N


@main
def app(view: View) -> N:
    """"""
    with view.zone("main") as line:
        line.new(
            "main_A",
            action="main",
            label=view.hold.language.TRANSLATOR_MAIN_BUTTON,
        )
