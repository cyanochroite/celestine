"""
more-itertools 8.13.0
https://more-itertools.readthedocs.io/en/stable/api.html
"""


def split_when(iterable, pred, maxsplit=-1):
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


def filter_true(iterable, predicate=None):
    """Filter when we see a True value."""
    return list(filter(predicate, iterable))


def first_true(iterable, default=None, pred=None):
    """Return the first True value."""
    return next(filter(pred, iterable), default)
