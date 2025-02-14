""""""

import itertools
import math

from celestine import bank
from celestine.data.notational_systems import BRAILLE_PATTERNS
from celestine.data.palette import (
    curses_table,
    pillow_table,
)
from celestine.interface import Abstract as Abstract_
from celestine.interface import Element as Element_
from celestine.interface import View as View_
from celestine.interface import Window as Window_
from celestine.package import (
    PIL,
    curses,
)
from celestine.typed import (
    LS,
    B,
    K,
    N,
    P,
    R,
    S,
    Z,
    ignore,
    override,
)
from celestine.window.cardinal import Round
from celestine.window.collection import (
    Area,
    Line,
    Plane,
    Point,
)
from celestine.window.container import Image

# Color pair 0 is hard-wired to white on black, and cannot be changed.
# 0:black, 1:red, 2:green, 3:yellow,
# 4:blue, 5:magenta, 6:cyan, and 7:white


palette_image = PIL.Image.new("P", (16, 16))
pillow_palette = list(itertools.chain.from_iterable(pillow_table))
palette_image.putpalette(pillow_palette)


#############


class Abstract(Abstract_):
    """"""

    def add_string(self, x_dot: Z, y_dot: Z, text: S, *extra: Z) -> N:
        """
        Curses swaps x and y.

        Also minus the window border to get local location.

        Text length need be size-1 long.
        """
        if y_dot == 27 and x_dot == 117:
            # TODO: figure out why last pixel returns ERROR
            return
        self.canvas.addstr(y_dot, x_dot, text, *extra)


class Element(Element_, Abstract):
    """"""

    @override
    def draw(self, **star: R) -> B:
        """"""
        if not super().draw(**star):
            return False

        x, y = self.area.world.origin.value

        # text
        canvas = star.pop("canvas")

        if self.text:
            canvas.addstr(y, x, self.text)
            return True

        if not PIL:
            (x_dot, y_dot) = self.area.world.origin
            self.add_string(
                x_dot,
                y_dot,
                self.path.name,
            )

        self.update_image(self.path)

        return True

    def update_image(self, path: P, **star: R) -> N:
        """"""
        self.path = path
        image = PIL.Image.open(self.path)
        image = image.convert(mode="RGB")

        #
        current = Plane.create(*image.size)
        target = Plane.create(*self.area.world.size)
        target *= (2, 4)

        if self.fit == Image.FILL:
            current.scale_to_min(target)
        elif self.fit == Image.FULL:
            current.scale_to_max(target)
        current.center(target)

        width, height = self.area.world.size.value
        length = width * height

        image = image.resize(current.size.value)
        resize = image.convert("1")

        def binary(number: Z) -> Z:
            return 1 if number else 0

        data = resize.getdata()
        data = map(binary, data)
        count = sum(data)
        ratio = count / length
        ratio1 = 1 / 3 - ratio
        ratio2 = max(0, ratio1)
        factor = 1 + ratio2 * 6
        image = PIL.ImageEnhance.Brightness(image)
        image = image.enhance(factor)

        #

        origin = self.area.world.origin

        def dot_x():
            for index in range(length):
                local = index % width
                world = local + origin.one
                yield world

        def dot_y():
            for index in range(length):
                local = index // width
                world = local + origin.two
                yield world

        def luma():
            hippo = PIL.Image.new("1", target.size.value)
            im = image
            box = current.value
            hippo.paste(im, box)

            cache = hippo.convert("1")
            pixels = list(cache.getdata())
            width, height = cache.size

            def shift(offset_x: Z, offset_y: Z) -> N:
                nonlocal braille
                nonlocal range_x
                nonlocal range_y

                index_x = range_x + offset_x
                index_y = range_y + offset_y

                index = index_y * width + index_x
                try:
                    pixel = 1 if pixels[index] > 127 else 0
                except IndexError:
                    pixel = 0

                braille <<= 1
                braille |= pixel

            for range_y in range(0, height, 4):
                for range_x in range(0, width, 2):
                    braille = 0

                    shift(0, 0)
                    shift(1, 0)
                    shift(0, 1)
                    shift(1, 1)
                    shift(0, 2)
                    shift(1, 2)
                    shift(0, 3)
                    shift(1, 3)

                    text = BRAILLE_PATTERNS[braille]
                    yield text

        def hue():
            plane = current / (2, 4)
            plane = plane.inplace(Round.increase)

            canvas = PIL.Image.new("RGB", self.area.world.size.value)
            im = image.resize(plane.size.value)
            box = plane.value
            canvas.paste(im, box)

            colour = canvas.quantize(
                colors=255,
                method=None,
                kmeans=0,
                palette=palette_image,
                dither=PIL.Image.Dither.FLOYDSTEINBERG,
            )

            colors = list(colour.getdata())
            for index in range(length):
                color = colors[index]
                pair = curses.color_pair(color)
                yield pair

        button = zip(dot_x(), dot_y(), luma(), hue())
        for x_dot, y_dot, text, extra in button:
            self.add_string(x_dot, y_dot, text, extra)

    def __init__(self, name: S, parent: K, **star: R) -> N:
        super().__init__(name, parent, **star)
        self.photo = None
        self.cache = PIL.Image.Image()
        self.color = PIL.Image.Image()


class View(View_, Abstract):
    """"""


class Window(Window_):
    """"""

    @override
    def draw(self, **star: R) -> N:
        """"""
        self.canvas.erase()
        super().draw(canvas=self.canvas, **star)

        self.stdscr.noutrefresh()
        self.canvas.noutrefresh()
        curses.doupdate()

    @override
    @classmethod
    def extension(cls) -> LS:
        """"""
        ignore(cls)

        if bool(PIL):
            return PIL.Image.registered_extensions()

        return []

    @override
    def run(self) -> N:
        super().run()

        (size_y, size_x) = self.stdscr.getmaxyx()

        header = self.stdscr.subwin(0, size_x, 0, 0)
        header.addstr(0, 1, bank.language.APPLICATION_TITLE)
        header.refresh()

        footer = self.stdscr.subwin(1, size_x, size_y - 1, 0)
        footer.addstr(0, 1, bank.language.CURSES_EXIT)
        footer.refresh()

        def move():
            size_x, size_y = self.area.local.size
            self.cord_x %= size_x
            self.cord_y %= size_y
            self.stdscr.move(
                math.floor(1 + self.cord_y),
                math.floor(1 + self.cord_x),
            )

        while True:
            bank.dequeue()
            event = self.stdscr.getch()
            match event:
                case 27:  # ESCAPE
                    break
                case 32:  # SPACE
                    point = Point(self.cord_x, self.cord_y)
                    self.page.click(point)
                case 258:  # KEY_DOWN
                    self.cord_y += 1
                    move()
                case 259:  # KEY_UP
                    self.cord_y -= 1
                    move()
                case 260:  # KEY_LEFT
                    self.cord_x -= 1
                    move()
                case 261:  # KEY_RIGHT
                    self.cord_x += 1
                    move()
                case _:
                    pass

        self.stdscr.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    @override
    def __init__(self, **star: R) -> N:
        element = {
            "element": Element,
            "view": View,
            "window": self,
        }
        super().__init__(element, **star)

        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)
        curses.start_color()

        self.stdscr.box()

        (size_y, size_x) = self.stdscr.getmaxyx()
        plane = Plane(
            Line(0, size_x - 2),
            Line(0, size_y - 2),
        )
        self.area = Area(plane, plane)
        self.cord_x = 0.5
        self.cord_y = 0.5

        self.canvas = self.stdscr.subwin(size_y - 2, size_x - 2, 1, 1)

        for index in range(255):
            red, green, blue = curses_table[index]
            curses.init_color(index, red, green, blue)
            curses.init_pair(index, index, 0)
