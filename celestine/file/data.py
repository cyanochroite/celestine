""""""

MAXIMUM_LINE_LENGTH = 72
SECTION_BREAK = "######################################################\
##################"





class String:
    """"""

    def read(self) -> S:
        """"""
        self.string.seek(0, io.SEEK_SET)
        string = self.string.read(self.count)
        self.string.seek(0, io.SEEK_SET)
        self.count = 0
        return string

    def write(self, text: S) -> N:
        """"""
        self.count += self.string.write(text)


    def __init__(self) -> N:
        self.string = io.StringIO()
        self.count = 0
