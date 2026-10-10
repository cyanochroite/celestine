""""""

import datetime
import hashlib
import io
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
    LINE_FEED,
    LOW_LINE,
    NONE,
    PERCENT_SIGN,
    join,
)
from celestine.stream import (
    Binary,
    Streamer,
)
from celestine.stream.stream2 import Carrot
from celestine.typed import (
    LP,
    C,
    D,
    Digest,
    N,
    P,
    S,
    Z,
    ignore,
)

########################################################################


def get_digest(fileobj: io.BufferedReader, digest: Digest) -> S:
    """"""
    file_digest = hashlib.file_digest(fileobj, digest)

    name = file_digest.name
    hexdigest = file_digest.hexdigest()
    result = join(name, HYPHEN_MINUS, hexdigest)

    return result


def get_size(stats: os.stat_result, width: Z) -> S:
    """"""
    st_size = str(stats.st_size)
    zfill = st_size.zfill(width)
    result = join(zfill, LATIN_CAPITAL_LETTER_B)

    return result


def get_time(stats: os.stat_result) -> S:
    """%Y%m%dT%H%M%SZ"""
    timestamp = stats.st_mtime
    timezone = datetime.timezone.utc
    fromtimestamp = datetime.datetime.fromtimestamp(timestamp, timezone)

    year = (PERCENT_SIGN, LATIN_CAPITAL_LETTER_Y)
    month = (PERCENT_SIGN, LATIN_SMALL_LETTER_M)
    day = (PERCENT_SIGN, LATIN_SMALL_LETTER_D)
    date = (*year, *month, *day, LATIN_CAPITAL_LETTER_T)

    hour = (PERCENT_SIGN, LATIN_CAPITAL_LETTER_H)
    minute = (PERCENT_SIGN, LATIN_CAPITAL_LETTER_M)
    second = (PERCENT_SIGN, LATIN_CAPITAL_LETTER_S)
    time = (*hour, *minute, *second, LATIN_CAPITAL_LETTER_Z)

    fmt = join(*date, *time)
    result = fromtimestamp.strftime(fmt)

    return result


########################################################################


type Rename = C[[Binary, P], S]
type Rename2 = C[[io.BufferedReader], S]


def rename(carrot: Carrot, function: Rename2) -> N:
    """"""
    for record in carrot.records():
        name = record.name

        with streamer.binary.reader(path) as file:
            name = function(file)

        target = path.with_name(name)
        path.rename(target)

        print(name)


def renamer(streamer: Streamer, function: Rename) -> N:
    """"""
    directory = streamer.directory
    for record in walk.records(directory):
        path: P = record
        name = function(streamer.binary, path)
        target = path.with_name(name)
        path.rename(target)

        print(name)


def _rename(streamer: Streamer, function: Rename) -> N:
    """"""
    directory = streamer.directory
    for record in walk.records(directory):
        path: P = record
        name = function(streamer.binary, path)
        target = path.with_name(name)
        path.rename(target)

        print(name)


def _renamer2(path: P, streamer: Streamer, function: Rename) -> S:
    """"""
    result = path.name

    with streamer.binary.reader(path) as file:
        result = function(file)

    return result


def renamer(path: P, streamer: Streamer, function: Rename) -> N:
    """"""
    name = _renamer2(path, streamer, function)
    target = path.with_name(name)
    path.rename(target)

    print(name)


def boost(file: io.BufferedReader) -> S:
    """
    150 characters

    index.html________________________________________
    __________________________________________________
    000000000000B-md5-d41d8cd98f00b204e9800998ecf8427e
    """
    path = pathlib.Path(file.name)
    path_name = path.name[0:100]
    stats = path.stat()

    name = f"{path_name:_<100s}"
    time = get_time(stats)
    dash1 = HYPHEN_MINUS
    size = get_size(stats, 12)
    dash2 = HYPHEN_MINUS
    digest = get_digest(file, hashlib.md5)
    suffix = path.suffix.lower()
    result = join(name, time, dash1, size, dash2, digest, suffix)

    return result


def major(file: io.BufferedReader) -> S:
    """
    100 characters

    19700101T000000Z-0000000000B-sha256-e3b0c44298fc1c
    149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    """
    path = pathlib.Path(file.name)
    stats = path.stat()

    time = get_time(stats)
    dash1 = HYPHEN_MINUS
    size = get_size(stats, 10)
    dash2 = HYPHEN_MINUS
    digest = get_digest(file, hashlib.sha256)
    suffix = path.suffix.lower()
    result = join(time, dash1, size, dash2, digest, suffix)

    return result


def minor(file: io.BufferedReader) -> S:
    """
    50 characters

    000000000000B-md5-d41d8cd98f00b204e9800998ecf8427e
    """
    path = pathlib.Path(file.name)
    stats = path.stat()

    size = get_size(stats, 12)
    dash = HYPHEN_MINUS
    digest = get_digest(file, hashlib.md5)
    suffix = suffix = path.suffix.lower()
    result = join(size, dash, digest, suffix)

    return result


def ultra(file: io.BufferedReader) -> S:
    """
    200 characters

    index.html________________________________________
    __________________________________________________
    19700101T000000Z-0000000000B-sha256-e3b0c44298fc1c
    149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    """
    path = pathlib.Path(file.name)
    path_name = path.name[0:100]
    stats = path.stat()

    name = f"{path_name:_<100s}"
    time = get_time(stats)
    dash1 = HYPHEN_MINUS
    size = get_size(stats, 10)
    dash2 = HYPHEN_MINUS
    digest = get_digest(file, hashlib.sha256)
    suffix = path.suffix.lower()
    result = join(name, time, dash1, size, dash2, digest, suffix)

    return result


# 32
# 64
# 96
# C8

ignore(
    rename,
)
