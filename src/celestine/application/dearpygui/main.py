"""Package dearpygui."""
# https://dearpygui.readthedocs.io/en/latest/
import dearpygui.dearpygui as dpg


def item_key(frame, tag):
    global item
    return F"{frame}-{tag}"


def item_get(frame, tag):
    global item
    return item[item_key(frame, tag)]


def item_set(frame, tag, value):
    global item
    item[item_key(frame, tag)] = value


def frame_key(index):
    return F"Page {index}"


def frame_get(frame):
    global item
    return item[frame]


def frame_set(frame, value):
    global item
    item[frame] = value


class Image():
    """Something to hold the images in."""

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
    """Some other callback thing."""
    dpg.configure_item(user_data, show=True)


def callback_file(sender, app_data, user_data):
    """File dialaog callback."""
    array = list(app_data["selections"])
    item = ""
    if len(array) > 0:
        item = array[0]
    dpg.set_value(user_data, item)


def show_frame(sender, app_data, user_data):
    """Some other callback thing."""
    current = sender.split("-")[0]
    dpg.hide_item(current)
    show_frame_simple(user_data)


def show_frame_simple(frame):
    dpg.show_item(frame)
    dpg.set_primary_window(frame, True)


def image_load(file):
    """Load image."""
    return Image(file)


def button(frame, tag, bind):
    """Make file dialog."""
    key = item_key(frame, tag)
    button = dpg.add_button(
        tag=key,
        label=tag,
        user_data=bind,
        callback=show_frame,
    )
    item[key] = button


def file_dialog(frame, tag, bind):
    """Make file dialog."""
    key = item_key(frame, tag)
    with dpg.file_dialog(
        label="Demo File Dialog",
        width=800,
        height=600,
        show=False,
        callback=callback_file,
        tag=key + "__demo_filedialog",
        user_data=bind,
    ):
        dpg.add_file_extension(".*", color=(255, 255, 255, 255))
        dpg.add_file_extension(
            "Source files (*.cpp *.h *.hpp){.cpp,.h,.hpp}",
            color=(0, 255, 255, 255),
        )
        dpg.add_file_extension(".txt", color=(255, 255, 0, 255))
        dpg.add_file_extension(
            ".gif", color=(255, 0, 255, 255),
            custom_text="header",
        )
        dpg.add_file_extension(".py", color=(0, 255, 0, 255))
    button = dpg.add_button(
        label="Show File Selector",
        user_data=dpg.last_container(),
        callback=callback_dvd
    )
    item[tag] = button


def image(frame, tag, image):
    """Make image."""
    key = item_key(frame, tag)
    image = dpg.add_image(image.name)
    item[key] = image


def label(frame, tag, text):
    """Make a label."""
    key = item_key(frame, tag)
    text = dpg.add_text(text, tag=key, label="Label", show_label=True)
    item[key] = text


def main(session):
    """def main"""
    global item
    item = {}

    title = session.language.APPLICATION_TITLE
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

    # with dpg.texture_registry(show=False):
    #    session.window.setup(session)

    # with dpg.window(tag="primary_window"):
    #    session.window.view(session)

    index = 0
    for window in session.window:
        key = frame_key(index)
        #frame_set(key, frame)
        with dpg.window(tag=key):
            window.main(session, key)
            dpg.configure_item(key, show=False)

        index += 1

    show_frame_simple(frame_key(0))

    dpg.setup_dearpygui()
    dpg.show_viewport(minimized=False, maximized=False)
    dpg.start_dearpygui()
    dpg.destroy_context()
