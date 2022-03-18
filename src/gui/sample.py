import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

def callback0(sender, app_data, user_data):
    value = dpg.get_value("cat")
    print(value)

def callback1(sender, app_data, user_data):
    value = dpg.set_value("cat", "Moo")

def callback2(sender, app_data, user_data):
    value = dpg.set_value("cat", "Oink")

with dpg.window():
    dpg.add_input_text(tag="cat", default_value="meow")
    dpg.add_button(label="What does a cat say?", callback=callback0)
    dpg.add_button(label="It says Moo", callback=callback1)
    dpg.add_button(label="It says Oink?", callback=callback2)

dpg.show_viewport(minimized=False, maximized=False)
dpg.start_dearpygui()
dpg.destroy_context()
