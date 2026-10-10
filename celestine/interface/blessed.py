""""""

import itertools

from celestine import (
    bank,
    literal,
)
from celestine.interface import Abstract as Abstract_
from celestine.interface import Element as Element_
from celestine.interface import (
    Object,
    Plane,
    Point,
)
from celestine.interface import Window as Window_
from celestine.literal import (
    NONE,
    TILDE,
)
from celestine.package import (
    blessed,
)
from celestine.typed import (
    GS,
    LS,
    A,
    B,
    D,
    G,
    N,
    R,
    S,
    T,
    ignore,
    override,
)

char_index = 0


class Cells:
    """Yields a row of cells from a single element."""

    def __init__(self, abstract: Abstract) -> N:
        self.iterable = iter(abstract.cells)
        self.length = abstract.area.x_len

    def __iter__(self) -> GS:
        for _ in range(self.length):
            try:
                result = next(self.iterable)
            except StopIteration:
                result = NONE
            yield result


class Lines:
    """Yields a row of cells aggregated from a row of elements."""

    def __init__(self, abstracts: T[Abstract, ...]) -> N:
        self.iterable = [Cells(abstract) for abstract in abstracts]
        self.length = abstracts[0].area.y_len if self.iterable else 0

    def __iter__(self) -> GS:
        for _ in range(self.length):
            for iterable in self.iterable:
                yield from iterable


class All:
    """Yields all rows one at a time from all children."""

    def __init__(self, element: Element) -> N:
        self.iterable = iter(element)
        self.x_len = element.width if element.width else len(element)
        self.y_len = element.height if element.height else len(element)

    def cols(self) -> G[Abstract, None, None]:
        """"""
        for _ in range(self.x_len):
            try:
                result = next(self.iterable)
            except StopIteration:
                result = Abstract(NONE)
            yield result

    def rows(self) -> G[T[Abstract, ...], None, None]:
        """"""
        for _ in range(self.y_len):
            iterable = self.cols()
            yield tuple(iterable)

    def __iter__(self) -> GS:
        for row in self.rows():
            yield from Lines(row)


class Abstract(Abstract_):
    """"""

    begin: LS
    cells: LS
    close: LS

    @override
    def build(self, parent: A, star: D[S, A]) -> N:
        """"""
        super().build(parent, star)
        self.cells = [NONE] * self.area.z_len

    def __init__(self, name: S, **star: R) -> N:
        super().__init__(name, **star)
        self.begin = []
        self.cells = []
        self.close = []


class Element(Element_, Abstract):
    """"""

    @override
    def draw(self) -> B:
        """"""
        if not super().draw():
            return False

        length = len(self)
        if length:
            # View object
            iterable = All(self)
            self.cells = list(iterable)
        else:
            # Element

            global char_index
            chars = ["!", "@", "#", "$", "%", "^", "&", "*"] * 100
            char = chars[char_index]
            char_index += 1
            repeat = itertools.repeat(char, self.area.z_len)
            chain = itertools.chain(*self.text, repeat)
            sliced = itertools.islice(chain, self.area.z_len)
            self.cells = list(sliced)

            peek = self.cells[0:100]

        return True


class Window(Window_, Abstract):
    """"""

    mouse: Point
    terminal: blessed.Terminal

    @override
    def draw(self) -> B:
        """"""
        if not super().draw():
            return False

        cache = []
        for value in self:
            if not value.hidden:
                cache = value.cells

        self.cells = cache.copy()
        index = self.mouse.y_var * self.area.x_len + self.mouse.x_var
        if self.cells:
            self.cells[index] = "?"

        objects: LS = []
        objects.extend(self.begin)
        objects.extend(self.cells)
        objects.extend(self.close)

        print(*objects, sep=NONE, end=NONE, file=None, flush=True)

        return True

    @override
    @classmethod
    def make(cls, *data: A, **star: R) -> Object:
        """"""
        ignore(cls)
        result = Element(*data, **star)
        return result

    def move_down(self) -> N:
        """"""
        x = self.mouse.x_var
        y = self.mouse.y_var + 1
        if y > self.area.y_max:
            y = self.area.y_min

        self.mouse = Point(x, y)
        self.make_dirty()

    def move_left(self) -> N:
        """"""
        x = self.mouse.x_var - 1
        y = self.mouse.y_var
        if x < self.area.x_min:
            x = self.area.x_max

        self.mouse = Point(x, y)
        self.make_dirty()

    def move_right(self) -> N:
        """"""
        x = self.mouse.x_var + 1
        y = self.mouse.y_var
        if x > self.area.x_max:
            x = self.area.x_min

        self.mouse = Point(x, y)
        self.make_dirty()

    def move_up(self) -> N:
        """"""
        x = self.mouse.x_var
        y = self.mouse.y_var - 1
        if y < self.area.y_min:
            y = self.area.y_max

        self.mouse = Point(x, y)
        self.make_dirty()

    @override
    def run(self) -> N:
        """"""
        terminal = self.terminal
        term = terminal

        with term.cbreak(), term.fullscreen(), term.hidden_cursor():
            super().run()

            self.is_dirty = True  # Why is this here?
            while True:
                bank.dequeue()
                self.draw()
                key = terminal.inkey()

                match key:
                    case literal.SPACE:
                        self.clicker(self, self.mouse)
                    case _:
                        pass

                # KEY_DELETE and KEY_BACKSPACE
                match key.code:
                    case terminal.KEY_DOWN:
                        self.move_down()
                    case terminal.KEY_ENTER:
                        self.clicker(self, self.mouse)
                    case terminal.KEY_ESCAPE:
                        break
                    case terminal.KEY_LEFT:
                        self.move_left()
                    case terminal.KEY_RIGHT:
                        self.move_right()
                    case terminal.KEY_UP:
                        self.move_up()
                    case _:
                        pass

    @override
    def __init__(self) -> N:
        super().__init__()

        terminal = blessed.Terminal()

        size_x = terminal.width
        size_y = terminal.height
        self.area = Plane.make(size_x - 1, size_y - 1)
        self.terminal = terminal

        self.begin.append(terminal.clear)
        self.begin.append(terminal.home)
        self.begin.append(terminal.white_on_blue)

        self.mouse = Point(0, 0)


ignore(
    Window,
)

# cat and dog don't hide because there is nothing to draw instead
# need to rework to have a background, or resize and have others grow

# need a way to loop over all children with a function.
