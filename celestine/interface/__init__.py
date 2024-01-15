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
    Tree,
)
from celestine.window.container import Image as Mode


class Button(Abstract):
    """"""

    def click_action(self) -> N:
        """"""
        self.hold.queue(self.call, self.action, self.argument)

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


class View(Abstract, Tree):
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

    def click_action(self) -> N:
        pass

    def click(self, point: collection.Point) -> N:
        if self.hidden:
            return

        if point not in self.area:
            return

        self.click_action()

        for _, item in self:
            item.click(point)

    @override
    def draw(self, **star: R) -> N:
        """"""
        if self.hidden:
            return

        for _, item in self:
            item.draw(**star)

    @override
    def make(self, canvas: A, **star: R) -> B:
        """"""
        super().make(canvas, **star)

        for _, item in self:
            item.make(canvas, **star)

        return True

    def new(
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
                self.element,
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
        element,
        *,
        mode=container.Zone.NONE,
        row=0,
        col=0,
        **star: R,
    ) -> N:
        #
        self.element = element
        self._button = element["button"]
        self._image = element["image"]
        self._label = element["label"]
        self._view = element["view"]
        self._window = element["window"]

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


class Window(View):
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

    def find(self, name: S) -> Abstract:
        """"""
        item = super().find(name)
        if item:
            return item
        raise KeyError(name)

    @override
    def draw(self, **star: R) -> N:
        """"""
        super().draw(**star)

    @override
    def make(self, canvas: A, **star: R) -> B:
        """"""
        if super().make(canvas, **star):
            pass

        return True

    @override
    def spot(self, area: Plane) -> N:
        """"""
        super().spot(area)

    def turn(self, page: S) -> N:
        """"""
        self.page.hide()
        self.page = self.view[page]
        self.page.show()
        self.draw()

    def work(self, code, **star: R):
        """"""
        caller = self.code.get(code)
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

    def __init__(self, hold: H, element, **star: R) -> N:
        self.hold = hold
        self.code = {}
        self.view = {}

        self.page = View(hold, "", element, parent=None)

        super().__init__(self.hold, "window", element, parent=None)
