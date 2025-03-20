""""""

from celestine.data import wrapper
from celestine.typed import (
    R,
    Z,
)


class Event:
    """"""

    type: Z
    button: Z


@wrapper(__name__)
def wait(**star: R) -> Event:
    """"""
    raise NotImplementedError()
