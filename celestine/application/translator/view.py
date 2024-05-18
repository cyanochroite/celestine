"""The View page."""

from celestine import language
from celestine.data import draw
from celestine.interface import View
from celestine.typed import N


@draw(True)
def main(view: View) -> N:
    """"""
    with view.zone("main") as line:
        line.new(
            "main_A",
            text=language.TRANSLATOR_MAIN_BUTTON,
            code="translate",
        )


# TODO: Add report functionality back in, and make it better.
@draw
def report(view: View) -> N:
    """"""
    with view.zone("head") as line:
        line.new("title", text="Page main")
    train = {}

    line.new(
        "main_action",
        text=language.TRANSLATOR_REPORT_BUTTON,
        code="train",
        page=hold,
    )

    for tag, text in train.items():
        with view.zone("body") as line:
            line.new(tag, text=text)
