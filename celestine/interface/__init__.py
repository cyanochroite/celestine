""""""

import collections.abc
import math
import pathlib

from celestine import bank
from celestine.typed import (
    ANY,
    BF,
    IT,
    LS,
    TZ2,
    B,
    D,
    K,
    N,
    Object,
    P,
    R,
    S,
    Z,
    ignore,
    override,
)
from celestine.window.collection import (
    Area,
    Dictionary,
    Line,
    Plane,
    Point,
)
from celestine.window.container import (
    Image,
    Zone,
)


class Tree(Object, collections.abc.MutableMapping[S, ANY]):
    """"""

    children: D[S, K]
    name: S  # The key to use to find this in the window dictionary.

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

    def set(self, item: K) -> K:
        """"""
        self.children[item.name] = item
        return item

    def __delitem__(self, key: S) -> N:
        del self.children[key]

    def __getitem__(self, key: S) -> K:
        return self.children[key]

    def __init__(self, name: S, **star: R) -> N:
        super().__init__(**star)
        self.name = name
        self.children = {}

    def __iter__(self) -> IT[S]:
        return iter(self.children)

    def __len__(self) -> Z:
        return len(self.children)

    def __setitem__(self, key: S, value: ANY) -> N:
        self.children[key] = value


class Abstract(Tree):
    """"""

    area: Area
    canvas: ANY
    hidden: B

    action: S  # The action to perform when the user clicks the button.
    fit: Image  # The way the image scales to fit the view space.
    goto: S  # The page to go to when clicked.
    path: P  # The path to the image to use as a background.
    text: S  # Text that describes the purpose of the button's action.

    def click(self, point: Point, **star: R) -> B:
        """"""
        ignore(star)
        if self.hidden:
            return False

        if point not in self.area:
            return False

        if self.action:
            bank.queue(
                bank.window.work,
                self.action,
                self.star | {"caller": self.name},
            )

        if self.goto:
            bank.queue(
                bank.window.turn,
                self.goto,
                self.star | {},
            )

        return True

    def draw(self, **star: R) -> B:
        """"""
        ignore(star)
        return not self.hidden

    def hide(self) -> N:
        """"""
        self.hidden = True

    def build(self, parent: ANY, **star: R) -> N:
        """"""
        ignore(star)
        self.canvas = parent

    def show(self) -> N:
        """"""
        self.hidden = False

    def spot(self, area: Area) -> N:
        """"""
        self.area = area

    def image_size(self, size: TZ2, scale: TZ2 = (1, 1)) -> Plane:
        """"""
        result = Plane.create(*size)
        target = Plane.create(*self.area.world.size)
        target *= scale

        if self.fit == Image.FILL:
            result.scale_to_min(target)
        elif self.fit == Image.FULL:
            result.scale_to_max(target)

        result.center(target)
        return result

    def __init__(self, name: S, **star: R) -> N:
        super().__init__(name, **star)
        self.area = Area.fast(0, 0)
        self.canvas = None
        self.hidden = False

        self.star = star

        # Contains all remaining keyword arguments.

        self.warp("action")
        # The action to perform when the user triggers the button.

        self.warp("fit", Image, Image.FILL)
        # The way the image scales to fit the view space.

        self.warp("goto")
        # The page to go to when clicked.

        self.warp("path", pathlib.Path)
        # The path to the image to use as a background.

        self.warp("text")
        # Text that describes the purpose of the button's action.


class Element(Abstract):
    """"""

    image: ANY
    item: ANY

    @override
    def build(self, parent: ANY, **star: R) -> N:
        """"""
        super().build(parent, **star)

        if self.path:
            self.reimage(self.path)

        if self.text:
            self.retext(self.text)

    def reimage(self, path: P, **star: R) -> N:
        """"""
        ignore(star)
        self.path = path

    def retext(self, text: S, **star: R) -> N:
        """"""
        ignore(star)
        self.text = text

    def __init__(self, name: S, **star: R) -> N:
        super().__init__(name, **star)
        self.image = None
        self.item = None


class View(Abstract):
    """"""

    item: D[S, Abstract]
    width: Z
    height: Z
    element_item: D[S, Abstract]

    def click(self, point: Point, **star: R) -> B:
        if not super().click(point, **star):
            return False

        for value in self.values():
            value.click(point)

        return True

    @override
    def draw(self, **star: R) -> B:
        """"""
        if self.hidden:
            return False

        for value in self.values():
            value.draw(**star)

        return True

    @override
    def build(self, parent: ANY, **star: R) -> N:
        """"""
        super().build(parent, **star)
        for value in self.values():
            value.build(parent, **star)

    @override
    def spot(self, area: Area) -> N:
        """"""
        super().spot(area)

        length = max(1, len(self))
        match self.mode:
            case Zone.DROP:
                partition_x = 1
                partition_y = length
            case Zone.SPAN:
                partition_x = length
                partition_y = 1
            case Zone.GRID:
                partition_x = self.width
                partition_y = math.ceil(length / self.width)
            case Zone.NONE:
                partition_x = 1
                partition_y = 1

        index = 0
        for value in self.values():
            this = self.area.world

            one = Line(0, 1)
            one += index % partition_x
            one *= this.one.length // partition_x
            one += this.one.one

            two = Line(0, 1)
            two += min(index // partition_x, partition_y - 1)
            two *= this.two.length // partition_y
            two += this.two.one

            world = Plane(one, two)

            local = world.copy()
            local -= area.world.origin

            rectangle = Area(local, world)
            value.spot(rectangle)
            index += 1

    def zone(
        self,
        name: S,
        *,
        mode: Zone = Zone.NONE,
        **star: R,
    ) -> K:
        """"""
        return self.set(
            self._view(
                name,
                self.element_item,
                mode=mode,
                **star,
            )
        )

    def drop(self, name: S, **star: R) -> K:
        """"""
        return self.zone(name, mode=Zone.DROP, **star)

    def span(self, name: S, **star: R) -> K:
        """"""
        return self.zone(name, mode=Zone.SPAN, **star)

    def __enter__(self) -> K:
        return self

    def __exit__(
        self,
        exc_type: ANY,
        exc_value: ANY,
        traceback: ANY,
    ) -> BF:
        ignore(self)
        if exc_type or exc_value or traceback:
            print("ERROR", exc_type, exc_value, traceback)
        return False

    def __init__(
        self,
        name: S,
        element_item: D[S, ANY],
        *,
        mode: Zone = Zone.NONE,
        **star: R,
    ) -> N:
        super().__init__(name, **star)
        row = self.pull("row", int, 0)
        col = self.pull("col", int, 0)

        self.element_item = element_item
        self._element = element_item["element"]
        self._view = element_item["view"]
        self._window = element_item["window"]

        self.width = col
        self.height = row
        self.mode = mode

    def element(self, name: S, **star: R) -> N:
        """"""
        self.set(
            self._element(
                name,
                **star,
            )
        )

    # syntax sugar

    def button(self, name: S, task: S, /, text: S, **star: R) -> N:
        """"""
        self.element(name, action=task, text=text, **star)

    def link(self, name: S, task: S, /, text: S, **star: R) -> N:
        """"""
        self.element(name, goto=task, text=text, **star)

    def icon(self, name: S, /, **star: R) -> N:
        """"""
        self.element(name, fit=Image.FILL, **star)

    def image(self, name: S, /, **star: R) -> N:
        """"""
        self.element(name, fit=Image.FULL, **star)

    def label(self, name: S, /, text: S, **star: R) -> N:
        """"""
        self.element(name, text=text, **star)


class Window(Tree):
    """"""

    page: View
    main: S
    code: Dictionary[ANY]  # function
    view: Dictionary[View]

    canvas: ANY

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

    def drop(self, name: S, **star: R) -> Tree:
        """"""
        return self.set(
            self.element_item["view"](
                name,
                self.element_item,
                mode=Zone.DROP,
                **star,
            )
        )

    ###############
    # star might not be needed for all functions
    # but it will stay for now for ease of itegration later

    def draw(self, **star: R) -> N:
        """"""
        for value in self.values():
            value.draw(**star)

    def build(self, parent: ANY, **star: R) -> N:
        """"""
        for value in self.values():
            value.build(parent, **star)

    def turn(self, page: S, **star: R) -> N:
        """"""
        ignore(star)
        key = f"{self.page.name}::{page}"
        view = self.view.get(key)
        if not view:
            return

        self.page.hide()
        self.page = view
        self.page.show()
        self.draw()

    ###############
    # No star functions

    def click(self, point: Point) -> N:
        """"""
        for value in self.values():
            value.click(point)

    def spot(self, area: Area) -> N:
        """"""
        self.area = area
        for value in self.values():
            value.spot(area)

    ###############

    def work(self, code: S, **star: R) -> N:
        """"""
        key = f"{self.page.name}::{code}"
        caller = self.code.get(key)
        if not caller:
            return

        caller(**star)
        # TODO: Sometimes this is called when nothing is changed.
        self.draw(**star)

    def run(self) -> N:
        """"""
        self.spot(self.area)
        self.build(self.canvas)

        for value in self.values():
            value.hide()

        self.page.name = self.main
        self.turn(self.main)

    def __init__(self, element_item: D[S, ANY], **star: R) -> N:
        super().__init__("window", **star)
        self.main = ""
        self.area = Area.fast(0, 0)
        self.code = Dictionary()
        self.view = Dictionary()
        self.element_item = element_item
        self.page = View("", element_item)


ignore(Element, Window)
