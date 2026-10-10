""""""

import datetime
import hashlib
import io
import multiprocessing
import os
import pathlib

from celestine import (
    walk,
)
from celestine.literal import (
    HYPHEN_MINUS,
    LATIN_CAPITAL_LETTER_B,
    LATIN_CAPITAL_LETTER_H,
    LATIN_CAPITAL_LETTER_M,
    LATIN_CAPITAL_LETTER_S,
    LATIN_CAPITAL_LETTER_T,
    LATIN_CAPITAL_LETTER_Y,
    LATIN_CAPITAL_LETTER_Z,
    LATIN_SMALL_LETTER_D,
    LATIN_SMALL_LETTER_M,
    NONE,
    PERCENT_SIGN,
    join,
)
from celestine.stream import (
    Binary,
    Text,
)
from celestine.typed import (
    GP,
    N,
    P,
    S,
)


def get_digest(file: io.BufferedReader) -> S:
    """"""
    fileobj = file
    digest = hashlib.sha256
    file_digest = hashlib.file_digest(fileobj, digest)

    name = file_digest.name
    hexdigest = file_digest.hexdigest()
    result = join(name, HYPHEN_MINUS, hexdigest)

    return result


def get_time(stats: os.stat_result) -> S:
    """%Y%m%dT%H%M%SZ"""
    fromtimestamp = datetime.datetime.fromtimestamp
    timestamp = stats.st_mtime
    timezone = datetime.timezone.utc
    fromtime = fromtimestamp(timestamp, timezone)

    year = (PERCENT_SIGN, LATIN_CAPITAL_LETTER_Y)
    month = (PERCENT_SIGN, LATIN_SMALL_LETTER_M)
    day = (PERCENT_SIGN, LATIN_SMALL_LETTER_D)
    date = (*year, *month, *day, LATIN_CAPITAL_LETTER_T)

    hour = (PERCENT_SIGN, LATIN_CAPITAL_LETTER_H)
    minute = (PERCENT_SIGN, LATIN_CAPITAL_LETTER_M)
    second = (PERCENT_SIGN, LATIN_CAPITAL_LETTER_S)
    time = (*hour, *minute, *second, LATIN_CAPITAL_LETTER_Z)

    fmt = join(*date, *time)
    result = fromtime.strftime(fmt)

    return result


def get_size(stats: os.stat_result) -> S:
    """"""
    st_size = str(stats.st_size)
    zfill = st_size.zfill(10)
    result = join(zfill, LATIN_CAPITAL_LETTER_B)

    return result


def work(path: P) -> S:
    """"""
    result = NONE

    binary = Binary(path.parent)
    with binary.reader(path) as file:
        stats = path.stat()

        modified = get_time(stats)
        size = get_size(stats)
        digest = get_digest(file)
        suffix = path.suffix.lower()

        name = f"{modified}-{size}-{digest}{suffix}"
        if path.name != name:
            result = f"ERROR {path.name} {name}"

    return result


def screenshots() -> GP:
    """"""
    paths = pathlib.Path("/run/media/system/data/picture/game/")
    paths = pathlib.Path("/run/media/system/data/verify")
    for path in paths.iterdir():
        if not path:
            continue
        yield from path.iterdir()


def main2() -> N:
    """"""
    print("run")

    with multiprocessing.Pool() as pool:
        func = work
        iterable = screenshots()
        results = pool.imap_unordered(func, iterable)

        for result in results:
            if result:
                print(result)

    print("end")


def shopy(text: Text, top: P) -> N:
    """"""
    save = pathlib.Path(top, "out.txt")
    with text.writer(save) as file:
        record = sorted(list(walk.records(top)))
        for item in record:
            file.write(f"{item.name}\n")


def main() -> N:
    """"""
    work(
        pathlib.Path(
            "/run/media/system/data/celestine/requirements.txt"
        )
    )
    print("run")

    directory = pathlib.Path("/run/media/system/data/verify")
    text = Text(directory)

    folders = sorted(list(walk.folders(directory)))
    for folder in folders:
        shopy(text, folder)

    print("end")


if __name__ == "__main__":
    main()
