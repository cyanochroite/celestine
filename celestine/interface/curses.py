""""""

from celestine import load
from celestine.package import pillow
from celestine.package.curses import package as curses
from celestine.window.element import Abstract as abstract
from celestine.window.element import Button as button
from celestine.window.element import Image as image
from celestine.window.element import Label as label
from celestine.window.window import Window as window

TERMINAL_RATIO = 15 / 7
WIDTH = 18
HEIGHT = 4

WIDTH = 24
HEIGHT = 8


WIDTH = 48
HEIGHT = 16

ASCII_CHARS = [
    "@",
    "$",
    "&",
    "#",
    "%",
    "?",
    "*",
    "=",
    "+",
    '"',
    "!",
    "^",
    ";",
    "-",
    ",",
    "'",
    "`",
    ".",
]


class Abstract(abstract):
    """"""

    def add_string(self, frame, x_dot, y_dot, text):
        """Curses swaps x and y."""
        frame.addstr(y_dot, x_dot, text)

    def origin(self):
        """"""
        x_dot = int(self.x_min)
        y_dot = int(self.y_min)
        return (x_dot, y_dot)

    def render(self, collection, item, **star):
        """"""
        text = item
        (x_dot, y_dot) = self.origin()
        self.add_string(collection, x_dot, y_dot, text)


class Button(Abstract, button):
    """"""

    def draw(self, collection, **star):
        """"""
        item = f"button:{self.data}"
        self.render(collection, item, **star)


class Image(Abstract, image):
    """"""

    def output(self, text):
        row = self.height

        start = 0
        stop = len(text)
        step = self.width
        for index in range(start, stop, step):
            if row <= 0:
                return
            yield text[index : index + step]
            row -= 1

    def render(self, collection, item, **star):
        """"""
        text = item
        (x_dot, y_dot) = self.origin()

        text = item

        row = 0
        for stuff in self.output(text):
            self.add_string(collection, x_dot, y_dot + row, stuff)
            row += 1

    def draw(self, collection, **star):
        """"""
        path = self.image or load.asset("null.png")

        self.cache = pillow.Image(path)
        self.cache.convert("RGB")

        (x, y) = self.cache.size

        if x > WIDTH or y > HEIGHT:
            x *= TERMINAL_RATIO
            y *= 1

        width = x * min(x / y, 1)
        height = y * min(y / x, 1)

        self.width = max(min(round(width), WIDTH), 1)
        self.height = max(min(round(height), HEIGHT), 1)

        self.cache.resize(self.width, self.height)
        self.cache.quantize()
        self.cache.convert("L")

        initial_pixels = list(self.cache.image.getdata())
        new_pixels = [
            ASCII_CHARS[pixel_value // 15]
            for pixel_value in initial_pixels
        ]
        text = "".join(new_pixels)

        item = f"image:{path}"

        item = text

        # self.cache.image.show()
        # print(text)
        self.render(collection, item, **star)


class Label(Abstract, label):
    """"""

    def draw(self, collection, **star):
        """"""
        item = f"label:{self.data}"
        self.render(collection, item, **star)


class Window(window):
    """"""

    def data(self, container):
        """"""
        container.data = curses.window(
            1,
            1,
            self.width - 1,
            self.height - 2,
        )

    def draw(self, **star):
        """"""
        self.data(self.page)

        super().draw(**star)

        self.stdscr.noutrefresh()
        self.background.noutrefresh()
        self.page.data.noutrefresh()
        curses.doupdate()

    def __enter__(self):
        super().__enter__()

        self.stdscr = curses.initscr()
        curses.cbreak()
        curses.noecho()
        self.stdscr.keypad(1)
        curses.start_color()

        self.background = curses.window(0, 0, self.width, self.height)
        self.background.box()

        header = curses.subwindow(self.background, 0, 0, self.width, 1)
        header.addstr(self.session.language.APPLICATION_TITLE)

        footer = curses.subwindow(
            self.background, 0, self.height - 1, self.width, 1
        )
        footer.addstr(self.session.language.CURSES_EXIT)

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        while True:
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

                    self.cord_x %= self.width
                    self.cord_y %= self.height
                    self.stdscr.move(self.cord_y, self.cord_x)
                case curses.KEY_EXIT:
                    break
                case curses.KEY_CLICK:
                    (x_dot, y_dot) = (
                        self.cord_x - 1,
                        self.cord_y - 1,
                    )
                    self.page.poke(x_dot, y_dot)

        self.stdscr.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        return False

    def __init__(self, session, element, size, **star):
        super().__init__(session, element, size, **star)
        self.background = None
        self.cord_x = 0
        self.cord_y = 0
        self.frame = None
        self.stdscr = None


def image_format():
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


def window(session, **star):
    """"""
    element = {
        "button": Button,
        "image": Image,
        "label": Label,
    }
    size = (80, 24)
    size = (120, 35)
    return Window(session, element, size, **star)
