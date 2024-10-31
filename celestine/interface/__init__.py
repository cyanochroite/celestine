""""""

import math
import pathlib

from celestine import bank
from celestine.typed import (
    BF,
    GA,
    GS,
    LS,
    TY,
    A,
    B,
    D,
    G,
    K,
    N,
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


class Object:
    """"""

    star: R

    def pull(self, name: S, cast: TY[A] = str, default: A = None) -> A:
        """Extracts keyword arguments from star object and returns."""
        try:
            pop = self.star.pop(name)
            value = cast(pop)
        except KeyError:
            value = default
        return value

    def warp(self, name: S, cast: TY[A] = str, default: A = None) -> N:
        """Extracts keyword arguments from star object and saves."""
        try:
            pop = self.star.pop(name)
            value = cast(pop)
        except KeyError:
            value = default
        setattr(self, name, value)

    def __init__(self, **star: R) -> N:
        super().__init__()
        ignore(self)
        self.star = star


class Abstract(Object):
    """"""

    parent: K

    area: Area
    canvas: A
    hidden: B
    name: S  # The key to use to find this in the window dictionary.

    action: S  # The action to perform when the user clicks the button.
    fit: Image  # The way the image scales to fit the view space.
    goto: S  # The page to go to when clicked.
    path: P  # The path to the image to use as a background.
    text: S  # Text that describes the purpose of the button's action.

    def click(self, point: Point, **star: R) -> B:
        """"""
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
        return not self.hidden

    def hide(self) -> N:
        """"""
        self.hidden = True

    def can_build(self, **star: R) -> B:
        """"""
        ignore(self)
        return True

    def build(self, canvas: A, **star: R) -> N:
        """"""
        self.canvas = canvas

    def show(self) -> N:
        """"""
        self.hidden = False

    def spot(self, area: Area) -> N:
        """"""
        self.area = area

    def __init__(self, name: S, parent: K, **star: R) -> N:
        super().__init__(**star)
        self.parent = parent
        self.area = Area.fast(0, 0)
        self.canvas = None
        self.hidden = False
        self.name = name

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

    image: A
    item: A

    def __init__(self, name: S, parent: K, **star: R) -> N:
        super().__init__(name, parent, **star)
        self.image = None
        self.item = None


class Tree[X](Object):
    """"""

    # TODO Python 3.12: Make class Tree[TYPE] and replace ANY.
    _children: D[S, Abstract]

    def find(self, name: S) -> Abstract:
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

    def get(self, name: S) -> Abstract:
        """"""
        result = self._children[name]
        return result

    def items(self) -> GA:
        """"""
        iterator = iter(self._children.items())
        yield from iterator

    def keys(self) -> GS:
        """"""
        iterator = iter(self._children.keys())
        yield from iterator

    def set(self, item: Abstract) -> Abstract:
        """"""
        self._children[item.name] = item
        return item

    def values(self) -> G[Abstract, N, N]:
        """"""
        iterator = iter(self._children.values())
        yield from iterator

    def __bool__(self) -> B:
        boolean = bool(self._children)
        return boolean

    def __init__(self, **star: R) -> N:
        self._children = {}
        super().__init__(**star)

    def __len__(self) -> Z:
        length = len(self._children)
        return length


class View(Abstract, Tree):
    """"""

    item: D[S, Abstract]
    width: Z
    height: Z
    element_item: D[S, A]
    tree: Tree[K]

    def click(self, point: Point, **star: R) -> B:
        if not super().click(point, **star):
            return False

        for value in self.values():
            value.click(point)

        return True

    @override
    def draw(self, **star: R) -> N:
        """"""
        if self.hidden:
            return

        for value in self.values():
            value.draw(**star)

    @override
    def build(self, canvas: A, **star: R) -> N:
        """"""
        for value in self.values():
            value.build(canvas, **star)

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
                parent=self,
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

    def __exit__(self, exc_type: A, exc_value: A, traceback: A) -> BF:
        ignore(self)
        if exc_type or exc_value or traceback:
            print("ERROR", exc_type, exc_value, traceback)
        return False

    def __init__(
        self,
        name: S,
        element_item: D[S, A],
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

        for range_y in range(row):
            for range_x in range(col):
                name = f"{self.name}_{range_x}-{range_y}"
                self.set(
                    Abstract(
                        name,
                        self,
                    )
                )

    def element(self, name: S, **star: R) -> N:
        """"""
        self.set(
            self._element(
                name,
                self,
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
    code: Dictionary[A]  # function
    view: Dictionary[View]

    canvas: A

    @staticmethod
    def extension() -> LS:
        """"""
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

    def drop(
        self,
        name: S,
        **star: R,
    ) -> Abstract:
        """"""
        return self.set(
            self.element_item["view"](
                name,
                self.element_item,
                mode=Zone.DROP,
                parent=self,
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

    def build(self, **star: R) -> N:
        """"""
        for value in self.values():
            value.build(self.canvas, **star)

    def turn(self, page: S, **star: R) -> N:
        """"""
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
        self.draw(**star)

    def run(self) -> N:
        """"""
        self.spot(self.area)
        self.build()

        for value in self.values():
            value.hide()

        self.page.name = self.main
        self.turn(self.main)

    def __init__(self, element_item: D[S, A], **star: R) -> N:
        super().__init__(**star)
        self.main = ""
        self.area = Area.fast(0, 0)
        self.code = Dictionary()
        self.view = Dictionary()
        self.element_item = element_item
        self.page = View("", element_item, parent=None)
