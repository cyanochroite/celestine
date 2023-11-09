""""""

from celestine.typed import S, H, R, N


def cow(*, say: S, hold: H, **star: R) -> N:
    """"""
    talk = hold.language.DEMO_COW_TALK
    print(talk, say)
