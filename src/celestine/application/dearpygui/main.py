from celestine.application.window import Window as Window_
from celestine.package import dearpygui


class Widget():
    def __init__(self, window, item):
        self.window = window
        self.item = item

    def grid(self, cord_x, cord_y):
        self.window.grid[cord_y][cord_x] = self.item


class Button(Widget):
    def __init__(self, sender, tag, label, action, function):
        dearpygui.add_button(
            tag=tag,
            label= label,
            user_data= (sender, action),
            callback=function,
        )


class Label(Widget):
    def __init__(self, tag, text, label):
        dearpygui.add_text(
            text,
            tag=tag,
            label=F"{tag}{label}",
            show_label=True,
        )


class Image(Widget):
    def __init__(self, window, frame, tag, image):
        super().__init__(
            window,
            (
                dearpygui.add_image,
                (image.name),
                {
                    "tag": window.item_key(frame, tag),
                }
            ),
        )


class Filee(Widget):
    def __init__(self, window, frame, tag, bind):
        with dearpygui.file_dialog(
            label="Demo File Dialog",
            width=800,
            height=600,
            show=False,
            callback=window.callback_file,
            tag=window.item_key(frame, tag) + "__demo_filedialog",
            user_data=bind,
        ):
            dearpygui.add_file_extension(".*", color=(255, 255, 255, 255))
            dearpygui.add_file_extension(
                "Source files (*.cpp *.h *.hpp){.cpp,.h,.hpp}",
                color=(0, 255, 255, 255),
            )
            dearpygui.add_file_extension(".txt", color=(255, 255, 0, 255))
            dearpygui.add_file_extension(
                ".gif", color=(255, 0, 255, 255),
                custom_text="header",
            )
            dearpygui.add_file_extension(".py", color=(0, 255, 0, 255))

        super().__init__(
            window,
            (
                dearpygui.add_button,
                (),
                {
                    "tag": window.item_key(frame, tag),
                    "label": "Show File Selector",
                    "user_data": dearpygui.last_container(),
                    "callback": window.callback_dvd,
                }
            ),
        )


class Image_load():
    """Something to hold the images in."""

    def __init__(self, file):
        image = dearpygui.load_image(file)
        if image is None:
            image = (0, 0, 0, [])
        self.width = image[0]
        self.height = image[1]
        #self.channels = image[2]
        self.image = image[3]
        self.name = file

        with dearpygui.texture_registry(show=False):
            dearpygui.add_static_texture(
                width=self.width,
                height=self.height,
                default_value=self.image,
                tag=self.name
            )


class Frame():
    def item_get(self, tag):
        return self.item[tag]

    def item_set(self, tag, value):
        self.item[tag] = value
        return value

    def __init__(self, window, tag):
        self.window = window
        self.item = {}
        self.tag = tag
        self.frame = dearpygui.window(tag=tag)

    def __enter__(self):
        self.frame.__enter__()
        dearpygui.configure_item(self.tag, show=False)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.frame.__exit__(exc_type, exc_value, traceback)
        return False

    def row(self, tag):
        return self.item_set(tag, Row(self, tag))


class Row():
    def __init__(self, frame, tag):
        self.frame = frame
        self.tag = tag
        self.row = dearpygui.group(horizontal=True)

    def __enter__(self):
        self.row.__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.row.__exit__(exc_type, exc_value, traceback)
        return False

    def button(self, tag, label, action):
        return self.frame.item_set(
            tag,
            Button(
                self.frame.tag,
                self.frame.window.item_key(self.frame.tag, tag),
                label,
                action,
                self.frame.window.show_frame_simple,
            ),
        )

    def label(self, tag, text):
        return self.frame.item_set(
            tag,
            Label(
                self.frame.window.item_key(self.frame.tag, tag),
                text,
                "Label",
            ),
        )


class Window(Window_):

    def __init__(self, session):
        super().__init__(session)
        ignore = None

    def item_key(self, frame, tag):
        return F"_{frame}__{tag}"

    def frame_key(self, index):
        return F"Page {index}"

    def show_frame_simple(self, sender, app_data, user_data):
        """Some other callback thing."""
        (sent, frame) = user_data
        dearpygui.hide_item(sent)
        self.show_frame(frame)

    def show_frame(self, index):
        tag = self.item[index].tag
        dearpygui.show_item(tag)
        dearpygui.set_primary_window(tag, True)

    def callback_dvd(self, sender, app_data, user_data):
        """Some other callback thing."""
        dearpygui.configure_item(user_data, show=True)

    def callback_file(self, sender, app_data, user_data):
        """File dialaog callback."""
        array = list(app_data["selections"])
        item = ""
        if len(array) > 0:
            item = array[0]
        tag = sender[0:4]  # hacky
        tag = F"{tag}{user_data}"
        dearpygui.set_value(tag, item)

    def image_load(self, file):
        """Load image."""
        return Image_load(file)

    def button(self, frame, tag, label, action):
        item = Button(
            self,
            frame,
            tag,
            label,
            action,
        )
        self.item_set(frame, tag, item)
        return item

    def file_dialog(self, frame, tag, bind):
        item = Filee(
            self,
            frame,
            tag,
            bind,
        )
        self.item_set(frame, tag, item)
        return item

    def image(self, frame, tag, image):
        item = Image(
            self,
            frame,
            tag,
            image,
        )
        self.item_set(frame, tag, item)
        return item

    def label(self, frame, tag, text):
        item = Label(
            self,
            frame,
            tag,
            "Label",
            text,
        )
        self.item_set(frame, tag, item)
        return item

    def frame(self):
        index = F"Page_{len(self.item)}"
        value = Frame(self, index)
        self.item.append(value)
        return value

    def main(self):
        """def main"""

        title = self.session.language.APPLICATION_TITLE
        dearpygui.create_context()
        dearpygui.create_viewport(
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

        for window in self.session.window:
            window.main(self)

        self.show_frame(0)

        dearpygui.setup_dearpygui()
        dearpygui.show_viewport(minimized=False, maximized=False)
        dearpygui.start_dearpygui()
        dearpygui.destroy_context()
