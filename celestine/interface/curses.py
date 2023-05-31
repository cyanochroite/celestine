""""""

import io

from celestine import load
from celestine.package import pillow
from celestine.package.curses import package as curses
from celestine.unicode import LINE_FEED
from celestine.window.element import Abstract as abstract
from celestine.window.element import Button as button
from celestine.window.element import Image as image
from celestine.window.element import Label as label
from celestine.window.window import Window as window

BRAILLE = {
    0b00000000: chr(0x2800),
    0b10000000: chr(0x2801),
    0b00100000: chr(0x2802),
    0b10100000: chr(0x2803),
    0b00001000: chr(0x2804),
    0b10001000: chr(0x2805),
    0b00101000: chr(0x2806),
    0b10101000: chr(0x2807),
    0b01000000: chr(0x2808),
    0b11000000: chr(0x2809),
    0b01100000: chr(0x280A),
    0b11100000: chr(0x280B),
    0b01001000: chr(0x280C),
    0b11001000: chr(0x280D),
    0b01101000: chr(0x280E),
    0b11101000: chr(0x280F),
    0b00010000: chr(0x2810),
    0b10010000: chr(0x2811),
    0b00110000: chr(0x2812),
    0b10110000: chr(0x2813),
    0b00011000: chr(0x2814),
    0b10011000: chr(0x2815),
    0b00111000: chr(0x2816),
    0b10111000: chr(0x2817),
    0b01010000: chr(0x2818),
    0b11010000: chr(0x2819),
    0b01110000: chr(0x281A),
    0b11110000: chr(0x281B),
    0b01011000: chr(0x281C),
    0b11011000: chr(0x281D),
    0b01111000: chr(0x281E),
    0b11111000: chr(0x281F),
    0b00000100: chr(0x2820),
    0b10000100: chr(0x2821),
    0b00100100: chr(0x2822),
    0b10100100: chr(0x2823),
    0b00001100: chr(0x2824),
    0b10001100: chr(0x2825),
    0b00101100: chr(0x2826),
    0b10101100: chr(0x2827),
    0b01000100: chr(0x2828),
    0b11000100: chr(0x2829),
    0b01100100: chr(0x282A),
    0b11100100: chr(0x282B),
    0b01001100: chr(0x282C),
    0b11001100: chr(0x282D),
    0b01101100: chr(0x282E),
    0b11101100: chr(0x282F),
    0b00010100: chr(0x2830),
    0b10010100: chr(0x2831),
    0b00110100: chr(0x2832),
    0b10110100: chr(0x2833),
    0b00011100: chr(0x2834),
    0b10011100: chr(0x2835),
    0b00111100: chr(0x2836),
    0b10111100: chr(0x2837),
    0b01010100: chr(0x2838),
    0b11010100: chr(0x2839),
    0b01110100: chr(0x283A),
    0b11110100: chr(0x283B),
    0b01011100: chr(0x283C),
    0b11011100: chr(0x283D),
    0b01111100: chr(0x283E),
    0b11111100: chr(0x283F),
    0b00000010: chr(0x2840),
    0b10000010: chr(0x2841),
    0b00100010: chr(0x2842),
    0b10100010: chr(0x2843),
    0b00001010: chr(0x2844),
    0b10001010: chr(0x2845),
    0b00101010: chr(0x2846),
    0b10101010: chr(0x2847),
    0b01000010: chr(0x2848),
    0b11000010: chr(0x2849),
    0b01100010: chr(0x284A),
    0b11100010: chr(0x284B),
    0b01001010: chr(0x284C),
    0b11001010: chr(0x284D),
    0b01101010: chr(0x284E),
    0b11101010: chr(0x284F),
    0b00010010: chr(0x2850),
    0b10010010: chr(0x2851),
    0b00110010: chr(0x2852),
    0b10110010: chr(0x2853),
    0b00011010: chr(0x2854),
    0b10011010: chr(0x2855),
    0b00111010: chr(0x2856),
    0b10111010: chr(0x2857),
    0b01010010: chr(0x2858),
    0b11010010: chr(0x2859),
    0b01110010: chr(0x285A),
    0b11110010: chr(0x285B),
    0b01011010: chr(0x285C),
    0b11011010: chr(0x285D),
    0b01111010: chr(0x285E),
    0b11111010: chr(0x285F),
    0b00000110: chr(0x2860),
    0b10000110: chr(0x2861),
    0b00100110: chr(0x2862),
    0b10100110: chr(0x2863),
    0b00001110: chr(0x2864),
    0b10001110: chr(0x2865),
    0b00101110: chr(0x2866),
    0b10101110: chr(0x2867),
    0b01000110: chr(0x2868),
    0b11000110: chr(0x2869),
    0b01100110: chr(0x286A),
    0b11100110: chr(0x286B),
    0b01001110: chr(0x286C),
    0b11001110: chr(0x286D),
    0b01101110: chr(0x286E),
    0b11101110: chr(0x286F),
    0b00010110: chr(0x2870),
    0b10010110: chr(0x2871),
    0b00110110: chr(0x2872),
    0b10110110: chr(0x2873),
    0b00011110: chr(0x2874),
    0b10011110: chr(0x2875),
    0b00111110: chr(0x2876),
    0b10111110: chr(0x2877),
    0b01010110: chr(0x2878),
    0b11010110: chr(0x2879),
    0b01110110: chr(0x287A),
    0b11110110: chr(0x287B),
    0b01011110: chr(0x287C),
    0b11011110: chr(0x287D),
    0b01111110: chr(0x287E),
    0b11111110: chr(0x287F),
    0b00000001: chr(0x2880),
    0b10000001: chr(0x2881),
    0b00100001: chr(0x2882),
    0b10100001: chr(0x2883),
    0b00001001: chr(0x2884),
    0b10001001: chr(0x2885),
    0b00101001: chr(0x2886),
    0b10101001: chr(0x2887),
    0b01000001: chr(0x2888),
    0b11000001: chr(0x2889),
    0b01100001: chr(0x288A),
    0b11100001: chr(0x288B),
    0b01001001: chr(0x288C),
    0b11001001: chr(0x288D),
    0b01101001: chr(0x288E),
    0b11101001: chr(0x288F),
    0b00010001: chr(0x2890),
    0b10010001: chr(0x2891),
    0b00110001: chr(0x2892),
    0b10110001: chr(0x2893),
    0b00011001: chr(0x2894),
    0b10011001: chr(0x2895),
    0b00111001: chr(0x2896),
    0b10111001: chr(0x2897),
    0b01010001: chr(0x2898),
    0b11010001: chr(0x2899),
    0b01110001: chr(0x289A),
    0b11110001: chr(0x289B),
    0b01011001: chr(0x289C),
    0b11011001: chr(0x289D),
    0b01111001: chr(0x289E),
    0b11111001: chr(0x289F),
    0b00000101: chr(0x28A0),
    0b10000101: chr(0x28A1),
    0b00100101: chr(0x28A2),
    0b10100101: chr(0x28A3),
    0b00001101: chr(0x28A4),
    0b10001101: chr(0x28A5),
    0b00101101: chr(0x28A6),
    0b10101101: chr(0x28A7),
    0b01000101: chr(0x28A8),
    0b11000101: chr(0x28A9),
    0b01100101: chr(0x28AA),
    0b11100101: chr(0x28AB),
    0b01001101: chr(0x28AC),
    0b11001101: chr(0x28AD),
    0b01101101: chr(0x28AE),
    0b11101101: chr(0x28AF),
    0b00010101: chr(0x28B0),
    0b10010101: chr(0x28B1),
    0b00110101: chr(0x28B2),
    0b10110101: chr(0x28B3),
    0b00011101: chr(0x28B4),
    0b10011101: chr(0x28B5),
    0b00111101: chr(0x28B6),
    0b10111101: chr(0x28B7),
    0b01010101: chr(0x28B8),
    0b11010101: chr(0x28B9),
    0b01110101: chr(0x28BA),
    0b11110101: chr(0x28BB),
    0b01011101: chr(0x28BC),
    0b11011101: chr(0x28BD),
    0b01111101: chr(0x28BE),
    0b11111101: chr(0x28BF),
    0b00000011: chr(0x28C0),
    0b10000011: chr(0x28C1),
    0b00100011: chr(0x28C2),
    0b10100011: chr(0x28C3),
    0b00001011: chr(0x28C4),
    0b10001011: chr(0x28C5),
    0b00101011: chr(0x28C6),
    0b10101011: chr(0x28C7),
    0b01000011: chr(0x28C8),
    0b11000011: chr(0x28C9),
    0b01100011: chr(0x28CA),
    0b11100011: chr(0x28CB),
    0b01001011: chr(0x28CC),
    0b11001011: chr(0x28CD),
    0b01101011: chr(0x28CE),
    0b11101011: chr(0x28CF),
    0b00010011: chr(0x28D0),
    0b10010011: chr(0x28D1),
    0b00110011: chr(0x28D2),
    0b10110011: chr(0x28D3),
    0b00011011: chr(0x28D4),
    0b10011011: chr(0x28D5),
    0b00111011: chr(0x28D6),
    0b10111011: chr(0x28D7),
    0b01010011: chr(0x28D8),
    0b11010011: chr(0x28D9),
    0b01110011: chr(0x28DA),
    0b11110011: chr(0x28DB),
    0b01011011: chr(0x28DC),
    0b11011011: chr(0x28DD),
    0b01111011: chr(0x28DE),
    0b11111011: chr(0x28DF),
    0b00000111: chr(0x28E0),
    0b10000111: chr(0x28E1),
    0b00100111: chr(0x28E2),
    0b10100111: chr(0x28E3),
    0b00001111: chr(0x28E4),
    0b10001111: chr(0x28E5),
    0b00101111: chr(0x28E6),
    0b10101111: chr(0x28E7),
    0b01000111: chr(0x28E8),
    0b11000111: chr(0x28E9),
    0b01100111: chr(0x28EA),
    0b11100111: chr(0x28EB),
    0b01001111: chr(0x28EC),
    0b11001111: chr(0x28ED),
    0b01101111: chr(0x28EE),
    0b11101111: chr(0x28EF),
    0b00010111: chr(0x28F0),
    0b10010111: chr(0x28F1),
    0b00110111: chr(0x28F2),
    0b10110111: chr(0x28F3),
    0b00011111: chr(0x28F4),
    0b10011111: chr(0x28F5),
    0b00111111: chr(0x28F6),
    0b10111111: chr(0x28F7),
    0b01010111: chr(0x28F8),
    0b11010111: chr(0x28F9),
    0b01110111: chr(0x28FA),
    0b11110111: chr(0x28FB),
    0b01011111: chr(0x28FC),
    0b11011111: chr(0x28FD),
    0b01111111: chr(0x28FE),
    0b11111111: chr(0x28FF),
}


WIDTH = 18
HEIGHT = 4

# WIDTH = 24
# HEIGHT = 8


WIDTH = 48 * 2
HEIGHT = 16 * 4


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

    def output(self):
        pixels = list(self.cache.getdata())
        string = io.StringIO()

        def shift(offset_x, offset_y):
            nonlocal braille
            nonlocal range_x
            nonlocal range_y

            index_x = range_x + offset_x
            index_y = range_y + offset_y

            index = index_y * self.width + index_x
            pixel = pixels[index] // 255

            braille <<= 1
            braille |= pixel

        for range_y in range(0, self.height, 4):
            for range_x in range(0, self.width, 2):
                braille = 0

                shift(0, 0)
                shift(1, 0)
                shift(0, 1)
                shift(1, 1)
                shift(0, 2)
                shift(1, 2)
                shift(0, 3)
                shift(1, 3)

                text = BRAILLE[braille]
                string.write(text)

            string.write(LINE_FEED)

        value = string.getvalue()
        value = value[0:-1]
        return value.split(LINE_FEED)

    def render(self, collection, item, **star):
        """"""
        (x_dot, y_dot) = self.origin()

        row = 0
        for stuff in item:
            self.add_string(collection, x_dot, y_dot + row, stuff)
            row += 1

    def draw(self, collection, **star):
        """"""
        path = self.image or load.asset("null.png")

        self.cache = pillow.Mono(path)
        self.cache.resize(WIDTH, HEIGHT)
        self.cache.convert()

        self.width, self.height = self.cache.size

        item = self.output()
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
