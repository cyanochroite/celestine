""""""

from celestine import (
    bank,
    language,
)
from celestine.typed import (
    B,
    R,
    S,
    ignore,
)
from celestine.window.decorator import call


@call
def cow(*, say: S, **star: R) -> B:
    """"""
    ignore(star)
    talk = language.DEMO_COW_TALK
    print(talk, say)
    return True


@call
def dog(**star: R) -> B:
    """"""
    ignore(star)
    item = bank.window.find("zero_title")
    if item.hidden:
        item.show()
    else:
        item.hide()
    return True


@call
def cat(**star: R) -> B:
    """"""
    ignore(star)
    item = bank.window.find("zero_body")
    if item.hidden:
        item.show()
    else:
        item.hide()
    return True
