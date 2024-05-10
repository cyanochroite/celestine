""""""

import io
import math

from celestine import bank
from celestine.data.notational_systems import BRAILLE_PATTERNS
from celestine.interface import Abstract as Abstract_
from celestine.interface import Element as Element_
from celestine.interface import View as View_
from celestine.interface import Window as Window_
from celestine.package import (
    curses,
    pillow,
)
from celestine.typed import (
    N,
    R,
    B,
    override,
)
from celestine.unicode import LINE_FEED
from celestine.window.collection import (
    Area,
    Line,
    Plane,
    Point,
)

color_index = 8  # skip the 8 reserved colors
color_table = {}

COLORS = 15


def get_colors(curses, image):
    """Fails after being called 16 times."""
    global color_index
    global color_table

    colors = image.getcolors()
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
            pass
            # print(red, green, blue)
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
        self.canvas.addstr(y_dot - 1, x_dot - 1, text, *extra)

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

    def draw(self, **star: R):
        """"""

        if not pillow:
            self.render(self.path.name, **star)
            return

        self.cache = self.image
        self.color = self.cache.copy()

        # Crop box.
        source_length_x = self.cache.image.width
        source_length_y = self.cache.image.height

        length_x, length_y = self.area.world.size

        target_length_x = length_x * 2
        target_length_y = length_y * 4

        source_length = Plane.make(source_length_x, source_length_y)
        target_length = Plane.make(target_length_x, target_length_y)

        source_length.scale_to_min(target_length)
        box = source_length.size
        # Done.

        self.color.brightwing()

        # self.cache.resize(target_length.size, box)
        # self.color.resize(self.area.size, box)
        self.cache.resize(target_length.size)
        self.color.resize(self.area.local.size)

        self.color.quantize()

        self.cache.convert_to_mono()
        self.color.convert_to_color()

        get_colors(curses, self.color.image)

        item = self.output()
        self.render(item, **star)


class View(View_, Abstract):
    """"""


class Window(Window_):
    """"""

    @override
    def draw(self, **star: R) -> B:
        """"""

        # Do normal draw stuff.

        self.canvas.erase()
        # canvas = curses.window(*self.area.value)

        super().draw(**star)

        self.stdscr.noutrefresh()
        self.background.noutrefresh()
        self.canvas.noutrefresh()
        curses.doupdate()

        # Reset the global color counter.
        global color_index
        global color_table
        color_index = 8
        color_table = {}

    @override
    def extension(self):
        """"""
        if pillow:
            return pillow.extension()

        return []

    @override
    def make(self, **star: R) -> N:
        """"""
        self.canvas = self.background

        super().make(**star)

    @override
    def setup(self, name):
        """"""

        return curses.window(*self.area.int)

    @override
    def __enter__(self):
        super().__enter__()

        (size_y, size_x) = self.stdscr.getmaxyx()
        self.full = Plane.make(size_x, size_y)

        self.background = curses.window(0, 0, size_x, size_y)
        self.background.box()

        header_box = (0, 0, size_x, 1)
        header = curses.subwindow(self.background, *header_box)
        header.addstr(0, 1, bank.language.APPLICATION_TITLE)

        footer_box = (0, size_y - 1, size_x, 1)
        footer = curses.subwindow(self.background, *footer_box)
        footer.addstr(0, 1, bank.language.CURSES_EXIT)

        #
        # TODO check why repeat code from init
        plane = Plane(
            Line(1, size_x - 2),
            Line(1, size_y - 2),
        )
        self.area = Area(plane, plane)

        return self

    @override
    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)

        while True:
            bank.dequeue()
            event = self.stdscr.getch()
            match event:
                case 258 | 259 | 260 | 261 as key:
                    match key:
                        case curses.KEY_UP:
                            self.cord_y -= 1
                        case curses.KEY_DOWN:
                            self.cord_y += 1
                        case curses.KEY_LEFT:
                            self.cord_x -= 1
                        case curses.KEY_RIGHT:
                            self.cord_x += 1

                    size_x, size_y = self.full.size
                    self.cord_x %= size_x
                    self.cord_y %= size_y
                    self.stdscr.move(
                        math.floor(self.cord_y),
                        math.floor(self.cord_x),
                    )
                case curses.KEY_EXIT:
                    break
                case curses.KEY_CLICK:
                    self.page.click(Point(self.cord_x, self.cord_y))

        self.stdscr.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        return False

    @override
    def __init__(self, **star: R) -> N:
        element = {
            "element": Element,
            "view": View,
            "window": self,
        }

        self.stdscr = curses.initscr()

        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(1)
        curses.start_color()

        (size_y, size_x) = self.stdscr.getmaxyx()
        self.full = Plane.make(size_x, size_y)

        self.background = curses.window(0, 0, size_x, size_y)
        self.background.box()

        super().__init__(element, **star)
        plane = Plane(
            Line(1, size_x - 2),
            Line(1, size_y - 2),
        )
        self.area = Area(plane, plane)
        self.cord_x = 0.5
        self.cord_y = 0.5
