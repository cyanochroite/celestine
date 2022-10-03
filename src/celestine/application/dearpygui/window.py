from celestine.application.window import Window as Window_

from . import dearpygui
from .page import Page


class Window(Window_):

    def __init__(self, session):
        super().__init__(session)

    def item_key(self, frame, tag):
        return F"_{frame}__{tag}"

    def frame_key(self, index):
        return F"Page {index}"

    def show_frame_simple(self, sender, app_data, user_data):
        """Some other callback thing."""
        (sent, frame) = user_data
        dearpygui.hide_item(sent)
        self.turn(frame)

    def turn(self, page):
        tag = self.item[page].tag
        dearpygui.show_item(tag)
        dearpygui.set_primary_window(tag, True)

    def callback_dvd(self, sender, app_data, user_data):
        """Some other callback thing."""
        dearpygui.configure_item(user_data, show=True)

    def callback_file(self, sender, app_data, user_data):
        """File dialaog callback."""
        array = list(app_data["selections"])
        item = ""
        if len(array) > 0:
            item = array[0]
        tag = sender[0:4]  # hacky
        tag = F"{tag}{user_data}"
        dearpygui.set_value(tag, item)

    def page(self):
        index = F"Page_{len(self.item)}"
        value = Page(self, index)
        self.item.append(value)
        return value

    def __enter__(self):
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
            clear_color=(0, 0, 0)
        )
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        dearpygui.setup_dearpygui()
        dearpygui.show_viewport(minimized=False, maximized=False)
        dearpygui.start_dearpygui()
        dearpygui.destroy_context()
        return False
