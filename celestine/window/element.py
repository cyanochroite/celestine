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
        self.data = text
        super().__init__(tag, **star)


class Image(Abstract):
    """"""

    def size(self):
        x_size = self.x_max - self.x_min
        y_size = self.y_max - self.y_min
        return (x_size, y_size)

    def resize(self, x_length, y_length):
        x_size = self.x_max - self.x_min
        y_size = self.y_max - self.y_min

        x_over_y = x_length / y_length
        y_over_x = y_length / x_length

        if x_over_y > y_over_x:
            y_size = min(y_size, x_size / x_over_y)
        else:
            x_size = min(x_size, y_size / y_over_x)

        return (round(x_size), round(y_size))


    def crop(self, x_length, y_length):
        x_min = 0
        y_min = 0
        x_max = self.x_max - self.x_min
        y_max = self.x_max - self.x_min

        x_over_y = x_length / y_length
        y_over_x = y_length / x_length

        if x_over_y > y_over_x:
            stuff = y_max * x_over_y
            thing = stuff - x_max
            diff = thing // 2
            x_min += diff
            x_max += diff
        else:
            stuff = x_max * y_over_x
            thing = stuff - y_max
            diff = thing // 2
            y_min += diff
            y_max += diff

        return (x_min, y_min, x_max, y_max)


    def crop(self, x_length, y_length):
        x_min = 0
        y_min = 0
        x_max = self.x_max - self.x_min
        y_max = self.x_max - self.x_min

        x_over_y_import = x_length / y_length
        x_over_y_export = x_max / y_max

        y_over_x_import = y_length / x_length
        y_over_x_export = y_max / x_max


        ratio_import = x_length / y_length
        ratio_export = x_max / y_max

        if ratio_import > ratio_export:
            length = x_length * y_over_x_import
            offset = (x_length - length) / 2
            return ( 0 + offset, 0, length + offset, y_length)

        if ratio_import < ratio_export:
            length = x_length * y_over_x_import
            offset = (y_length - length) / 2
            return (0, 0 + offset, x_length, length + offset)

        return (0, 0, x_length, y_length)


    def update(self, *, image, **star):
        """"""
        if not image:
            return False

        self.image = image
        return True

    def __init__(self, tag, image, **star):
        self.cache = None
        self.image = image
        super().__init__(tag, **star)


class Label(Abstract):
    """"""

    def __init__(self, tag, text, **star):
        self.data = text
        super().__init__(tag, **star)
