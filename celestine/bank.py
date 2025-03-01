"""Package wide global variables."""

from celestine.typed import (
    ANY,
    A,
    C,
    L,
    N,
    T,
    ignore,
)

#  These types might not be right.
application: ANY = None  # M
attribute: ANY = None  # LS
configuration: ANY = None  # P
directory: ANY = None  # P
interface: ANY = None  # M
language: ANY = None  # M
window: ANY = None  # Window


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
