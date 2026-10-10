""""""

from celestine.typed import (
    R,
    Z,
    ignore,
)


class Event:
    """"""

    type: Z
    button: Z


def wait(**star: R) -> Event:
    """"""
    raise NotImplementedError()


ignore(wait)
