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


class Wiget():
    def __init__(self, column, row, width, height):
        self.x = column
        self.y = row
        self.width = width
        self.height = height

    def select(self, x, y):
        a = x >= self.x
        b = x < self.x + self.width
        c = y >= self.y
        d = y < self.y + self.height
        return a and b and c and d


class String(Wiget):
    def __init__(self, x, y, text):
        super().__init__(x, y, len(text), 1)
        self.text = text

    def draw(self, window):
        window.addstr(self.y, self.x, self.text)


class Button(String):
    def __init__(self, x, y, text):
        super().__init__(x, y, text)


def image_load(file):
    return file


def button(frame, tag, text):
    _add_string(frame, tag, F"button:{text}")


def file_dialog(frame, tag, bind):
    _add_string(frame, tag, "File dialog thing.")


def image(frame, tag, image):
    _add_string(frame, tag, image)


def label(frame, tag, text):
    _add_string(frame, tag, F"label:{text}")


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


def _add_string(frame, tag, string):
    global line

    y = line
    x = 0
    line += 1

    key = item_key(frame, tag)
    window = item_get(frame)
    thing = String(x, y, string)
    thing.draw(window)

    item_set(key, thing)
    #item_get(key).draw(window)


def main(session):
    """def main"""
    global item
    item = {}

    global line
    line = 0

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    try:
        key = ord(' ')

        cursor = Cursor(session, stdscr)

        background = _new_window(0, 0, WIDTH, HEIGHT)
        background.box()

        stdscr.noutrefresh()
        background.noutrefresh()

        header1 = _new_subwindow(background, 0, 0, WIDTH, 1)
        header1.addstr(session.language.APPLICATION_TITLE)

        header2 = _new_subwindow(background, 0, HEIGHT - 1, WIDTH, 1)
        header2.addstr(session.language.CURSES_EXIT)


        index = 0
        for window in session.window:
            key2 = frame_key(index)

            frame = _new_window(
                1,
                1,
                WIDTH - 1,
                HEIGHT - 2,
            )

            frame_set(key2, frame)
            window.main(session, key2)

            #stdscr.noutrefresh()
            #frame.noutrefresh()

            index += 1

        frame = show_frame(frame_key(0))

        curses.doupdate()

        while key != ord('q'):

            if key == ord(' '):
                # refresh
                stdscr.noutrefresh() # one time only?
                background.noutrefresh()
                frame.noutrefresh()
                curses.doupdate()

                for key, thing in item.items():
                    if "-" not in key:
                        continue
#                    split = key.split("-")[0]
#                    if split
                    if thing.select(cursor.x - 1, cursor.y - 1):
                        new = thing.text.split(":")[1]
                        indexer = int(new.split(" ")[1])

                        frame.clear()
                        frame = frame_get(new)

                        line = 0
                        key2 = frame_key(indexer)
                        session.window[indexer].main(session, key2)

                        stdscr.noutrefresh()
                        frame.noutrefresh()

                        print(thing.text)

            cursor.input(key)
            cursor.move()

            key = stdscr.getch()

    finally:
        stdscr.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()
