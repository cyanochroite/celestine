""""""

import math

from celestine import bank
from celestine.literal import NONE
from celestine.package import pillow
from celestine.typed import (
    LS,
    A,
    B,
    D,
    H,
    K,
    N,
    P,
    R,
    S,
    Z,
    override,
)
from celestine.window.collection import (
    Area,
    Line,
    Object,
    Plane,
    Point,
    Tree,
)
from celestine.window.container import (
    Image,
    Zone,
)


class Abstract(Object):
    """"""

    item: A  # The object that the window system interacts with.
    parent: K

    area: Area
    canvas: A
    hidden: B
    name: S  # The key to use to find this in the window dictionary.

    action: S  # The action to perform when the user clicks the button.
    fit: Image  # The way the image scales to fit the view space.
    goto: S  # The page to go to when clicked.
    path: S  # The path to the image to use as a background.
    text: S  # Text that describes the purpose of the button's action.

    def click(self, point: Point, **star: R) -> B:
        """"""
        if self.hidden:
            return False

        if point not in self.area:
            return False

        if self.action:
            action = bank.window.work
            argument = self.action
            star = self.star | {"caller": self.name}
            bank.queue(action, argument, star)

        if self.goto:
            action = bank.window.turn
            argument = self.goto
            star = self.star | {}
            bank.queue(action, argument, star)

        return True

    def draw(self, **star: R) -> B:
        """"""
        if self.hidden:
            return False

        return True

    def hide(self) -> N:
        """"""
        self.hidden = True

    def can_make(self, **star: R) -> B:
        """"""
        return True

    def make(self, canvas: A, **star: R) -> N:
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
        self.area = Area.make(0, 0)
        self.canvas = None
        self.hidden = False
        self.name = name
        self.item = None

        self.star = star

        # Contains all remaining keyword arguments.

        def warp(name: S, default: S = NONE) -> N:
            value = star.pop(name, default)
            setattr(self, name, value)

        warp("action")
        # The action to perform when the user triggers the button.

        warp("fit", Image.FILL)
        # The way the image scales to fit the view space.

        warp("goto")
        # The page to go to when clicked.

        warp("path")
        # The path to the image to use as a background.

        warp("text")
        # Text that describes the purpose of the button's action.


class Element(Abstract):
    """"""

    image: A

    @override
    def make(self, canvas: A, **star: R) -> N:
        """"""
        size = self.area.world.size.value
        blender_mode = False
        if pillow and not blender_mode:
            self.image = pillow.new(size)
        else:
            self.image = None

        super().make(canvas, **star)

    def draw(self, **star: R) -> B:
        """"""
        if not super().draw():
            return False

        #  TODO: Check if other types want this here.
        if self.path:
            self.update(self.path)

        return True

    def update(self, path: P, **star: R) -> N:
        """"""
        self.path = path

        image = pillow.open(self.path)

        curent = Plane.make(image.image.width, image.image.height)
        target = Plane.make(*self.area.world.size.value)

        match self.fit:
            case Image.FILL:
                result = curent.scale_to_min(target)
            case Image.FULL:
                result = curent.scale_to_max(target)

        result.center(target)

        image.resize(result.size)
        self.image.paste(image, result)

    def __init__(self, name: S, parent: K, **star: R) -> N:
        super().__init__(name, parent, **star)
        self.image = None


class View(Abstract, Tree):
    """"""

    item: D[S, Abstract]
    width: Z
    height: Z
    element_item: D[S, A]

    def find(self, name: S) -> N | Abstract:
        """"""
        for key, value in self:
            if key == name:
                return value
            if not getattr(value, "find", False):
                continue
            item = value.find(name)
            if item:
                return item
        return None

    def click(self, point: Point, **star: R) -> B:
        if not super().click(point, **star):
            return False

        for _, item in self:
            item.click(point)

        return True

    @override
    def draw(self, **star: R) -> N:
        """"""
        if self.hidden:
            return

        for _, item in self:
            item.draw(**star)

    @override
    def make(self, canvas: A, **star: R) -> N:
        """"""
        for _, item in self:
            item.make(canvas, **star)

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
        for _, item in self:
            this = self.area.world

            one = Line(0, 1)
            one += index % partition_x
            one *= this.one.length // partition_x
            one += this.one.minimum

            two = Line(0, 1)
            two += min(index // partition_x, partition_y - 1)
            two *= this.two.length // partition_y
            two += this.two.minimum

            world = Plane(one, two)

            local = world.copy()
            local -= area.world.origin

            rectangle = Area(local, world)
            item.spot(rectangle)
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

    def __exit__(self, exc_type: A, exc_value: A, traceback: A) -> B:
        if exc_type or exc_value or traceback:
            print("ERROR", exc_type, exc_value, traceback)
        return False

    def __init__(
        self,
        name: S,
        element_item: D[S, A],
        *,
        mode: Zone = Zone.NONE,
        row: Z = 0,
        col: Z = 0,
        **star: R,
    ) -> N:
        #
        self.element_item = element_item
        self._element = element_item["element"]
        self._view = element_item["view"]
        self._window = element_item["window"]

        super().__init__(name, **star)

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

    hold: H
    page: View
    main: S
    code: D[S, A]  # function
    view: D[S, View]

    canvas: A

    def extension(self) -> LS:
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
    ) -> K:
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
        for _, item in self:
            item.draw(**star)

    def make(self, **star: R) -> N:
        """"""
        for _, item in self:
            item.make(self.canvas, **star)

    def turn(self, page: S, **star: R) -> N:
        """"""
        view = self.view.get(page)
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
        for _, item in self:
            item.click(point)

    def find(self, name: S) -> N | Abstract:
        """"""
        for key, value in self:
            if key == name:
                return value
            item = value.find(name)
            if item:
                return item
        raise KeyError(name)

    def spot(self, area: Area) -> N:
        """"""
        self.area = area
        for _, item in self:
            item.spot(area)

    ###############

    def work(self, code: S, **star: R) -> N:
        """"""
        caller = self.code.get(code)
        if not caller:
            return

        caller(**star)
        self.draw(**star)

    def __enter__(self) -> K:
        return self

    def __exit__(self, exc_type: A, exc_value: A, traceback: A) -> B:
        if exc_type:
            raise exc_type
        if exc_value:
            raise exc_value
        if traceback:
            raise traceback

        self.spot(self.area)
        self.make()

        for _, item in self:
            item.hide()

        self.turn(self.main)

        return False

    def __init__(self, element_item: D[S, A], **star: R) -> N:
        super().__init__(**star)
        self.main = ""
        self.area = Area.make(0, 0)
        self.code = {}
        self.view = {}
        self.element_item = element_item
        self.page = View("", element_item, parent=None)
