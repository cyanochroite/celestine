""""DearPyGui: A simple Python GUI Toolkit."""


from celestine.typed import A

from . import Abstract


class Package(Abstract):
    """"""

    add_button: A
    add_dynamic_texture: A
    add_file_extension: A
    add_image: A
    add_static_texture: A
    add_table_column: A
    add_text: A
    configure_item: A
    create_context: A
    create_viewport: A
    destroy_context: A
    file_dialog: A
    hide_item: A
    last_container: A
    load_image: A
    set_primary_window: A
    set_value: A
    setup_dearpygui: A
    show_item: A
    show_viewport: A
    start_dearpygui: A
    table: A
    table_row: A
    texture_registry: A
    window: A

    group: A

    def tag_root(self, tag):
        """"""
        root = tag.split("_")[0]
        combine = f"{root}"
        return combine

    def __init__(self, ring, /, name, **star):
        super().__init__(ring, name, pypi="dearpygui.dearpygui")
