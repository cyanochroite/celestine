""""""

from celestine.session.session import Session
from celestine.typed import N
from celestine.window.container import Container as View


def main(session: Session, view: View) -> N:
    """"""
    language = view.session.language
    with view.span("main_head") as line:
        line.label("main_title", language.DEMO_MAIN_TITLE)
        line.call("main_action", "Greet Cow", "clean")
    with view.span("main_body") as line:
        line.call("main_licence", "Clean licence files.", "licence")
