""""""

from celestine.typed import R


def cow(*, say, hold, **star: R):
    """"""
    talk = hold.language.DEMO_COW_TALK
    print(talk, say)
