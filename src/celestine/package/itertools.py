try:
    import more_itertools
    package = True
except ModuleNotFoundError:
    package = False


def split_when(iterable, predicate):
    if package:
        return list(more_itertools.split_when(iterable, predicate))
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

def filter_true(iterable, predicate=None):
    return list(filter(predicate, iterable))
