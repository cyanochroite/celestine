""""""

from celestine import language
from celestine.data import draw
from celestine.interface import View
from celestine.session.session import SuperSession
from celestine.typed import N


class Session(SuperSession):
    """"""


@draw
def main(view: View) -> N:
    """"""
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
    with view.span("main_foot") as line:
        line.button(
            "main_L",
            "test",
            text="test",
        )
        line.button(
            "main_R",
            "licence",
            text="unused",
        )
