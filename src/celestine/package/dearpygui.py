"""Package dearpygui."""
# https://dearpygui.readthedocs.io/en/latest/
import dearpygui.dearpygui as dpg


class Image():
    def __init__(self, file):
        image = dpg.load_image(file)
        if image is None:
            image = (0, 0, 0, [])
        self.width = image[0]
        self.height = image[1]
        #self.channels = image[2]
        self.image = image[3]
        self.name = file

        dpg.add_static_texture(
            width=self.width,
            height=self.height,
            default_value=self.image,
            tag=self.name
        )


def callback_dvd(sender, app_data, user_data):
    dpg.configure_item(user_data, show=True)


def callback_file(sender, app_data, user_data):
    array = list(app_data["selections"])
    item = ""
    if len(array) > 0:
        item = array[0]
    dpg.set_value(user_data, item)


class Window():
    def __init__(self, session):
        self.session = session
        self.item = {}

    def file_dialog(self, tag, bind):
        with dpg.file_dialog(
            label="Demo File Dialog",
            width=800,
            height=600,
            show=False,
            callback=callback_file,
            tag="__demo_filedialog",
            user_data=bind,
        ):
            dpg.add_file_extension(".*", color=(255, 255, 255, 255))
            dpg.add_file_extension("Source files (*.cpp *.h *.hpp){.cpp,.h,.hpp}", color=(0, 255, 255, 255))
            dpg.add_file_extension(".txt", color=(255, 255, 0, 255))
            dpg.add_file_extension(".gif", color=(255, 0, 255, 255), custom_text="header")
            dpg.add_file_extension(".py", color=(0, 255, 0, 255))
        item = dpg.add_button(
            label="Show File Selector",
            user_data=dpg.last_container(),
            callback=callback_dvd
        )
        self.item[tag] = item

    def image(self, tag, image):
        item = dpg.add_image(image.name)
        self.item[tag] = item

    def image_load(self, file):
        return Image(file)

    def label(self, tag, text):
        item = dpg.add_text(text, tag=tag, label="Label", show_label=True)
        self.item[tag] = item

    def run(self, app):
        title = self.session.language.TITLE
        dpg.create_context()
        dpg.create_viewport(
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

        with dpg.texture_registry(show=False):
            app.setup(self)

        with dpg.window(tag="primary_window"):
            app.view(self)

        dpg.setup_dearpygui()
        dpg.show_viewport(minimized=False, maximized=False)
        dpg.set_primary_window("primary_window", True)
        dpg.start_dearpygui()
        dpg.destroy_context()
