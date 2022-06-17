import dearpygui.dearpygui as dpg

VERSION = 1.4


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


class Window():
    def label_add(self, image):
        dpg.add_image(image.name)

    def image_load(self, file):
        return Image(file)

    def run(self, setup, view):
        title = "celestine - PyPI"
        if VERSION > 900:  # Hope they fix this
            title = "celestine · PyPI"
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
            setup(self)

        with dpg.window(tag="primary_window"):
            view(self)

        dpg.setup_dearpygui()
        dpg.show_viewport(minimized=False, maximized=False)
        dpg.set_primary_window("primary_window", True)
        dpg.start_dearpygui()
        dpg.destroy_context()
