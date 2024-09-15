""""""

from celestine import language
from celestine.data import draw
from celestine.interface import View
from celestine.typed import N


@draw
def main(view: View) -> N:
    """"""
    with view.span("main_head") as line:
        line.label(
            "main_title",
            text="Logo generation functions."
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
