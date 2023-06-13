"""The View page."""


from celestine.session.session import Session
from celestine.typed import N
from celestine.window.container import Container as View


def main(this: Session, view: View) -> N:
    """"""
    with view.span("main") as line:
        line.call(
            "main_action",
            "Translate Files",
            "translate",
            this=this,
        )


# TODO:figure out how to make actions not trigger on function load
def report(this: Session, view: View) -> N:
    """"""
    with view.span("head") as line:
        line.label("title", "Page main")
    train = {}

    line.call(
        "main_action",
        "Translate Files",
        "train",
        page=this,
    )

    for tag, text in train.items():
        with view.span("body") as line:
            line.label(tag, text)
