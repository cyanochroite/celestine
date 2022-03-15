import dearpygui
import dearpygui.dearpygui as dpg


def _create_static_textures():

    # create static textures
    texture_data1 = []
    for i in range(100 * 100):
        texture_data1.append(255 / 255)
        texture_data1.append(0)
        texture_data1.append(255 / 255)
        texture_data1.append(255 / 255)

    texture_data2 = []
    for i in range(50 * 50):
        texture_data2.append(255 / 255)
        texture_data2.append(255 / 255)
        texture_data2.append(0)
        texture_data2.append(255 / 255)

    texture_data3 = []
    for row in range(50):
        for column in range(50):
            texture_data3.append(255 / 255)
            texture_data3.append(0)
            texture_data3.append(0)
            texture_data3.append(255 / 255)
        for column in range(50):
            texture_data3.append(0)
            texture_data3.append(255 / 255)
            texture_data3.append(0)
            texture_data3.append(255 / 255)
    for row in range(50):
        for column in range(50):
            texture_data3.append(0)
            texture_data3.append(0)
            texture_data3.append(255 / 255)
            texture_data3.append(255 / 255)
        for column in range(50):
            texture_data3.append(255 / 255)
            texture_data3.append(255 / 255)
            texture_data3.append(0)
            texture_data3.append(255 / 255)

    dpg.add_static_texture(100, 100, texture_data1, parent="__demo_texture_container", tag="__demo_static_texture_1", label="Static Texture 1")
    dpg.add_static_texture(50, 50, texture_data2, parent="__demo_texture_container", tag="__demo_static_texture_2", label="Static Texture 2")
    dpg.add_static_texture(100, 100, texture_data3, parent="__demo_texture_container", tag="__demo_static_texture_3", label="Static Texture 3")


def _on_demo_close(sender, app_data, user_data):
    dpg.delete_item(sender)
    dpg.delete_item("__demo_texture_container")
    dpg.delete_item("__demo_colormap_registry")
    dpg.delete_item("__demo_hyperlinkTheme")
    dpg.delete_item("__demo_theme_progressbar")
    dpg.delete_item("stock_theme1")
    dpg.delete_item("stock_theme2")
    dpg.delete_item("stock_theme3")
    dpg.delete_item("stock_theme4")
    dpg.delete_item("stem_theme1")
    dpg.delete_item("__demo_keyboard_handler")
    dpg.delete_item("__demo_mouse_handler")
    dpg.delete_item("__demo_filedialog")
    dpg.delete_item("__demo_stage1")
    dpg.delete_item("__demo_popup1")
    dpg.delete_item("__demo_popup2")
    dpg.delete_item("__demo_item_reg3")
    dpg.delete_item("__demo_item_reg6")
    dpg.delete_item("__demo_item_reg7")
    dpg.delete_item("demoitemregistry")
    for i in range(7):
        dpg.delete_item("__demo_theme" + str(i))
        dpg.delete_item("__demo_theme2_" + str(i))
    for i in range(5):
        dpg.delete_item("__demo_item_reg1_" + str(i))
        dpg.delete_item("__demo_item_reg2_" + str(i))
    for i in range(3):
        dpg.delete_item("__demo_item_reg4_" + str(i))
    for i in range(4):
        dpg.delete_item("__demo_item_reg5_" + str(i))

def show_demo():

    dpg.add_texture_registry(label="Demo Texture Container", tag="__demo_texture_container")
    dpg.add_colormap_registry(label="Demo Colormap Registry", tag="__demo_colormap_registry")

    with dpg.theme(tag="__demo_hyperlinkTheme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 0, 0, 0])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 0, 0, 0])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [29, 151, 236, 25])
            dpg.add_theme_color(dpg.mvThemeCol_Text, [29, 151, 236])

    def _log(sender, app_data, user_data):
        print(f"sender: {sender}, \t app_data: {app_data}, \t user_data: {user_data}")

    _create_static_textures()

    with dpg.window(label="Dear PyGui Demo", width=800, height=800, on_close=_on_demo_close, pos=(100, 100), tag="Main"):

        with dpg.group(horizontal=True):
            with dpg.group():
                dpg.add_text("Image Button")
                dpg.add_image_button("__demo_static_texture_1")

            with dpg.group():
                dpg.add_text("Image")
                dpg.add_image("__demo_static_texture_2")

            with dpg.group():
                dpg.add_text("Image (texture size)")
                dpg.add_image("__demo_static_texture_3")

            with dpg.group():
                dpg.add_text("Image (2x texture size)")
                dpg.add_image("__demo_static_texture_3", width=200, height=200)


        with dpg.group(horizontal=True):
            with dpg.group():
                dpg.add_text("Image Button")
                dpg.add_image_button("__demo_static_texture_1")

            with dpg.group():
                dpg.add_text("Image")
                dpg.add_image("__demo_static_texture_2")

            with dpg.group():
                dpg.add_text("Image (texture size)")
                dpg.add_image("__demo_static_texture_3")

            with dpg.group():
                dpg.add_text("Image (2x texture size)")
                dpg.add_image("__demo_static_texture_3", width=200, height=200)


        with dpg.group(horizontal=True):
            with dpg.group():
                dpg.add_text("Image Button")
                dpg.add_image_button("__demo_static_texture_1")

            with dpg.group():
                dpg.add_text("Image")
                dpg.add_image("__demo_static_texture_2")

            with dpg.group():
                dpg.add_text("Image (texture size)")
                dpg.add_image("__demo_static_texture_3")

            with dpg.group():
                dpg.add_text("Image (2x texture size)")
                dpg.add_image("__demo_static_texture_3", width=200, height=200)


        with dpg.group(horizontal=True):
            with dpg.group():
                dpg.add_text("Image Button")
                dpg.add_image_button("__demo_static_texture_1")

            with dpg.group():
                dpg.add_text("Image")
                dpg.add_image("__demo_static_texture_2")

            with dpg.group():
                dpg.add_text("Image (texture size)")
                dpg.add_image("__demo_static_texture_3")

            with dpg.group():
                dpg.add_text("Image (2x texture size)")
                dpg.add_image("__demo_static_texture_3", width=200, height=200)

        with dpg.collapsing_header(label="Node Editor"):

            dpg.add_text("Ctrl+Click to remove a link.", bullet=True)

            with dpg.node_editor(callback=lambda sender, app_data: dpg.add_node_link(app_data[0], app_data[1], parent=sender),
                                 delink_callback=lambda sender, app_data: dpg.delete_item(app_data)):

                with dpg.node(label="Node 1", pos=[10, 10]):

                    with dpg.node_attribute():
                        dpg.add_input_float(label="F1", width=150)

                    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output):
                        dpg.add_input_float(label="F2", width=150)

                with dpg.node(label="Node 2", pos=[300, 10]):

                    with dpg.node_attribute() as na2:
                        dpg.add_input_float(label="F3", width=200)

                    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output):
                        dpg.add_input_float(label="F4", width=200)

                with dpg.node(label="Node 3", pos=[25, 150]):
                    with dpg.node_attribute():
                        dpg.add_input_text(label="T5", width=200)
                    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                        dpg.add_simple_plot(label="Node Plot", default_value=(0.3, 0.9, 2.5, 8.9), width=200, height=80, histogram=True)

 


dearpygui.dearpygui.create_context()
dpg.create_viewport(title='Custom Title', width=2600, height=1600)
dearpygui.dearpygui.setup_dearpygui()

dearpygui.dearpygui.show_style_editor()
dearpygui.dearpygui.show_metrics()
dearpygui.dearpygui.show_about()
dearpygui.dearpygui.show_debug()
dearpygui.dearpygui.show_documentation()
dearpygui.dearpygui.show_font_manager()
dearpygui.dearpygui.show_item_registry()

show_demo()
dpg.set_primary_window("Main", True)

dearpygui.dearpygui.show_viewport(minimized=False, maximized=False)
dearpygui.dearpygui.start_dearpygui()
dearpygui.dearpygui.destroy_context()


    
