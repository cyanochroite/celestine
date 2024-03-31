""""""


from celestine import bank
from celestine.data import (
    code,
    main,
    scene,
)
from celestine.interface import View
from celestine.session.session import SuperSession
from celestine.typed import (
    H,
    N,
    R,
    S,
)


class Session(SuperSession):
    """"""


@code
def cow(hold: H, *, say: S, **star: R) -> N:
    """"""
    talk = bank.language.DEMO_COW_TALK
    print(talk, say)


@code
def dog(hold: H, **star: R) -> N:
    """"""
    item = hold.window.find("zero_title")
    if item.hidden:
        item.show()
    else:
        item.hide()


@code
def cat(hold: H, **star: R) -> N:
    """"""
    item = hold.window.find("zero_body")
    if item.hidden:
        item.show()
    else:
        item.hide()


@main
def zero(view: View) -> N:
    """"""
    language = view.hold.language
    with view.span("zero_head") as line:
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
    with view.span("zero_body") as line:
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


@scene
def one(view: View) -> N:
    """"""
    language = view.hold.language
    with view.span("one_head") as line:
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
    with view.span("one_body") as line:
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


@scene
def two(view: View) -> N:
    """"""
    language = view.hold.language
    with view.span("two_head") as line:
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
    with view.span("two_body") as line:
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
