""""""

from celestine.data import main
from celestine.typed import N
from celestine.window import View


@main
def enter(view: View) -> N:
    """"""
    language = view.hold.language
    with view.span("main_head") as line:
        line.new("main_title", text=language.CLEAN_MAIN_TITLE)
        line.new(
            "main_action", text=language.CLEAN_MAIN_CLEAN, code="clean"
        )
    with view.span("main_body") as line:
        line.new(
            "main_L", text=language.CLEAN_MAIN_VERSION, code="version"
        )
        line.new(
            "main_R", text=language.CLEAN_MAIN_LICENCE, code="licence"
        )
