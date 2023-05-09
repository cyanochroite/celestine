""""""

from celestine.package import dearpygui
from celestine.window.window import Window as window


class Window(window):
    """"""

    def view(self, name, document):
        value = self.container.drop(name)
        value.data = dearpygui.window(tag=value.tag)
        self._view.set(name, value)
        with value.data:
            dearpygui.configure_item(value.tag, show=False)
            document(value)
            value.spot(0, 0, 1920, 1080)
            value.draw(None, make=True)

    def draw(self, **star):
        """"""

    def turn(self, page, **star):
        if self.page:
            dearpygui.hide_item(self.page.tag)

        super().turn(page, **star)

        tag = self.page.tag
        dearpygui.show_item(tag)
        dearpygui.set_primary_window(tag, True)

    def __enter__(self):
        super().__enter__()
        title = self.session.language.APPLICATION_TITLE
        dearpygui.create_context()
        dearpygui.create_viewport(
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
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        dearpygui.setup_dearpygui()
        dearpygui.show_viewport(minimized=False, maximized=False)
        dearpygui.start_dearpygui()
        dearpygui.destroy_context()
        self.container = None
        return False

    def __init__(self, session, element, size, **star):
        super().__init__(session, element, size, **star)
        self.tag = "window"
