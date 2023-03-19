""""""

from celestine.window.button import Button as button

from . import package
from .element import Element


class Button(button, Element):
    """"""

    def callback(self, sender, app_data, user_data):
        """"""
        self.call(self.action, **self.argument)

    def draw(self, collection, **star):
        """"""
        package.add_button(
            tag=self.tag,
            label=self.text,
            callback=self.callback,
        )
        super().draw(collection, **star)

