# more-itertools 8.13.0
# https://more-itertools.readthedocs.io/en/stable/api.html
from celestine.extension import extension
more_itertools = extension("more_itertools")


def split_when(iterable, pred, maxsplit=-1):
    if maxsplit == 0:
        yield list(iterable)
        return

    it = iter(iterable)
    try:
        cur_item = next(it)
    except StopIteration:
        return

    buf = [cur_item]
    for next_item in it:
        if pred(cur_item, next_item):
            yield buf
            if maxsplit == 1:
                yield [next_item] + list(it)
                return
            buf = []
            maxsplit -= 1

        buf.append(next_item)
        cur_item = next_item

    yield buf


def filter_true(iterable, predicate=None):
    return list(filter(predicate, iterable))


def first_true(iterable, default=None, pred=None):
    return more_itertools.first_true(iterable, default, pred)
