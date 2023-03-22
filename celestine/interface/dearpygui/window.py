""""""

from celestine.window.container import Container
from celestine.window.window import Window as window

from . import package
from .element import (
    Button,
    Image,
    Label,
)


class Window(window):
    """"""

    def page(self, name, document):
        value = self.container.drop(name)
        value.data = package.window(tag=value.tag)
        self.item_set(name, value)
        with value.data:
            package.configure_item(value.tag, show=False)
            document(value)
            value.spot(0, 0, 1920, 1080)
            value.draw(None)

    def turn(self, page, **star):
        if self.last:
            package.hide_item(self.last)

        book = self.item_get(page)
        tag = book.tag
        package.show_item(tag)
        package.set_primary_window(tag, True)

        self.last = page

    def __enter__(self):
        self.last = None
        #
        super().__enter__()
        title = self.session.language.APPLICATION_TITLE
        package.create_context()
        package.create_viewport(
            title=title,
            small_icon="celestine_small.ico",
            large_icon="celestine_large.ico",
            width=1920,
            height=1080,
            x_pos=256,
            y_pos=256,
            min_width=640,
            max_width=3840,
            min_height=480,
            max_height=2160,
            resizable=True,
            vsync=True,
            always_on_top=False,
            decorated=True,
            clear_color=(0, 0, 0),
        )

        self.container = Container(
            self.session,
            "window",
            self,
            Button,
            Image,
            Label,
            x_min=0,
            y_min=0,
            x_max=1920,
            y_max=1080,
            offset_x=0,
            offset_y=0,
        )

        self.tag = "window"

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        package.setup_dearpygui()
        package.show_viewport(minimized=False, maximized=False)
        package.start_dearpygui()
        package.destroy_context()
        self.container = None
        return False
