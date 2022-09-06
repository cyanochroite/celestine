"""Package celestine."""
import curses


HEIGHT = 24
WIDTH = 80


def item_key(frame, tag):
    global item
    return F"{frame}-{tag}"


def item_get(key):
    global item
    return item[key]


def item_set(key, value):
    global item
    item[key] = value


def frame_key(index):
    return F"Page {index}"


def frame_get(frame):
    global item
    return item[frame]


def frame_set(frame, value):
    global item
    item[frame] = value


def show_frame(text):
    global item

    frame = item[text]

    return frame


class Cursor():
    def __init__(self, session, stdscr):
        self.session = session
        self.stdscr = stdscr
        self.x = 0
        self.y = 0
        self.width = WIDTH
        self.height = HEIGHT

    def move(self):
        self.stdscr.move(self.y, self.x)

    def input(self, key):
        (x, y) = self.session.python.curses_cursor_input_match(
            key,
            curses,
            self.x,
            self.y
        )
        self.x = x % self.width
        self.y = y % self.height


class String():
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.width = len(text)
        self.height = 1
        self.text = text

    def draw(self, window):
        window.addstr(self.y, self.x, self.text)

    def select(self, x, y):
        a = x >= self.x
        b = x < self.x + self.width
        c = y >= self.y
        d = y < self.y + self.height
        print(a, b, c, d)
        return a and b and c and d


def image_load(file):
    return file


def button(frame, tag, text):
    key = item_key(frame, tag)
    _add_string(key, quote_text_window, F"button: {text}")


def file_dialog(frame, tag, bind):
    key = item_key(frame, tag)
    _add_string(key, quote_text_window, "File dialog thing.")


def image(frame, tag, image):
    key = item_key(frame, tag)
    _add_string(key, quote_text_window, image)


def label(frame, tag, text):
    key = item_key(frame, tag)
    _add_string(key, quote_text_window, F"label: {text}")


def _new_window(column, row, width, height):
    nlines = height
    ncols = width
    begin_y = row
    begin_x = column
    return curses.newwin(nlines, ncols, begin_y, begin_x)


def _new_subwindow(window, column, row, width, height):
    nlines = height
    ncols = width
    begin_y = row
    begin_x = column
    return window.subwin(nlines, ncols, begin_y, begin_x)


def _add_string(key, window, string):
    global line

    y = line
    x = 0
    line += 1

    food = key
    fight = String(x, y, string)
    print(food, fight.text)
    item_set(key, fight)
    #item_set(key, String(x, y, string))
    item_get(key).draw(window)


def main(session):
    """def main"""
    global item
    item = {}

    global line
    line = 0

    global quote_window
    quote_window = None

    global quote_text_window
    quote_text_window = None

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    try:
        key = 0

        cursor = Cursor(session, stdscr)

        quote_window = _new_window(0, 0, WIDTH, HEIGHT)
        quote_window.box()

        header1 = _new_subwindow(quote_window, 0, 0, WIDTH, 1)
        header1.addstr(session.language.APPLICATION_TITLE)

        header2 = _new_subwindow(quote_window, 0, HEIGHT - 1, WIDTH, 1)
        header2.addstr(session.language.CURSES_EXIT)

        quote_text_window = _new_subwindow(quote_window, 1, 1, WIDTH - 1, HEIGHT - 2)

        index = 0
        for window in session.window:
            key = frame_key(index)
            frame = None
            frame_set(key, frame)
            window.main(session, key)
            index += 1

        show_frame(frame_key(0))

        stdscr.noutrefresh()
        quote_window.noutrefresh()
        curses.doupdate()

        while key != ord('q'):

            if key == ord(' '):
                for key, thing in item.items():
                    print(key, thing)
                    print("sanity")
                    if "-" in key and thing.select(cursor.x - 1, cursor.y - 1):
                        print("MOO")
                        print(thing.text)

            stdscr.refresh()

            cursor.input(key)
            cursor.move()

            key = stdscr.getch()

    finally:
        stdscr.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()
