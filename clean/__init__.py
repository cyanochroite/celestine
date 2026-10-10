""""""

import celestine
from celestine import language
from celestine.interface import Element
from celestine.session.session import SuperSession
from celestine.typed import (
    N,
    ignore,
)
from celestine.window.decorator import view


class Session(SuperSession):
    """"""


def main():
    """"""
    celestine.init(__package__)
    celestine.main("clean:run", __package__)


@view
def run(element: Element) -> N:
    """"""
    with element.span("main_head") as line:
        line.label(
            "main_title",
            text=language.CLEAN_MAIN_TITLE,
        )
        line.button(
            "main_action",
            "clean.code:clean",
            text=language.CLEAN_MAIN_CLEAN,
        )
    with element.span("main_body") as line:
        line.button(
            "main_L",
            "clean.code:version",
            text=language.CLEAN_MAIN_VERSION,
        )
        line.button(
            "main_R1",
            "clean.code:unicode",
            text="Unicode Normalize",
        )
    with element.span("main_foot") as line:
        line.button(
            "main_L1",
            "clean.code:test",
            text="test",
        )
        line.button(
            "main_R1",
            "clean.code:none",
            text="unused",
        )


ignore(Session, main, run)
