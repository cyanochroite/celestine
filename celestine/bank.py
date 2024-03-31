"""Package wide global variables."""


from celestine.package import Package
from celestine.typed import (
    LS,
    C,
    D,
    M,
    P,
    S,
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
package: Package
view: D[S, C]
window: M

_queue = []


def queue(action, argument, star):
    """Add to event queue and call function at end of update."""
    _queue.append((action, argument, star))


def dequeue(self):
    """"""
    for action, argument, star in _queue:
        action(argument, **star)
    _queue.clear()


# _queue: L[T[C[..., N], A, A]]: []
# def queue(self, action: C[..., N], argument: A, star: A) -> N:
#    """Add to event queue and call function at end of update."""
#    self._queue.append((action, argument, star))
# def dequeue(self) -> N:
#    """"""
#    for action, argument, star in self._queue:
#        action(argument, **star)
#            self.window.work(action, **star)
#            self.window.turn(action, **star)
#    self._queue.clear()
