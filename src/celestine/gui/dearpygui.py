import dearpygui.dearpygui as dpg

VERSION = 1.4


import dearpygui.dearpygui as dpg

path = "D:\\file\\demo.png"


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


class Window():
    def __init__(self):
        self.image = {}

    def label_add(self, name):
        image = self.image[name].image #try catch fail?
        dpg.add_image(name)

    def image_load(self, file):
        image = Image(file)
        name = image.name
        self.image[name] = image

        dpg.add_static_texture(
            width=image.width,
            height=image.height,
            default_value=image.image,
            tag=name
        )

        return name

    def run(self, setup, view):
        title = "celestine - PyPI"
        if VERSION > 900:  # Hope they fix this
            title = "celestine · PyPI"
        dpg.create_context()
        dpg.create_viewport(
            title=title,
            small_icon="celestine_small.ico",
            large_icon="celestine_large.ico",
            width=2600,
            height=1600,
            x_pos=256,
            y_pos=256,
            min_width=256,
            max_width=4096,
            min_height=256,
            max_height=4096,
            resizable=True,
            vsync=True,
            always_on_top=False,
            decorated=True,
            clear_color=(0, 0, 0)
        )


        with dpg.texture_registry(show=True):
            setup(self)

        with dpg.window(tag="primary_window"):
            view(self)

        dpg.setup_dearpygui()
        dpg.show_viewport(minimized=False, maximized=False)
        dpg.set_primary_window("primary_window", True)
        dpg.start_dearpygui()
        dpg.destroy_context()
