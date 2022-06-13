import dearpygui.dearpygui as dpg

VERSION = 1.4


import dearpygui.dearpygui as dpg

path = "D:\\file\\demo.png"


def load_image(file: str, gamma: float = 1.0, gamma_scale_factor: float = 1.0):
    return dpg.load_image(
        file,
        gamma=gamma,
        gamma_scale_factor=gamma_scale_factor
    )


class Image():
    def __init__(self, file):
        image = dpg.load_image(file)
        if image is None:
            image = (0, 0, 0, [])
        self.width = image[0]
        self.height = image[1]
        #self.channels = image[2]
        self.image = image[3]


def cat():
    load_image(path)

    load_image("cat")

    dpg.create_context()

    width, height, channels, data = dpg.load_image(path)

    with dpg.texture_registry(show=True):
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="texture_tag")

    with dpg.window(label="Tutorial"):
        dpg.add_image("texture_tag")

    dpg.create_viewport(title='Custom Title', width=800, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


class Window():
    def __init__(self):
        self.image = []

    def label_add(self, image):
        image = "texture_tag"
        with dpg.window(label="Tutorial"):
            dpg.add_image(image)

    def draw(self):
        with dpg.window(tag="primary_window"):
            dpg.add_text("Hello, world")
            dpg.add_button(label="Save")
            dpg.add_input_text(label="string", default_value="Quick brown fox")
            dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

    def image_load(self, file):
        image = Image(file)
        self.image.append(image)

        with dpg.texture_registry(show=True):
            dpg.add_static_texture(
                width=image.width,
                height=image.height,
                default_value=image.image,
                tag="texture_tag"
            )
            return image

    def run(self, call):
        name = "celestine - PyPI"
        if VERSION > 900:  # Hope they fix this
            name = "celestine · PyPI"
        dpg.create_context()
        dpg.create_viewport(
            title=name,
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

        call(self)

        dpg.setup_dearpygui()
        dpg.show_viewport(minimized=False, maximized=False)
        #dpg.set_primary_window("primary_window", True)
        dpg.start_dearpygui()
        dpg.destroy_context()

        # mvFormat_Float_rgba
