from Unicode.U0000 import EXCLAMATION_MARK
from Unicode.U0000 import AMPERSAND
from Unicode.U0000 import VERTICAL_LINE
from Unicode.U0000 import CIRCUMFLEX_ACCENT
from Unicode.U0000 import TILDE

class Atoken:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class AND(Atoken):
    def __init__(self, value):
        super().__init__(AMPERSAND)


class IS(Atoken):
    def __init__(self, value):
        super().__init__(CIRCUMFLEX_ACCENT)


class NOT(Atoken):
    def __init__(self, value):
        super().__init__(TILDE)


class OR(Atoken):
    def __init__(self, value):
        super().__init__(VERTICAL_LINE)


class Atag(Atoken):
    def __init__(self, value):
        super().__init__(value)


class Asymbol(Atoken):
    def __init__(self, value):
        super().__init__("&")
