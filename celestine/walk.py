"""Central place for loading and importing external files."""

import importlib
import importlib.resources
import pathlib
import re

from celestine.literal import (
    ASTERISK,
    FULL_STOP,
    INIT,
    NONE,
    join,
)
from celestine.typed import (
    GM,
    GP,
    LS,
    B,
    C,
    G,
    N,
    P,
    S,
    T,
    ignore,
)


def record(top: P, include: LS, exclude: LS) -> GP:
    """
    Item 'name_exclude': a list of directory names to exclude.

    Item 'suffix_include': a list of file name suffix to include
    if none, it ignores it.
    """
    included = set(include)
    excluded = set(exclude)

    for dirpath, dirnames, filenames in walk(top):
        for dirname in dirnames:
            if dirname in excluded:
                dirnames.remove(dirname)

        for filename in filenames:
            path = pathlib.Path(dirpath, filename)
            suffix = path.suffix.lower()
            if not included or suffix in included:
                yield path


def iterdir(directory: P, skip: C[[P], B], pattern: S = NONE) -> GP:
    """"""
    pattern = pattern or join(FULL_STOP, ASTERISK)
    regex = re.compile(pattern)
    for item in directory.iterdir():
        if not item:
            continue

        path: P = item
        if skip(path):
            continue

        string = path.name
        if regex.fullmatch(string):
            yield path


def records(directory: P, pattern: S = NONE) -> GP:
    """"""

    def skip(path: P) -> B:
        result = not path.is_file()
        return result

    # raise DeprecationWarning("Don't use records")
    yield from iterdir(directory, skip, pattern)


def folders(directory: P, pattern: S = NONE) -> GP:
    """"""

    def skip(path: P) -> B:
        result = not path.is_dir()
        return result

    yield from iterdir(directory, skip, pattern)


def folder(top: P, exclude: LS) -> GP:
    """
    Item 'name_exclude': a list of directory names to exclude.

    Item 'suffix_include': a list of file name suffix to include
    if none, it ignores it.
    """
    excluded = set(exclude)

    for dirpath, dirnames, _ in walk(top):
        for dirname in dirnames:
            if dirname not in excluded:
                path = pathlib.Path(dirpath, dirname)
                yield path


def package(base: S) -> GM:
    """Load all decorated functions from all modules found in path."""
    find = importlib.import_module(base)
    spec = find.__spec__
    if not spec:
        raise NotImplementedError("Why is your spec None?")
    if not spec.origin:
        raise NotImplementedError("Why is your spec origin also None?")
    spot = pathlib.Path(spec.origin)
    if spot.stem != INIT:
        yield find
        return

    root = spot.parent
    walked = python(root, [], [])
    for item in walked:
        if not item:
            continue
        path: P = item
        with_name = path.with_name(path.stem)
        # relative to what though?
        relative_to = with_name.relative_to(root)
        parts = relative_to.parts
        strip = parts[:-1] if parts[-1] == INIT else parts
        name = FULL_STOP.join((base, *strip))
        yield importlib.import_module(name)


def python(path: P, include: LS, exclude: LS) -> GP:
    """"""
    include = [
        ".py",
        *include,
    ]
    exclude = [
        ".mypy_cache",
        ".ruff_cache",
        "__pycache__",
        *exclude,
    ]
    yield from record(path, include, exclude)


def walk(path: P) -> G[T[P, LS, LS], N, N]:
    """Yields a 3-tuple (dirpath, dirnames, filenames)."""
    top_down = True
    on_error = None
    follow_symlinks = False
    yield from path.walk(top_down, on_error, follow_symlinks)


ignore(
    folder,
    folders,
    package,
    python,
    record,
    records,
    walk,
)
