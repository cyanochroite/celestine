""""""

import itertools
import math
import typing
from typing import NamedTuple

from celestine import bank
from celestine.literal import (
    VERTICAL_LINE,
    join,
)

# from celestine.package import PIL
from celestine.typed import (
    BF,
    DA,
    IT,
    LS,
    TA,
    TZ2,
    A,
    B,
    D,
    G,
    K,
    N,
    P,
    R,
    S,
    T,
    Z,
    ignore,
    override,
)
from celestine.window.collection import (
    Dictionary,
)
from celestine.window.container import (
    Image,
    Zone,
)


class Point(NamedTuple):
    """"""

    x_var: Z
    y_var: Z


class Plane(NamedTuple):
    """"""

    x_len: Z
    x_max: Z
    x_min: Z
    y_len: Z
    y_max: Z
    y_min: Z
    z_len: Z

    @property
    def centroid(self) -> Point:
        """"""
        # TODO: Optimize this by eliminate the need.
        x_var = (self.x_min + self.x_max) // 2
        y_var = (self.y_min + self.y_max) // 2
        result = Point(x_var, y_var)
        return result

    @classmethod
    def make(
        cls,
        x_max: Z = 0,
        y_max: Z = 0,
        x_min: Z = 0,
        y_min: Z = 0,
    ) -> K:
        """"""
        x_len = x_max - x_min + 1
        y_len = y_max - y_min + 1
        z_len = x_len * y_len
        result = cls(
            x_len,
            x_max,
            x_min,
            y_len,
            y_max,
            y_min,
            z_len,
        )
        return result

    def __contains__(self, item: object) -> B:
        if not isinstance(item, Point):
            raise TypeError

        result = (
            self.x_min <= item.x_var <= self.x_max
            and self.y_min <= item.y_var <= self.y_max
        )
        return result


class Spot:
    """Yields all rows one at a time from all children."""

    @staticmethod
    def divide(length: Z, partition: Z) -> G[T[Z, Z], N, N]:
        """"""
        quotient, remainder = divmod(length, partition)

        stop = 0
        for index in range(partition):
            start = stop
            stop += quotient + 1 if index < remainder else quotient
            yield start, stop - 1

    def drop(self) -> G[Plane, N, N]:
        """Zone.DROP"""
        y_divide = self.divide(self.view.area.y_len, self.length)
        for y_min, y_max in y_divide:
            result = Plane.make(
                self.view.area.x_max,
                self.view.area.y_min + y_max,
                self.view.area.x_min,
                self.view.area.y_min + y_min,
            )
            yield result

    def grid(self) -> G[Plane, N, N]:
        """Zone.GRID"""
        partition_x = self.view.width
        partition_y = math.ceil(self.length / self.view.width)
        y_divide = self.divide(self.view.area.y_len, partition_y)
        for y_min, y_max in y_divide:
            x_divide = self.divide(self.view.area.x_len, partition_x)
            for x_min, x_max in x_divide:
                result = Plane.make(
                    self.view.area.x_min + x_max,
                    self.view.area.y_min + y_max,
                    self.view.area.x_min + x_min,
                    self.view.area.y_min + y_min,
                )
                yield result

    def none(self) -> G[Plane, N, N]:
        """Zone.NONE"""
        for _ in range(self.length):
            result = Plane.make(
                self.view.area.x_max,
                self.view.area.y_max,
                self.view.area.x_min,
                self.view.area.y_min,
            )
            yield result

    def span(self) -> G[Plane, N, N]:
        """Zone.SPAN"""
        x_divide = self.divide(self.view.area.x_len, self.length)
        for x_min, x_max in x_divide:
            result = Plane.make(
                self.view.area.x_min + x_max,
                self.view.area.y_max,
                self.view.area.x_min + x_min,
                self.view.area.y_min,
            )
            yield result

    def __init__(self, view: Element) -> N:
        self.view = view
        self.length = len(self.view)

    def __iter__(self) -> G[Plane, N, N]:
        match self.view.mode:
            case Zone.DROP:
                yield from self.drop()
            case Zone.SPAN:
                yield from self.span()
            case Zone.GRID:
                yield from self.grid()
            case Zone.NONE:
                yield from self.none()

    def __len__(self) -> Z:
        result = self.length
        return result


class Object:
    """"""

    _data: TA
    _star: DA

    def copy(self) -> K:
        """"""
        result = self.__class__(*self._data, **self._star)
        return result

    def get_data(self) -> TA:
        """"""
        result = self._data
        return result

    def get_star(self) -> DA:
        """"""
        result = self._star
        return result

    @classmethod
    def make(cls, *data: A, **star: R) -> K:
        """"""
        result = cls(*data, **star)
        return result

    def pull(self, name: S, default: A = None) -> A:
        """Extracts keyword arguments from star object and returns."""
        result = self._star.get(name, default)
        return result

    def warp(self, name: S, default: A = None) -> N:
        """Extracts keyword arguments from star object and saves."""
        value = self._star.get(name, default)
        setattr(self, name, value)

    def __init__(self, *data: A, **star: R) -> N:
        super().__init__(*data, **star)
        self._data = data
        self._star = star


class Mapping:
    """"""

    _children: D[S, K]

    def items(self) -> typing.ItemsView:
        """"""
        result = self._children.items()
        return result

    def keys(self) -> typing.KeysView:
        """"""
        result = self._children.keys()
        return result

    def values(self) -> typing.ValuesView:
        """"""
        result = self._children.values()
        return result

    def __delitem__(self, key: S) -> N:
        del self._children[key]

    def __getitem__(self, subscript: S) -> K:
        result = self._children[subscript]
        return result

    def __init__(self, *data: A, **star: R) -> N:
        ignore(data, star)
        self._children = {}

    def __iter__(self) -> IT[K]:
        values = self._children.values()
        result = iter(values)
        return result

    def __len__(self) -> Z:
        result = len(self._children)
        return result

    def __setitem__(self, key: S, value: A) -> N:
        self._children[key] = value


class Abstract(Object, Mapping):
    """"""

    name: S  # The key to use to find this in the window dictionary.
    area: Plane

    hidden: B
    item: A  # The cached object that is being drawn.
    parent: K  # The parent object in the tree.
    canvas: A  # The object to draw ourselfs into.

    action: S  # The action to perform when the user clicks the button.
    fit: Image  # The way the image scales to fit the view space.
    goto: S  # The page to go to when clicked.
    path: P  # The path to the image to use as a background.
    text: S  # Text that describes the purpose of the button's action.

    is_dirty: B  # Tells the renderer if we should redraw ourself.

    def build(self, parent: A, star: D[S, A]) -> N:
        """"""
        self.parent = parent
        star |= {}

    def click(self, point: Point, **star: R) -> N:
        """"""
        ignore(point)

        if self.action:
            bank.queue(
                bank.window.work,
                self.action,
                self.get_star() | {"caller": self.name},
            )

        if self.goto:
            bank.queue(
                bank.window.turn,
                self.goto,
                self.get_star() | {},
            )

    def draw(self) -> B:
        """"""
        if self.hidden:
            return False

        if not self.is_dirty:
            return False

        self.is_dirty = False

        for value in self:
            value.draw()

        return True

    def find(self, name: S) -> K:
        """"""
        for key, value in self.items():
            if key == name:
                return value
            try:
                return value.find(name)
            except AttributeError:
                pass
            except KeyError:
                pass
        raise KeyError(name)

    def hide(self) -> N:
        """"""
        self.hidden = True
        self.make_dirty()

    def image_size(self, size: TZ2, scale: TZ2 = (1, 1)) -> Plane:
        """"""
        result = Plane.create(*size)
        target = Plane.create(*self.area.size)
        target *= scale

        if self.fit == Image.FILL:
            result.scale_to_min(target)
        elif self.fit == Image.FULL:
            result.scale_to_max(target)

        result.center(target)
        return result

    def make_dirty(self) -> N:
        """"""
        self.is_dirty = True
        if self.parent:
            self.parent.make_dirty()

    def show(self) -> N:
        """"""
        self.hidden = False
        self.make_dirty()

    def spot(self, area: Plane) -> N:
        """"""
        self.area = area

    def __init__(self, *data: A, **star: R) -> N:
        super().__init__(*data, **star)

        self.area = Plane.make()
        self.name = data[0]

        self.hidden = False
        self.is_dirty = True
        self.item = None
        self.parent = None
        self.canvas = None

        # Contains all remaining keyword arguments.

        self.warp("action")
        # The action to perform when the user triggers the button.

        self.warp("fit", Image.FILL)
        # The way the image scales to fit the view space.

        self.warp("goto")
        # The page to go to when clicked.

        self.warp("path")
        # The path to the image to use as a background.

        self.warp("text")
        # Text that describes the purpose of the button's action.


class Element(Abstract):
    """"""

    # image: A
    # item: A
    # path: A
    # text: A

    _element: A
    _window: A

    mode: Zone
    width: Z
    height: Z

    _hide = (
        """
    def imagin(
        self,
        image: PIL.Image.Image,
        plane: Plane,
        size: Point,
        mode: S,
    ) -> PIL.Image.Image:
        """
        """
        ignore(self)
        plane = plane.round()
        result = PIL.Image.new(mode, size.data)
        im = image.resize(plane.size.data)
        box = plane.data
        result.paste(im, box)
        return result

    """
    )

    def element(self, name: S, **star: R) -> N:
        """"""
        mode = star.get("mode", Zone.NONE)
        item = self.make(
            name,
            mode=mode,
            **star,
        )
        self[item.name] = item

    def reimage(self, path: P, **star: R) -> N:
        """"""
        ignore(self, path, star)
        # self.path = path

    def retext(self, text: S, **star: R) -> N:
        """"""
        ignore(self, text, star)
        # self.text = text

    @override
    def spot(self, area: Plane) -> N:
        """"""
        super().spot(area)

        values = Spot(self)
        for value, world in itertools.zip_longest(self, values):
            value.spot(world)

    def zone(self, name: S, *, mode: Zone, **star: R) -> K:
        """"""
        item = self.make(
            name,
            mode=mode,
            **star,
        )
        self[item.name] = item
        return item

    def __enter__(self) -> K:
        return self

    def __exit__(self, exc_type: A, exc_value: A, traceback: A) -> BF:
        ignore(self)
        if exc_type or exc_value or traceback:
            print("ERROR", exc_type, exc_value, traceback)
        return False

    def __init__(self, name: S, *, mode: Zone, **star: R) -> N:
        super().__init__(name, **star)

        row = self.pull("row", 0)
        col = self.pull("col", 0)

        self.width = col
        self.height = row
        self.mode = mode

        match self.mode:
            case Zone.DROP:
                self.width = 1
                self.height = 0
            case Zone.SPAN:
                self.width = 0
                self.height = 1
            case Zone.GRID:
                self.width = col
                self.height = row
            case Zone.NONE:
                self.width = 1
                self.height = 1

    # syntax sugar

    def button(self, name: S, task: S, /, text: S, **star: R) -> N:
        """"""
        self.element(name, action=task, text=text, **star)

    def drop(self, name: S, **star: R) -> K:
        """"""
        result = self.zone(name, mode=Zone.DROP, **star)
        return result

    def grid(self, name: S, **star: R) -> K:
        """"""
        result = self.zone(name, mode=Zone.GRID, **star)
        return result

    def icon(self, name: S, /, **star: R) -> N:
        """"""
        self.element(name, fit=Image.FILL, **star)

    def image(self, name: S, /, **star: R) -> N:
        """"""
        self.element(name, fit=Image.FULL, **star)

    def label(self, name: S, /, text: S, **star: R) -> N:
        """"""
        self.element(name, text=text, **star)

    def link(self, name: S, task: S, /, text: S, **star: R) -> N:
        """"""
        self.element(name, goto=task, text=text, **star)

    def span(self, name: S, **star: R) -> K:
        """"""
        result = self.zone(name, mode=Zone.SPAN, **star)
        return result


class Mouse(Abstract):
    """"""

    def __init__(self, **star: R) -> N:
        ignore(self)
        super().__init__("mouse", **star)


class Window(Element):
    """"""

    main: S
    code: Dictionary[A]  # function
    view: Dictionary[Element]

    item: Element

    @classmethod
    def extension(cls) -> LS:
        """"""
        ignore(cls)
        return [
            ".bmp",
            ".sgi",
            ".rgb",
            ".bw",
            ".png",
            ".jpg",
            ".jpeg",
            ".jp2",
            ".j2c",
            ".tga",
            ".cin",
            ".dpx",
            ".exr",
            ".hdr",
            ".tif",
            ".tiff",
            ".webp",
            ".pbm",
            ".pgm",
            ".ppm",
            ".pnm",
            ".gif",
            ".png",
        ]

    @classmethod
    def formats(cls) -> LS:
        """Pillow Image Formats."""
        ignore(cls)
        return [
            "BLP",
            "BMP",
            "BUFR",
            "CUR",
            "DCX",
            "DDS",
            "DIB",
            "EPS",
            "FITS",
            "FLI",
            "FTEX",
            "GBR",
            "GIF",
            "GRIB",
            "HDF5",
            "ICNS",
            "ICO",
            "IM",
            "IPTC",
            "JPEG",
            "JPEG2000",
            "MPEG",
            "MSP",
            "PCD",
            "PCX",
            "PIXAR",
            "PNG",
            "PPM",
            "PSD",
            "QOI",
            "SGI",
            "SUN",
            "TGA",
            "TIFF",
            "WEBP",
            "WMF",
            "XBM",
            "XPM",
        ]

    ###############
    # star might not be needed for all functions
    # but it will stay for now for ease of itegration later

    def clicker(self, item: A, point: Point, **star: R) -> N:
        """"""
        if item.hidden:
            return

        if point not in item.area:
            return

        item.click(point, **star)

        for value in item:
            self.clicker(value, point, **star)

    def builder(self, item: A, parent: A, star: D[S, A]) -> N:
        """"""
        deep = star.copy()
        item.build(parent, deep)

        if item.path:
            item.reimage(item.path)

        if item.text:
            item.retext(item.text)

        for value in item:
            self.builder(value, item, deep)

    def turn(self, page: S, **star: R) -> N:
        """"""
        key = join(self.item.name, VERTICAL_LINE, page)
        view = self.view.get(key)
        if not view:
            return

        self.item.hide()
        self.item = view
        self.item.show()
        self.draw()

    ###############
    # No star functions

    ###############

    def work(self, code: S, **star: R) -> N:
        """"""
        key = join(self.item.name, VERTICAL_LINE, code)
        caller = self.code.get(key)
        if not caller:
            return

        caller(**star)
        # TODO: Sometimes this is called when nothing is changed.
        self.draw()

    def run(self) -> N:
        """"""
        self.spot(self.area)
        self.builder(self, None, {})

        for value in self:
            value.hide()

        self.item.name = self.main
        self.turn(self.main)

    def __init__(self) -> N:
        super().__init__("window", mode=Zone.NONE)
        self.main = ""
        self.code = Dictionary()
        self.view = Dictionary()
        self.item = Element("", mode=Zone.NONE)


ignore(Element, Mouse, Window)
