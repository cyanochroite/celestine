import dearpygui.dearpygui as dpg

dpg.create_context()

width, height, channels, data = dpg.load_image("24923261.jpg")


with dpg.window(label="Tutorial"):
    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="texture_tag")
    dpg.add_image("texture_tag")


dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()