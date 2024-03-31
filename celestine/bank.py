"""Package wide global variables."""


from celestine.typed import (
    LS,
    A,
    C,
    D,
    L,
    M,
    N,
    P,
    S,
    T,
)

#  These types might not be right.
application: M
attribute: LS
code: D[S, C]
configuration: P
directory: P
interface: M
language: M
main: S
package: M  # Package
view: D[S, C]
window: M

_queue: L[T[C[..., N], A, A]] = []


def queue(action: C[..., N], argument: A, star: A) -> N:
    """Add to event queue and call function at end of update."""
    _queue.append((action, argument, star))


def dequeue() -> N:
    """"""
    for action, argument, star in _queue:
        action(argument, **star)
        # self.window.work(action, **star)
        # self.window.turn(action, **star)
    _queue.clear()
