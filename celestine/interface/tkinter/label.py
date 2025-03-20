from . import package
from .widget import Widget


class Label(Widget):
    def __init__(self, frame, **kwargs):
        super().__init__(
            package.Label(
                frame,
                **kwargs,
            )
        )
