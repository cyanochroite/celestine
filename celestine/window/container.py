""""""

import enum
import math

from celestine.typed import (
    B,
    D,
    I,
    K,
    N,
    R,
    S,
)
from celestine.window.collection import (
    Collection,
    Item,
    Rectangle,
)


class Zone(enum.Enum):
    """"""

    DROP = enum.auto()
    GRID = enum.auto()
    NONE = enum.auto()
    SPAN = enum.auto()


class Image(enum.Enum):
    """"""

    FILL = enum.auto()
    FULL = enum.auto()


class Call(enum.Enum):
    """"""

    NONE = enum.auto()
    VIEW = enum.auto()
    WORK = enum.auto()


class View(Item, Collection):
    """"""

    item: D[S, Item]

    def draw(self, **star: R) -> N:
        """"""
        if self.hidden:
            return

        for _, item in self.item.items():
            item.draw(**star)

    def make(self) -> N:
        """"""
        for _, item in self.item.items():
            item.make()

    def new(
        self, name, *, text="", path="", code="", view="", **star: R
    ) -> N:
        """"""
        if text != "" and path != "":
            raise AttributeError("text and path can't both be set")

        if code != "" and view != "":
            raise AttributeError("code and view path can't both be set")

        call = None
        action = Call.NONE
        work = None

        if view:
            call = view
            action = Call.VIEW
            work = self.window.turn

        if code:
            call = code
            action = Call.WORK
            work = self.window.work

        if action == Call.NONE:
            if path:
                self.save(
                    self._image(
                        self.hold,
                        self.canvas,
                        name,
                        path,
                        **star,
                    )
                )
            else:
                self.save(
                    self._label(
                        self.hold,
                        self.canvas,
                        name,
                        text,
                        **star,
                    )
                )
        else:
            self.save(
                self._button(
                    self.hold,
                    self.canvas,
                    name,
                    text,
                    call=work,  # the window function to call
                    action=call,  # the name of the user function
                    argument=star,
                    **star,
                )
            )

    def poke(self, x_dot: I, y_dot: I, **star: R) -> B:
        """"""
        if self.hidden:
            return False

        result = False
        for _, item in self.item.items():
            result |= item.poke(x_dot, y_dot, **star)
        return result

    def spot(self, area: Rectangle, **star: R) -> N:
        """"""
        self.area.copy(area)
        length = max(1, len(self.item))

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

        size_x, size_y = self.area.size
        index = 0

        fragment_x = size_x // partition_x
        fragment_y = size_y // partition_y

        items = self.item.items()
        for _, item in items:
            index_x = index % partition_x
            index_y = min(index // partition_x, partition_y - 1)
            index += 1

            ymin = self.area.upper + fragment_y * (index_y + 0)
            ymax = self.area.upper + fragment_y * (index_y + 1)
            xmin = self.area.left + fragment_x * (index_x + 0)
            xmax = self.area.left + fragment_x * (index_x + 1)

            rectangle = Rectangle(xmin, ymin, xmax, ymax)
            item.spot(rectangle)

    def zone(self, name: S, *, mode=Zone.SPAN, **star: R) -> K:
        """"""
        return self.item_set(
            name,
            View(
                self.hold,
                self.canvas,
                name,
                self.window,
                self.element,
                mode=mode,
                **star,
            ),
        )

    def __enter__(self) -> K:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> B:
        return False

    def __init__(
        self,
        hold,
        canvas,
        name,
        window,
        element,
        *,
        mode=Zone.NONE,
        row=0,
        col=0,
        **star: R,
    ) -> N:
        self.window = window

        self.canvas = None
        #
        self.element = element
        self._button = element["button"]
        self._image = element["image"]
        self._label = element["label"]

        super().__init__(hold, canvas, name, **star)

        self.width = col
        self.height = row
        self.mode = mode

        for range_y in range(row):
            for range_x in range(col):
                name = f"{self.name}_{range_x}-{range_y}"
                self.item[name] = Item(hold, self.canvas, name)
