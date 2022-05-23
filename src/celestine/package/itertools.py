try:
    import more_itertools as _
    package = True
except ModuleNotFoundError:
    package = False


def split_when(iterable, pred):
    if package:
        return list(more_itertools.split_when(iterable, pred))
    inner = []
    outer = []
    last = None
    for item in iterable:
        if last:
            inner.append(last)
            if pred(last, item):
                outer.append(inner)
                inner = []
        last = item
    if last:
        inner.append(last)
        outer.append(inner)
    return outer
