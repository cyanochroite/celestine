"""The View page."""

from celestine import language
from celestine.interface import View
from celestine.typed import (
    D,
    N,
    S,
    ignore,
)
from celestine.window.decorator import draw


@draw
def main(view: View) -> N:
    """"""
    with view.zone("main") as line:
        line.button(
            "main_A",
            "translate",
            text=language.TRANSLATOR_MAIN_BUTTON,
        )


# TODO: Add report functionality back in, and make it better.
@draw
def report(view: View) -> N:
    """"""
    with view.zone("head") as line:
        line.label("title", text="Page main")
    train: D[S, S] = {}

    line.button(
        "main_action",
        "train",
        text=language.TRANSLATOR_REPORT_BUTTON,
        view=main,
    )

    for tag, text in train.items():
        with view.zone("body") as line:
            line.label(tag, text=text)


ignore(report)
