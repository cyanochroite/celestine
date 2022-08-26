"""Package celestine."""
import curses


HEIGHT = 24
WIDTH = 80


class Cursor():
    def __init__(self, session, stdscr):
        self.session = session
        self.stdscr = stdscr
        self.x = 0
        self.y = 0
        self.width = WIDTH
        self.height = HEIGHT

    def move(self):
        self.stdscr.move(self.y, self.x)

    def input(self, key):
        (x, y) = self.session.python.curses_cursor_input_match(
            key,
            curses,
            self.x,
            self.y
        )
        self.x = x % self.width
        self.y = y % self.height


def file_dialog(tag, bind):
    _add_string(quote_text_window, "File dialog thing.")
    item[tag] = tag


def image(tag, image):
    _add_string(quote_text_window, image)
    item[tag] = tag


def image_load(file):
    return file


def label(tag, text):
    _add_string(quote_text_window, "This is a label.")
    item[tag] = tag


def _new_window(column, row, width, height):
    nlines = height
    ncols = width
    begin_y = row
    begin_x = column
    return curses.newwin(nlines, ncols, begin_y, begin_x)


def _new_subwindow(window, column, row, width, height):
    nlines = height
    ncols = width
    begin_y = row
    begin_x = column
    return window.subwin(nlines, ncols, begin_y, begin_x)


def _add_string(window, string):
    global line

    y = line
    x = 0
    line += 1
    window.addstr(y, x, string)


def main(session):
    """def main"""
    global item
    item = {}

    global line
    line = 0

    global quote_window
    quote_window = None

    global quote_text_window
    quote_text_window = None

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    try:
        key = 0

        cursor = Cursor(session, stdscr)

        quote_window = _new_window(0, 0, WIDTH, HEIGHT)
        quote_window.box()

        header1 = _new_subwindow(quote_window, 0, 0, WIDTH, 1)
        header1.addstr(session.language.APPLICATION_TITLE)

        header2 = _new_subwindow(quote_window, 0, HEIGHT - 1, WIDTH, 1)
        header2.addstr(session.language.CURSES_EXIT)

        quote_text_window = _new_subwindow(quote_window, 1, 1, WIDTH - 1, HEIGHT - 2)

        session.window.setup(session)
        session.window.view(session)

        stdscr.noutrefresh()
        quote_window.noutrefresh()
        curses.doupdate()

        while key != ord('q'):
            stdscr.refresh()

            cursor.input(key)
            cursor.move()

            key = stdscr.getch()

    finally:
        stdscr.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()


# <pep8-80 compliant>
import bpy  # pylint: disable=import-error

from . import data
from . import make
from . import mesh
from . import preferences
from . import UV


ready = False
Image_Formats = [
    ".bmp",
    ".sgi",
    ".rgb",
    ".bw",
    ".png",
    ".jpg",
    "jpeg",
    ".jp2",
    ".jp2",
    ".j2c",
    ".tga",
    ".cin",
    ".dpx",
    ".exr",
    ".hdr",
    ".tif",
    ".tiff"
]


class BOORU_mesh_make(bpy.types.Operator):
    bl_label = "Plane"
    bl_idname = "blenderbooru.mesh_make"

    def __init__(self):
        self.spot = 0

    def _new_object(self, context, image):
        mush = mesh.image(image)
        box = make.mesh("image", mush)
        box.location = (self.spot, 0, 0)
        self.spot += 2.5
        return box

    def execute(self, context):
        print("start")
        self.spot = 0
        from .plugin import OS
        content = preferences.content()
        (path, file) = OS.walk_directory(content.root)
        images = []
        for (filenames) in file:
            (dirpath, name) = filenames
            ext = OS.file_extension(name).lower()
            if ext in Image_Formats:
                merge = OS.join(dirpath, name)
                images.append(merge)
        for file in images:
            print("convert " + file)
            image = data.image.load(file)
            material = UV.material("pretty", image)
            object = self._new_object(context, image)
            object.data.materials.append(material)
        print("done")
        return {'FINISHED'}


class BOORU_mesh_delete(bpy.types.Operator):
    bl_label = "Delete Me Now"
    bl_idname = "blenderbooru.mesh_delete"

    def execute(self, context):
        # currently selected at the momnet
        object = bpy.context.object
        if object:
            # what about the other materials?
            if object.active_material:
                data.material.remove(object.active_material)
            data.object.remove(object)
        return {'FINISHED'}


class BOORU_clear_all(bpy.types.Operator):
    bl_label = "Clear all data"
    bl_idname = "blenderbooru.clear_all"

    def execute(self, context):
        # this probably highly unoptimized.
        # try doing this backwarks
        for camera in bpy.data.cameras:
            data.camera.remove(camera)
        for light in bpy.data.lights:
            data.light.remove(light)
        for material in bpy.data.materials:
            data.material.remove(material)
        for mesh in bpy.data.meshes:
            data.mesh.remove(mesh)
        for image in bpy.data.images:
            data.image.remove(image)
        for texture in bpy.data.textures:
            data.texture.remove(texture)
        light = make.light.sun("lili")
        light.location = (0, 0, 1)
        camera = make.camera("cool cat")
        camera.location = (0, 0, 10)
        return {'FINISHED'}


class BOORU_checkers(bpy.types.Operator):
    bl_label = "Spawn Checkers"
    bl_idname = "blenderbooru.checkers"

    def _red(self, x, y, z):
        mush = mesh.plane()
        mush.location = (x, y, z)
        return mush

    def _green(self, x, y, z):
        mush = mesh.plane()
        mush.location = (x, y, z)
        return mush

    def execute(self, context):
        self._red(0, 0, 0)
        self._green(0, 10, 0)
        self._red(0, 0, 10)
        return {'FINISHED'}


class BOORU_main(bpy.types.Panel):
    bl_category = "Tab Name"
    bl_context = ""
    bl_idname = "BOORU_PT_main_panel2"
    bl_label = "Main Panel"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 0
    bl_owner_id = ""
    bl_parent_id = ""
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_translation_context = "*"
    bl_ui_units_x = 0

    bl_label = "Select a TAG"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    #bl_context = 'object'
    # bl_context = "OBJECT"
    bl_options = {'DEFAULT_CLOSED'}
    ###
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "bbb"
    bl_label = "Landmarks yay"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global ready
        if not ready:
            self.layout.operator("blenderbooru.register")
        else:
            self.layout.operator("blenderbooru.unregister")
            #
            self.layout.label(text="Hello World")
            self.layout.operator("blenderbooru.mesh_make")
            self.layout.operator("blenderbooru.mesh_delete")
            self.layout.operator("blenderbooru.clear_all")
            self.layout.operator("blenderbooru.checkers")
            #
            content = preferences.content()
            self.layout.prop(content, "boolean")
            if content.boolean:
                self.layout.label(text="checkbox is on")
            else:
                self.layout.label(text="checkbox is off")


class BOORU_register(bpy.types.Operator):
    bl_label = "Startup"
    bl_idname = "blenderbooru.register"

    def execute(self, context):
        global ready
        data.register()
        ready = True
        return {'FINISHED'}


class BOORU_unregister(bpy.types.Operator):
    bl_label = "Shutdown"
    bl_idname = "blenderbooru.unregister"

    def execute(self, context):
        global ready
        data.unregister()
        ready = False
        return {'FINISHED'}


def register():
    bpy.utils.register_class(BOORU_main)
    bpy.utils.register_class(BOORU_mesh_make)
    bpy.utils.register_class(BOORU_mesh_delete)
    bpy.utils.register_class(BOORU_clear_all)
    bpy.utils.register_class(BOORU_checkers)
    #
    bpy.utils.register_class(BOORU_unregister)
    bpy.utils.register_class(BOORU_register)


def unregister():
    bpy.utils.unregister_class(BOORU_checkers)
    bpy.utils.unregister_class(BOORU_mesh_delete)
    bpy.utils.unregister_class(BOORU_mesh_make)
    bpy.utils.unregister_class(BOORU_clear_all)
    bpy.utils.unregister_class(BOORU_main)
    #
    bpy.utils.unregister_class(BOORU_register)
    bpy.utils.unregister_class(BOORU_unregister)
