""""""

from celestine.typed import N
from celestine.window.container import View


def main(view: View) -> N:
    """"""
    language = view.ring.language
    with view.zone("main_head") as line:
        line.new("main_title", text=language.CLEAN_MAIN_TITLE)
        line.new(
            "main_action", text=language.CLEAN_MAIN_CLEAN, code="clean"
        )
    with view.zone("main_body") as line:
        line.new(
            "main_L", text=language.CLEAN_MAIN_VERSION, code="version"
        )
        line.new(
            "main_R", text=language.CLEAN_MAIN_LICENCE, code="licence"
        )
