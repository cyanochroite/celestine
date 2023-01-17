from math import radians

from .widget import Widget


class Mouse(Widget):
    def __init__(self, rectangle):
        super().__init__(
            "mouse",
            rectangle,
        )
        self.mesh.location = (1, 1, 1)
        self.mesh.rotation_euler = (0, 0, radians(45))
        self.mesh.scale = (0.5, 0.5, 0.5)
