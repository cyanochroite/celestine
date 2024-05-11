"""Package wide global variables."""

from celestine.interface import Window
from celestine.typed import (
    LS,
    A,
    C,
    L,
    M,
    N,
    P,
    T,
)

#  These types might not be right.
application: M = None
attribute: LS = None
configuration: P = None
directory: P = None
interface: M = None
language: M = None
window: Window

_queue: L[T[C[..., N], A, A]] = []


def queue(action: C[..., N], argument: A, star: A) -> N:
    """Add to event queue and call function at end of update."""
    _queue.append((action, argument, star))


def dequeue() -> N:
    """"""
    for action, argument, star in _queue:
        action(argument, **star)
    _queue.clear()
