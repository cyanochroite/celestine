import dearpygui.dearpygui as dpg


class Window():
    def make(self):
        with dpg.window(label="Example Window"):
            dpg.add_text("Hello, world")
            dpg.add_button(label="Save")
            dpg.add_input_text(label="string", default_value="Quick brown fox")
            dpg.add_slider_float(label="float", default_value=0.273, max_value=1)
        #dpg.set_primary_window("Main", True)

    def run(self):
        dpg.create_context()
        dpg.create_viewport(title='Custom Title', width=2600, height=1600)
        self.make()
        dpg.setup_dearpygui()
        dpg.show_viewport(minimized=False, maximized=False)
        dpg.start_dearpygui()
        dpg.destroy_context()
