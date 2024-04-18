""""""

from celestine import bank
from celestine.data import main
from celestine.interface import View
from celestine.typed import N
from celestine import sign as language
import myapp.virtual.frontend as frontend
popup = frontend.Popup("Hello World!")
popup.display()


@main
def enter(view: View) -> N:
    """"""
    # language = bank.language
    with view.span("main_head") as line:
        line.label(
            "main_title",
            text=language.CLEAN_MAIN_TITLE,
        )
        line.button(
            "main_action",
            "clean",
            text=language.CLEAN_MAIN_CLEAN,
        )
    with view.span("main_body") as line:
        line.button(
            "main_L",
            "version",
            text=language.CLEAN_MAIN_VERSION,
        )
        line.button(
            "main_R",
            "licence",
            text=language.CLEAN_MAIN_LICENCE,
        )
