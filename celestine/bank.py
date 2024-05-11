"""Package wide global variables."""

from celestine.typed import (
    LS,
    A,
    B,
    C,
    K,
    L,
    M,
    N,
    P,
    T,
)


class Window:
    """"""

    code: A
    drop: A
    view: A

    def __enter__(self) -> K: ...

    def __exit__(
        self, exc_type: A, exc_value: A, traceback: A
    ) -> B: ...


#  These types might not be right.
application: M = None
attribute: LS = None
configuration: P = None
directory: P = None
interface: M = None
language: M = None
window: Window = Window()

_queue: L[T[C[..., N], A, A]] = []


def queue(action: C[..., N], argument: A, star: A) -> N:
    """Add to event queue and call function at end of update."""
    _queue.append((action, argument, star))


def dequeue() -> N:
    """"""
    for action, argument, star in _queue:
        action(argument, **star)
    _queue.clear()
