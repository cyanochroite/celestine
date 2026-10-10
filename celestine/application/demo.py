"""This only exists because old dependicy requires it to be here."""

# TODO Remove this module.

from celestine import (
    bank,
    language,
)
from celestine.interface import Element
from celestine.session.session import SuperSession
from celestine.typed import (
    B,
    N,
    R,
    S,
    ignore,
)
from celestine.window.decorator import (
    call,
    view,
)


class Session(SuperSession):
    """"""


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


@view
def zero(element: Element) -> N:
    """"""
    with element.span("zero_head") as line:
        line.label(
            "zero_title",
            language.DEMO_ZERO_TITLE,
        )
        line.button(
            "zero_B",
            "dog",
            text="DOG",
        )
        line.button(
            "zero_C",
            "cat",
            text="CAT",
        )
        line.button(
            "zero_A",
            "cow",
            text=language.DEMO_ZERO_ACTION,
            say=language.DEMO_ZERO_SAY,
        )
        line.button(
            "zero_A",
            "cow",
            language.DEMO_ZERO_ACTION,
            say=language.DEMO_ZERO_SAY,
        )
    with element.span("zero_body") as line:
        line.link(
            "zero_past",
            "one",
            text=language.DEMO_MAIN_PAST,
        )
        line.link(
            "zero_next",
            "two",
            text=language.DEMO_MAIN_NEXT,
        )


@view
def one(element: Element) -> N:
    """"""
    with element.span("one_head") as line:
        line.label(
            "one_title",
            text=language.DEMO_ONE_TITLE,
        )
        line.button(
            "one_A",
            "cow",
            text=language.DEMO_ONE_ACTION,
            say=language.DEMO_ONE_SAY,
        )
    with element.span("one_body") as line:
        line.link(
            "one_past",
            "zero",
            text=language.DEMO_ONE_PAST,
        )
        line.link(
            "one_next",
            "two",
            text=language.DEMO_ONE_NEXT,
        )


@view
def two(element: Element) -> N:
    """"""
    with element.span("two_head") as line:
        line.label(
            "two_title",
            language.DEMO_TWO_TITLE,
        )
        line.button(
            "two_A",
            "cow",
            text=language.DEMO_TWO_ACTION,
            say=language.DEMO_TWO_SAY,
        )
    with element.span("two_body") as line:
        line.link(
            "two_past",
            "one",
            text=language.DEMO_TWO_PAST,
        )
        line.link(
            "two_next",
            "zero",
            text=language.DEMO_TWO_NEXT,
        )


ignore(Session, cat, cow, dog, one, two, zero)
