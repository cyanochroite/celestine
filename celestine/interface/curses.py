""""""

import itertools
import math

from celestine import bank
from celestine.data.palette import (
    COLOR_PAIRS,
    curses_table,
    pillow_table,
)
from celestine.interface import Abstract as Abstract_
from celestine.interface import Element as Element_
from celestine.interface import View as View_
from celestine.interface import Window as Window_
from celestine.literal import LATIN_SMALL_LETTER_R
from celestine.package import (
    PIL,
    curses,
)
from celestine.typed import (
    ANY,
    GS,
    GZ,
    LS,
    LZ,
    B,
    D,
    N,
    P,
    R,
    S,
    cast,
    ignore,
    override,
)
from celestine.window.collection import (
    Area,
    Line,
    Plane,
    Point,
)

# Color pair 0 is hard-wired to white on black, and cannot be changed.
# 0:black, 1:red, 2:green, 3:yellow,
# 4:blue, 5:magenta, 6:cyan, and 7:white


if bool(PIL):
    palette_image = PIL.Image.new("P", (16, 16))
    pillow_palette = list(itertools.chain.from_iterable(pillow_table))
    palette_image.putpalette(pillow_palette)


class Abstract(Abstract_):
    """"""


class Element(Element_, Abstract):
    """"""

    @override
    def draw(self, **star: R) -> B:
        """"""
        if not super().draw(**star):
            return False

        x, y = self.area.world.origin.value

        # text
        parent = star.pop("parent")

        if self.text:
            parent.addstr(y, x, self.text)
            return True

        if self.path:
            self.reimage(self.path)

        return True

    @override
    def reimage(self, path: P, **star: R) -> N:
        """"""
        super().reimage(path, **star)

        if not bool(PIL):
            (x_dot, y_dot) = self.area.world.origin
            self.parent.addstr(y_dot, x_dot, self.path.name)
            return

        image = PIL.Image.open(
            fp=path,
            mode=LATIN_SMALL_LETTER_R,
            formats=bank.window.formats(),
        )
        image = image.convert(mode="RGB")

        #

        image_size = self.image_size(image.size, (2, 4))

        image = image.resize(image_size.size.value)

        image = brightness(image)

        target = Plane.create(*self.area.world.size)
        target *= (2, 4)
        cache = self.imagin(image, image_size, target.size, "1")

        plane = image_size / (2, 4)
        cat = self.imagin(image, plane, self.area.world.size, "RGB")
        self.render(cache, cat)

    def render(self, one: PIL.Image.Image, two: PIL.Image.Image) -> N:
        """"""
        size = self.area.local.size.copy()
        size -= (1, 1)
        world = self.area.world
        button = zip(dot_x(world), dot_y(world), luma(one), hue(two))
        for x_dot, y_dot, text, extra in button:
            if x_dot == size.one and y_dot == size.two:
                continue  # TODO: figure out why last pixel causes ERROR
            self.parent.addstr(y_dot, x_dot, text, extra)

    def __init__(self, name: S, **star: R) -> N:
        super().__init__(name, **star)
        self.photo = None
        self.cache = PIL.Image.Image()
        self.color = PIL.Image.Image()


class View(View_, Abstract):
    """"""


class Window(Window_, Abstract):
    """"""

    def build(self, parent: ANY, star: D[S, ANY]) -> N:
        """"""
        super().build(parent, star)
        (size_y, size_x) = self.stdscr.getmaxyx()
        self.item = self.stdscr.subwin(size_y - 2, size_x - 2, 1, 1)

    @override
    def draw(self, **star: R) -> B:
        """"""
        self.item.erase()
        super().draw(parent=self.item, **star)

        self.stdscr.noutrefresh()
        self.item.noutrefresh()
        curses.doupdate()
        return True

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
    def __init__(self) -> N:
        element = {
            "element": Element,
            "view": View,
            "window": self,
        }
        super().__init__(element)

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

        for index in range(COLOR_PAIRS):
            red, green, blue = curses_table[index]
            curses.init_color(index + 16, red, green, blue)
            curses.init_pair(index + 16, index + 16, 16)


def brightness(image: PIL.Image.Image) -> PIL.Image.Image:
    """
    Makes dark images brighter.

    If less then 1/3 of pixels are bright, brighten the image up to x3.
    Otherwise, brighten the image by x1, which does nothing.

    factor: 1 + max(0, 1 / 3 - 0) * 6 = 3
    factor: 1 + max(0, 1 / 3 - 1 / 3) * 6 = 1
    factor: 1 + max(0, 1 / 3 - 1) * 6 = 1
    """
    convert = image.convert("1")
    data = convert.getdata()
    flat = cast(LZ, data)
    binary = (pixel // 255 for pixel in flat)
    count = sum(binary)
    length = image.width * image.height
    ratio = count / length
    factor = 1 + max(0, 1 / 3 - ratio) * 6
    enhance = PIL.ImageEnhance.Brightness(image)
    result = enhance.enhance(factor)
    return result


def dot_x(world: Plane) -> GZ:
    """"""
    width, height = world.size.value
    length = width * height
    offset = int(world.origin.one)
    for index in range(length):
        local = index % width
        result = local + offset
        yield result


def dot_y(world: Plane) -> GZ:
    """"""
    width, height = world.size.value
    length = width * height
    offset = int(world.origin.two)
    for index in range(length):
        local = index // width
        result = local + offset
        yield result


def hue(image: PIL.Image.Image) -> GZ:
    """"""
    pixels = image.quantize(
        colors=COLOR_PAIRS,
        palette=palette_image,
    )
    colors = cast(LZ, pixels.getdata())
    for color in colors:
        result = curses.color_pair(color + 16)
        yield result


def luma(image: PIL.Image.Image) -> GS:
    """
    Tranlate image into Braille Patterns.

    Website: https://en.wikipedia.org/wiki/Braille_Patterns
    Section: Identifying, naming and ordering
    """
    data = image.getdata()
    pixels = cast(LZ, data)

    width, height = image.size
    length = width * height

    dots = [
        width + width + width + 1,
        width + width + width + 0,
        width + width + 1,
        width + 1,
        1,
        width + width + 0,
        width + 0,
        0,
    ]

    for index in range(length):
        index_x = index % width
        index_y = index // width
        if index_x % 2 or index_y % 4:
            continue

        pattern = 0
        for dot in dots:
            pattern <<= 1
            pixel = index + dot
            if pixels[pixel] > 127:
                pattern |= 1

        braille = 0x2800 + pattern
        result = chr(braille)
        yield result


ignore(Window)
