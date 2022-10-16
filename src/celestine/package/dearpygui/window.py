from celestine.package.master.window import Window as master

from . import package
from .page import Page


class Window(master):
    def page(self, document):
        index = len(self.item)
        value = Page(self, str(index))
        self.item_set(index, value)
        return value

    def turn(self, page, sent=None):
        if sent:
            package.hide_item(sent)
        tag = self.item_get(page).tag
        package.show_item(tag)
        package.set_primary_window(tag, True)

    def __enter__(self):
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
            clear_color=(0, 0, 0)
        )
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        package.setup_dearpygui()
        package.show_viewport(minimized=False, maximized=False)
        package.start_dearpygui()
        package.destroy_context()
        return False

    def __init__(self, session, **kwargs):
        super().__init__(session, **kwargs)
