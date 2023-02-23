""""""

from celestine.window.button import Button as button

from .element import Element

from . import package


class Button(button, Element):
    """"""

    def draw(self, collection, **star):
        """"""
        return

        package.add_button(
            tag=self.tag,
            label=self.text,
            user_data=("action", "sender"),
            callback=self.action,
        )
        super().draw(collection, **star)

    def __init__(self, tag, label, sender, action, function):
        package.add_button(
            tag=tag,
            label=label,
            user_data=(action, sender),
            callback=function,
        )
