from . import package
from .widget import Widget


class Label(Widget):
    def __init__(self, tag, text, label):
        package.add_text(
            text,
            tag=tag,
            label=F"{tag}{label}",
            show_label=True,
        )
