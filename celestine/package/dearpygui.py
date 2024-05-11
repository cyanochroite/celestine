"""DearPyGui: A simple Python GUI Toolkit."""

from celestine.package import Abstract
from celestine.typed import (
    A,
    N,
    R,
    S,
)

add_button: A
add_dynamic_texture: A
add_image: A
add_text: A
configure_item: A
create_context: A
create_viewport: A
destroy_context: A
hide_item: A
load_image: A
set_primary_window: A
set_value: A
setup_dearpygui: A
show_item: A
show_viewport: A
start_dearpygui: A
texture_registry: A
window: A


class Package(Abstract):
    """"""

    def tag_root(self, tag: S) -> S:
        """"""
        root = tag.split("_")[0]
        combine = f"{root}"
        return combine

    def __init__(self, **star: R) -> N:
        super().__init__(pypi="dearpygui.dearpygui")
