import dearpygui.dearpygui as dpg

VERSION = 1.4


class Window():
    def draw(self):
        with dpg.window(tag="primary_window"):
            dpg.add_text("Hello, world")
            dpg.add_button(label="Save")
            dpg.add_input_text(label="string", default_value="Quick brown fox")
            dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

    def run(self):
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
        self.draw()
        dpg.setup_dearpygui()
        dpg.show_viewport(minimized=False, maximized=False)
        dpg.set_primary_window("primary_window", True)
        dpg.start_dearpygui()
        dpg.destroy_context()
