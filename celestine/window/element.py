""""""


from celestine.window.collection import Box


class Abstract(Box):
    """"""

    def poke(self, x_dot, y_dot):
        """"""
        return self.inside(x_dot, y_dot)

    def spot(self, x_min, y_min, x_max, y_max):
        """"""
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def __init__(self, tag, **star):
        self.item = None
        self.tag = tag
        super().__init__(**star)


class Button(Abstract):
    """"""

    def poke(self, x_dot, y_dot):
        """"""
        if super().poke(x_dot, y_dot):
            self.call(self.action, **self.argument)

    def __init__(self, tag, text, *, call, action, argument, **star):
        self.action = action
        self.argument = argument
        self.call = call
        self.text = text
        super().__init__(tag, **star)


class Image(Abstract):
    """"""

    def __init__(self, tag, image, **star):
        self.image = image
        super().__init__(tag, **star)


class Label(Abstract):
    """"""

    def __init__(self, tag, text, **star):
        self.text = text
        super().__init__(tag, **star)
