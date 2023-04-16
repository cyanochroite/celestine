""""""

import glob
import traceback
from typing import List

import dearpygui.dearpygui as dpg
import DearPyGui_ImageController as dpg_img

# import celestine.package.DearPyGui_ImageController as dpg_img

images_path = glob.glob("D:/file/*.*")

dpg.create_context()

dpg_img.set_texture_registry(dpg.add_texture_registry(show=True))
dpg_img.default_controller.max_inactive_time = 3
dpg_img.default_controller.unloading_check_sleep_time = 1

all_image_viewers: List[dpg_img.ImageViewer] = []


image_viewer = dpg_img.ImageViewer(unload_width=1, unload_height=1)


def add_all_images():
    """"""
    for i, file in enumerate(images_path):
        if not i % 8:
            group = dpg.add_group(horizontal=True, parent="image_group")
        _image_viewer = dpg_img.add_image(
            file, height=100, parent=group
        )  # noqa
        all_image_viewers.append(_image_viewer)


def delete_all_images():
    """"""
    for _ in range(len(all_image_viewers)):
        _image_viewer = all_image_viewers.pop()
        _image_viewer.delete()
    dpg.delete_item("image_group", children_only=True)


def set_size():
    """"""
    for _image_viewer in all_image_viewers:
        _image_viewer.set_size(width=50, height=50)


def load_image(path):
    """"""
    if path == "{None}":
        image_viewer.unload()
        dpg.set_value("image_info", path)
        return

    image_viewer.load(path)
    width = image_viewer.image.width
    height = image_viewer.image.height
    dpg.set_value("image_info", f"{path} | {width}x{height}")


with dpg.window(label="Example Window", height=400, width=500):
    with dpg.tab_bar():
        with dpg.tab(label='Example "gallery"'):
            with dpg.group(horizontal=True):
                dpg.add_button(
                    label="Set size (50x50)", callback=set_size
                )
                dpg.add_button(label="Add all", callback=add_all_images)
                dpg.add_button(
                    label="Delete all", callback=delete_all_images
                )
            with dpg.group(tag="image_group"):
                pass

        with dpg.tab(label='Example "viewer"'):
            dpg.add_combo(
                ["{None}"] + images_path,
                callback=lambda _, path: load_image(path),
            )
            image_viewer.create()
            dpg.add_text("{None}", tag="image_info")

dpg.show_metrics()

dpg.create_viewport(
    title="DearPyGui-ImageController", width=1200, height=600
)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
