"""Package dearpygui."""
# https://dearpygui.readthedocs.io/en/latest/
import dearpygui.dearpygui as dpg

from celestine.application.window import Window as Window_


class Wiget():
    def __init__(self, window, item):
        self.window = window
        self.item = item

    def grid(self, cord_x, cord_y):
        self.window.grid[cord_y][cord_x] = self.item


class Button(Wiget):
    def __init__(self, window, frame, tag, label, action):
        super().__init__(
            window,
            (
                dpg.add_button,
                (),
                {
                    "tag": window.item_key(frame, tag),
                    "label": F"{tag}{label}",
                    "user_data": action,
                    "callback": window.show_frame,
                }
            ),
        )


class Label(Wiget):
    def __init__(self, window, frame, tag, label, text):
        super().__init__(
            window,
            (
                dpg.add_text,
                (text),
                {
                    "tag": window.item_key(frame, tag),
                    "label": F"{tag}{label}",
                    "show_label": True,
                }
            ),
        )


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

        with dpg.texture_registry(show=False):
            dpg.add_static_texture(
                width=self.width,
                height=self.height,
                default_value=self.image,
                tag=self.name
            )


class Window(Window_):

    def __init__(self, session):
        super().__init__(session)
        ignore = None

    def item_key(self, frame, tag):
        return F"_{frame}__{tag}"

    def frame_key(self, index):
        return F"Page {index}"

    def show_frame(self, sender, app_data, user_data):
        """Some other callback thing."""
        current = int(sender.split("_")[1])
        index = self.frame_get(current)
        dpg.hide_item(index)
        # to field
        self.show_frame_simple(user_data)

    def show_frame_simple(self, index):
        frame = self.frame_get(index)
        dpg.show_item(frame)
        dpg.set_primary_window(frame, True)

    def callback_dvd(self, sender, app_data, user_data):
        """Some other callback thing."""
        dpg.configure_item(user_data, show=True)

    def callback_file(self, sender, app_data, user_data):
        """File dialaog callback."""
        array = list(app_data["selections"])
        item = ""
        if len(array) > 0:
            item = array[0]
        dpg.set_value(user_data, item)

    def image_load(self, file):
        """Load image."""
        return Image(file)

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

    def file_dialog(self, frame, tag, bind, cord_x, cord_y):
        """Make file dialog."""
        key = self.item_key(frame, tag)
        with dpg.file_dialog(
            label="Demo File Dialog",
            width=800,
            height=600,
            show=False,
            callback=self.callback_file,
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

        self.grid[cord_y][cord_x] = (dpg.add_button, (), {
            "tag": key,
            "label": "Show File Selector",
            "user_data": dpg.last_container(),
            "callback": self.callback_dvd,
        })

        self.item[tag] = self.grid[cord_y][cord_x]

    def image(self, frame, tag, image, cord_x, cord_y):
        """Make image."""
        key = self.item_key(frame, tag)
        self.grid[cord_y][cord_x] = (dpg.add_image, (image.name), {})
        #image = dpg.add_image(image.name)
        self.item[key] = image

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

    def main(self):
        """def main"""

        title = self.session.language.APPLICATION_TITLE
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

        index = 0
        for window in self.session.window:
            self.grid = []
            for rowrow in range(self.rows):
                temp = []
                for colcol in range(self.cols):
                    temp.append(None)
                self.grid.append(temp)

            self.grid[0][0] = (dpg.add_text, (f"moo Row{0} Column{4}"), {})
            self.grid[1][0] = (dpg.add_text, (f"moo Row{1} Column{6}"), {})
            self.grid[2][0] = (dpg.add_text, (f"moo Row{2} Column{8}"), {})

            key = self.frame_key(index)
            self.frame_set(index, key)

            window.main(self.session, index, self)

            with dpg.window(tag=key):
                with dpg.table(header_row=False):
                    for colcol in range(self.cols):
                        dpg.add_table_column()
                    for index_a in range(self.rows):
                        with dpg.table_row():
                            for index_b in range(self.cols):
                                if self.grid[index_a][index_b]:
                                    (func, args,
                                     kw) = self.grid[index_a][index_b]
                                    if args:
                                        func(args, **kw)
                                    else:
                                        func(**kw)

            dpg.configure_item(key, show=False)
            index += 1

        self.show_frame_simple(0)

        dpg.setup_dearpygui()
        dpg.show_viewport(minimized=False, maximized=False)
        dpg.start_dearpygui()
        dpg.destroy_context()
