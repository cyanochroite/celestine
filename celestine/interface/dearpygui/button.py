from . import package
from .widget import Widget


class Button(Widget):
    def __init__(self, tag, label, sender, action, function):
        package.add_button(
            tag=tag,
            label=label,
            user_data=(action, sender),
            callback=function,
        )
