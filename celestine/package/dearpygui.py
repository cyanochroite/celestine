"""DearPyGui: A simple Python GUI Toolkit."""

from celestine.package import Package
from celestine.typed import (
    A,
    N,
    R,
    ignore,
    override,
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
delete_item: A
add_image_button: A
add_texture_registry: A
add_window: A
add_group: A


class Self(Package):
    """"""

    @override
    def __init__(self, **star: R) -> N:
        ignore(self)
        super().__init__(pypi="dearpygui.dearpygui")
