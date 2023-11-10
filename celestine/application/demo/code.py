""""""

from celestine.typed import (
    H,
    N,
    R,
    S,
)


def cow(*, say: S, hold: H, **star: R) -> N:
    """"""
    talk = hold.language.DEMO_COW_TALK
    print(talk, say)
