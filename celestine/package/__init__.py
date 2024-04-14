""""""
from celestine.window.collection import (
    Plane,
    Point,
)
from celestine import (
    bank,
    package,
)
import random
import importlib
import importlib.abc
import importlib.machinery
import sys
import types
import typing
import pathlib
from typing import override
import os
from celestine.unicode import (
    ESCAPE,
    SPACE,
)
from celestine.typed import LS
from celestine.typed import (
    M,
    N,
    A,
    P,
    LS,
    GP,
    LP,
    B,
    S,
    D,
    OS,
    I,
    R,
    IMAGE,
    LI,
    LS,
    I,
    K,
    N,
    P,
    R,
    S,
    T,
    FN,
    GP,
    LP,
    LS,
    A,
    B,
    D,
    G,
    L,
    M,
    N,
    P,
    S,
    T,
    string,
)

CELESTINE = "celestine"
FULL_STOP = "."


def project_path() -> P:
    """When running as a package, sys.path[0] is wrong."""
    for path in sys.path:
        directory = pathlib.Path(path, CELESTINE)
        if directory.is_dir():
            return directory
    directory = pathlib.Path(os.curdir)
    return directory


class Abstract:
    """"""

    name: S
    package: M | N

    def main(self, package: M, path: S) -> N:
        """"""
        sys.argv.append(path)
        package.main()

    def module(self) -> LS:
        """The 'import PACKAGE.MODULE' name."""
        return []

    def run(self) -> N:
        """"""

        if not self.package:
            return

        argv = sys.argv

        path = str(project_path())
        sys.argv = [path, path]
        try:
            module = package(self.name, *self.module())
            self.main(module, path)
        except SystemExit:
            pass

        sys.argv = argv

    def __bool__(self) -> B:
        return self.package is not None

    def __getattr2__(self, name: S) -> S:
        return getattr(self.package, name)

    def __init__(self, name: S, pypi: OS = None, **star: R) -> N:
        self.name = name
        self.pypi = pypi or name

        # pygame prints an anoying message on import
        # so this here to hide any messages a package may print
        # when being imported
        sys_stdout = sys.stdout

        with open(
            os.devnull,
            "wt",
            encoding="utf-8",
            #            stream.Mode.WRITE_TEXT.value,
            #            encoding=stream.Encoding.UTF_8.value,

        ) as stdout:
            sys.stdout = stdout  # as TextIO
            try:
                self.package = package(self.pypi)
            except ModuleNotFoundError:
                self.package = None
                # found = f"Package '{self.name}' not found."
                # install = f"Install with 'pip install {self.pypi}'."
                # message = f"{found} {install}"
                # logging.warning(message)

        sys.stdout = sys_stdout


class Package:
    """"""

    dictionary: D[S, M]

    def __getattr__(self, name: S) -> M:
        """"""
        try:
            return self.dictionary[name]
        except KeyError as error:
            message = f"'{PACKAGE}' object has no attribute '{name}'"
            raise AttributeError(message) from error

    def __init__(self, **star: R) -> N:
        self.dictionary = {}
        argument = load.argument(PACKAGE)
        for name in argument:
            attribute = load.attribute(PACKAGE, name, "Package")
            package = attribute(name)
            self.dictionary[name] = package


def walk(*path: S) -> G[T[S, LS, LS], N, N]:
    """Yields a 3-tuple (dirpath, dirnames, filenames)."""
    top = pathlib.Path(*path)
    topdown = True
    onerror = None
    followlinks = False
    return os.walk(top, topdown, onerror, followlinks)


def walk_file(top: P, include: LS, exclude: LS) -> GP:
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


def walk_python(top: P, include: LS, exclude: LS) -> LP:
    """"""
    include = [".py", *include]
    exclude = [
        ".mypy_cache",
        ".ruff_cache",
        "__pycache__",
        *exclude,
    ]
    return walk_file(top, include, exclude)


def package(base: S, *path: S) -> M:
    """Load an external package from the system path."""
    iterable = [base, *path]
    name = FULL_STOP.join(iterable)
    result = importlib.import_module(name)
    return result


type SO = typing.Sequence[str] | None
type OM = types.ModuleType | None
type MS = importlib.machinery.ModuleSpec | None
type N = None


class _autoflake(Abstract):
    """Removes unused imports and unused variables."""


class _black(Abstract):
    """The uncompromising code formatter."""

    def main(self, package: M, path: S) -> N:
        """"""
        sys.argv.append(path)
        package.patched_main()


class _curses(Abstract):
    """Terminal handling for character-cell displays."""

    def window(self, column: I, row: I, width: I, height: I) -> A:
        """"""
        nlines = height
        ncols = width
        begin_y = row
        begin_x = column
        return self.package.newwin(nlines, ncols, begin_y, begin_x)

    def subwindow(
        self, window, column: I, row: I, width: I, height: I
    ) -> A:
        """"""
        nlines = height
        ncols = width
        begin_y = row
        begin_x = column
        return window.subwin(nlines, ncols, begin_y, begin_x)

    def __getattr__(self, name: S) -> A:
        result = None
        match name:
            case "KEY_EXIT":
                result = ord(ESCAPE)
            case "KEY_CLICK":
                result = ord(SPACE)
            case "space":
                result = 32
            case "quit":
                result = 113
            case "down":
                result = 258
            case "up":
                result = 259
            case "left":
                result = 260
            case "right":
                result = 261
            case "initscr":
                # This a temporary fix for windows-curses.
                # https://github.com/zephyrproject-rtos/windows-curses/
                # issues/50#issuecomment-1840485627
                _curses = package("_curses")
                for key, value in _curses.__dict__.items():
                    if key[0:4] == "ACS_" or key in ("LINES", "COLS"):
                        setattr(self.package, key, value)
                result = _curses.initscr
            case _:
                result = getattr(self.package, name)
        return result


class _dearpygui(Abstract):
    """DearPyGui: A simple Python GUI Toolkit."""

    def tag_root(self, tag: S) -> S:
        """"""
        root = tag.split("_")[0]
        combine = f"{root}"
        return combine

    def __init__(self, name: S, **star: R) -> N:
        super().__init__(name, pypi="dearpygui.dearpygui")


class _isort(Abstract):
    """A Python utility / library to sort Python imports."""

    def module(self) -> LS:
        """"""
        return ["main"]


class _platformdirs(Abstract):
    """A package for determining appropriate platform-specific dirs."""

    def __init__(self, name, pypi=None, **star):
        self.directory = pathlib.Path(os.getcwd())


class _pydocstringformatter(Abstract):
    """A tool to automatically format Python docstrings."""

    def main(self, package: M, path: S) -> N:
        """
        This package is troublesome.

        It can't find the pyproject file unless run from root directory.
        Exclude argument simply does not work.
        Manually feeding it files works.
        """
        location = os.getcwd()
        os.chdir(sys.path[0])

        files = walk_python(path, [], ["unicode"])

        file = map(str, files)
        argv = [*file]
        package.run_docstring_formatter(argv)

        os.chdir(location)


class _pygame(Abstract):
    """Python Game Development."""

    image: M

    def __getattr__(self, name: S) -> A:
        result = None
        match name:
            case _:
                result = getattr(self.package, name)
        return result


class _pyupgrade(Abstract):
    """Removes unused imports and unused variables."""

    def main(self, package: M, path: S) -> N:
        """
        This package has no configuration file options.

        Since no way to configure exclude files, we do it ourself.
        """
        # TODO: This is breaking the language files. Find out why.
        files = walk_python(path, [], ["language"])

        file = map(str, files)
        argv = [*file, "--py311-plus"]
        package.main(argv)

    def module(self) -> LS:
        """"""
        return ["_main"]


class _tkinter(Abstract):
    """Python interface to Tcl/Tk."""


########################################################################
COLORS = 15  # int(255 - 8 / 16)


class Image:
    """"""

    image: IMAGE

    def brightwing(self):
        """
        Brightwing no like the dark colors.

        Make image bright.
        """

        def brighter(pixel: I) -> I:
            invert = (255 - pixel) / 255
            boost = invert * 64
            shift = pixel + boost
            return shift

        hue, saturation, value = self.image.convert("HSV").split()
        new_value = value.point(brighter)

        bands = (hue, saturation, new_value)

        merge = package.pillow.Image.merge("HSV", bands)
        self.image = merge.convert("RGB")

    @classmethod
    def clone(cls, self: K) -> K:
        """"""
        image = self.image.copy()
        return cls(image)

    def convert(self, mode: S) -> N:
        """"""
        matrix = None  # Unused default.
        dither = package.pillow.Image.Dither.FLOYDSTEINBERG
        palette = package.pillow.Image.Palette.WEB  # Unused default.
        colors = 256  # Unused default.

        hold = self.image.convert(mode, matrix, dither, palette, colors)
        self.image = hold

    def convert_to_alpha(self) -> N:
        """"""
        self.convert("RGBA")

    def convert_to_color(self) -> N:
        """"""
        self.convert("RGB")

    def convert_to_mono(self) -> N:
        """"""
        self.convert("1")

    def copy(self) -> K:
        """"""
        return self.clone(self)

    def getdata(self) -> LI:
        """"""
        return self.image.getdata()

    @property
    def size(self):
        """"""
        return self.image.size

    def resize(self, point: Point) -> N:
        """"""
        size = point.value
        resample = package.pillow.Image.Resampling.LANCZOS
        box = None
        reducing_gap = None
        self.image = self.image.resize(
            size,
            resample,
            box,
            reducing_gap,
        )

    def paste(self, image: K, plane: Plane) -> N:
        """"""
        im = image.image
        box = plane.value
        mask = None
        self.image.paste(im, box, mask)

    def quantize(self):
        """"""
        pillow = bank.package.pillow
        # Median Cut only works in RGB mode.
        self.convert_to_color()

        colors = COLORS
        method = pillow.Image.Quantize.MEDIANCUT
        kmeans = 0
        palette = None
        dither = pillow.Image.Dither.FLOYDSTEINBERG

        self.image = self.image.quantize(
            colors, method, kmeans, palette, dither
        )

    def __init__(self, image: IMAGE, **star: R):
        self.image = image


class _pillow(Abstract):
    """Python Imaging Library (Fork)."""

    def new(self, size: T[I, I]) -> Image:
        """"""
        mode = "RGBA"
        color = (250, 250, 0, 250)
        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            255,
        )

        image = self.package.Image.new(mode, size, color)

        item = Image(image)
        return item

    def open(self, path: P) -> Image:
        """"""
        file = self.package.Image.open(
            fp=path,
            mode="r",
            formats=None,
        )

        image = file.convert(
            mode="RGBA",
            matrix=None,
            dither=self.package.Image.Dither.NONE,
            palette=self.package.Image.Palette.ADAPTIVE,
            colors=256,
        )

        item = Image(image)
        return item

    def extension(self) -> LS:
        """"""
        dictionary = self.package.Image.registered_extensions()
        items = dictionary.items()
        values = self.package.Image.OPEN
        result = [key for key, value in items if value in values]
        result.sort()
        return result

    def __init__(self, name: S, **star: R) -> N:
        super().__init__(name, pypi="PIL")
        if self.package:
            setattr(self, "ImageTk", package("PIL", "ImageTk"))


class Loader(importlib.abc.Loader):
    """"""

    _COMMON_PREFIX = "myapp.virtual."

    def __init__(self):
        self._services = {}
        # create a dummy module to return when Python attempts to import
        # myapp and myapp.virtual, the :-1 removes the last "." for
        # aesthetic reasons :)
        self._dummy_module = types.ModuleType(self._COMMON_PREFIX[:-1])
        # set __path__ so Python believes our dummy module is a package
        # this is important, since otherwise Python will believe our
        # dummy module can have no submodules
        self._dummy_module.__path__ = []

    @override
    def create_module(self, spec: importlib.machinery.ModuleSpec) -> OM:
        """"""
        names = spec.name.split(".")
        name = names[-1]

        print(spec.name, name, "HI")
        match name:
            case "autoflake":
                return _autoflake(name)
            case "black":
                return _black(name)
            case "curses":
                return _curses(name)
            case "dearpygui":
                return _dearpygui(name)
            case "isort":
                return _isort(name)
            case "pillow":
                return _pillow(name)
            case "platformdirs":
                return _platformdirs(name)
            case "pydocstringformatter":
                return _pydocstringformatter(name)
            case "pygame":
                return _pygame(name)
            case "pyupgrade":
                return _pyupgrade(name)
            case "tkinter":
                return _tkinter(name)
            case _:
                return None

    @override
    def exec_module(self, module: M) -> N:
        return None
