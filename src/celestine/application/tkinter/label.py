from celestine.package import tkinter
from celestine.application.tkinter.widget import Widget


class Label(Widget):
    def __init__(self, frame, **kwargs):
        super().__init__(
            tkinter.Label(
                frame,
                **kwargs,
            )
        )
