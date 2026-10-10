"""Central place for loading and importing external files."""

import io
import lzma
import os
import pathlib
import re
import shutil

from celestine import load
from celestine.literal import (
    FULL_STOP,
    NONE,
)
from celestine.stream.data import (
    Buffering,
    Encoding,
    Errors,
    Mode,
    Newline,
)
from celestine.system import (
    locked,
    unlock,
)
from celestine.typed import (
    LS,
    B,
    Lzma,
    N,
    Open,
    P,
    Path,
    S,
    ignore,
    override,
)


class File:
    """"""

    directory: P

    def load(self, *paths: Path) -> S:
        """"""
        with self.reader(*paths) as file:
            return file.read()

    def path(self, *paths: Path, strict: B = True) -> P:
        """"""
        root = self.directory

        make: S = os.path.join(root, *paths)
        norm: S = os.path.normpath(make)
        real: S = os.path.realpath(norm, strict=strict)

        safe = os.path.commonpath((root, real))

        if not os.path.samefile(root, safe):
            raise RuntimeError()

        result = pathlib.Path(real)
        return result

    def reader(self, *paths: Path) -> Open:
        """"""
        return open(
            self.path(*paths, strict=True),
            Mode.READ_TEXT,
        )

    def save(self, data: S, *paths: Path) -> N:
        """"""
        with self.writer(*paths) as file:
            file.write(data)

    def writer(self, *paths: Path) -> Open:
        """"""
        return open(
            self.path(*paths, strict=False),
            Mode.WRITE_TEXT,
        )

    def __init__(self, root: P) -> N:
        norm: S = os.path.normpath(root)
        real: S = os.path.realpath(norm, strict=True)
        self.directory = pathlib.Path(real)


class Folder:
    """"""

    directory: P

    def load(self, *paths: Path) -> S:
        """"""
        with self.reader(*paths) as file:
            return file.read()

    def path(self, *paths: Path, strict: B = True) -> P:
        """"""
        root = self.directory

        make: S = os.path.join(root, *paths)
        norm: S = os.path.normpath(make)
        real: S = os.path.realpath(norm, strict=strict)

        safe = os.path.commonpath((root, real))

        if not os.path.samefile(root, safe):
            raise RuntimeError()

        result = pathlib.Path(real)
        return result

    def reader(self, *paths: Path) -> Open:
        """"""
        return open(
            self.path(*paths, strict=True),
            Mode.READ_TEXT,
        )

    def save(self, data: S, *paths: Path) -> N:
        """"""
        with self.writer(*paths) as file:
            file.write(data)

    def writer(self, *paths: Path) -> Open:
        """"""
        return open(
            self.path(*paths, strict=False),
            Mode.WRITE_TEXT,
        )

    def __init__(self, root: P) -> N:
        norm: S = os.path.normpath(root)
        real: S = os.path.realpath(norm, strict=True)
        self.directory = pathlib.Path(real)


class Record:
    """"""

    path: P

    def load(self) -> S:
        """"""
        with self.reader() as file:
            return file.read()

    def reader(self) -> Open:
        """"""
        return open(
            self.path,
            Mode.READ_TEXT,
        )

    def save(self, data: S) -> N:
        """"""
        with self.writer() as file:
            file.write(data)

    def writer(self) -> Open:
        """"""
        return open(
            self.path,
            Mode.WRITE_TEXT,
        )

    def __init__(self, root: P) -> N:
        norm: S = os.path.normpath(root)
        real: S = os.path.realpath(norm, strict=True)
        self.directory = pathlib.Path(real)


########################################################################


class Binary(File):
    """"""

    @override
    def reader(self, *paths: Path) -> io.BufferedReader:
        """"""
        return io.BufferedReader(
            open(
                self.path(*paths, strict=True),
                Mode.READ_BINARY.value,
                Buffering.OFF.value,
            )
        )

    @override
    def writer(self, *paths: Path) -> io.BufferedWriter:
        """"""
        return io.BufferedWriter(
            open(
                self.path(*paths, strict=False),
                Mode.WRITE_BINARY.value,
                Buffering.OFF.value,
            )
        )


class Compress(File):
    """"""

    @override
    def reader(self, *paths: Path) -> Lzma:
        """"""
        return lzma.open(
            self.path(*paths, strict=True),
            Mode.READ_BINARY,
        )

    @override
    def writer(self, *paths: Path) -> Lzma:
        """"""
        return lzma.open(
            self.path(*paths, strict=False),
            Mode.WRITE_BINARY,
            format=lzma.FORMAT_XZ,
            check=lzma.CHECK_SHA256,
            preset=9,
        )


class Text(File):
    """"""

    @override
    def reader(self, *paths: Path) -> io.TextIOWrapper:
        """"""
        return open(
            self.path(*paths, strict=True),
            Mode.READ_TEXT.value,
            Buffering.ON.value,
            Encoding.UTF_8.value,
            Errors.STRICT.value,
        )

    @override
    def writer(self, *paths: Path) -> io.TextIOWrapper:
        """"""
        return open(
            self.path(*paths, strict=False),
            Mode.WRITE_TEXT.value,
            Buffering.ON.value,
            Encoding.UTF_8.value,
            Errors.STRICT.value,
        )


class Module(Text):
    """"""

    @override
    def reader(self, *paths: Path) -> io.TextIOWrapper:
        """"""
        ignore(self)
        items = list(map(str, paths))
        file = load.python(*items)
        return super().reader(file)

    @override
    def writer(self, *paths: Path) -> io.TextIOWrapper:
        """"""
        ignore(self)
        items = list(map(str, paths))
        file = load.python(*items)
        return super().writer(file)


########################################################################


def _ignore(directory: S, contents: LS) -> LS:
    """"""
    ignored: LS = []
    for text in contents:
        path = pathlib.Path(directory, text)

        if path.is_dir():
            for pattern in [".git", ".vs", ".vscode", "__pycache__"]:
                pattern = pattern.replace(".", "\\.")
                pattern = pattern.replace("*", ".*")
                if re.match(pattern, text) is not None:
                    ignored.append(text)
                    break
    return ignored


class Pathway:
    """"""

    path: P
    streamer: Streamer

    def load(self, *paths: Path) -> S:
        """"""
        with self.reader(*paths) as file:
            return file.read()

    def path(self, *paths: Path, strict: B = True) -> P:
        """"""
        root = self.directory

        make: S = os.path.join(root, *paths)
        norm: S = os.path.normpath(make)
        real: S = os.path.realpath(norm, strict=strict)

        safe = os.path.commonpath((root, real))

        if not os.path.samefile(root, safe):
            raise RuntimeError()

        result = pathlib.Path(real)
        return result

    def reader(self, *paths: Path) -> Open:
        """"""
        return open(
            self.path(*paths, strict=True),
            Mode.READ_TEXT,
        )

    def save(self, data: S, *paths: Path) -> N:
        """"""
        with self.writer(*paths) as file:
            file.write(data)

    def writer(self, *paths: Path) -> Open:
        """"""
        return open(
            self.path(*paths, strict=False),
            Mode.WRITE_TEXT,
        )

    def __init__(self, streamer: Streamer, *paths: Path) -> N:
        self.path = pathlib.Path(*paths)
        self.streamer = streamer


class Streamer(File):
    """"""

    binary: Binary
    compress: Compress
    module: Module
    text: Text

    def copy(self, source: P, target: P, *, lock: B = False) -> N:
        """"""
        self.remove(target)
        target.parent.mkdir(parents=True, exist_ok=True)

        if source.is_dir():
            shutil.copytree(source, target, ignore=_ignore)
        else:
            shutil.copy2(source, target)

        if lock:
            locked(target)
        else:
            unlock(target)

    def make(self, *paths: Path) -> P:
        """"""
        path = self.path(*paths, strict=False)
        if not path.exists():
            if FULL_STOP in path.name:
                self.text.save(NONE, path)
            else:
                path.mkdir(parents=True, exist_ok=True)
        return path

    def move(self, source: P, target: P, *, lock: B = False) -> N:
        """"""
        self.copy(source, target, lock=lock)
        self.remove(source)

    def pathway(self, *paths: P) -> Pathway:
        """"""
        result = Pathway(self, *paths)
        return result

    def remake(self, *paths: Path) -> P:
        """"""
        self.remove(*paths)
        result = self.make(*paths)
        return result

    def remove(self, *paths: Path) -> P:
        """"""
        path = self.path(*paths, strict=False)
        if not path.exists():
            return path

        unlock(path)

        if path.is_dir():

            shutil.rmtree(path)
        elif path.is_file():
            path.unlink()

        return path

    def __init__(self, *paths: Path) -> N:
        path = pathlib.Path(*paths) if paths else load.project_root()
        self.binary = Binary(path)
        self.compress = Compress(path)
        self.module = Module(path)
        self.text = Text(path)
        super().__init__(path)


ignore(
    Streamer,
)
