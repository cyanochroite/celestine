""""""

import functools
import itertools
import operator
import pathlib

from celestine import walk
from celestine.stream import Streamer
from celestine.typed import (
    N,
    P,
    S,
    Z,
    ignore,
)


class Scan:
    """"""

    @staticmethod
    def encode(text: S) -> Z:
        """"""
        iterable = map(ord, text)

        index = range(1, 6)
        cycle = itertools.cycle(index)

        sequence = map(operator.mul, iterable, cycle)
        total = functools.reduce(operator.add, sequence)

        result = total % 10000
        return result

    def read(self, load_path: P, save_path: P) -> N:
        """"""
        save_path.parent.mkdir(parents=True, exist_ok=True)
        with self.load_it.text.reader(load_path) as load_file:
            with self.save_it.text.writer(save_path) as save_file:
                for line in load_file:
                    value = self.encode(line)
                    text = f"{value:04}\n"
                    save_file.write(text)

    def scan(self) -> N:
        """"""
        load_path = self.load_it.directory
        save_path = self.save_it.directory
        for path in walk.python(load_path, [], []):
            load: P = path
            file = load.relative_to(load_path)
            save = pathlib.Path(save_path, file).with_suffix(".txt")
            self.read(load, save)

    def __init__(self, load_it: Streamer, save_it: Streamer) -> N:
        self.load_it = load_it
        self.save_it = save_it


ignore(
    Scan,
)
