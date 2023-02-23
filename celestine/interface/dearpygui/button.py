""""""

from celestine.window.button import Button as button

from .element import Element

from . import package


class Button(button, Element):
    """"""

    def __init__(self, tag, label, sender, action, function):
        package.add_button(
            tag=tag,
            label=label,
            user_data=(action, sender),
            callback=function,
        )
