from celestine.package import package
more_itertools = package("more_itertools")


def split_when_external(iterable, predicate):
    return list(more_itertools.split_when(iterable, predicate))


def split_when_internal(iterable, predicate):
    inner = []
    outer = []
    last = None
    for item in iterable:
        if last:
            inner.append(last)
            if predicate(last, item):
                outer.append(inner)
                inner = []
        last = item
    if last:
        inner.append(last)
        outer.append(inner)
    return outer

def split_when(iterable, predicate):
    return (split_when_external if more_itertools else split_when_internal)(iterable, predicate)


def filter_true(iterable, predicate=None):
    return list(filter(predicate, iterable))
