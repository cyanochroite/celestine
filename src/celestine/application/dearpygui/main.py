from celestine.application.window import Window as Window_
from celestine.package import dearpygui


class Widget():
    pass


class Button(Widget):
    def __init__(self, tag, label, sender, action, function):
        dearpygui.add_button(
            tag=tag,
            label=label,
            user_data=(sender, action),
            callback=function,
        )


class Image(Widget):
    def __init__(self, tag, file):
        image = dearpygui.load_image(file) or (0, 0, 0, [])
        self.width = image[0]
        self.height = image[1]
        self.channels = image[2]
        self.image = image[3]
        self.name = file

        with dearpygui.texture_registry(show=False):
            dearpygui.add_static_texture(
                width=self.width,
                height=self.height,
                default_value=self.image,
                tag=self.name
            )

        dearpygui.add_image(self.name, tag=tag)


class Label(Widget):
    def __init__(self, tag, text, label):
        dearpygui.add_text(
            text,
            tag=tag,
            label=F"{tag}{label}",
            show_label=True,
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
                self.frame.window.item_key(self.frame.tag, tag),
                label,
                self.frame.tag,
                action,
                self.frame.window.show_frame_simple,
            ),
        )

    def image(self, tag, image):
        return self.frame.item_set(
            tag,
            Image(
                self.frame.window.item_key(self.frame.tag, tag),
                image,
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



