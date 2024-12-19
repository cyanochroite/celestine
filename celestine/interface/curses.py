""""""

import io
import math

from celestine import bank
from celestine.data.notational_systems import BRAILLE_PATTERNS
from celestine.interface import Abstract as Abstract_
from celestine.interface import Element as Element_
from celestine.interface import View as View_
from celestine.interface import Window as Window_
from celestine.literal import LINE_FEED
from celestine.package import (
    curses,
    pillow,
)
from celestine.typed import (
    LS,
    B,
    N,
    P,
    R,
    override,
)
from celestine.window.collection import (
    Area,
    Line,
    Plane,
    Point,
)

color_index = 8  # skip the 8 reserved colors
color_table = {}

COLORS = 15


def brightwing(image):
    """
    Brightwing no like the dark colors.

    Make image bright.
    """
    def brighter(pixel):
        invert = (255 - pixel) / 255
        boost = invert * 64
        shift = pixel + boost
        return shift

    hue, saturation, value = image.convert("HSV").split()
    new_value = value.point(brighter)

    bands = (hue, saturation, new_value)

    return pillow.Image.merge("HSV", bands).convert("RGB")


def convert(image, mode):
    """"""

    matrix = None  # Unused default.
    dither = pillow.Image.Dither.FLOYDSTEINBERG
    palette = pillow.Image.Palette.WEB  # Unused default.
    colors = 256  # Unused default.

    hold = image.convert(mode, matrix, dither, palette, colors)
    image = hold
    return image


def get_colors(curses, image):
    """Fails after being called 16 times."""
    global color_index
    global color_table

    colors = image.getcolors()
    if not colors:
        print("Yo where my color go?")
        return
    for color in colors:
        (count, pixel) = color
        (red, green, blue) = pixel

        red *= 1000
        green *= 1000
        blue *= 1000

        red //= 255
        green //= 255
        blue //= 255

        if red >= 920 or green >= 920 or blue >= 920:
            print(red, green, blue)

        curses.init_color(color_index, red, green, blue)
        curses.init_pair(color_index, color_index, 0)

        color_table[pixel] = color_index
        color_index += 1


class Abstract(Abstract_):
    """"""

    def add_string(self, x_dot, y_dot, text, *extra):
        """
        Curses swaps x and y.

        Also minus the window border to get local location.

        Text length need be size-1 long.
        """
        self.canvas.addstr(y_dot, x_dot, text, *extra)

    def render(self, item, **star: R) -> N:
        """"""
        if self.hidden:
            return

        text = item
        (x_dot, y_dot) = self.area.origin.int
        self.add_string(x_dot, y_dot, text)


class Element(Element_, Abstract):
    """"""

    def output(self):
        width, height = self.cache.size

        pixels = list(self.cache.getdata())
        string = io.StringIO()

        def shift(offset_x, offset_y):
            nonlocal braille
            nonlocal range_x
            nonlocal range_y

            index_x = range_x + offset_x
            index_y = range_y + offset_y

            index = index_y * width + index_x
            pixel = pixels[index] // 255

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
                string.write(text)

            string.write(LINE_FEED)

        value = string.getvalue()
        value = value[0:-1]
        return value.split(LINE_FEED)

    def render(self, item, **star: R):
        """"""

        (x_dot, y_dot) = self.area.world.origin

        if not pillow:
            self.add_string(
                x_dot,
                y_dot,
                item,
            )
            return

        color = list(self.color.getdata())

        index_y = 0
        for row_text in item:
            index_x = 0
            for col_text in row_text:
                width, height = self.color.size
                index = index_y * width + index_x

                (red, green, blue) = color[index]
                table = color_table[(red, green, blue)]
                extra = curses.color_pair(table)

                self.add_string(
                    x_dot + index_x,
                    y_dot + index_y,
                    col_text,
                    extra,
                )

                index_x += 1

            index_y += 1

    def draw_old(self, **star: R):
        """"""
        self.path = P()
        if not pillow:
            self.render(self.path.name, **star)
            return

        self.cache = pillow.open(self.path)
        self.color = self.cache.copy()

        # Crop box.
        source_length_x = self.cache.image.width
        source_length_y = self.cache.image.height

        length_x, length_y = self.area.size

        target_length_x = length_x * 2
        target_length_y = length_y * 4

        source_length = (source_length_x, source_length_y)
        target_length = (target_length_x, target_length_y)

        box = self.crop(source_length, target_length)
        # Done.

        self.color.brightwing()

        target_length = (target_length_x, target_length_y)
        self.cache.resize(target_length, box)
        self.color.resize(self.area.size, box)

        self.color.quantize()

        self.cache.convert_to_mono()
        self.color.convert_to_color()

        get_colors(curses, self.color.image)

        item = self.output()
        self.render(item, **star)

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
            return

        if not pillow:
            self.render(self.path.name, **star)
            return

        self.cache = pillow.Image.open(self.path)
        self.color = pillow.Image.open(self.path)
        self.color.convert("RGBA")

        # self.cache = self.image
        self.color = self.cache.copy()

        # Crop box.
        source_length_x, source_length_y = self.cache.size

        length_x, length_y = self.area.world.size

        target_length_x = length_x * 2
        target_length_y = length_y * 4

        source_length = Plane.create(source_length_x, source_length_y)
        target_length = Plane.create(target_length_x, target_length_y)

        source_length.scale_to_min(target_length)
        box = source_length.size
        # Done.

        self.color = brightwing(self.color)

        self.cache.resize(target_length.size)
        self.color.resize(self.area.local.size)

        self.color.quantize()

        self.cache = convert(self.cache, "1")
        self.color = convert(self.color, "RGB")

        get_colors(curses, self.color)

        item = self.output()
        self.render(item, **star)


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

        # Reset the global color counter.
        global color_index
        global color_table
        color_index = 8
        color_table = {}

    @override
    @staticmethod
    def extension() -> LS:
        """"""
        if bool(pillow):
            return pillow.extension()

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
