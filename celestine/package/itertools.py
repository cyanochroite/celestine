"""More routines for operating on iterables, beyond itertools."""

from celestine.typed import (
    A,
    G,
    I,
    L,
    N,
    R,
    S,
)

from . import Abstract


class Package(Abstract):
    """"""

    def split_when(
        self, iterable: A, pred: A, maxsplit: I = -1
    ) -> G[A, N, N]:
        """Split this when we feel like it."""
        if maxsplit == 0:
            yield list(iterable)
            return

        itt = iter(iterable)
        try:
            cur_item = next(itt)
        except StopIteration:
            return

        buf = [cur_item]
        for next_item in itt:
            if pred(cur_item, next_item):
                yield buf
                if maxsplit == 1:
                    yield [next_item] + list(itt)
                    return
                buf = []
                maxsplit -= 1

            buf.append(next_item)
            cur_item = next_item

        yield buf

    def filter_true(self, iterable, predicate=None) -> L[A]:
        """Filter when we see a True value."""
        return list(filter(predicate, iterable))

    def first_true(self, iterable, default=None, pred=None) -> L[A]:
        """Return the first True value."""
        return next(filter(pred, iterable), default)

    def __init__(self, name: S, **star: R) -> N:
        super().__init__(name, pypi="more_itertools")
