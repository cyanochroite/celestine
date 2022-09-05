import dearpygui.dearpygui as dpg
from math import sin

dpg.create_context()


def render_login():
    """
    Position the login window in the middle of the screen
    """
    if not dpg.does_item_exist("login_window"):
        return
    main_width = dpg.get_viewport_width()
    main_height = dpg.get_viewport_height()
    login_width = dpg.get_item_width("login_window")
    login_height = dpg.get_item_height("login_window")
    pos_x = int((main_width // 2 - login_width // 2))
    pos_y = int((main_height / 2 - login_height / 2))
    dpg.set_item_pos("login_window", [pos_x, pos_y])


def back_to_login():
    dpg.hide_item("main_window")
    dpg.show_item("login_window")

def login():
    dpg.hide_item("login_window")
    dpg.show_item("main_window")

with dpg.window(tag="login_window", label='Login', menubar=False, no_title_bar=True, autosize=True, no_resize=True,
                no_move=True) as login_window:
    with dpg.group(horizontal=True):
        dpg.add_text("Benutzer: ", tag="login_user_name_text")
        dpg.add_input_text()
    with dpg.group(horizontal=True):
        dpg.add_text("Password: ", tag="login_user_name_pw")
        dpg.add_input_text(tag="login_password_input", label='', default_value='', password=True,
                           on_enter=True, callback=login)
    dpg.add_checkbox(tag="login_checkbox_password_save", label="Save password", default_value=True)
    with dpg.group(horizontal=True):
        dpg.add_button(label='Login', callback=login, width=100)
    with dpg.item_handler_registry(tag="widget handler"):
        dpg.add_item_visible_handler(callback=lambda: render_login(),
                                     tag="visible_handler_login")
    dpg.bind_item_handler_registry(login_window, "widget handler")

with dpg.window(label="Tutorial", show=False, tag="main_window") as main:
    dpg.add_text("Hello")
    dpg.add_button(label="Back to Login", callback=back_to_login)

dpg.set_primary_window(main, True)
dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()