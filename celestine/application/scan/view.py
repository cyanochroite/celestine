""""""

from celestine.data import main
from celestine.interface import View
from celestine.typed import N


@main
def run(view: View) -> N:
    """"""
    language = view.hold.language
    with view.zone("main_head") as line:
        line.new("main_title", text=language.SCAN_MAIN_TITLE)
        line.new(
            "main_A",
            text=language.SCAN_MAIN_BUTTON,
            code="cow",
            say="Hello!",
        )
