"""Package celestine."""
import curses


HEIGHT = 24
WIDTH = 80


class Frame():
    def __init__(self, frame):
        self.frame = frame
        self.item = {}

    def item_get(self, tag):
        return self.item[tag]

    def item_set(self, tag, value):
        self.item[tag] = value

    def clear(self):
        self.frame.clear()

    def noutrefresh(self):
        self.frame.noutrefresh()



def item_get(frame, tag):
    global item
    return item[frame].item_get(tag)


def item_set(frame, tag, value):
    global item
    item[frame].item_set(tag, value)


def frame_get(index):
    global item
    return item[index].frame


def frame_set(index, value):
    global item
    item[index] = value


def show_frame(index):
    global item
    return frame_get(index)


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

    window = frame_get(frame)
    thing = String(x, y, string)
    thing.draw(window)

    item_set(frame, tag, thing)


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

            _frame = _new_window(
                1,
                1,
                WIDTH - 1,
                HEIGHT - 2,
            )
            frame = Frame(_frame)

            frame_set(index, frame)
            window.main(session, index)

            #stdscr.noutrefresh()
            #frame.noutrefresh()

            index += 1

        display_it_now = 0

        frame = show_frame(display_it_now)

        curses.doupdate()

        while key != ord('q'):

            if key == ord(' '):
                # refresh
                stdscr.noutrefresh() # one time only?
                background.noutrefresh()
                frame.noutrefresh()
                curses.doupdate()

                for key, thing in item[display_it_now].item.items():
                    if thing.select(cursor.x - 1, cursor.y - 1):
                        new = thing.text.split(":")[1]
                        indexer = int(new.split(" ")[1])

                        frame.clear()
                        frame = frame_get(indexer)

                        line = 0
                        session.window[indexer].main(session, indexer)

                        stdscr.noutrefresh()
                        frame.noutrefresh()

                        display_it_now = indexer

                        print(thing.text)

            cursor.input(key)
            cursor.move()

            key = stdscr.getch()

    finally:
        stdscr.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()
