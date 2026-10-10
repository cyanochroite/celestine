"""Package wide global variables."""

from celestine.typed import (
    A,
    C,
    L,
    N,
    T,
    ignore,
)

#  These types might not be right.
application: A = None  # M
attribute: A = None  # LS
configuration: A = None  # P
directory: A = None  # P
interface: A = None  # M
language: A = None  # M
window: A = None  # Window

_queue: L[T[C[..., N], A, A]] = []


def queue(action: C[..., N], argument: A, star: A) -> N:
    """Add to event queue and call function at end of update."""
    _queue.append((action, argument, star))


def dequeue() -> N:
    """"""
    for action, argument, star in _queue:
        action(argument, **star)
    _queue.clear()


ignore(
    application,
    attribute,
    configuration,
    dequeue,
    directory,
    interface,
    language,
    queue,
    window,
)
