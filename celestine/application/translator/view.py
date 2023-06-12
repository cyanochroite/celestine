"""The View page."""


from celestine.session.session import Session
from celestine.typed import N
from celestine.window.container import Container as Page


def main(page: Page, session: Session) -> N:
    """"""
    with page.span("main") as line:
        line.call(
            "main_action",
            "Translate Files",
            "translate",
            session=page.session,
        )


# TODO:figure out how to make actions not trigger on function load
def report(page: Page, session: Session) -> N:
    """"""
    with page.span("head") as line:
        line.label("title", "Page main")
    train = {}

    line.call(
        "main_action",
        "Translate Files",
        "train",
        page=page.session,
    )

    for tag, text in train.items():
        with page.span("body") as line:
            line.label(tag, text)
