""""""

from celestine.window.label import Label as label

from .element import Element

from . import package


class Label(label, Element):
    """"""

    def draw(self, collection, **star):
        """"""
        label = "Label"
        package.add_text(
            self.text,
            tag=self.tag,
            label=f"{self.tag}{label}",
            show_label=True,
        )
        super().draw(collection, **star)
