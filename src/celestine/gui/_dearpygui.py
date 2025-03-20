from celestine.package.python.os import os
from celestine.package.pillow.Image import Image
from celestine.package.pillow.ImageDraw import ImageDraw
from celestine.package.pillow.ImageFont import ImageFont

#import PIL.Image










############## convert.py
import PIL.Image;
import os;
import hashlib;

def image_open(path):#{
    return PIL.Image.open(path);
#}

def image_new(size):#{
    mode = "RGBA";
#    size = size;
    color = (0x00,0x00,0x00,0x00);
    return PIL.Image.new(mode,size,color);
#}

def image_save(image, path):#{
    if os.path.isfile(path):#{
        os.remove(path);
    #}
    with open(path, "wb") as file:#{
        image.save(file, "PNG", optimize=True);
    #}
#}
        
def file_cypher(path):#{
    cypher = hashlib.sha3_512();
    with open(path, "rb") as file:#{
        cypher.update(file.read());
    #}
    return cypher.hexdigest().upper();
#}
    
def os_rename(open_spot, save_path):#{
    save_spot = save_path + file_cypher(open_spot) + ".png";
    if not os.path.isfile(save_spot):#{
        os.rename(open_spot, save_spot);
    #}
#}

def file_save(load_file):#{
    load_path = "D:/todo/"
    save_path = "D:/done/";
    save_file = "demo.png";
    base = image_open(load_path + load_file);
    image = image_new(base.size);
    image.paste(base);
    image_save(image, save_path + save_file);
    os_rename(save_path + save_file, save_path);
#}
print("scan");


#file_save("Control_Screenshot_2.jpg");
#file_save("Control_Screenshot_3.jpg");


print("done");


############################ lookup.py


import os

path = '.'
path = os.path.abspath(path)

print(path)
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.normpath(path))
print(os.path.normpath('.'))

import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))


mypath = os.path.normpath(path)
f = []
for (dirpath, dirnames, filenames) in os.walk(mypath):
    f.extend(filenames)
    break

for (path) in f:
    print("HI " + path)

print(f)

###############################

class Array:
    @staticmethod
    def subdivide(array, subdivision_size):
        L = array
        S = subdivision_size
        print(array)
        print(len(range(S)))
        print(len(L))
        return [[L[a + b] for a in range(S)] for b in range(0, len(L), S)]


####
print("start")


class Style:
    def __del__(self):
        self.fill = None
        self.anchor = None
        self.spacing = None
        self.align = None
        self.stroke_width = None
        self.stroke_fill = None
        self.font = None
        self.size = None

    def __init__(self, font, size):
        self.fill = (255, 255, 255)
        self.anchor = "ma"
        self.spacing = 4
        self.align = "center"
        self.stroke_width = 0
        self.stroke_fill = (255, 255, 255)
        self.font = font
        self.size = size

    def truetype(self):
        return ImageFont.truetype(self.font, self.size)

    def text(self, x, y, text, ImageDraw):
        xy = (int(x), int(y))
        text = text
        fill = self.fill,
        font = self.truetype()
        anchor = self.anchor
        spacing = self.spacing
        align = self.align
        direction = None
        features = None
        language = None
        stroke_width = self.stroke_width
        stroke_fill = self.stroke_fill
        embedded_color = "SBIX"
        ImageDraw.text(xy, text, fill, font, anchor, spacing, align, direction, features, language, stroke_width, stroke_fill, embedded_color)


class Style2:
    def __del__(self):
        self.fill = None
        self.anchor = None
        self.spacing = None
        self.align = None
        self.stroke_width = None
        self.stroke_fill = None
        self.font = None
        self.size = None

    def __init__(self, font, size):
        self.fill = 255
        self.anchor = "ma"
        self.spacing = 4
        self.align = "center"
        self.stroke_width = 0
        self.stroke_fill = 255
        self.font = font
        self.size = size

    def truetype(self):
        return ImageFont.truetype(self.font, self.size)

    def text(self, x, y, text, ImageDraw):
        xy = (int(x), int(y))
        text = text
        fill = self.fill,
        font = self.truetype()
        anchor = self.anchor
        spacing = self.spacing
        align = self.align
        direction = None
        features = None
        language = None
        stroke_width = self.stroke_width
        stroke_fill = self.stroke_fill
        embedded_color = False
        ImageDraw.text(xy, text, fill, font, anchor, spacing, align, direction, features, language, stroke_width, stroke_fill, embedded_color)


class Canvas:
    def __del__(self):
        self.height = None
        self.ratio = None
        self.width = None

    def __init__(self, x1, y1, x2, y2):
        self.x1 = int(round(x1))
        self.y1 = int(round(y1))
        self.x2 = int(round(x2))
        self.y2 = int(round(y2))
        self.height = self.y2 - self.y1
        self.width = self.x2 - self.x1
        self.ratio = self.width / self.height

    @classmethod
    def scale(cls, canvas, x, y):
        width = canvas.width * x
        height = canvas.height * y
        offset_x = (canvas.width - width) / 2
        offset_y = (canvas.height - height) / 2
        return cls(offset_x, offset_y, offset_x + width, offset_y + height)


JPG_QUALITY = 100
#
screen = Canvas(0, 0, 3840, 2160)
screen = Canvas(0, 0, 1920 * 4, 1080 * 4)
action_safe = Canvas.scale(screen, 0.93, 0.93)
title_safe = Canvas.scale(screen, 0.80, 0.90)
#
picture = Canvas(0, 0, screen.width, screen.width / 2)
caption = Canvas(title_safe.x1, picture.height, title_safe.x2, screen.height)
text = Canvas(0, 0, caption.width, caption.height / 3)
#
page = Canvas(0, 0, screen.height * 8.5 / 11, screen.height)
page_left = Canvas(0, 0, page.width, page.height)
page_right = Canvas(screen.width / 2, 0, page.width, page.height)



paths = [
    ("Control_Screenshot_2.jpg", "Phil in his military uniform", "November 1944", ""),
    ("Control_Screenshot_3.jpg", "Phil in his military uniform", "November 1944", "")
]

# ("A.jpg", "1234567890!@#$%^&*()_+=-[]}{;':./?>,<QWzxZXOILPyY", "1234567890!@#$%^&*()_+=-[]}{;':./?>,<QWzxZXOILPyY", "1234567890!@#$%^&*()_+=-[]}{;':./?>,<QWzxZXOILPyY"),


def convert_to_jpg(array):
    global screen
    global text

    (name, text_0, text_1, text_2) = array
    path = os.join("todo", name)
    print("convert " + path)

    photo = Image.open(path)

    mode = "L" if photo.image.mode == "L" else "RGB"

    image = Image.new("RGB", screen.width, screen.height)

    #style = Style("/System/Library/Fonts/HelveticaNeue.ttc", 64)
    #style = Style("/System/Library/Fonts/Supplemental/AmericanTypewriter.ttc", 128)
    print("C:\Windows\Fonts\Arial.ttf")
    style = Style("C:\Windows\Fonts\Arial.ttf", 128)
    

    line = [item for item in [text_0, text_1, text_2] if item != ""]
    lines = len(line)

    picture = Canvas(0, 0, screen.width, screen.height - (text.height * lines))
    new_width = picture.width
    new_height = picture.height
    if photo.ratio >= picture.ratio:
        new_height = round(picture.width / photo.ratio)
    else:
        new_width = round(picture.height * photo.ratio)
    photo.resize(new_width, new_height)
    offx = (picture.width - new_width) / 2
    offy = (picture.height - new_height) / 2

    image.paste(photo, offx, offy)
    draw = ImageDraw.Draw(image.image)

    if lines == 0:
        pass
    if lines == 1:
        style.text(screen.width / 2, caption.y1 + (text.height * 2), line[0], draw)
    if lines == 2:
        style.text(screen.width / 2, caption.y1 + (text.height * 1), line[0], draw)
        style.text(screen.width / 2, caption.y1 + (text.height * 2), line[1], draw)
    if lines == 3:
        style.text(screen.width / 2, caption.y1 + (text.height * 0), line[0], draw)
        style.text(screen.width / 2, caption.y1 + (text.height * 1), line[1], draw)
        style.text(screen.width / 2, caption.y1 + (text.height * 2), line[2], draw)

    image.convert(mode)

    new_name = os.join("D:/done", name)
    names = new_name.split(".")
    image_save = names[0] + ".jpg"
    print("saved " + image_save)
    image.save_jpg(image_save)


def make_dvd(left, right):
    name1 = os.join("D:/todo", left)
    name2 = os.join("D:/todo", right)
    print("convert " + name1)
    print("convert " + name2)
    background = Image.new("RGB", screen.width, screen.height)

    image_left = Image.open(name1)
    image_left.resize_to_height(screen.height)

    image_right = Image.open(name2)
    image_right.resize_to_height(screen.height)

    screen_middle = screen.width / 2
    background.paste(image_left, screen_middle - image_left.width, 0)
    background.paste(image_right, screen_middle, 0)

    new_name = os.join("done", left)
    names = new_name.split(".")
    image_save = names[0] + ".jpg"
    print("saved " + image_save)
    background.save_jpg(image_save)







print("finish")


# https://help.fontlab.com/fontlab/7/manual/Color-Font-Formats/


print("scan")


def load_paths():
    (path, file) = os.chdir("D:/todo", os.walk_directory)
    os.chdir("D:/done", os.makedirs, path)
    array = []
    for (item) in file:
        root = "D:/todo"
        (name, path) = item
        array.append(name)
    return array


def jpg_quality_test(path):
    image_open = os.join("D:/todo", path)
    image = Image.open(image_open)
    for quality in range(101):
        name = str(quality) + ".jpg"
        image_save = os.join("done", name)
        print("saved " + image_save)
        image.save_jpg(image_save, quality)




def main(array):
    for item in array:
        convert_to_jpg(item)


def dvd(array):
    for item in Array.subdivide(array, 2):
        left = item[0]
        right = item[1]
        make_dvd(left, right)

def print_path(paths):
    paths.sort()
    # paths.remove(".DS_Store")
    for item in paths:
        print(item + ",")

#main(paths)
#paths = load_paths()
#print_path(paths)

#dvd(paths)

# jpg_quality_test(paths[0])


print("done")


# /System/Library/Fonts/Supplemental/Arial\ Unicode.ttf
# /System/Library/Fonts/Supplemental/AmericanTypewriter.ttc



###########################
import celestine.core.star


import dearpygui
import dearpygui.dearpygui as dpg

def callback_testy(sender, app_data, user_data):
    print(sender)


def callback_main(sender, app_data, user_data):
    global paths
    main(paths)

def callback_dvd(sender, app_data, user_data):
    global paths
    dvd(paths)

def callback_test(sender, app_data, user_data):
    global paths
    jpg_quality_test(paths)

def callback_star(sender, app_data, user_data):
    star.main.main()

###########################

from celestine.package.dearpygui.file_dialog import file_dialog

def callback(sender, app_data, user_data):
    print("Sender: ", sender)
    print("App Data: ", app_data)
    print("user_data Data: ", user_data)

def callback_file_dialog(sender, app_data, user_data):
    selection = file_dialog.selection(app_data)
    if selection:
        selection = selection[0]
    if user_data:
        dpg.set_value(user_data, selection)
    print(selection)
    print(user_data)

def callback2(sender, app_data, user_data):
    dpg.configure_item("file_dialog_id", user_data="cat")
    dpg.show_item("file_dialog_id")



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



def callback2(sender, app_data, user_data):
    value = dpg.get_value("input")
    dpg.set_value("print", value)


def window():
    dpg.add_file_dialog(directory_selector=True, show=False, callback=callback_file_dialog, tag="file_dialog_id", user_data="cows")
    #
    with dpg.window(label="Dear PyGui Demo", width=800, height=800, pos=(100, 100), tag="Main"):
        dpg.add_input_text(label="moo", tag="cat")
        dpg.add_button(label="Directory Selector", callback=callback2)
        
        dpg.add_button(label="Test", tag="Test", callback=callback_testy)
        dpg.add_button(label="DVD", callback=callback_dvd)
        dpg.add_button(label="Main", callback=callback_main)
        dpg.add_button(label="JPG", callback=callback_test)
        dpg.add_button(label="Star", callback=callback_star)

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
    
        # main stuff
        dpg.add_input_text(label="moo", tag="input")
        dpg.add_button(label="Directory Selector", callback=callback2)
        dpg.add_text(label="Result", tag="print")
        

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

###########################
dearpygui.dearpygui.create_context()
dpg.create_viewport(title='Custom Title', width=2600, height=1600)
dearpygui.dearpygui.setup_dearpygui()

debug=False
if debug:
    dearpygui.dearpygui.show_style_editor()
    dearpygui.dearpygui.show_metrics()
    dearpygui.dearpygui.show_about()
    dearpygui.dearpygui.show_debug()
    dearpygui.dearpygui.show_documentation()
    dearpygui.dearpygui.show_font_manager()
    dearpygui.dearpygui.show_item_registry()

window()

dpg.set_primary_window("Main", True)


dearpygui.dearpygui.show_viewport(minimized=False, maximized=False)
dearpygui.dearpygui.start_dearpygui()
dearpygui.dearpygui.destroy_context()


    
