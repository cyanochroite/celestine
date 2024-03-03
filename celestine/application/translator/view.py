"""The View page."""


from celestine.data import main
from celestine.interface import View
from celestine.typed import N


@main
def trans(view: View) -> N:
    """"""
    view.label("label", "Here we are.")
