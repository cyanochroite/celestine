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
        line.new(
            "zero_title",
            label=language.DEMO_ZERO_TITLE,
        )
        line.new(
            "zero_B",
            action="dog",
            label="DOG",
        )
        line.new(
            "zero_C",
            action="cat",
            label="CAT",
        )
        line.new(
            "zero_A",
            action="cow",
            label=language.DEMO_ZERO_ACTION,
            say=language.DEMO_ZERO_SAY,
        )
    with view.span("zero_body") as line:
        line.new(
            "zero_past",
            label=language.DEMO_MAIN_PAST,
            navigate="one",
        )
        line.new(
            "zero_next",
            label=language.DEMO_MAIN_NEXT,
            navigate="two",
        )


@scene
def one(view: View) -> N:
    """"""
    language = view.hold.language
    with view.span("one_head") as line:
        line.new(
            "one_title",
            label=language.DEMO_ONE_TITLE,
        )
        line.new(
            "one_A",
            action="cow",
            label=language.DEMO_ONE_ACTION,
            say=language.DEMO_ONE_SAY,
        )
    with view.span("one_body") as line:
        line.new(
            "one_past",
            label=language.DEMO_ONE_PAST,
            navigate="zero",
        )
        line.new(
            "one_next",
            label=language.DEMO_ONE_NEXT,
            navigate="two",
        )


@scene
def two(view: View) -> N:
    """"""
    language = view.hold.language
    with view.span("two_head") as line:
        line.new(
            "two_title",
            label=language.DEMO_TWO_TITLE,
        )
        line.new(
            "two_A",
            action="cow",
            label=language.DEMO_TWO_ACTION,
            say=language.DEMO_TWO_SAY,
        )
    with view.span("two_body") as line:
        line.new(
            "one",
            label=language.DEMO_TWO_PAST,
            navigate="one",
        )
        line.new(
            "zero",
            label=language.DEMO_TWO_NEXT,
            navigate="zero",
        )


# if __spec__.name == "__main__":
#    celestine.main(__spec__.origin)
