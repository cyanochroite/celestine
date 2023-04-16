""""""

from celestine.window.window import Window as window

from .package import package


class Window(window):
    """"""

    def data(self, container):
        """"""
        container.data = package.window(
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
        package.doupdate()

    def __enter__(self):
        super().__enter__()

        self.stdscr = package.initscr()
        package.cbreak()
        package.noecho()
        self.stdscr.keypad(1)
        package.start_color()

        self.background = package.window(0, 0, self.width, self.height)
        self.background.box()

        header = package.subwindow(self.background, 0, 0, self.width, 1)
        header.addstr(self.session.language.APPLICATION_TITLE)

        footer = package.subwindow(
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
                        case package.KEY_UP:
                            self.cord_y -= 1
                        case package.KEY_DOWN:
                            self.cord_y += 1
                        case package.KEY_LEFT:
                            self.cord_x -= 1
                        case package.KEY_RIGHT:
                            self.cord_x += 1

                    self.cord_x %= self.width
                    self.cord_y %= self.height
                    self.stdscr.move(self.cord_y, self.cord_x)
                case package.KEY_EXIT:
                    break
                case package.KEY_CLICK:
                    (x_dot, y_dot) = (
                        self.cord_x - 1,
                        self.cord_y - 1,
                    )
                    self.page.poke(x_dot, y_dot)

        self.stdscr.keypad(0)
        package.echo()
        package.nocbreak()
        package.endwin()
        return False

    def __init__(self, session, element, size, **star):
        super().__init__(session, element, size, **star)
        self.background = None
        self.cord_x = 0
        self.cord_y = 0
        self.frame = None
        self.stdscr = None
