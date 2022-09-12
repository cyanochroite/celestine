"""Package celestine."""
import curses


HEIGHT = 24
WIDTH = 80
ITEM = {}


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


class Cursor():
    def __init__(self, session, stdscr):
        self.session = session
        self.stdscr = stdscr
        self.cord_x = 0
        self.cord_y = 0
        self.width = WIDTH
        self.height = HEIGHT

    def move(self):
        self.stdscr.move(self.cord_y, self.cord_x)

    def input(self, key):
        (cord_x, cord_y) = self.session.python.curses_cursor_input_match(
            key,
            curses,
            self.cord_x,
            self.cord_y
        )
        self.cord_x = cord_x % self.width
        self.cord_y = cord_y % self.height


class Wiget():
    def __init__(self, column, row, width, height):
        self.cord_x = column
        self.cord_y = row
        self.width = width
        self.height = height

    def select(self, cord_x, cord_y):
        temp_a = cord_x >= self.cord_x
        temp_b = cord_x < self.cord_x + self.width
        temp_c = cord_y >= self.cord_y
        temp_d = cord_y < self.cord_y + self.height
        return temp_a and temp_b and temp_c and temp_d

    def unselect(self, cord_x, cord_y):
        return not self.select(cord_x, cord_y)


class String(Wiget):
    def __init__(self, x, y, text):
        super().__init__(x, y, len(text), 1)
        self.text = text

    def draw(self, window):
        window.addstr(self.cord_y, self.cord_x, self.text)


class Curses():
    @staticmethod
    def window(column, row, width, height):
        nlines = height
        ncols = width
        begin_y = row
        begin_x = column
        return curses.newwin(nlines, ncols, begin_y, begin_x)

    @staticmethod
    def subwindow(window, column, row, width, height):
        nlines = height
        ncols = width
        begin_y = row
        begin_x = column
        return window.subwin(nlines, ncols, begin_y, begin_x)

    @staticmethod
    def string(frame, tag, string, cord_x, cord_y):
        window = frame_get(frame)
        thing = String(cord_x, cord_y, string)
        thing.draw(window)
        item_set(frame, tag, thing)

    @staticmethod
    def doupdate():
        curses.doupdate()


def item_get(frame, tag):
    return ITEM[frame].item_get(tag)


def item_set(frame, tag, value):
    ITEM[frame].item_set(tag, value)


def frame_get(index):
    return ITEM[index].frame


def frame_set(index, value):
    ITEM[index] = value


def show_frame(index):
    return frame_get(index)


def image_load(file):
    return file


def button(frame, tag, text, cord_x, cord_y):
    Curses.string(frame, tag, F"button:{text}", cord_x, cord_y)


def file_dialog(frame, tag, _, cord_x, cord_y):
    Curses.string(frame, tag, "File dialog thing.", cord_x, cord_y)


def image(frame, tag, _image, cord_x, cord_y):
    Curses.string(frame, tag, _image, cord_x, cord_y)


def label(frame, tag, text, cord_x, cord_y):
    Curses.string(frame, tag, F"label:{text}", cord_x, cord_y)


def main_it(stdscr, session):
    key = ord(' ')

    cursor = Cursor(session, stdscr)

    background = Curses.window(0, 0, WIDTH, HEIGHT)
    background.box()

    header1 = Curses.subwindow(background, 0, 0, WIDTH, 1)
    header1.addstr(session.language.APPLICATION_TITLE)

    header2 = Curses.subwindow(background, 0, HEIGHT - 1, WIDTH, 1)
    header2.addstr(session.language.CURSES_EXIT)

    for index in range(len(session.window)):
        _frame = Curses.window(
            1,
            1,
            WIDTH - 1,
            HEIGHT - 2,
        )
        frame = Frame(_frame)
        frame_set(index, frame)

    display_it_now = 0

    frame = show_frame(display_it_now)
    session.window[0].main(session, 0)

    #  refresh
    stdscr.noutrefresh()
    background.noutrefresh()
    frame.noutrefresh()
    Curses.doupdate()

    while key != ord('q'):

        if key == ord(' '):

            for key, thing in ITEM[display_it_now].item.items():
                if thing.select(cursor.cord_x - 1, cursor.cord_y - 1):
                    new = thing.text.split(":")[1]
                    indexer = int(new.split(" ")[1])

                    frame.clear()
                    frame = frame_get(indexer)

                    session.window[indexer].main(session, indexer)

                    display_it_now = indexer

                    #  refresh
                    stdscr.noutrefresh()
                    background.noutrefresh()
                    frame.noutrefresh()
                    Curses.doupdate()

        cursor.input(key)
        cursor.move()

        key = stdscr.getch()


def main(session):
    curses.wrapper(main_it, session)
