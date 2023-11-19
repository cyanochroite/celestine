"""The View page."""


from celestine.data import main
from celestine.typed import N
from celestine.window.container import View


@main
def enter(view: View) -> N:
    """"""
    with view.zone("main") as line:
        line.new(
            "main_A",
            text=view.hold.language.TRANSLATOR_MAIN_BUTTON,
            code="main",
            prompt="A cute baby dragon with a gold bed.",
        )
