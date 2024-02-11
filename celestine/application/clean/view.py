""""""

from celestine.data import main
from celestine.interface import View
from celestine.typed import N


@main
def enter(view: View) -> N:
    """"""
    language = view.hold.language
    with view.span("main_head") as line:
        line.new(
            "main_title",
            label=language.CLEAN_MAIN_TITLE,
        )
        line.new(
            "main_action",
            action="clean",
            label=language.CLEAN_MAIN_CLEAN,
        )
    with view.span("main_body") as line:
        line.new(
            "main_L",
            action="version",
            label=language.CLEAN_MAIN_VERSION,
        )
        line.new(
            "main_R",
            action="licence",
            label=language.CLEAN_MAIN_LICENCE,
        )
