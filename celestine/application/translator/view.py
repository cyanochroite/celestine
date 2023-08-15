"""The View page."""


from celestine.typed import (
    N,
    R,
)
from celestine.window.container import View


def main(ring: R, view: View) -> N:
    """"""
    with view.zone("main") as line:
        line.new("main_A", text="Translate Files", code="translate")


# TODO:figure out how to make actions not trigger on function load
def report(ring: R, view: View) -> N:
    """"""
    with view.zone("head") as line:
        line.new("title", text="Page main")
    train = {}

    line.new(
        "main_action",
        text="Translate Files",
        code="train",
        page=ring,
    )

    for tag, text in train.items():
        with view.zone("body") as line:
            line.new(tag, text=text)
