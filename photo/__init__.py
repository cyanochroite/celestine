""""""

from celestine.stream import Streamer
from celestine.stream.stream2 import Carrot
from celestine.typed import (
    N,
    ignore,
)
from photo.scan import Scan
from photo.verify import (
    extract,
    generate,
    rename,
    rename_major,
    rename_minor,
    rename_ultra,
    validate_folder,
    validate_record,
)


def scanner() -> N:
    """"""
    print("run scanner")

    root = "/run/media/system/data/celestine/"
    load_it = Streamer(root, "celestine")
    save_it = Streamer(root, "scan")

    scan = Scan(load_it, save_it)
    scan.scan()

    print("end scanner")


def main() -> N:
    """"""
    print("run")

    # scanner()

    # streamer = Streamer("/home/cyanochroite/Pictures/Screenshots/")
    # rename(streamer, rename_minor)
    # rename(streamer, rename_major)
    # rename(streamer, rename_ultra)

    # streamer = Streamer("/run/media/system/data/verify/")
    # validate_record(streamer)

    # streamer = Streamer("/run/media/system/data/picture/game/")

    # generate(streamer)
    # validate(streamer)

    # extract(streamer)

    record = Carrot("/run/media/system/data/verify/Zolg")
    rename(record, rename_major)

    print("end")


ignore(
    rename,
    rename_major,
    rename_minor,
    rename_ultra,
    scanner,
    generate,
    extract,
    scanner,
    main,
    validate_record,
    validate_folder,
)
