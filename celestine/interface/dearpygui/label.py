""""""

from celestine.window.label import Label as label

from .element import Element

from . import package


class Label(label, Element):
    """"""

    def __init__(self, tag, text, label):
        package.add_text(
            text,
            tag=tag,
            label=F"{tag}{label}",
            show_label=True,
        )
