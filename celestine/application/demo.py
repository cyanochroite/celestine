""""""


from celestine.data import (
    code,
    main,
    scene,
)
from celestine.session.session import SuperSession
from celestine.typed import (
    H,
    N,
    S,
)
from celestine.window import View


class Session(SuperSession):
    """"""


@code
def cow(hold: H, *, say: S) -> N:
    """"""
    talk = hold.language.DEMO_COW_TALK
    print(talk, say)


@main
def zero(view: View) -> N:
    """"""
    language = view.hold.language
    with view.span("zero_head") as line:
        line.new("zero_title", text=language.DEMO_ZERO_TITLE)
        line.new(
            "zero_A",
            text=language.DEMO_ZERO_ACTION,
            code="cow",
            say=language.DEMO_ZERO_SAY,
        )
    with view.span("zero_body") as line:
        line.new("zero_past", text=language.DEMO_MAIN_PAST, view="one")
        line.new("zero_next", text=language.DEMO_MAIN_NEXT, view="two")


@scene
def one(view: View) -> N:
    """"""
    language = view.hold.language
    with view.span("one_head") as line:
        line.new("one_title", text=language.DEMO_ONE_TITLE)
        line.new(
            "one_A",
            text=language.DEMO_ONE_ACTION,
            code="cow",
            say=language.DEMO_ONE_SAY,
        )
    with view.span("one_body") as line:
        line.new("one_past", text=language.DEMO_ONE_PAST, view="zero")
        line.new("one_next", text=language.DEMO_ONE_NEXT, view="two")


@scene
def two(view: View) -> N:
    """"""
    language = view.hold.language
    with view.span("two_head") as line:
        line.new("two_title", text=language.DEMO_TWO_TITLE)
        line.new(
            "two_A",
            text=language.DEMO_TWO_ACTION,
            code="cow",
            say=language.DEMO_TWO_SAY,
        )
    with view.span("two_body") as line:
        line.new("two_past", text=language.DEMO_TWO_PAST, view="one")
        line.new("two_next", text=language.DEMO_TWO_NEXT, view="zero")


# if __spec__.name == "__main__":
#    celestine.main(__spec__.origin)
