"""Package wide global variables."""

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
application: M
attribute: LS
configuration: P
directory: P
interface: M
language: M
window: A  # Window

_queue: L[T[C[..., N], A, A]] = []


def queue(action: C[..., N], argument: A, star: A) -> N:
    """Add to event queue and call function at end of update."""
    _queue.append((action, argument, star))


def dequeue() -> N:
    """"""
    for action, argument, star in _queue:
        action(argument, **star)
    _queue.clear()
