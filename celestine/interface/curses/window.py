""""""

from celestine.window.window import Window as master

from .package import package

from .container import Container


class Window(master):
    """"""

    def page(self, name, document):
        self.item_set(name, document)

    def turn(self, page):
        self.frame = self.container.drop(page)
        self.item_get(page)(self.frame)
        self.frame.spot(0, 0, self.width - 2, self.height - 2)

        frame = package.window(
            1,
            1,
            self.width - 1,
            self.height - 2,
        )

        for _, item in self.frame.item.items():
            item.draw(frame)

        self.stdscr.noutrefresh()
        self.background.noutrefresh()
        frame.noutrefresh()
        package.doupdate()

    def __enter__(self):
        super().__enter__()

        self.container = Container(
            self.session,
            "window",
            self.turn,
            x_min=0,
            y_min=0,
            x_max=self.width,
            y_max=self.height,
            offset_x=0,
            offset_y=0,
        )

        self.background = package.window(0, 0, self.width, self.height)
        self.background.box()

        header1 = package.subwindow(
            self.background, 0, 0, self.width, 1
        )
        header1.addstr(self.session.language.APPLICATION_TITLE)

        header2 = package.subwindow(
            self.background, 0, self.height - 1, self.width, 1
        )
        header2.addstr(self.session.language.CURSES_EXIT)

        self.stdscr.noutrefresh()
        self.background.noutrefresh()
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
                    self.frame.poke(x_dot, y_dot)

        self.stdscr.keypad(0)
        package.echo()
        package.nocbreak()
        package.endwin()
        return False

    def __init__(self, session, **kwargs):
        super().__init__(session, **kwargs)
        self.cord_x = 0
        self.cord_y = 0
        self.height = 24
        self.width = 80

        self.window = 0

        #
        self.container = None
        self.background = None

        #
        self.stdscr = package.initscr()
        package.noecho()
        package.cbreak()
        self.stdscr.keypad(1)
        package.start_color()
        #
        self.frame = None
