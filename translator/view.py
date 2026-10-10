"""The element page."""

from celestine import language
from celestine.interface import Element
from celestine.typed import (
    D,
    N,
    S,
    ignore,
)
from celestine.window.decorator import view


@view
def main(element: Element) -> N:
    """"""
    with element.zone("main") as line:
        line.button(
            "main_A",
            "translate",
            text=language.TRANSLATOR_MAIN_BUTTON,
        )


# TODO: Add report functionality back in, and make it better.
@view
def report(element: Element) -> N:
    """"""
    with element.zone("head") as line:
        line.label("title", text="Page main")
    train: D[S, S] = {}

    line.button(
        "main_action",
        "train",
        text=language.TRANSLATOR_REPORT_BUTTON,
        element=main,
    )

    for tag, text in train.items():
        with element.zone("body") as line:
            line.label(tag, text=text)


ignore(report)
