""""""

import celestine
from celestine import language
from celestine.interface import View
from celestine.session.session import SuperSession
from celestine.typed import (
    N,
    ignore,
)
from celestine.window.decorator import draw


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
            "main_R1",
            "unicode",
            text="Unicode Normalize",
        )
    with view.span("main_foot") as line:
        line.button(
            "main_L1",
            "test",
            text="test",
        )
        line.button(
            "main_R1",
            "none",
            text="unused",
        )


ignore(Session, main)

celestine.main(__package__)
