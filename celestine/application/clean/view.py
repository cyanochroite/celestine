""""""

from celestine.session.session import Session
from celestine.typed import N
from celestine.window.container import View


def main(ring: Session, view: View) -> N:
    """"""
    language = view.ring.language
    with view.zone("main_head") as line:
        line.label("main_title", language.DEMO_MAIN_TITLE)
        line.call("main_action", "Greet Cow", "clean")
    with view.zone("main_body") as line:
        line.call("main_licence", "Clean licence files.", "licence")
