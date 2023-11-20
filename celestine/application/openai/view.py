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
            #prompt="A cute baby dragon with a gold bed.",
            prompt="An octopus with bananas for arms. It is swimming in the ocean. It is happy to be with its fish friends. There is a starfish that looks like bacon."
        )
