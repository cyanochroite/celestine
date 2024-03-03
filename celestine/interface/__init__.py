""""""

import math

from celestine.typed import (
    BOX,
    LS,
    PAIR,
    A,
    B,
    D,
    H,
    I,
    K,
    N,
    P,
    R,
    S,
    T,
    override,
)
from celestine.window import (
    collection,
    container,
)
from celestine.window.collection import (
    Abstract,
    Plane,
    Point,
    Tree,
)
from celestine.window.container import Image as Mode


class Button(Abstract):
    """"""

    def __init__(
        self,
        hold: H,
        name,
        text,
        *,
        call,
        action,
        argument,
        **star: R,
    ):
        self.action = action
        self.argument = argument
        self.call = call
        self.data = text
        super().__init__(hold, name, **star)


class Image(Abstract):
    """"""

    path: P  # The location of the image on disk.
    image: A  # The image object after being loaded from disk.
    size: T[I, I]  # The width and height of the image.
    mode: Mode

    """
    A small version of an image.

    Terminal:
    minimum = 2**4 = 16
    maximum = 2**6 = 64

    Regular:
    minimum = 2**5 = 32
    maximum = 2**8 = 256

    Minimum:
    Smallest thumbnail seems to be 40.
    Resolution of 16 too small for regular images.

    Maximum
    Largest thumbnail seems to be 250.
    Keeping it within a byte (256) a nice goal.
    """

    def update(self, path: P, **star: R) -> N:
        """"""
        self.path = path

    def resize(self, size):
        """"""
        (size_x, size_y) = size
        (area_x, area_y) = self.area.size

        down_x = math.floor(area_y * size_x / size_y)
        down_y = math.floor(area_x * size_y / size_x)

        best_x = min(area_x, down_x)
        best_y = min(area_y, down_y)

        return (best_x, best_y)

    def scale_to_fit(self, area):
        """"""
        (size_x, size_y) = self.size
        (area_x, area_y) = area

        down_x = math.floor(area_y * size_x / size_y)
        down_y = math.floor(area_x * size_y / size_x)

        best_x = min(area_x, down_x)
        best_y = min(area_y, down_y)

        return (best_x, best_y)

    def __init__(self, hold: H, name, path, *, mode, **star: R):
        pillow = hold.package.pillow

        self.path = path

        if pillow:
            self.image = pillow.new((0, 0))
        else:
            # Blender
            self.image = None
        self.mode = mode

        super().__init__(hold, name, **star)
        # minimum = 2**6
        # maximum = 2**16
        # minimum = 2**5
        # maximum = 2**8

    """
    A small version of an image.

    Terminal:
    minimum = 2**5 = 32
    maximum = 2**7 = 128

    Regular:
    minimum = 2**05 = 64
    maximum = 2**13 = 8192

    Minimum:
    Fairly good detail preservation at 64 pixels.

    Maximum
    Biggest TV is 8k and "biggest" monitors are less then 8K.
    """

    def resize_(self, size):
        # TODO this is old
        x_size, y_size = self.size
        return (math.floor(x_size), math.floor(y_size))

    def crop(self, source_length: PAIR, target_length: PAIR) -> BOX:
        """"""

        (source_length_x, source_length_y) = source_length
        (target_length_x, target_length_y) = target_length

        source_ratio = source_length_x / source_length_y
        target_ratio = target_length_x / target_length_y

        if source_ratio < target_ratio:
            length = round(source_length_x / target_ratio)
            offset = round((source_length_y - length) / 2)
            return (0, 0 + offset, source_length_x, length + offset)

        if source_ratio > target_ratio:
            length = round(source_length_y * target_ratio)
            offset = round((source_length_x - length) / 2)
            return (0 + offset, 0, length + offset, source_length_y)

        return (0, 0, source_length_x, source_length_y)


class Label(Abstract):
    """"""

    def __init__(self, hold: H, name, text, **star: R):
        self.data = text
        super().__init__(hold, name, **star)


class View1(Abstract, Tree):
    """"""

    item: D[S, Abstract]

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

    def click(self, point: Point) -> B:
        if not super().click(point):
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
        super().make(canvas, **star)

        for _, item in self:
            item.make(canvas, **star)

    @override
    def spot(self, area: Plane) -> N:
        """"""
        super().spot(area)
        length = max(1, len(self))

        match self.mode:
            case container.Zone.DROP:
                partition_x = 1
                partition_y = length
            case container.Zone.SPAN:
                partition_x = length
                partition_y = 1
            case container.Zone.GRID:
                partition_x = self.width
                partition_y = math.ceil(length / self.width)
            case container.Zone.NONE:
                partition_x = 1
                partition_y = 1

        size_x, size_y = self.area.size
        index = 0

        fragment_x = size_x // partition_x
        fragment_y = size_y // partition_y

        for _, item in self:
            index_x = index % partition_x
            index_y = min(index // partition_x, partition_y - 1)
            index += 1

            left = self.area.one.minimum
            upper = self.area.two.minimum

            ymin = upper + fragment_y * (index_y + 0)
            ymax = upper + fragment_y * (index_y + 1)
            xmin = left + fragment_x * (index_x + 0)
            xmax = left + fragment_x * (index_x + 1)

            one = collection.Line(xmin, xmax)
            two = collection.Line(ymin, ymax)

            rectangle = Plane(one, two)
            item.spot(rectangle)

    def zone(
        self,
        name: S,
        *,
        mode=container.Zone.NONE,
        **star: R,
    ) -> K:
        """"""
        return self.set(
            self._view(
                self.hold,
                name,
                self.element_item,
                mode=mode,
                parent=self,
                **star,
            )
        )

    def drop(self, name: S, **star: R) -> K:
        """"""
        return self.zone(name, mode=container.Zone.DROP, **star)

    def span(self, name: S, **star: R) -> K:
        """"""
        return self.zone(name, mode=container.Zone.SPAN, **star)

    def __enter__(self) -> K:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> B:
        return False

    def __init__(
        self,
        hold,
        name,
        element_item,
        *,
        mode=container.Zone.NONE,
        row=0,
        col=0,
        **star: R,
    ) -> N:
        #
        self.element_item = element_item
        # self._button = element_item["button"]
        # self._image = element_item["image"]
        # self._label = element_item["label"]
        self._abstract = element_item["abstract"]
        self._view = element_item["view"]
        self._window = element_item["window"]

        super().__init__(hold, name, **star)

        self.width = col
        self.height = row
        self.mode = mode

        for range_y in range(row):
            for range_x in range(col):
                name = f"{self.name}_{range_x}-{range_y}"
                self.set(
                    Abstract(
                        hold,
                        name,
                        self,
                    )
                )

    def new2(
        self, name, *, text="", path="", code="", view="", **star: R
    ) -> N:
        """"""
        if text != "" and path != "":
            raise AttributeError("text and path can't both be set")

        if code != "" and view != "":
            raise AttributeError("code and view path can't both be set")

        call = None
        action = container.Call.NONE
        work = None

        if view:
            call = view
            action = container.Call.VIEW
            work = self._window.turn

        if code:
            call = code
            action = container.Call.WORK
            work = self._window.work

        if action == container.Call.NONE:
            if path:
                self.set(
                    self._image(
                        self.hold,
                        name,
                        path,
                        parent=self,
                        **star,
                    )
                )
            else:
                self.set(
                    self._label(
                        self.hold,
                        name,
                        text,
                        parent=self,
                        **star,
                    )
                )
        else:
            self.set(
                self._button(
                    self.hold,
                    name,
                    text,
                    parent=self,
                    call=work,  # the window function to call
                    action=call,  # the name of the user function
                    argument=star,
                    **star,
                )
            )

    def element(self, name: S, **star: R) -> N:
        """"""
        self.set(
            self._abstract(
                self.hold,
                name,
                self,
                **star,
            )
        )


class View(View1):
    """"""

    def button(self, name: S, task: S, /, text: S, **star: R) -> N:
        self.element(name, action=task, text=text, **star)

    def link(self, name: S, task: S, /, text: S, **star: R) -> N:
        self.element(name, goto=task, text=text, **star)

    def icon(self, name: S, /, **star: R) -> N:
        self.element(name, fit=Mode.FILL, **star)

    def image(self, name: S, /, **star: R) -> N:
        self.element(name, fit=Mode.FULL, **star)

    def label(self, name: S, /, text: S, **star: R) -> N:
        self.element(name, text=text, **star)


class Window(Tree):
    """"""

    hold: H
    page: View
    code: D[S, A]  # function
    view: D[S, View]

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

    def drop(self, name: S, **star: R,) -> K:
        """"""
        return self.set(
            self.element_item["view"](
                self.hold,
                name,
                self.element_item,
                mode=container.Zone.DROP,
                parent=self,
                **star,
            )
        )

    ###############
    # star might not be needed for all functions
    # but it will stay for now for ease of itegration later

    def click(self, point: Point, **star: R) -> N:
        """"""
        for _, item in self:
            item.click(point, **star)

    def draw(self, **star: R) -> N:
        """"""
        for _, item in self:
            item.draw(**star)

    def make(self, canvas: A, **star: R) -> N:
        """"""
        self.canvas = canvas
        for _, item in self:
            item.make(canvas, **star)

    def spot(self, area: Plane, **star: R) -> N:
        """"""
        self.area = area
        for _, item in self:
            item.spot(area, **star)

    ###############
    # No star functions

    def find(self, name: S) -> N | Abstract:
        """"""
        for key, value in self:
            if key == name:
                return value
            item = value.find(name)
            if item:
                return item
        raise KeyError(name)

    ###############

    def turn(self, page: S, **star: R) -> N:
        """"""
        view = self.view.get(page)
        if not view:
            return

        self.page.hide()
        self.page = view
        self.page.show()
        self.draw()

    def work(self, code: S, **star: R) -> N:
        """"""
        caller = self.code.get(code)
        if not caller:
            return

        caller(self.hold, **star)
        self.draw(**star)

    def __enter__(self) -> K:
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            raise exc_type
        if exc_value:
            raise exc_value
        if traceback:
            raise traceback

        self.spot(self.area)
        self.make(None)

        for _, item in self:
            item.hide()

        self.turn(self.hold.main)

        return False

    def __init__(self, hold: H, element_item, **star: R) -> N:
        super().__init__(**star)
        self.area = Plane.make(0, 0)
        self.hold = hold
        self.code = {}
        self.view = {}
        self.element_item = element_item
        self.page = View(hold, "", element_item, parent=None)
