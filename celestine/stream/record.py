""""""

import io
import lzma

from celestine.stream.data import (
    Buffering,
    Encoding,
    Errors,
    Mode,
    Newline,
)
from celestine.typed import (
    Load,
    Lzma,
    N,
    Open,
    P,
    S,
    Save,
    ignore,
    override,
)


class Abstract:
    """"""

    path: P

    def load(self, call: Load) -> S:
        """"""
        with self.reader() as file:
            if call:
                result = call(file)
            else:
                result = file.read()
            return result

    @property
    def name(self) -> S:
        """"""
        result = self.path.name
        return result

    def reader(self) -> Open:
        """"""
        return open(
            self.path,
            Mode.READ_TEXT,
        )

    def rename(self, name: S) -> N:
        """"""
        target = self.path.with_name(name)
        self.path = self.path.rename(target)

    def save(self, data: S, call: Save) -> N:
        """"""
        with self.writer() as file:
            if call:
                call(file, data)
            else:
                file.write(data)

    def writer(self) -> Open:
        """"""
        return open(
            self.path,
            Mode.WRITE_TEXT,
        )

    def __init__(self, path: P) -> N:
        """"""
        self.path = path

    def __str__(self) -> S:
        """"""
        result = str(self.path)
        return result


class Binary(Abstract):
    """"""

    @override
    def reader(self) -> io.BufferedReader:
        """"""
        return io.BufferedReader(
            open(
                self.path,
                Mode.READ_BINARY.value,
                Buffering.OFF.value,
            )
        )

    @override
    def writer(self) -> io.BufferedWriter:
        """"""
        return io.BufferedWriter(
            open(
                self.path,
                Mode.WRITE_BINARY.value,
                Buffering.OFF.value,
            )
        )


class Compress(Abstract):
    """"""

    @override
    def reader(self) -> Lzma:
        """"""
        return lzma.open(
            self.path,
            Mode.READ_BINARY,
        )

    @override
    def writer(self) -> Lzma:
        """"""
        return lzma.open(
            self.path,
            Mode.WRITE_BINARY,
            format=lzma.FORMAT_XZ,
            check=lzma.CHECK_SHA256,
            preset=9,
        )


class Document(Abstract):
    """"""

    @override
    def reader(self) -> io.TextIOWrapper:
        """"""
        return open(
            self.path,
            Mode.READ_TEXT.value,
            Buffering.ON.value,
            Encoding.UTF_8.value,
            Errors.STRICT.value,
            Newline.APPLE,
        )

    @override
    def writer(self) -> io.TextIOWrapper:
        """"""
        return open(
            self.path,
            Mode.WRITE_TEXT.value,
            Buffering.ON.value,
            Encoding.UTF_8.value,
            Errors.STRICT.value,
            Newline.APPLE,
        )


ignore(
    Abstract,
    Binary,
    Compress,
    Document,
)
