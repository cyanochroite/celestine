""""""

import colorsys
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
    PIL,
    curses,
)
from celestine.typed import (
    LS,
    LZ,
    TF3,
    B,
    K,
    L,
    N,
    P,
    R,
    S,
    override,
)
from celestine.window.collection import (
    Area,
    Line,
    Plane,
    Point,
)

COLORS = 15


###########


colours: L[TF3] = []

for index_finger in range(16):
    hsv_val = index_finger / 15
    color_crayon = colorsys.hsv_to_rgb(0.0, 0.0, hsv_val)
    colours.append(color_crayon)

for values in range(1, 5):
    hsv_val = math.sqrt(values / 4)

    for saturations in range(1, 5):
        saturation = math.sqrt(saturations / 4)
        # saturation = saturations / 4

        options = values * 6
        for hues in range(0, options):
            hue = hues / options
            color_crayon = colorsys.hsv_to_rgb(hue, saturation, hsv_val)
            colours.append(color_crayon)

colours.sort()

colony: LZ = []
for item_index in colours:
    r, g, b = item_index
    colony.append(round(r * 255))
    colony.append(round(g * 255))
    colony.append(round(b * 255))

palimage = PIL.Image.new("P", (16, 16))
palimage.putpalette(colony, "RGB")


###


color_table = {}


def set_colors() -> N:
    """"""
    global color_table

    color_index = 8  # skip the 8 reserved colors

    curses_colour = set(colours)
    curses_colour.remove((0.0, 0.0, 0.0))
    curses_colour.remove((1.0, 0.0, 0.0))
    curses_colour.remove((0.0, 1.0, 0.0))
    curses_colour.remove((0.0, 0.0, 1.0))
    curses_colour.remove((0.0, 1.0, 1.0))
    curses_colour.remove((1.0, 0.0, 1.0))
    curses_colour.remove((1.0, 1.0, 0.0))
    curses_colour.remove((1.0, 1.0, 1.0))

    curses_list = list(curses_colour)
    curses_list.sort()

    for colorado in curses_list:
        red = round(colorado[0] * 1000)
        green = round(colorado[1] * 1000)
        blue = round(colorado[2] * 1000)
        curses.init_color(color_index, red, green, blue)
        curses.init_pair(color_index, color_index, 0)

        red = round(colorado[0] * 255)
        green = round(colorado[1] * 255)
        blue = round(colorado[2] * 255)
        pixel = (red, green, blue)
        color_table[pixel] = color_index

        color_index += 1


#############


def convert(image, mode):
    """"""
    matrix = None  # Unused default.
    dither = PIL.Image.Dither.FLOYDSTEINBERG
    palette = PIL.Image.Palette.WEB  # Unused default.
    colors = 256  # Unused default.

    hold = image.convert(mode, matrix, dither, palette, colors)
    return hold


def convert_to_alpha(image):
    """"""
    return convert(image, "RGBA")


def convert_to_color(image):
    """"""
    return convert(image, "RGB")


def convert_to_mono(image):
    """"""
    return convert(image, "1")


def crop(source_length, target_length):
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
        """"""
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

    def render(self, item: LS, **star: R) -> N:
        """"""

        (x_dot, y_dot) = self.area.world.origin

        if not PIL:
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
                width, _ = self.color.size
                index = index_y * width + index_x

                (red, green, blue) = color[index]
                table = color_table.get((red, green, blue), 2)
                extra = curses.color_pair(table)

                self.add_string(
                    x_dot + index_x,
                    y_dot + index_y,
                    col_text,
                    extra,
                )

                index_x += 1

            index_y += 1

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
            self.render(self.path.name, **star)
            return True

        self.update_image(self.path)

        return True

    def update_image(self, path: P, **star: R) -> N:
        """"""
        self.path = path

        image = PIL.Image.open(path)
        image.convert()

        self.cache = image.copy()
        self.color = image.convert(mode="RGB")

        # Crop box.
        source_length_x = self.cache.width
        source_length_y = self.cache.height

        length_x, length_y = self.area.world.size

        target_length_x = length_x * 2
        target_length_y = length_y * 4

        target_length_x = 16
        target_length_y = 16

        source_length = (source_length_x, source_length_y)
        target_length = (target_length_x, target_length_y)

        box = crop(source_length, target_length)
        # Done.

        target_length = (target_length_x, target_length_y)
        # self.cache.resize(target_length, box)
        # self.color.resize(self.area.world.size, box)
        self.cache = self.cache.resize(target_length)
        self.color = self.color.resize(self.area.world.size)

        self.color.quantize(palette=palimage)

        self.cache = convert_to_mono(self.cache)
        self.color = convert_to_color(self.color)

        item = self.output()
        self.render(item, **star)

    def __init__(self, name: S, parent: K, **star: R) -> N:
        super().__init__(name, parent, **star)
        self.photo = None
        self.cache = None
        self.color = None


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
    @staticmethod
    def extension() -> LS:
        """"""
        if bool(PIL):
            # return PIL.Image.registered_extensions()
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

        set_colors()
