""""""


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
    S,
)


class Session(SuperSession):
    """"""


@code
def cow(hold: H, *, say: S) -> N:
    """"""
    talk = hold.language.DEMO_COW_TALK
    print(talk, say)


@code
def dog(hold: H) -> N:
    """"""
    item = hold.window.find("zero_title")
    if item.hidden:
        item.show()
    else:
        item.hide()


@code
def cat(hold: H) -> N:
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
        line.new("zero_title", text=language.DEMO_ZERO_TITLE)
        line.new(
            "zero_B",
            text="DOG",
            code="dog",
        )
        line.new(
            "zero_C",
            text="CAT",
            code="cat",
        )
        line.new(
            "zero_A",
            # text=language.DEMO_ZERO_ACTION,
            text="COW",
            code="cow",
            say=language.DEMO_ZERO_SAY,
        )
    with view.span("zero_body") as line:
        line.new("zero_past", view="one", text=language.DEMO_MAIN_PAST)
        line.new("zero_next", view="two", text=language.DEMO_MAIN_NEXT)


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
        line.new("one_past", view="zero", text=language.DEMO_ONE_PAST)
        line.new("one_next", view="two", text=language.DEMO_ONE_NEXT)


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
        line.new("two_past", view="one", text=language.DEMO_TWO_PAST)
        line.new("two_next", view="zero", text=language.DEMO_TWO_NEXT)


# if __spec__.name == "__main__":
#    celestine.main(__spec__.origin)
